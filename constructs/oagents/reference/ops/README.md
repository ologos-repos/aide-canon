# Operational Logging Schemas

All operational events are logged as append-only structured JSON.

## Files

| File | Contents |
|------|----------|
| sysadmin_log.json | Deploys, health checks, incidents, restarts |
| qa_log.json | QA reviews with model ID, verdict, findings |
| security_log.json | Security audit results by category |
| metrics_history.json | Ring buffer of host resource metrics |
| sysadmin_watchlist.json | Open infrastructure concerns |

## Schema Conventions

- All entries include `timestamp` (ISO 8601) and `type`
- Logs are append-only — never delete entries
- Watchlist items have `status` (open/resolved) with timestamps
- QA entries include `model_used`, `result` (pass/fail), and `findings`
