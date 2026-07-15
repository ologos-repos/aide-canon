# vsok/ — V/S/O/K methodology product

The structured artifact that operationalizes [Vision-Strategy](..) into four named slots. VSOK decomposes the corpus's umbrella strategic frame into discrete, navigable components — each slot reserved for its own artifact.

For a full guided tour of this slot + the analysis peer, see [`vision-strategy/README.md`](..).

## The four slots

| Slot | What it carries | State |
|---|---|---|
| [`vision/`](vision/) | Long-horizon outcome the corpus advances toward | **Populated** (1–3 yr AI-speed horizon; *"AI-enabled Digital Ecosystems as an exemplar for next-generation Enterprise IT transformation"*) |
| [`strategy/`](strategy/) | Positioning argument bridging Vision to action — carries *Enterprise Agentic AI Platform Strategy* | **Populated** (relocated from `enterprise-platforms/strategy/` per [ADR-EA-0007](../../decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md)) |
| [`objectives/`](objectives/) | Doerr-style qualitative strategic goals deriving from Vision | **Populated — v0.2** (SOTA-survey-derived, ratified 2026-06-02; O1–O5) |
| [`key-results/`](key-results/) | Doerr-style quantitative measurable signals anchoring Objectives | **Populated — v0.2** (KRs for O1–O5; survey-confirmed + KR5.x new) |

## Methodology

Objectives and Key Results are constructed per **John Doerr's OKR methodology** (*Measure What Matters*) — qualitative, ambitious, time-bound objectives anchored by quantitative, specific, stretch-calibrated key results. 3–5 of each at any horizon. ~70% attainment indicates a well-calibrated OKR.

Locked by [ADR-EA-0010](../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md). See that ADR for the SOTA-driven derivation pattern (catch-up / defend-and-extend / converge-or-differentiate Objective shapes).

This is the **corpus** VSOK. AIDE *instances* maintain their own VSOK that **branches** from it — inheriting Vision + Strategy by reference and holding instance-scoped Objectives + Key Results — per [ADR-EA-0025](../../decisions/ADR-EA-0025-instance-vsok-derivation.md). See [`objectives/` § Instance VSOKs](objectives/#instance-vsoks-branched).

## Evidence base

Objectives + Key Results derive from the SOTA-vs-AIDE gap analysis in the **[`analysis/`](../analysis/)** peer artifact (sibling at Tier 0, not a sub-folder of VSOK). The survey produces classified findings; Doerr-shaped Objectives consume them.

## Why VSOK is *inside* Vision-Strategy, not its own tier

Vision-Strategy is the *umbrella concept*; VSOK is the methodology product that operationalizes the umbrella. Conflating them would (a) lock Tier 0's artifact surface to exactly four slots with no room for additional umbrella-altitude artifacts (investment thesis, market positioning brief), and (b) cause naming redundancy in hierarchy listings ("Tier 0 — VSOK / VSOK paper").

Separating the tier from the artifact preserves a clean *tier ↔ artifact* relationship throughout the canon and keeps Tier 0's artifact surface open. See [ADR-EA-0007 §Alternatives considered (option 6)](../../decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) for the full reasoning.
