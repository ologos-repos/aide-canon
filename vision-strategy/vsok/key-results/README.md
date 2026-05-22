# key-results/ — Key Results (reserved)

The **Key Results** slot of [VSOK](..) within [Vision-Strategy](../..). Reserved placeholder; first population pending [Objectives](../objectives/) authoring (per [ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md)).

## What this slot holds

Measurable outcomes that anchor [Objectives](../objectives/). Each Key Result is a concrete, observable signal — quantified threshold or pass/fail — that signals progress on its parent Objective.

Key Results are Doerr's OKR accountability layer: they make Objectives auditable without requiring deep familiarity with the corpus's argument.

## Methodology

Key Results in this slot are constructed per **John Doerr's OKR methodology** (per [ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md)). The framework's normative properties:

- **Quantitative** — measurements with concrete thresholds; never adjectives
- **Specific** — exactly one observable outcome per KR, with explicit threshold and time horizon
- **Time-bound** — each KR has a measurement date or window
- **Stretch-calibrated** — like Objectives, KRs require effort; ~70% attainment is good
- **Cardinality** — 3–5 Key Results per Objective

Anti-pattern example: *"Increase AIDE citations"* — vague, no threshold, no date.
Well-formed example: *"At least 5 third-party citations of the AIDE corpus on Zenodo by 2027-Q4."*

KRs derive from the same SOTA-vs-AIDE gap analysis that produces Objectives. Each KR ties to observable SOTA movement: published adoptions, named citations, conformance test results, deployment milestones, etc.

## Status

Reserved. The canon commits to populating Key Results once Objectives are authored. The empty slot is an explicit IOU per [ADR-EA-0007 §Consequences](../../../decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md); methodology is locked per [ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md).
