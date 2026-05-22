#!/usr/bin/env python3
"""Operational intelligence analyzer for the Ologos ecosystem.

Reads ops/ logs and watchlists, detects patterns, reports open incidents,
QA rejection rates, fragile services, and compliance status.

Usage:
    python3 scripts/ops-analyze.py              # Full analysis, human-readable
    python3 scripts/ops-analyze.py --json       # JSON output
    python3 scripts/ops-analyze.py --update     # Update watchlists with new findings
"""
import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = REPO_ROOT / "ops"

FRAGILE_THRESHOLD = 3       # incidents in window = fragile
FRAGILE_WINDOW_DAYS = 30
QA_FAIL_RATE_THRESHOLD = 0.3  # 30%
QA_FAIL_WINDOW = 10          # last N reviews
HALLUCINATION_RECURRENCE = 3  # same type = pattern
ESCALATION_WINDOW_DAYS = 7


def load_json(filename: str) -> dict:
    path = OPS_DIR / filename
    return json.loads(path.read_text())


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_ts(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def days_ago(days: int) -> datetime:
    return datetime.now(timezone.utc) - timedelta(days=days)


def analyze_incidents(sysadmin_log: dict) -> dict:
    """Analyze incidents: open, recurrence, fragile services."""
    incidents = [e for e in sysadmin_log.get("entries", []) if e.get("type") == "incident"]
    cutoff = days_ago(FRAGILE_WINDOW_DAYS)

    open_incidents = []
    recent_by_service = defaultdict(list)

    for inc in incidents:
        details = inc.get("details", {})
        if details.get("open", False):
            open_incidents.append(inc)

        ts = parse_ts(inc["timestamp"])
        if ts >= cutoff:
            service = inc.get("service", "unknown")
            recent_by_service[service].append(inc)

    fragile_services = {
        svc: len(incs) for svc, incs in recent_by_service.items()
        if len(incs) >= FRAGILE_THRESHOLD
    }

    # Recurrence chains
    recurrences = []
    for inc in incidents:
        ref = inc.get("details", {}).get("recurrence_of")
        if ref:
            recurrences.append({"incident": inc["id"], "recurrence_of": ref})

    return {
        "open_incidents": open_incidents,
        "total_incidents_30d": sum(len(v) for v in recent_by_service.values()),
        "fragile_services": fragile_services,
        "recurrence_chains": recurrences,
    }


def analyze_qa(qa_log: dict) -> dict:
    """Analyze QA: rejection rates, model performance, artifact types, hallucinations."""
    entries = qa_log.get("entries", [])
    if not entries:
        return {"total_reviews": 0, "message": "No QA log entries yet"}

    # Overall stats
    results = Counter(e.get("result") for e in entries)
    total = len(entries)
    fail_count = results.get("fail", 0)
    fail_rate = fail_count / total if total > 0 else 0

    # Recent window
    recent = entries[-QA_FAIL_WINDOW:]
    recent_results = Counter(e.get("result") for e in recent)
    recent_fail_rate = recent_results.get("fail", 0) / len(recent) if recent else 0

    # By model
    by_model = defaultdict(lambda: {"total": 0, "fail": 0})
    for e in entries:
        model = e.get("details", {}).get("model_used") or e.get("model_used", "unknown")
        by_model[model]["total"] += 1
        if e.get("result") == "fail":
            by_model[model]["fail"] += 1

    model_stats = {}
    for model, stats in by_model.items():
        rate = stats["fail"] / stats["total"] if stats["total"] > 0 else 0
        model_stats[model] = {
            "total": stats["total"],
            "failures": stats["fail"],
            "fail_rate": round(rate, 2),
            "flagged": rate > QA_FAIL_RATE_THRESHOLD,
        }

    # By artifact type
    by_type = defaultdict(lambda: {"total": 0, "fail": 0})
    for e in entries:
        atype = (e.get("details") or {}).get("artifact_type", "unknown")
        by_type[atype]["total"] += 1
        if e.get("result") == "fail":
            by_type[atype]["fail"] += 1

    type_stats = {}
    for atype, stats in by_type.items():
        rate = stats["fail"] / stats["total"] if stats["total"] > 0 else 0
        type_stats[atype] = {
            "total": stats["total"],
            "failures": stats["fail"],
            "fail_rate": round(rate, 2),
        }

    # Hallucination patterns
    hallucinations = [e for e in entries if e.get("type") == "hallucination_catch"]
    h_types = Counter(
        (e.get("details") or {}).get("hallucination_type", "unknown")
        for e in hallucinations
    )
    recurring_patterns = {t: c for t, c in h_types.items() if c >= HALLUCINATION_RECURRENCE}

    # Failure reasons
    reasons = Counter(
        (e.get("details") or {}).get("rejection_reason", "unspecified")
        for e in entries if e.get("result") == "fail"
    )

    return {
        "total_reviews": total,
        "overall_fail_rate": round(fail_rate, 2),
        "recent_fail_rate": round(recent_fail_rate, 2),
        "recent_fail_rate_alert": recent_fail_rate > QA_FAIL_RATE_THRESHOLD,
        "by_model": model_stats,
        "by_artifact_type": type_stats,
        "hallucination_patterns": recurring_patterns,
        "top_failure_reasons": dict(reasons.most_common(5)),
        "results_breakdown": dict(results),
    }


def analyze_promotions(promotion_log: dict) -> dict:
    """Analyze promotion compliance."""
    entries = promotion_log.get("entries", [])
    if not entries:
        return {"total_promotions": 0, "message": "No promotions logged yet"}

    total = len(entries)
    violations = [e for e in entries if e.get("violation")]
    cutoff = days_ago(ESCALATION_WINDOW_DAYS)
    recent_violations = [
        e for e in violations if parse_ts(e["timestamp"]) >= cutoff
    ]

    compliance_rate = (total - len(violations)) / total if total > 0 else 1.0

    return {
        "total_promotions": total,
        "violations": len(violations),
        "recent_violations_7d": len(recent_violations),
        "compliance_rate": round(compliance_rate, 2),
        "violation_details": [
            {"id": v["id"], "repo": v.get("repo"), "justification": v.get("violation_justification")}
            for v in recent_violations
        ],
    }


def analyze_watchlists() -> dict:
    """Report open items from both watchlists."""
    sys_wl = load_json("sysadmin_watchlist.json")
    qa_wl = load_json("qa_watchlist.json")

    sys_open = [i for i in sys_wl.get("items", []) if i.get("status") == "open"]
    qa_open = [i for i in qa_wl.get("items", []) if i.get("status") == "open"]

    return {
        "sysadmin_open": len(sys_open),
        "sysadmin_items": [{"id": i["id"], "severity": i.get("severity"), "summary": i.get("summary")} for i in sys_open],
        "qa_open": len(qa_open),
        "qa_items": [{"id": i["id"], "severity": i.get("severity"), "summary": i.get("summary")} for i in qa_open],
    }


def update_watchlists(qa_analysis: dict, incident_analysis: dict):
    """Auto-create watchlist items based on analysis findings."""
    now = now_iso()
    date = now[:10]
    updated = False

    # QA watchlist updates
    qa_wl_path = OPS_DIR / "qa_watchlist.json"
    qa_wl = json.loads(qa_wl_path.read_text())
    existing_ids = {i["id"] for i in qa_wl.get("items", [])}

    # High QA failure rate
    if qa_analysis.get("recent_fail_rate_alert"):
        item_id = f"watch-{date}-qa-fail-rate-high"
        if item_id not in existing_ids:
            qa_wl["items"].append({
                "id": item_id,
                "added_at": now,
                "status": "open",
                "resolved_at": None,
                "severity": "warning",
                "category": "artifact_quality",
                "summary": f"QA rejection rate {qa_analysis['recent_fail_rate']*100:.0f}% in last {QA_FAIL_WINDOW} reviews (threshold: {QA_FAIL_RATE_THRESHOLD*100:.0f}%)",
                "details": json.dumps(qa_analysis.get("top_failure_reasons", {})),
                "affected_skills": [],
                "recurrence_count": 0,
                "related_incidents": [],
            })
            updated = True

    # Hallucination patterns
    for h_type, count in qa_analysis.get("hallucination_patterns", {}).items():
        item_id = f"watch-{date}-hallucination-{h_type[:30].lower().replace(' ', '-')}"
        if item_id not in existing_ids:
            qa_wl["items"].append({
                "id": item_id,
                "added_at": now,
                "status": "open",
                "resolved_at": None,
                "severity": "error",
                "category": "hallucination_pattern",
                "summary": f"Recurring hallucination pattern: {h_type} ({count} occurrences)",
                "details": f"Same hallucination type detected {count} times. Review QA prompt and skill files.",
                "affected_skills": [],
                "recurrence_count": count,
                "related_incidents": [],
            })
            updated = True

    # Flagged models
    for model, stats in qa_analysis.get("by_model", {}).items():
        if stats.get("flagged"):
            item_id = f"watch-{date}-model-{model[:30].lower().replace(' ', '-')}"
            if item_id not in existing_ids:
                qa_wl["items"].append({
                    "id": item_id,
                    "added_at": now,
                    "status": "open",
                    "resolved_at": None,
                    "severity": "warning",
                    "category": "artifact_quality",
                    "summary": f"Model {model} has {stats['fail_rate']*100:.0f}% QA failure rate ({stats['failures']}/{stats['total']})",
                    "details": "Consider switching to a different model or adjusting prompts.",
                    "affected_skills": [],
                    "recurrence_count": 0,
                    "related_incidents": [],
                })
                updated = True

    if updated:
        qa_wl_path.write_text(json.dumps(qa_wl, indent=2) + "\n")

    # Sysadmin watchlist: fragile services
    sys_wl_path = OPS_DIR / "sysadmin_watchlist.json"
    sys_wl = json.loads(sys_wl_path.read_text())
    existing_ids = {i["id"] for i in sys_wl.get("items", [])}
    sys_updated = False

    for svc, count in incident_analysis.get("fragile_services", {}).items():
        item_id = f"watch-{date}-fragile-{svc.lower().replace(' ', '-')}"
        if item_id not in existing_ids:
            sys_wl["items"].append({
                "id": item_id,
                "added_at": now,
                "status": "open",
                "resolved_at": None,
                "severity": "warning",
                "category": "service",
                "summary": f"Fragile service: {svc} ({count} incidents in last {FRAGILE_WINDOW_DAYS} days)",
                "details": f"Review incident history before making changes. Requires {FRAGILE_WINDOW_DAYS} days incident-free to resolve.",
                "check_command": f"python3 scripts/ops-analyze.py --json | python3 -c \"import sys,json; print(json.dumps(json.load(sys.stdin)['incidents'], indent=2))\"",
                "threshold": f"{FRAGILE_THRESHOLD} incidents/{FRAGILE_WINDOW_DAYS}d",
                "related_incidents": [],
            })
            sys_updated = True

    if sys_updated:
        sys_wl_path.write_text(json.dumps(sys_wl, indent=2) + "\n")

    return updated or sys_updated


def print_human_summary(report: dict):
    """Print concise human-readable analysis."""
    print(f"Ops Analysis — {report['timestamp']}")

    # Open incidents
    inc = report["incidents"]
    if inc.get("open_incidents"):
        print(f"\n  OPEN INCIDENTS ({len(inc['open_incidents'])}):")
        for i in inc["open_incidents"]:
            print(f"    !! [{i.get('severity', '?').upper()}] {i.get('summary', i['id'])}")
    else:
        print("\n  No open incidents.")

    # Fragile services
    if inc.get("fragile_services"):
        print(f"\n  FRAGILE SERVICES:")
        for svc, count in inc["fragile_services"].items():
            print(f"    > {svc}: {count} incidents in last {FRAGILE_WINDOW_DAYS} days")

    # QA stats
    qa = report["qa"]
    if qa.get("total_reviews", 0) > 0:
        print(f"\n  QA: {qa['total_reviews']} reviews, {qa['overall_fail_rate']*100:.0f}% overall fail rate", end="")
        if qa.get("recent_fail_rate_alert"):
            print(f" — ALERT: recent rate {qa['recent_fail_rate']*100:.0f}%", end="")
        print()

        if qa.get("hallucination_patterns"):
            print(f"  Hallucination patterns: {qa['hallucination_patterns']}")

        flagged = [m for m, s in qa.get("by_model", {}).items() if s.get("flagged")]
        if flagged:
            print(f"  Flagged models: {', '.join(flagged)}")
    else:
        print(f"\n  QA: {qa.get('message', 'No data')}")

    # Promotions
    promo = report["promotions"]
    if promo.get("total_promotions", 0) > 0:
        print(f"\n  Promotions: {promo['total_promotions']} total, {promo['compliance_rate']*100:.0f}% dev-first compliant")
        if promo.get("recent_violations_7d"):
            print(f"    !! {promo['recent_violations_7d']} violation(s) in last 7 days")
    else:
        print(f"\n  Promotions: {promo.get('message', 'No data')}")

    # Watchlists
    wl = report["watchlists"]
    total_open = wl["sysadmin_open"] + wl["qa_open"]
    if total_open:
        print(f"\n  Open watchlist items: {wl['sysadmin_open']} sysadmin, {wl['qa_open']} QA")
        for item in wl.get("sysadmin_items", []) + wl.get("qa_items", []):
            print(f"    > [{item.get('severity', '?').upper()}] {item['summary']}")
    else:
        print(f"\n  No open watchlist items.")


def main():
    parser = argparse.ArgumentParser(description="Ologos ops intelligence analyzer")
    parser.add_argument("--json", action="store_true", help="Output raw JSON only")
    parser.add_argument("--update", action="store_true", help="Auto-update watchlists with findings")
    args = parser.parse_args()

    sysadmin_log = load_json("sysadmin_log.json")
    qa_log = load_json("qa_log.json")
    promotion_log = load_json("promotion_log.json")

    report = {
        "timestamp": now_iso(),
        "incidents": analyze_incidents(sysadmin_log),
        "qa": analyze_qa(qa_log),
        "promotions": analyze_promotions(promotion_log),
        "watchlists": analyze_watchlists(),
    }

    if args.update:
        watchlists_updated = update_watchlists(report["qa"], report["incidents"])
        report["watchlists_updated"] = watchlists_updated
        if watchlists_updated:
            # Re-read after update
            report["watchlists"] = analyze_watchlists()

    if args.json:
        print(json.dumps(report, indent=2, default=str))
    else:
        print_human_summary(report)

    sys.exit(0)


if __name__ == "__main__":
    main()
