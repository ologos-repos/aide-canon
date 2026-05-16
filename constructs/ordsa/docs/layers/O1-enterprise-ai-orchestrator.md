# O1 — Enterprise AI Orchestrator

> Governance, routing, identity, model access, policy enforcement.

## Definition

The highest *operational* AI coordination layer. O1 does not "do all the AI work." It **governs** it.

O1 is the runtime translation of O0 policy into enforceable decisions about who may do what, with what model, against what data, with what audit trail.

## Authority boundary

- **Receives:** policy and constraints from O0.
- **Sets:** identity binding, model access, routing rules, cross-domain coordination, telemetry collection.
- **Delegates to:** O2 domain orchestrators, each with a bounded subset of authority for its domain.
- **Cannot be bypassed by:** O3 agents, O4 tools, or O5 data pipelines reaching past it.

If an action can be taken in the enterprise without first being authorized by the O1 layer or its delegate, that is a **governance gap**, not a feature.

## What O1 answers

Every AI invocation in the enterprise must produce answers to:

1. **What may be done?** — Is this task within the policy envelope?
2. **By whom?** — Identity of the requesting human, agent, or system, with attribution chain.
3. **With what model?** — Which approved model handles this task, at what tier?
4. **Under what boundary?** — What data is in-scope, what tools are in-scope, what is the impact ceiling?
5. **With what audit trail?** — What evidence must be captured for O6?

If any of those answers is missing, O1's job is to refuse the invocation, not let it proceed and "log it for later."

## What lives here

- Identity binding for humans, agents, and service principals
- Authorization gates (role, group, tenant, attribute-based)
- Model registry — approved models, their tiers, their authorized use cases
- Routing logic — which model handles which task class
- Telemetry collection and forwarding to O6
- Agent registration — every active agent in the enterprise is known here
- Cross-domain coordination — when a task crosses O2 boundaries, O1 is the broker

## What does not live here

- Domain-specific workflows (O2)
- Agent task logic (O3)
- Tool invocations themselves (O4)
- Data retrieval (O5)
- Outcome metrics (O6)

O1 is the air-traffic-control layer. It does not fly the planes. It clears them to take off.

## Anti-patterns

- **The "smart router" that has no policy view.** An orchestrator that picks models on latency or cost alone, without consulting O0 policy, is not an O1 — it is an O4 disguised as governance.
- **Agents that authenticate to tools directly.** If an O3 agent can present credentials to an O4 tool without O1 in the path, O1 is decorative.
- **Implicit identity.** Operations where the "user" is the orchestrator's service principal. O1 must propagate the originating-actor identity, not collapse it.
- **Policy in code only.** Authorization logic encoded inline in orchestrator code instead of as inspectable, versioned policy. Auditable policy beats clever code.

## Evidence flowing up

To O0 (via O6): aggregate authorization decisions, refusal rates and reasons, model-routing distribution, identity propagation health, gaps where policy was inexpressible at runtime.

## See also

- [O0 — Enterprise Intent](O0-enterprise-intent.md) — the policy O1 enforces
- [O2 — Domain Orchestrators](O2-domain-orchestrators.md) — where O1 delegates
- [`../reference-implementations.md`](../reference-implementations.md) — concrete O1 implementations (forward placeholder)
