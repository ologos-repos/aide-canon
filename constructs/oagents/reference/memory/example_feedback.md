---
name: Dev-First Workflow
description: All changes must be tested in dev environment before production
type: feedback
---

All changes go to dev branch/container first, promote to production on approval.

**Why:** A direct-to-production deployment broke the chatbot during a live demo. The pre-push hook was built to enforce this after the incident.

**How to apply:** Never push directly to main without dev testing evidence in ops/qa_log.json. The pre-push hook checks for this automatically.
