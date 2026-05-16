# O2 — Capability Domain Orchestrators

> Development, infrastructure, cyber, mission, engineering, business.

## Definition

Domain-specific orchestration systems aligned to enterprise business or mission capabilities. Each O2 inherits its authority envelope from O1 and applies it to its own domain's workflows, data boundaries, tooling, approval chains, and performance objectives.

O2 is where enterprise policy meets domain reality. A "cybersecurity orchestrator" and a "development orchestrator" share the same governance grammar — but the *content* of their policies differs because their domains differ.

## Authority boundary

- **Receives:** delegated authority from O1, scoped to the domain.
- **Sets:** domain-specific workflows, approval chains, agent rosters, tool allow-lists within the delegation.
- **Cannot:** widen its own scope, reach into another O2's domain without going through O1.

A development orchestrator that can deploy production infrastructure is not really a development orchestrator — it has effectively merged with the infrastructure orchestrator, and the architecture should say so explicitly.

## Examples

- **Development Orchestrator** — code authoring, code review, test generation, build coordination
- **Infrastructure Operations Orchestrator** — capacity, deployment, configuration management, observability response
- **Cybersecurity Orchestrator** — threat enrichment, vulnerability triage, response playbook execution
- **Mission Engineering Orchestrator** — requirements decomposition, mission-thread analysis, model-based engineering
- **Business Operations Orchestrator** — ticketing, customer interactions, internal process automation
- **Digital Engineering Orchestrator** — design artifact management, simulation orchestration, digital-thread integration

A given enterprise will not have all of these, and may have ones not listed. The pattern is what matters: **per-domain orchestrator with bounded delegation, not a single super-orchestrator pretending to know every domain.**

## What lives here

- Domain workflows and playbooks
- Domain-specific agent roster (which O3 agents are registered for which domain tasks)
- Domain tool allow-list (which O4 tools the agents may invoke for which task classes)
- Domain approval chains (which humans approve which class of action)
- Domain performance objectives (latency, throughput, accuracy targets)
- Domain data scope (which O5 stores the domain may query, and under what conditions)

## What does not live here

- Identity binding (O1)
- Approved-model registry (O1 — domains pick *from* the approved list, they don't approve models)
- Cross-domain coordination logic (O1)
- Strategic policy (O0)

## Anti-patterns

- **The omnibus orchestrator.** One system claiming all domains. Tends to collapse policy distinctions and produce one-size-fits-no-one workflows.
- **Domain bleed.** A development orchestrator that quietly takes infrastructure actions because "the agent had the tool available." Symptom that O1's delegation is too broad.
- **Implicit domain boundaries.** Two O2s share a workflow without naming the handoff. Risk: the responsibility for the action is ambiguous when it goes wrong.
- **Domain hierarchy creep.** O2s starting to delegate to "sub-O2s." If a sub-orchestration emerges, name it: either it is a distinct O2, or it is a workflow inside the existing O2 — not a hidden layer.

## Evidence flowing up

To O1 (and via O1 to O0/O6): workflow completion rates, approval-chain timing, agent-roster usage, domain-policy violation events, and where the domain delegation envelope was insufficient for the task being requested.

## See also

- [O1 — Enterprise AI Orchestrator](O1-enterprise-ai-orchestrator.md) — the layer that delegates to O2
- [O3 — Agents and Workflows](O3-agents-workflows.md) — what O2 governs
- [`../reference-implementations.md`](../reference-implementations.md) — concrete O2 implementations (forward placeholder)
