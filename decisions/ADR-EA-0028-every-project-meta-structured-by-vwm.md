# ADR-EA-0028 — Every Project is meta-structured by the VWM process (enterprise → systems → solutions baselines)

- **Status:** Proposed (drafted by thinx-Claude on JD-Founder direction; for OlogosAI canon-prime authoring + JD ratification)
- **Date:** 2026-06-18
- **Author:** thinx-Claude (operator-altitude per ADR-EA-0017), drafting in collaborator mode on JD's direction. Canon-prime authorship/ownership to OlogosAI per ADR-EA-0017; this is a proposal for adoption, not a canon-prime act.
- **Reviewers:** JD Longmire (Founder ratification — pending); OlogosAI (canon-prime review — pending)
- **Related:** [ADR-EA-0007](ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) (VSOK at Tier 0), [ADR-EA-0010](ADR-EA-0010-adopt-doerr-okr-methodology.md) (Doerr OKR for O/K), [ADR-EA-0025](ADR-EA-0025-instance-vsok-derivation.md) (instance branched-VSOK derivation)

## Context

The canon defines the pieces but not the mandate:

- **VSOK** (Vision · Strategy · Objectives · Key Results) is the Tier-0 enterprise-strategic artifact (EA-0007), with Doerr's OKR methodology for its Objectives and Key Results (EA-0010).
- **Branched-VSOK** (EA-0025): an instance inherits the corpus Vision + Strategy by reference and holds its own instance-scoped Objectives + Key Results in its own repo; authority flows down, evidence flows up.
- The **WBS/MBSE** decomposition into `1-enterprise-baseline` / `2-systems-baseline` / `3-solutions-baseline` is the working structure across instances (NG-AIDE, aide-core, ologos-office), traced at session-wrap (Method #21).

What is missing is a **rule requiring every Project to adopt this meta-structure**. Projects have been structured ad hoc — some carry the three baselines, others carry prose vision-strategy or nothing. The result is uneven discoverability, traceability, and portfolio comparability. JD directs that the structure be **mandatory and uniform**.

The combined process is named **VWM = VSOK · WBS · MBSE**.

## Decision

1. **Every Project is meta-structured by the three baselines:** `1-enterprise-baseline/`, `2-systems-baseline/`, `3-solutions-baseline/` (the WBS/MBSE decomposition).

2. **Every Project follows the VWM process:**
   - **VSOK** at the enterprise baseline (`1-`): Vision (inherited by reference per EA-0025), Strategy, Objectives, Key Results — the enterprise-strategic frame.
   - **WBS / MBSE** decomposing downward: systems architecture at `2-`, concrete solution/build at `3-`, with the MBSE spine traced end-to-end.

3. **Branched-VSOK attach (per EA-0025):** a Project inherits its parent/corpus Vision + Strategy by reference and holds its own instance-scoped Objectives + Key Results under `1-enterprise-baseline/vision-strategy/vsok/`. Authority/derivation flows down; conformance/evidence flows up.

4. **Scope:** applies to **every Project** — instances, products, and programs — in the Ologos / AIDE corpus. Pre-existing prose vision-strategy is reshaped into the branched VSOK structure by an instance-local ADR (no corpus migration burden, per EA-0025).

## Consequences

- **(+)** Uniform structure across the portfolio → discoverability, traceability, comparability; enables VWM-level program management.
- **(+)** The MSFT-parity / M365-equivalence program (`ologos-office`) is the first worked explication target.
- **(−)** Per-Project scaffolding cost — mitigated by a project-scaffold template (a Means surface).
- **(−)** Enforcement needs a surface: a scaffold check at Project creation + the existing MBSE-baseline trace (Method #21) extended to assert the three baselines exist.

## Rollout

- **New Projects:** scaffold the three baselines from a template at creation.
- **Existing Projects:** reshape incrementally via an instance-local ADR (no big-bang migration).
- **First instance:** explicate the MSFT-parity program across `ologos-office`'s `1-/2-/3-` baselines as the worked example.
