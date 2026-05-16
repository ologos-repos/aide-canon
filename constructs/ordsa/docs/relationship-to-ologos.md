# OSA Relative to Ologos Constructs

OSA is a framework. Ologos Corp has been building concrete AI systems for a while, several of which sit cleanly at specific OSA layers. This file makes those relationships explicit so OSA can be read alongside the in-flight work, not treated as competing with it.

The constructs covered here:

1. **Modus Primus** — the multi-axis runtime architecture (modus-primus PR #28, candidate 12)
2. **OAgent framework** — Ologos's agent standard (oagent-core)
3. **Cross-fleet decision register** — the harness-agnostic consensus layer between Ologos AI and peer fleets

---

## Modus Primus — orthogonal axes, mapped onto OSA layers

Modus Primus cand-12 names five **horizontal axes of variation** along which any concrete enterprise-AI deployment varies:

| Axis | What varies |
|---|---|
| Tenant | Per-customer isolation boundary |
| User | Identity inside a tenant |
| Domain | Capability area inside a tenant |
| Agent | The specific worker invoked |
| Orchestrator | The coordinating runtime |

OSA's seven ordinal layers are **vertical** — they describe authority levels, not deployment variations. The two are orthogonal:

| Modus Primus axis | Sits at OSA layer |
|---|---|
| Orchestrator | O1 (Enterprise) and O2 (Domain) — Modus Primus's orchestrator stack populates both |
| Domain | O2 — each Modus Primus domain is a distinct O2 |
| Agent | O3 — the agent axis is exactly OSA's agent layer |
| User | O1 identity surface — propagated through every lower layer |
| Tenant | A cross-cutting envelope on every layer — present at every ordinal, not "at" one |

The right way to read this: **Modus Primus is a concrete reference implementation of OSA's O1 and O2 layers, with the axes describing how that implementation varies across deployments.**

A second clarification, since the question will come up: OSA does **not** replace Modus Primus. Modus Primus is the *runtime stack*; OSA is the *authority grammar* the runtime stack must satisfy. A Modus Primus deployment that does not respect "authority flows downward, evidence flows upward" is an incorrect Modus Primus deployment — not a counter-example to OSA.

## OAgent framework — Ologos's agent standard at O3

The OAgent framework (maintained at `ologos-corp/oagent-core` and related repos) is Ologos's specification of what an agent is, how it registers, how it declares capabilities, and how it surfaces evidence.

In OSA terms:

- **OAgents live at O3.** Every OAgent is, by definition, a subordinate execution structure registered to an orchestrator.
- **OAgent registration is an O1 concern.** The registration ledger that says "this agent exists and may be dispatched against these task classes" is part of O1's responsibility.
- **OAgent capability declarations are hints, not authorizations.** Per OSA O3's anti-pattern list — *tool affinities as authorization* is wrong. An OAgent's declared toolset is a hint to the orchestrator; the envelope is what authorizes.
- **OAgent evidence flows to O6.** Every action an OAgent takes produces evidence; that evidence is part of O6's append-only record.

The OAgent framework is the **agent standard** that makes O3 implementable consistently across the Ologos ecosystem. OSA gives OAgents the authority frame they operate inside; OAgents give OSA's O3 a concrete shape.

## Cross-fleet decision register — governance across fleets

Ologos AI participates in a cross-fleet register (`ologos-corp/cross-ai`) of ADRs and architecture summaries shared with peer fleets (currently thinx-Claude, with JD Longmire as principal). Per ADR-GOV-0001 the register is authoritative on cross-fleet conflicts.

The register **is not** a layer in OSA. It is an **external governance artifact** that informs O0 across multiple enterprises and fleets simultaneously. Several relationships are worth naming:

- **Register-ratified ADRs influence O0.** When an ADR establishes a cross-fleet decision (e.g., on identity models or evidence formats), each fleet's O0 is expected to align unless it has explicit grounds to dissent. The register supersedes local memory on conflict — and by analogy, supersedes single-fleet O0 statements on shared topics.
- **OSA itself may be ratified via the register.** Once OSA v0.1 is published, a cross-fleet ADR ratifying OSA as the shared authority grammar would make the construct binding across all fleets that adopt the register.
- **Per-fleet adoption stays per-fleet.** The register names what *is decided*; how each fleet structures its O1 / O2 / O3 implementation against OSA is still local.

This relationship will be operationalized through an ADR in `cross-ai/reference/governance/decisions/` once OSA v0.1 has had review.

---

## Naming clarity

For internal Ologos discussions where these constructs coexist:

- **OSA** = the construct. Vendor-neutral. Defines authority and layers.
- **Modus Primus** = the runtime stack populating OSA's O1+O2 in the Ologos ecosystem.
- **OAgent framework** = the agent standard populating OSA's O3 in the Ologos ecosystem.
- **Ologos AI Operations** = the operational practice of running the stack (dev-first, QA, dual-push, etc.). Lives across O0 (operating principles) and O6 (evidence and audit).

None of these are interchangeable. Pull on the right thread depending on the question:

- "What may be done?" → OSA (and via OSA, the relevant orchestrator's policy)
- "How does the runtime express the user/tenant/domain split?" → Modus Primus
- "How do I build a new agent?" → OAgent framework
- "What is our operating discipline this quarter?" → Ologos AI Operations
