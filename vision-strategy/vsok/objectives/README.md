# objectives/ — Objectives (reserved)

The **Objectives** slot of [VSOK](..) within [Vision-Strategy](../..). Reserved placeholder; first population pending SOTA gap analysis (per [ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md) §2).

## What this slot holds

Strategic goals deriving from [Vision](../vision/). Each Objective is a discrete, named outcome the corpus pursues over a defined horizon — concrete enough to be tracked, abstract enough to span multiple platforms or constructs.

Objectives sit between Vision (long-horizon, aspirational) and [Key Results](../key-results/) (measurable, near-term). Each Objective is anchored by one or more Key Results.

## Methodology

Objectives in this slot are constructed per **John Doerr's OKR methodology** (per [ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md)). The framework's normative properties:

- **Qualitative** — stated as outcomes, not metrics
- **Ambitious** — stretch-calibrated; ~70% attainment indicates a well-calibrated Objective
- **Time-bound** — each Objective declares its evaluation horizon
- **Memorable** — one sentence; one phrase where possible
- **Cardinality** — 3–5 Objectives at any given horizon

Objectives derive from the SOTA-vs-AIDE gap analysis (housed at [`../../analysis/`](../../analysis/) — *to be created*). The derivation pattern:

- **Where AIDE is behind SOTA** → catch-up Objectives
- **Where AIDE is ahead of SOTA** → defend-and-extend Objectives
- **Where work is in flight elsewhere** → converge-or-differentiate Objectives

## Status

Reserved. The canon commits to populating Objectives once the SOTA gap analysis lands. The empty slot is an explicit IOU per [ADR-EA-0007 §Consequences](../../../decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md); methodology is locked per [ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md).
