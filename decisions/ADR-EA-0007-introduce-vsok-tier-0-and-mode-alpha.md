# ADR-EA-0007 — Introduce Vision-Strategy at Tier 0 (VSOK as artifact) and rename Tier 1 to Mode Alpha

- **Status:** Accepted
- **Date:** 2026-05-22
- **Author:** JD Longmire
- **Reviewers:** @jdlongmire
- **Amends:** [cross-ai #40 Refinement B](https://github.com/ologos-corp/cross-ai/issues/40) (Strategy classification + canon tier shape); applies post-stand-up to the structure landed by [ADR-EA-0006 (aide-canon umbrella migration)](https://github.com/ologos-repos/aide-canon/blob/main/decisions/ADR-EA-0006-migrate-corpus-to-aide-canon.md).
- **Ratification note:** Comment-out period waived by explicit maintainer ratification (JD Longmire, 2026-05-22). Basis: sole-maintainer status, substantive deliberation captured in cross-ai #40 plus the in-session conversation that generated this ADR, and the ADR being a refinement-grade follow-up to a recently-ratified parent (cross-ai #40 Refinement B). enterprise-ai is slated for archival per ADR-EA-0006 (migration); the canonical version of this ADR lives at [`ologos-repos/aide-canon/decisions/ADR-EA-0007-*.md`](https://github.com/ologos-repos/aide-canon/blob/main/decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md).
- **Numbering note:** Initially committed as ADR-EA-0006 (commits [`e43ae5f`](https://github.com/osa-ai-org/enterprise-ai/commit/e43ae5f) + [`250267c`](https://github.com/osa-ai-org/enterprise-ai/commit/250267c)). The 0006 slot was held in parallel by OlogosAI's umbrella migration ADR (committed earlier at 13:48 CDT to aide-canon's dev branch, merged via PR #2). Neither party saw the other's draft until after both landed. Per CONTRIBUTING.md sequential-numbering rule, this ADR renumbers to **ADR-EA-0007**; OlogosAI's umbrella migration ADR holds the canonical 0006 slot.
- **In-session amendment (2026-05-22, same-day):** Initial commit framed Tier 0 *as* VSOK. JD refined within the authoring session: Tier 0 is **Vision-Strategy** (the umbrella concept), and **VSOK** is a structured artifact *inside* Tier 0 (the methodology product that decomposes the umbrella into V/S/O/K). The Decision section below reflects the refined framing; the original framing is recorded under Alternatives considered (option 6).

## Context

The canon structure ratified in [cross-ai #40](https://github.com/ologos-corp/cross-ai/issues/40) established a four-tier hierarchy for `ologos-repos/aide-canon`:

- **Tier 1 — Master Thesis:** AI-centric Digital Ecosystem (synthesis)
- **Tier 2 — Foundation:** HCAE, AIDK, RLEG
- **Tier 3 — Constructs:** DEA, OrdSA, MxM, OAgents
- **Tier 4 — Enterprise Platforms:** Strategy, AEON, AIDEX, OAAD (HCAE moved to Foundation per Refinement B)

The AIDE Architecture Overview infographic (`ologos-repos/aide-canon/infographics/AIDE-Architecture-Overview.png`, v1 published 2026-05-22) surfaced two structural issues with the ratified shape on review:

1. **Strategy is not a platform peer.** AEON, AIDEX, and OAAD are buildable software targets. *Enterprise Agentic AI Platform Strategy* is umbrella positioning — a CIO/CTO-altitude artifact arguing for the platforms beneath it. cross-ai #40 Refinement B addressed this by flagging Strategy `buildable: false` in `MANIFEST.yaml` while leaving it co-located with the platforms. The flag acknowledged the altitude mismatch without resolving it; an agent reading the canon's tier structure still sees Strategy as a Tier 4 peer.

2. **"Master Thesis" reads narrow.** The Tier 1 label connotes academic-degree framing. The artifact it points to is the corpus's primary synthesizing orientation, not a degree submission. A naming consistent with the corpus's own architectural vocabulary is preferred.

The infographic also displayed HCAE in both Tier 2 (Foundation) and Tier 4 (Enterprise Platforms) — a duplication inconsistent with cross-ai #40 Refinement B. That correction is captured here alongside the structural amendments below.

## Decision

### 1. Introduce Tier 0 — Vision-Strategy (umbrella concept), with VSOK as the structured artifact inside

Add a new top-level tier above Tier 1, named **Vision-Strategy** — the corpus's enterprise-strategic frame at the umbrella altitude. The tier carries the corpus's strategic direction (the *what* and *why* at corpus level) and points downward into Mode Alpha (which carries the synthesizing argument).

**VSOK** lives as a structured artifact *inside* Vision-Strategy. VSOK is the methodology product that operationalizes Vision-Strategy into four named slots:

- **V**ision — long-horizon outcome the corpus advances toward
- **S**trategy — the positioning argument that bridges Vision to action; carries the *Enterprise Agentic AI Platform Strategy* paper (migrated from Tier 4 enterprise-platforms)
- **O**bjectives — strategic goals deriving from Vision
- **K**ey Results — measurable outcomes anchoring Objectives

The separation matters: **Vision-Strategy is the *tier*; VSOK is one of the *artifacts* within it.** Future artifacts at Tier 0 may sit alongside VSOK (e.g., investment thesis, market positioning brief) without expanding or fragmenting the methodology product. VSOK's four slots remain stable as a single methodology output; the tier's artifact surface can grow if the corpus's strategic frame requires additional umbrella-altitude work.

At stand-up time, only the Strategy artifact (existing paper) is populated. Vision and the remaining VSOK slots (Objectives, Key Results) are reserved placeholders the canon commits to populating over time.

### 2. Rename Tier 1 — Master Thesis → Mode Alpha

The synthesizing artifact at Tier 1 remains *AI-centric Digital Ecosystem*. The tier label changes from **Master Thesis** to **Mode Alpha** — the corpus's primary orientation mode (α).

The naming aligns with Greek-letter precedent already present in the corpus's deliberations (cross-ai #40 ADR-prefix decision used Pattern α). It scales naturally: Mode Beta, Mode Gamma reserved for future orientation modes if the corpus's intellectual surface broadens.

### 3. Tier 4 — Enterprise Platforms shrinks to three

Tier 4 becomes the buildable-software trio: **AEON, AIDEX, OAAD**.

- *Strategy* lifts to Tier 0 (VSOK / Strategy)
- *HCAE* was already migrated to Foundation per cross-ai #40 Refinement B; the prior infographic erroneously showed it in both tiers. This ADR corrects the visual record alongside the structural amendments.

### 4. Repository surface

The canon's directory layout changes as follows (relative to the cross-ai #40 ratified shape):

```
aide-canon/
├── vision-strategy/               # NEW — Tier 0 (umbrella)
│   ├── README.md                  # tier overview + how VSOK relates to other artifacts that may land here
│   └── vsok/                      # structured artifact: the V/S/O/K methodology product
│       ├── README.md              # VSOK methodology overview
│       ├── vision/                # reserved (artifact TBD)
│       ├── strategy/              # Enterprise Agentic AI Platform Strategy (relocated from enterprise-platforms)
│       ├── objectives/            # reserved (artifact TBD)
│       └── key-results/           # reserved (artifact TBD)
├── mode-alpha/                    # RENAMED from thesis/ (Tier 1)
│   └── ...                        # AI-centric Digital Ecosystem synthesis (forthcoming)
├── foundation/                    # unchanged (Tier 2 — HCAE, AIDK, RLEG)
├── constructs/                    # unchanged (Tier 3 — DEA, OrdSA, MxM, OAgents)
├── enterprise-platforms/          # unchanged shape, three subdirs only (Tier 4)
│   ├── aeon/
│   ├── aidex/
│   └── oaad/
├── related-work/                  # unchanged
│   └── theseus/
├── infographics/                  # unchanged
└── decisions/                     # unchanged
```

`enterprise-platforms/strategy/` is **removed** (Strategy migrates to `vision-strategy/vsok/strategy/`). `enterprise-platforms/hcae/` is not created (HCAE lives in `foundation/hcae/` only — already correct per the stand-up).

**Sequencing.** OlogosAI's umbrella migration ADR (ADR-EA-0006) landed the canon stand-up with the cross-ai #40 Refinement B shape (Strategy under `enterprise-platforms/` flagged `buildable: false`; `thesis/` reserved for Tier 1). This ADR (ADR-EA-0007) applies as a **post-stand-up structural amendment**: a follow-up restructure PR against `ologos-repos/aide-canon` is required to (a) create `vision-strategy/` + `vsok/` subtree, (b) move Strategy artifacts from `enterprise-platforms/strategy/` to `vision-strategy/vsok/strategy/`, (c) rename `thesis/` → `mode-alpha/` if present, and (d) remove the `buildable: false` MANIFEST entry once MANIFEST is created. That restructure PR is OlogosAI's to execute as canon prime (cross-ai #20 governance).

## Consequences

**Positive:**
- Strategy's altitude becomes structurally honest — umbrella positioning at Tier 0 inside Vision-Strategy, not a software peer at Tier 4.
- The canon gains an explicit strategic frame (Vision-Strategy as tier, VSOK as the methodology artifact within) above its intellectual content. Enterprise-architecture-native shape; reads correctly to readers familiar with VSOK / OKR conventions.
- The *tier ≠ artifact* separation gives Vision-Strategy room to host additional umbrella-altitude artifacts (investment thesis, positioning briefs) without expanding VSOK's four-slot methodology surface.
- *Mode Alpha* reads forward — the corpus's first orientation mode, with room for siblings if future work warrants.
- Infographic structure becomes correct (HCAE no longer appears in two tiers).
- MANIFEST.yaml's `buildable: false` flag for Strategy becomes unnecessary; Strategy's non-buildability is now structurally evident from its placement under Vision-Strategy rather than declared as an exception within enterprise-platforms.

**Negative:**
- Tier renumbering touches references to "Tier 1 — Master Thesis" in any pending artifacts. Mitigated because `ologos-repos/aide-canon` is not yet populated beyond the README + initial infographic; no published downstream artifact cites the prior tier numbering as load-bearing.
- Vision-Strategy at Tier 0 adds reserved-but-unpopulated surfaces (Vision, Objectives, Key Results within VSOK) the corpus commits to populating over time. Empty slots are an explicit IOU.
- The canon directory layout diverges from cross-ai #40 Refinement B's `MANIFEST.yaml` flag approach; OlogosAI's stand-up PR must reflect the amended shape.
- The tier-vs-artifact distinction (Vision-Strategy is the tier, VSOK is the artifact within) requires a clear README at `vision-strategy/` to prevent readers from collapsing them.

**Neutral:**
- Foundation (HCAE, AIDK, RLEG) and Constructs (DEA, OrdSA, MxM, OAgents) tiers unchanged.
- ADR-EA-NNNN prefix continuity holds per cross-ai #40's ratified (α) prefix decision.
- *Mode Alpha* relabeling does not change the synthesizing artifact itself — the master thesis paper, when authored, lives at Tier 1 under the new label.

## Alternatives considered

1. **Keep Strategy in `enterprise-platforms/` with `buildable: false`** (cross-ai #40 Refinement B's ratified position). Rejected. The flag acknowledges the altitude mismatch without resolving it. An agent traversing the canon's tier structure still encounters Strategy as a Tier 4 peer to AEON/AIDEX/OAAD; the MANIFEST flag is meta-information that requires a second pass to apply. Naming Strategy at Tier 0 inside VSOK makes the altitude explicit at first contact.

2. **Promote Strategy to Tier 1 as a peer of Master Thesis.** Rejected. Strategy and the AIDE synthesis paper are at different altitudes — Strategy is the enterprise-strategic frame (the *why and what* at corpus level); the synthesis is the integrative architectural argument (the *how the parts cohere*). Treating them as Tier 1 peers blurs the umbrella/synthesis distinction.

3. **Name Tier 1 "Mode 0" instead of "Mode Alpha".** Rejected. The combination *Tier 0 / Mode 0* reads as a numeric clash and visually suggests redundancy. *Mode Alpha* aligns with the corpus's existing Greek-letter convention (Pattern α from cross-ai #40's prefix discussion).

4. **Defer the structural amendment; keep cross-ai #40 Refinement B as-is and patch only the infographic.** Rejected. The infographic surfaced a structural problem in the ratified shape; patching the visual without correcting the structure would leave the canon's directory layout misaligned with its own positioning. Better to amend once than to ship with a known-wrong shape and patch later.

5. **Place VSOK inside `decisions/` rather than as a top-level tier.** Rejected. Vision-Strategy is not a decision artifact — it is the corpus's strategic frame, and VSOK is its operationalizing methodology. Burying it inside `decisions/` would make it discoverable only to readers who already know to look there. Top-level surfacing matches its load-bearing role.

6. **Tier 0 *is* VSOK (initial framing of this ADR's first commit).** Rejected. Treating VSOK as the tier itself conflates the umbrella (the corpus's strategic frame) with the methodology product that operationalizes the umbrella into four named slots. The conflation has two downstream costs: (a) it locks Tier 0's artifact surface to exactly four slots (V/S/O/K), with no room for additional umbrella-altitude artifacts (investment thesis, market positioning brief, etc.) that aren't part of the VSOK decomposition; (b) it makes the tier name overlap with the artifact name, which reads as redundancy in a hierarchy listing ("Tier 0 — VSOK / VSOK paper"). Separating Vision-Strategy as the tier from VSOK as the structured artifact within it resolves both costs and preserves a clean tier ↔ artifact relationship throughout the canon's layout.

## Related

- [cross-ai #40](https://github.com/ologos-corp/cross-ai/issues/40) — Canon structure proposal; this ADR amends Refinements A and B.
- [ADR-EA-0004](ADR-EA-0004-add-mx-modes-as-spine-construct.md) — Mx-Modes as spine construct (Greek-letter Pattern α precedent).
- [ADR-EA-0005](ADR-EA-0005-clarify-mxm-archetype.md) — MxM archetype clarification.
- [ADR-ORDSA-0007](https://github.com/osa-ai-org/ordsa-ai/) — Provenance promotion (pending OlogosAI execution; independent of this ADR).
- [`infographics/AIDE-Architecture-Overview.png`](https://github.com/ologos-repos/aide-canon/blob/main/infographics/AIDE-Architecture-Overview.png) — visual that surfaced the structural issues this ADR resolves; will be regenerated to reflect the amended shape.
