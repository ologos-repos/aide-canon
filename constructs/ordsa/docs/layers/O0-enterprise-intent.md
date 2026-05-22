# O0 — Enterprise Intent

> Mission, strategy, policy, risk appetite, standards.

## Definition

The strategic layer. O0 holds what the enterprise *wants to be true* about how AI is used: mission outcomes, business and operational objectives, policy posture, risk appetite, regulatory constraints, and approved AI operating principles.

O0 is not an AI system. It is the **specification** every AI system below it must be answerable to.

## Authority boundary

- **Sets:** the constraints all lower ordinals operate within.
- **Cannot be modified by:** any lower ordinal. Not by orchestrators, not by agents, not by tools.
- **Modified by:** the enterprise governance process (executives, board, compliance, regulatory updates) — not by AI activity.

This layer is sometimes summarized as **SARS**: Strategy, Architecture, Roadmaps, Standards.

## What lives here

- Mission and strategic objectives
- AI operating principles (e.g., "human approval required for any state-changing action above impact level X")
- Risk appetite statements (per category — financial, reputational, safety, compliance)
- Regulatory and statutory constraints (sector-specific: HIPAA, ITAR, FedRAMP, GDPR, etc.)
- Enterprise architecture standards
- Approved-vendor and approved-model lists (the *policy*; the *enforcement* is at O1)

## What does **not** live here

- Specific tools, APIs, or runtime configuration (that is O4)
- Agent definitions (O3)
- Domain workflows (O2)
- Model routing logic (O1)

O0 is policy. Everything below is implementation against that policy.

## How lower layers consume O0

O1 (Enterprise AI Orchestrator) is the layer responsible for **translating** O0 into enforceable runtime decisions. Domain orchestrators (O2) inherit those translations and refine them within their domain's scope.

If a policy at O0 cannot be expressed as an enforceable check at O1, that is a gap in the architecture, not a license for the lower layers to act unbounded.

## Anti-patterns

- **Aspirational-only policy.** Statements at O0 that no lower layer can verify or enforce. Risk: policy becomes documentation, not control.
- **Component-level policy at O0.** Mentioning a specific vendor or product at the strategy layer locks the architecture to a procurement decision. Keep O0 vendor-neutral.
- **Silent O0 drift.** Updating policy without re-deriving the O1 enforcement implications. Risk: enforcement keeps running on stale assumptions.

## Evidence flowing up

From the bottom, O0 should see (via O6): aggregate policy-violation rates, regulatory-exposure summaries, risk-tolerance breaches, and rejected-action analytics. O0 does not need every event — it needs the rate and the outliers.

## See also

- [O1 — Enterprise AI Orchestrator](O1-enterprise-ai-orchestrator.md) — the layer that translates O0 into enforceable runtime decisions
- [O6 — Outcome, Audit, Feedback](O6-outcome-audit.md) — what flows back up to O0
- [`../relationship-to-frameworks.md`](../relationship-to-frameworks.md) — how O0 maps to TOGAF strategy and NIST AI RMF *Govern*
