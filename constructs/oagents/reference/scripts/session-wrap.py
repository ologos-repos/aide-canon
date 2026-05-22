#!/usr/bin/env python3
"""Session wrap protocol — programmatic enforcement of the wrap checklist.

Checks all wrap requirements and reports pass/fail for each item.
Operator cannot claim "done" without this passing.

Usage:
    python3 scripts/session-wrap.py
    python3 scripts/session-wrap.py --json
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OPS = REPO_ROOT / "ops"


def run(cmd: list[str], timeout: int = 30) -> tuple[bool, str]:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.returncode == 0, r.stdout.strip()
    except (subprocess.TimeoutExpired, Exception) as e:
        return False, str(e)


def check_git_clean() -> dict:
    ok, out = run(["git", "-C", str(REPO_ROOT), "status", "--porcelain"])
    clean = ok and out == ""
    return {
        "item": "Git working tree clean",
        "pass": clean,
        "detail": "Clean" if clean else f"{len(out.splitlines())} uncommitted files",
    }


def check_remotes_pushed() -> dict:
    """Check if local HEAD matches all remote HEADs."""
    ok, local_head = run(["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"])
    if not ok:
        return {"item": "All remotes pushed", "pass": False, "detail": "Cannot read HEAD"}

    unpushed = []
    for remote in ["origin", "gitea"]:
        ok, remote_head = run(["git", "-C", str(REPO_ROOT), "rev-parse", f"{remote}/main"])
        if ok and remote_head != local_head:
            unpushed.append(remote)
        elif not ok:
            unpushed.append(f"{remote} (unreachable)")

    pushed = len(unpushed) == 0
    return {
        "item": "All remotes pushed",
        "pass": pushed,
        "detail": "All synced" if pushed else f"Unpushed: {', '.join(unpushed)}",
    }


def check_qa_ran() -> dict:
    """Check if QA agent was run during this session (last 4 hours)."""
    qa_log_path = OPS / "qa_log.json"
    if not qa_log_path.exists():
        return {"item": "QA agent ran this session", "pass": False, "detail": "ops/qa_log.json missing"}

    data = json.loads(qa_log_path.read_text())
    entries = data.get("entries", [])

    cutoff = (datetime.now(timezone.utc) - timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M:%SZ")
    recent = [e for e in entries if e.get("timestamp", "") >= cutoff]

    has_review = any(e.get("type") in ("artifact_review", "compliance_check") for e in recent)
    return {
        "item": "QA agent ran this session",
        "pass": has_review,
        "detail": f"{len(recent)} QA entries in last 4 hours" if has_review else "No recent QA entries",
    }


def check_ops_updated() -> dict:
    """Check if ops/ files were modified (indicates logging happened)."""
    ok, out = run(["git", "-C", str(REPO_ROOT), "diff", "--name-only", "HEAD", "--", "ops/"])
    staged_ok, staged = run(["git", "-C", str(REPO_ROOT), "diff", "--cached", "--name-only", "--", "ops/"])

    # Also check if ops files have uncommitted changes (they should be committed)
    ops_modified = bool(out) or bool(staged)

    # Check if ops/ log files have entries from today
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    has_today_entries = False
    for log_file in ["sysadmin_log.json", "qa_log.json"]:
        path = OPS / log_file
        if path.exists():
            data = json.loads(path.read_text())
            for entry in data.get("entries", []):
                if entry.get("timestamp", "").startswith(today):
                    has_today_entries = True
                    break

    return {
        "item": "ops/ files updated this session",
        "pass": has_today_entries,
        "detail": "Today's entries found in logs" if has_today_entries else "No entries from today",
    }


def check_ops_committed() -> dict:
    """Check that ops/ changes are committed (not just modified)."""
    ok, out = run(["git", "-C", str(REPO_ROOT), "diff", "--name-only", "--", "ops/"])
    uncommitted = [f for f in out.splitlines() if f.strip()] if out else []

    return {
        "item": "ops/ files committed",
        "pass": len(uncommitted) == 0,
        "detail": "All committed" if not uncommitted else f"Uncommitted: {', '.join(uncommitted)}",
    }


def check_hooks_installed() -> dict:
    """Check git hooks are installed."""
    pre_commit = (REPO_ROOT / ".git" / "hooks" / "pre-commit").exists()
    pre_push = (REPO_ROOT / ".git" / "hooks" / "pre-push").exists()
    both = pre_commit and pre_push
    return {
        "item": "Git hooks installed",
        "pass": both,
        "detail": "Both installed" if both else f"pre-commit: {'yes' if pre_commit else 'NO'}, pre-push: {'yes' if pre_push else 'NO'}",
    }


def check_no_qa_failures() -> dict:
    """Check that no unresolved QA failures exist from this session.

    A failure is considered resolved if a subsequent pass entry exists
    after it (either with a resolution_of reference or simply by timestamp).
    """
    qa_log_path = OPS / "qa_log.json"
    if not qa_log_path.exists():
        return {"item": "No unresolved QA failures", "pass": True, "detail": "No QA log"}

    data = json.loads(qa_log_path.read_text())
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M:%SZ")

    recent = [e for e in data.get("entries", []) if e.get("timestamp", "") >= cutoff]
    recent_fails = [e for e in recent if e.get("result") == "fail"]

    if not recent_fails:
        return {"item": "No unresolved QA failures", "pass": True, "detail": "Clean"}

    # Check if each failure was resolved by a subsequent pass
    recent_passes = [e for e in recent if e.get("result") == "pass"]
    last_pass_ts = max((e.get("timestamp", "") for e in recent_passes), default="")
    last_fail_ts = max((e.get("timestamp", "") for e in recent_fails), default="")

    # If the most recent pass is after the most recent fail, consider resolved
    resolved = last_pass_ts > last_fail_ts

    if resolved:
        return {
            "item": "No unresolved QA failures",
            "pass": True,
            "detail": f"{len(recent_fails)} failure(s) resolved (last pass after last fail)",
        }

    return {
        "item": "No unresolved QA failures",
        "pass": False,
        "detail": f"{len(recent_fails)} recent failure(s)",
    }


def check_recovery_current() -> dict:
    """Check if recovery/ docs were updated when infrastructure changed.

    Looks at git diff for infrastructure-related files (docker/, cloudflare,
    tunnel, Dockerfile, docker-compose, .env changes) and checks if recovery/
    was also modified in recent commits.
    """
    # Check if any infra-related files changed in this session (last 4 hours of commits)
    cutoff_seconds = 4 * 3600
    ok, log = run([
        "git", "-C", str(REPO_ROOT), "log",
        f"--since={cutoff_seconds} seconds ago",
        "--name-only", "--pretty=format:",
    ])
    if not ok or not log.strip():
        return {
            "item": "Recovery docs current",
            "pass": True,
            "detail": "No recent commits to check",
        }

    changed_files = set(log.strip().splitlines())
    infra_keywords = {"docker/", "tunnel/", "Dockerfile", "docker-compose", "cloudflare", "keycloak", ".env"}
    infra_changed = any(
        any(kw in f for kw in infra_keywords)
        for f in changed_files if f.strip()
    )

    if not infra_changed:
        return {
            "item": "Recovery docs current",
            "pass": True,
            "detail": "No infrastructure changes detected",
        }

    # Infra changed — check if recovery/ was also updated
    recovery_updated = any("recovery/" in f for f in changed_files if f.strip())

    return {
        "item": "Recovery docs current",
        "pass": recovery_updated,
        "detail": "Recovery docs updated with infra changes" if recovery_updated else "Infrastructure changed but recovery/ not updated — run recovery update",
    }


def run_all_checks() -> list[dict]:
    return [
        check_git_clean(),
        check_remotes_pushed(),
        check_qa_ran(),
        check_no_qa_failures(),
        check_ops_updated(),
        check_ops_committed(),
        check_recovery_current(),
        check_hooks_installed(),
    ]


def print_report(checks: list[dict]):
    print("=" * 60)
    print("  OLOGOS SESSION WRAP — CHECKLIST")
    print("=" * 60)

    passed = 0
    failed = 0
    for c in checks:
        icon = "✅" if c["pass"] else "❌"
        print(f"  {icon} {c['item']}")
        print(f"      {c['detail']}")
        if c["pass"]:
            passed += 1
        else:
            failed += 1

    print()
    print("=" * 60)
    if failed == 0:
        print(f"  VERDICT: ALL CHECKS PASSED ({passed}/{passed})")
    else:
        print(f"  VERDICT: {failed} CHECK(S) FAILED ({passed}/{passed + failed} passed)")
        print("  Fix the failures above before ending the session.")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Ologos session wrap checklist")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    checks = run_all_checks()

    if args.json:
        print(json.dumps(checks, indent=2))
    else:
        print_report(checks)

    failed = sum(1 for c in checks if not c["pass"])
    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
