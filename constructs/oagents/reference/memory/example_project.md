---
name: Ops Layer Migration
description: Health monitoring and security scanning moved to production host
type: project
---

## Ops Infrastructure Migration

Health monitoring, security scanning, and the ops dashboard were migrated from the dev host to the production host on 2026-04-03.

**Why:** Ops agents belong on the host they monitor. Running health checks via SSH from a remote host added latency and a failure point.

**How to apply:** All ops automation (health-check, sec-agent, metrics-collector) runs on the production host. QA agent and operator tooling remain on the dev host.
