#!/usr/bin/env python3
"""Session start protocol — single entry point for any AI operator or human.

Runs all discovery checks and produces a structured readiness report.
Any model, any provider — just run this script.

Usage:
    python3 scripts/session-start.py
    python3 scripts/session-start.py --json
    python3 scripts/session-start.py --skip-health  # Skip SSH checks (faster)
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "scripts"
OPS = REPO_ROOT / "ops"


def run(cmd: list[str], timeout: int = 90) -> tuple[bool, str]:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.returncode == 0, r.stdout.strip()
    except subprocess.TimeoutExpired:
        return False, "timeout"
    except Exception as e:
        return False, str(e)


def git_status() -> dict:
    ok, out = run(["git", "-C", str(REPO_ROOT), "status", "--porcelain"])
    branch_ok, branch = run(["git", "-C", str(REPO_ROOT), "branch", "--show-current"])
    return {
        "clean": ok and out == "",
        "branch": branch if branch_ok else "unknown",
        "uncommitted_files": [l.strip() for l in out.splitlines()] if out else [],
    }


def health_check(skip: bool = False) -> dict | None:
    if skip:
        return None
    ok, out = run(["python3", str(SCRIPTS / "health-check.py"), "--json", "--no-log"])
    if ok:
        try:
            return json.loads(out)
        except json.JSONDecodeError:
            pass
    return {"error": "health check failed", "output": out[:500]}


def ops_analysis() -> dict | None:
    ok, out = run(["python3", str(SCRIPTS / "ops-analyze.py"), "--json"])
    if ok:
        try:
            return json.loads(out)
        except json.JSONDecodeError:
            pass
    return None


def load_watchlists() -> dict:
    result = {}
    for name in ["sysadmin_watchlist.json", "qa_watchlist.json"]:
        path = OPS / name
        if path.exists():
            data = json.loads(path.read_text())
            open_items = [i for i in data.get("items", []) if i.get("status") == "open"]
            result[name.replace(".json", "")] = open_items
    return result


def recent_logs(filename: str, count: int = 5) -> list:
    path = OPS / filename
    if path.exists():
        data = json.loads(path.read_text())
        return data.get("entries", [])[-count:]
    return []


def recovery_staleness() -> dict:
    """Check if recovery/ docs are stale relative to infrastructure changes.

    Compares the most recent recovery/ commit to the most recent infra commit.
    If infra changed more recently than recovery, flag it.
    """
    recovery_dir = REPO_ROOT / "recovery"
    if not recovery_dir.exists():
        return {"stale": True, "detail": "recovery/ directory missing"}

    # Last recovery/ commit date
    ok, recovery_date = run([
        "git", "-C", str(REPO_ROOT), "log", "-1", "--format=%ci", "--", "recovery/",
    ])
    if not ok or not recovery_date:
        return {"stale": False, "detail": "No recovery commit history"}

    # Last infra commit date (docker/, tunnel, Dockerfile, cloudflare)
    ok, infra_date = run([
        "git", "-C", str(REPO_ROOT), "log", "-1", "--format=%ci", "--",
        "docker/", "scripts/deploy-plte.py",
    ])
    if not ok or not infra_date:
        return {"stale": False, "detail": "No infra commit history"}

    # Compare dates (string comparison works for ISO dates)
    stale = infra_date > recovery_date

    return {
        "stale": stale,
        "recovery_updated": recovery_date[:10],
        "infra_updated": infra_date[:10],
        "detail": f"Recovery last updated {recovery_date[:10]}, infra last changed {infra_date[:10]}"
            if stale else f"Recovery current (updated {recovery_date[:10]})",
    }


def print_report(report: dict):
    print("=" * 60)
    print("  OLOGOS SESSION START — READINESS REPORT")
    print("=" * 60)

    # Git
    git = report["git"]
    status = "CLEAN" if git["clean"] else f"DIRTY ({len(git['uncommitted_files'])} files)"
    print(f"\n  Git: {git['branch']} — {status}")
    if not git["clean"]:
        for f in git["uncommitted_files"][:5]:
            print(f"    {f}")

    # Health
    health = report.get("health")
    if health and "error" not in health:
        s = health.get("summary", {})
        print(f"\n  Health: {s.get('ok', '?')}/{s.get('total_checks', '?')} services OK", end="")
        if s.get("down"):
            print(f", {s['down']} DOWN", end="")
        if s.get("degraded"):
            print(f", {s['degraded']} degraded", end="")
        print()

        alerts = health.get("alerts", [])
        if alerts:
            print(f"\n  ALERTS ({len(alerts)}):")
            for a in alerts:
                icon = "!!" if a.get("severity") in ("error", "critical") else " >"
                print(f"    {icon} [{a['severity'].upper()}] {a['message']}")
    elif health and "error" in health:
        print(f"\n  Health: ERROR — {health['error']}")
    else:
        print("\n  Health: skipped (--skip-health)")

    # Analysis
    analysis = report.get("analysis")
    if analysis:
        inc = analysis.get("incidents", {})
        if inc.get("open_incidents"):
            print(f"\n  OPEN INCIDENTS ({len(inc['open_incidents'])}):")
            for i in inc["open_incidents"]:
                print(f"    !! {i.get('summary', i['id'])}")

        if inc.get("fragile_services"):
            print(f"\n  FRAGILE SERVICES:")
            for svc, count in inc["fragile_services"].items():
                print(f"    > {svc}: {count} incidents in 30 days")

        qa = analysis.get("qa", {})
        if qa.get("total_reviews", 0) > 0:
            print(f"\n  QA: {qa['total_reviews']} reviews, {qa['overall_fail_rate']*100:.0f}% fail rate")
            if qa.get("recent_fail_rate_alert"):
                print(f"    !! Recent fail rate {qa['recent_fail_rate']*100:.0f}% exceeds threshold")

    # Watchlists
    watchlists = report.get("watchlists", {})
    total_open = sum(len(v) for v in watchlists.values())
    if total_open:
        print(f"\n  WATCHLIST ({total_open} open):")
        for category, items in watchlists.items():
            for item in items:
                print(f"    > [{item.get('severity', '?').upper()}] {item.get('summary', item['id'])}")
    else:
        print("\n  Watchlists: clear")

    # Recovery
    recovery = report.get("recovery", {})
    if recovery.get("stale"):
        print(f"\n  !! RECOVERY DOCS STALE: {recovery['detail']}")
    else:
        print(f"\n  Recovery: {recovery.get('detail', 'ok')}")

    # Hooks
    hooks = report.get("hooks", {})
    print(f"\n  Hooks: pre-commit {'INSTALLED' if hooks.get('pre_commit') else 'MISSING'}, pre-push {'INSTALLED' if hooks.get('pre_push') else 'MISSING'}")

    print()
    print("=" * 60)
    health = report.get("health") or {}
    recovery_stale = report.get("recovery", {}).get("stale", False)
    verdict = "READY" if git["clean"] and not health.get("alerts") and not recovery_stale else "ISSUES FOUND"
    print(f"  VERDICT: {verdict}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Ologos session start protocol")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--skip-health", action="store_true", help="Skip SSH health checks")
    args = parser.parse_args()

    report = {
        "git": git_status(),
        "health": health_check(skip=args.skip_health),
        "analysis": ops_analysis(),
        "watchlists": load_watchlists(),
        "recent_sysadmin": recent_logs("sysadmin_log.json"),
        "recent_qa": recent_logs("qa_log.json"),
        "recent_promotions": recent_logs("promotion_log.json"),
        "recovery": recovery_staleness(),
        "hooks": {
            "pre_commit": (REPO_ROOT / ".git" / "hooks" / "pre-commit").exists(),
            "pre_push": (REPO_ROOT / ".git" / "hooks" / "pre-push").exists(),
        },
    }

    if args.json:
        print(json.dumps(report, indent=2, default=str))
    else:
        print_report(report)

    # Exit 1 if critical issues found
    health = report.get("health") or {}
    if health.get("summary", {}).get("down", 0) > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
