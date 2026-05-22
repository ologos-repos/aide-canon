# OAgents Reference Implementation

This directory contains a sanitized snapshot of a production OAgents implementation managing 20+ enterprise services across 2 hosts. It demonstrates the architectural feasibility of all 26 components defined in the OAgents specification.

## What This Is

Structural implementation artifacts — the actual scripts, skill files, hooks, memory schemas, and operational log formats used in the reference deployment described in Section 9 of the specification. These are the evidence artifacts that Appendix C requires conforming implementations to produce.

## What Was Sanitized

- Internal IP addresses, SSH paths, hostnames replaced with `<placeholders>`
- Team member names, emails, and Telegram IDs removed
- API keys and credentials removed (scripts use environment variables)
- Real operational log data replaced with synthetic examples demonstrating the schema
- Customer-specific branding and configuration removed
- Cloudflare tunnel UUIDs and DNS details removed

## What Is Intact

- File structure and naming conventions
- Script logic and control flow
- Hook enforcement mechanisms
- Memory schema (YAML frontmatter format with typed entries)
- QA agent architecture, prompts, and review logic
- Security agent check categories and reporting
- Skill file structure and operational standards
- Ops log schemas with realistic example entries
- Session protocol logic (start and wrap)
- Component taxonomy (intelligence/components.yml)

## Directory Map

```
reference/
├── CLAUDE.md                      # Operator instructions (behavioral envelope config)
├── memory/
│   ├── MEMORY.md                  # Memory index (example entries)
│   ├── example_feedback.md        # Feedback memory — behavioral correction
│   ├── example_project.md         # Project memory — operational context
│   └── example_reference.md       # Reference memory — infrastructure pointer
├── skills/
│   ├── sysadmin.md                # Systems administration skill (procedures, impact levels, monitoring)
│   └── quality_assurance.md       # Quality assurance skill (QA gates, anti-hallucination, smoke testing)
├── hooks/
│   ├── pre-commit                 # QA gate — blocks commit without independent review
│   └── pre-push                   # Dev-first enforcement + security scan
├── scripts/
│   ├── session-start.py           # Session initialization (health check, context load, hook verify)
│   ├── session-wrap.py            # Session finalization (git clean, QA confirm, ops log, push)
│   └── ops-analyze.py             # Operational pattern analysis (escalation, fragile service detection)
├── qa-agent/
│   ├── agent.py                   # Independent QA reviewer (model-agnostic, structured verdicts)
│   └── prompts/
│       └── qa_review.md           # QA review system prompt
├── sec-agent/
│   └── agent.py                   # Security auditor (7 check categories, scheduled + pre-push)
├── ops/
│   ├── README.md                  # Schema definitions for all operational log files
│   └── examples/
│       ├── sysadmin_log.json      # Example: deploy, health check, incident entries
│       ├── qa_log.json            # Example: pass and fail review entries with model ID
│       └── metrics_history.json   # Example: ring buffer metric entries
└── intelligence/
    └── components.yml             # Full 26-component taxonomy with categories and evidence
```

## Mapping to Specification

| Spec Section | Reference Artifact |
|-------------|-------------------|
| 4.1 Pre-Execution Gates | `CLAUDE.md`, `memory/`, `skills/` |
| 4.2 Post-Execution Gates | `qa-agent/`, `sec-agent/` |
| 4.3 Operational Gates | `scripts/session-*.py`, `ops/` |
| 5.1 Behavioral Shaping | `memory/example_feedback.md` |
| 5.2 Quality Gates | `hooks/pre-commit`, `qa-agent/agent.py` |
| 5.3 Operational Discipline | `scripts/session-start.py`, `scripts/session-wrap.py` |
| 5.4 Knowledge Injection | `memory/MEMORY.md`, `skills/*.md` |
| 5.5 Enforcement Mechanisms | `hooks/pre-commit`, `hooks/pre-push` |
| 5.6 Project Governance | `ops/README.md`, `CLAUDE.md` (session wrap section) |
| 5.7 Anti-Hallucination | `skills/quality_assurance.md` (Anti-Hallucination section) |
| Appendix C Evidence | `ops/examples/*.json`, all files above |
