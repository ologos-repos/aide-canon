# ADR-EA-0025 — Instance VSOK derivation: AIDE instances branch from the corpus VSOK

- **Status:** Accepted (operator-ratified 2026-05-27 by JD Longmire via the operator channel; same in-session override pattern as ADR-EA-0010 — methodology extension, not a positioning or scope change)
- **Date:** 2026-05-27
- **Author:** JD Longmire (decision); OlogosAI (ADR drafted)
- **Reviewers:** @jdlongmire; thinx-Claude (canon co-maintainer)
- **Extends:** [ADR-EA-0010](ADR-EA-0010-adopt-doerr-okr-methodology.md) (Doerr OKR methodology for VSOK) · [ADR-EA-0007](ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) (VSOK as the Tier-0 structured artifact)
- **First realized by:** `ologos-repos/ng-aide-01` (instance VSOK; adopted instance-side by ADR-NGAIDE-0002)

## Context

[ADR-EA-0007](ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) established VSOK (Vision · Strategy · Objectives · Key Results) as the Tier-0 structured artifact, and [ADR-EA-0010](ADR-EA-0010-adopt-doerr-okr-methodology.md) locked the Doerr OKR methodology for its Objectives and Key Results. Both spoke to a **single, corpus-level VSOK** — its Objectives are corpus-strategic: external recognition, external adoption, governance anchoring, discoverability (see [`vision-strategy/vsok/objectives/`](../vision-strategy/vsok/objectives/) O1–O4).

That register's *"What's not in this set"* section explicitly **held out** internal/operational/exemplar objectives — *"internal use is implementation evidence, but the strategic goal is external recognition, not internal completeness."* The hold-out was correct for the *corpus* register, but it left a real category homeless: **a deployed AIDE instance has genuine strategic objectives** (stand the platform up, conform to the architecture, deploy across sites, operate it) that are not corpus-altitude and should not inflate the corpus register — yet are exactly the goals that *produce the evidence* the corpus objectives measure.

This surfaced concretely with **NG-AIDE-01**, the first customer-grade instance. It already carried a prose `vision-strategy/` with nine "Strategic Objectives," but no VSOK structure and no objective asserting that the instance *conforms to the canon's substrate (Means) requirements*. The question — *where do instance objectives live?* — is general: every AIDE instance hits it, not just NG-AIDE-01. So it is resolved at the canon level.

## Decision

**An AIDE instance MAY maintain its own VSOK that *branches* from the corpus VSOK.** A branched instance VSOK has the same four slots and follows the same Doerr methodology ([ADR-EA-0010](ADR-EA-0010-adopt-doerr-okr-methodology.md)), with this derivation contract:

1. **Vision — inherited by reference.** The instance does **not** restate or fork the corpus Vision. It advances the same Vision (*"AIDE as an exemplar for next-generation enterprise IT transformation"*) by being a **worked exemplar** of it. The instance Vision slot links up to the corpus Vision and states the instance's exemplar role.

2. **Strategy — inherited by reference.** The instance inherits the corpus Strategy, optionally adding a short instance-positioning paragraph. It does not author a competing strategy.

3. **Objectives — instance-scoped.** Doerr-shaped objectives for **building, conforming, deploying, and operating that instance**. These are the objectives the corpus register holds out by design.

4. **Key Results — instance-scoped.** Quantitative, dated, stretch-calibrated signals anchoring the instance objectives (conformance pass/fail, build milestones, deployment go-lives).

**Directional relationship.** Instance objectives are **downstream** of corpus objectives: a live, conformant instance is itself a Key-Result signal for corpus objectives (e.g., corpus O2, external adoption / AEON-deployed exemplar). Authority/derivation flows **down** (corpus Vision/Strategy → instance); evidence flows **up** (instance conformance + deployment → corpus KRs) — the same OrdSA orientation the architecture uses everywhere else.

**Placement.** A branched instance VSOK lives **in the instance's own repository** (e.g., `ng-aide-01/vision-strategy/vsok/`), not in the canon — consistent with instances being instantiations of the architecture rather than members of the corpus. The branch relationship is expressed by reference (links up to the canon), not by duplication.

## Consequences

- **The corpus VSOK objectives register is amended** (this batch): the held-out "operational/exemplar" and "internal operational dependency" bullets now point instance objectives to the instance's branched VSOK rather than to "mission docs / not in VSOK," and an *"Instance VSOKs (branched)"* section is added. No corpus *Objective* changes — O1–O4 are untouched.
- **A reusable pattern exists** for every future AIDE instance, so instance objectives land consistently instead of being reinvented per deployment or smuggled into the corpus register.
- **No new tier or methodology.** This is a derivation rule layered on the existing VSOK tier (ADR-EA-0007) and Doerr methodology (ADR-EA-0010); both stand unchanged.
- **Migration burden: none for the corpus.** Instances that already carry prose vision-strategy content (NG-AIDE-01) reshape it into the branched VSOK structure instance-side; that work is governed by an instance-local ADR, not this one.

## Alternatives considered

- **A 5th corpus Objective for instance/operational outcomes.** Rejected: contradicts the corpus register's deliberate external-recognition altitude and the documented "what's not in this set" reasoning; would double-count exemplar work that already feeds corpus KRs, and would mix a specific instance's build detail into a corpus-wide register.
- **Instance objectives in the instance README only (no VSOK).** The status quo for NG-AIDE-01. Rejected: prose objectives without the Doerr O↔KR structure are not measurable or auditable, and there is no defined relationship to the corpus frame — exactly the gap a branched VSOK closes.
- **One shared VSOK with instance sub-sections inside the canon.** Rejected: puts instance-specific content in the corpus repo, conflating instances (instantiations) with the corpus (the model), and re-inflates the register the branch is meant to keep lean.

## References

- [ADR-EA-0007](ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) — VSOK as Tier-0 structured artifact (the tier this derivation rule layers on)
- [ADR-EA-0010](ADR-EA-0010-adopt-doerr-okr-methodology.md) — Doerr OKR methodology (inherited unchanged by branched instance VSOKs)
- [ADR-EA-0008](ADR-EA-0008-reframe-corpus-authorship.md) — corpus-as-independent-research framing (why the corpus register stays external-strategic)
- [`vision-strategy/vsok/objectives/`](../vision-strategy/vsok/objectives/) — the corpus Objectives register amended by this ADR (§ *Instance VSOKs (branched)*)
- `ologos-repos/ng-aide-01` — first instance to realize this pattern; adopted instance-side by **ADR-NGAIDE-0002** (which also references the instance deployment-substrate decision, ADR-NGAIDE-0001)
