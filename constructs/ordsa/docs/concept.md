# Ordinal Systems Architecture — Canonical Statement

This file is the canonical statement of the construct. Layer files in `layers/` expand on individual ordinals; this file is the whole thing in one read.

---

**Ordinal Systems Architecture (OSA)** is an enterprise architecture construct that orders AI systems by their governing rank in the enterprise, from strategy and policy down to domain orchestration, agent execution, tool use, data access, and observable outcomes.

The point is simple: enterprise AI cannot be governed only by components. It must be governed by *order*.

If *ordinal* means **ordered levels of authority, abstraction, risk, and execution**, then OSA is the construct that names those levels and the rules that connect them.

## Status of the construct

There does not appear to be an established mainstream EA discipline called "Ordinal Systems Architecture" — current search results do not show it as a recognized formal framework. That gives the construct room to be defined as a new contribution. Existing EA standards and languages already support adjacent ideas:

- **TOGAF** is positioned as an enterprise architecture methodology and framework.
- **ArchiMate** is designed to describe, analyze, and visualize relationships across business domains.
- **NIST AI RMF** reinforces the need for AI governance functions — *govern*, *map*, *measure*, *manage* — which fit naturally with an ordered control model.

OSA does not replace any of them. It supplies what they currently lack for Enterprise AI: a **control grammar** for authority across AI capability layers.

## The Ordinal Layers

### O0 — Enterprise Intent

The strategic layer. Mission outcomes, enterprise objectives, policy posture, risk appetite, regulatory constraints, approved AI operating principles.

This is where enterprise AI connects to **SARS**: Strategy, Architecture, Roadmaps, and Standards.

### O1 — Enterprise AI Orchestrator

The highest *operational* AI coordination layer. It does not "do all AI work." It **governs** routing, policy enforcement, identity, authorization, telemetry, model access, agent registration, and cross-domain coordination.

This layer answers:

- What may be done?
- By whom?
- With what model?
- Under what boundary?
- With what audit trail?

### O2 — Capability Domain Orchestrators

Domain-specific orchestration systems aligned to enterprise business or mission capabilities.

Examples:

- Development Orchestrator
- Infrastructure Operations Orchestrator
- Cybersecurity Orchestrator
- Mission Engineering Orchestrator
- Business Operations Orchestrator
- Digital Engineering Orchestrator

Each domain orchestrator inherits enterprise policy from O1 but applies **domain-specific** workflows, data boundaries, tooling, approval chains, and performance objectives.

### O3 — Agents and Workflows

Where agentic systems operate. Agents are **subordinate execution structures**. They do not define their own authority, access, or policy. They receive bounded tasks from orchestrators.

Examples:

- Code assistant agent
- Ticket triage agent
- Root-cause analysis agent
- Threat enrichment agent
- Requirements analysis agent
- Architecture documentation agent
- Test generation agent

The key distinction: **agents are workers, not governors.**

### O4 — Tools and Execution Channels

APIs, scripts, automation tools, CI/CD pipelines, ITSM integrations, cloud consoles, knowledge retrieval systems, engineering repositories, and data platforms.

This is where AI begins to affect enterprise state. Therefore this layer requires **strong execution boundaries**.

Read-only access, recommend-only access, draft-only access, supervised execution, and autonomous execution should be **separate ordinal permissions** — not a single Boolean.

### O5 — Data and Knowledge Substrate

Enterprise data, documents, tickets, logs, CMDB, architecture repositories, codebases, policy libraries, threat intelligence, design repositories, and operational telemetry.

This layer is **not passive**. In AI systems, data shapes output behavior. Context poisoning, stale documentation, ambiguous policies, and ungoverned retrieval pipelines become **architectural risks**, not mere data-quality issues.

### O6 — Outcome, Audit, and Feedback

Captures effects: decisions made, actions taken, human approvals, rejected actions, policy violations, hallucination incidents, cost, latency, model drift, security findings, and operational value.

This closes the loop. **AI architecture without outcome telemetry becomes unverifiable theater.**

## The Construct in One Sentence

**Ordinal Systems Architecture is an enterprise AI architecture pattern that organizes AI capability by ordered authority layers, ensuring that strategy governs orchestration, orchestration governs agents, agents govern tool use only within delegated boundaries, and all execution is traced back to enterprise intent.**

## The Governance Principle

```
No lower ordinal layer may expand its own authority.
Authority only flows downward.
Evidence must flow upward.
```

That is the architectural core. Every other rule is a consequence.

## Why this matters

The major advantage of OSA is that it prevents a common enterprise AI failure: **confusing intelligence with authority**.

A model may appear capable. That does not mean it should be authorized.

OSA makes that distinction explicit.

## Reference structure

```
O0  Enterprise Intent
    Mission, strategy, policy, risk appetite, standards

O1  Enterprise AI Orchestrator
    Governance, routing, identity, model access, policy enforcement

O2  Domain Orchestrators
    Development, infrastructure, cyber, mission, engineering, business

O3  Agents and Workflows
    Task-specific AI workers under bounded delegation

O4  Tools and Execution Channels
    APIs, automation, ITSM, CI/CD, cloud, repositories

O5  Data and Knowledge Substrate
    Documents, logs, CMDB, code, policies, telemetry, vector stores

O6  Outcome, Audit, and Feedback
    Evidence, metrics, decisions, incidents, drift, value realization
```

## Positioning vs. existing frameworks

OSA is **complementary** to TOGAF, UAF, ArchiMate, and NIST AI RMF, not a replacement:

- **TOGAF** gives you architecture method.
- **ArchiMate** gives you modeling language.
- **UAF** gives you systems-of-systems and mission alignment.
- **NIST AI RMF** gives you risk management vocabulary.
- **OSA** gives you the missing **control grammar** for enterprise AI authority.

See [`relationship-to-frameworks.md`](relationship-to-frameworks.md) for the detailed crosswalk.

## Thesis

> Enterprise AI needs an ordinal architecture because agentic systems are not merely applications. They are delegated actors inside a governed enterprise.
