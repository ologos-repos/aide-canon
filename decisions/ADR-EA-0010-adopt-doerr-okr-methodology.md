# ADR-EA-0010 — Adopt John Doerr OKR methodology for VSOK Objectives + Key Results

- **Status:** Accepted
- **Date:** 2026-05-22
- **Author:** JD Longmire (drafted by OlogosAI)
- **Reviewers:** @jdlongmire
- **Refines:** [ADR-EA-0007](ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) §Decision item 1 (VSOK as Tier 0 structured artifact; this ADR specifies the methodology for the O and KR slots that ADR-EA-0007 introduced as reserved placeholders).
- **Ratification note:** Comment-out period waived by explicit maintainer ratification (JD Longmire, 2026-05-22). Same override pattern as ADR-EA-0003 / 0004 / 0005 / 0007 / 0008 ratified earlier today. Basis: sole-maintainer status, in-session directive (*"on the OKR component of VSOK — leverage the John Doerr methodology"* / *"you can consider that an ADR"*), and the decision being a methodology selection rather than a positioning or scope change.

## Context

[ADR-EA-0007](ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) established Vision-Strategy as Tier 0 with VSOK as the structured artifact inside it. VSOK's four slots are:

- **V**ision — long-horizon outcome (now authored — see [`vision-strategy/vsok/vision/README.md`](../vision-strategy/vsok/vision/README.md))
- **S**trategy — positioning argument (populated by *Enterprise Agentic AI Platform Strategy*)
- **O**bjectives — strategic goals deriving from Vision (reserved placeholder)
- **K**ey Results — measurable outcomes anchoring Objectives (reserved placeholder)

ADR-EA-0007 specified the V/S/O/K decomposition but did not specify the **methodology** governing how Objectives and Key Results are written, related, or evaluated. Multiple competing frameworks exist for goal-setting at the strategic altitude (OKR, V2MOM, Balanced Scorecard, BHAG, MBO); without a named methodology, the O and KR slots risk inconsistent shape, unclear acceptance criteria, and difficulty distinguishing well-formed entries from drift.

This ADR ratifies the methodology choice: **John Doerr's OKR framework** (as defined in *Measure What Matters*, 2018, and originally derived from Andy Grove's iMBO at Intel).

## Decision

### 1. Adopt John Doerr's OKR methodology for the Objectives and Key Results slots

The canon's VSOK Objectives and Key Results slots are constructed per John Doerr's OKR framework. The framework's normative properties apply:

**Objectives are:**
- **Qualitative.** Stated as outcomes, not metrics. An Objective answers *what do we want to achieve?* in language a non-author can read and understand.
- **Ambitious.** Stretch goals — successful execution at ~70% indicates a well-calibrated Objective. Objectives consistently scored 100% are too conservative; Objectives consistently scored under 40% are mis-scoped.
- **Time-bound.** Each Objective declares the horizon over which progress is evaluated. The canon's Vision horizon is 1–3 years (per [`vision-strategy/vsok/vision/README.md`](../vision-strategy/vsok/vision/README.md)); Objectives may operate at the full horizon or at intermediate cadences depending on the goal.
- **Memorable.** Stated concisely (one sentence; ideally one phrase). If an Objective requires a paragraph to express, it is two Objectives or it is a Key Result.

**Key Results are:**
- **Quantitative.** Stated as measurements with concrete thresholds. A Key Result answers *how will we know we made progress?* in numbers, dates, or pass/fail signals — never in adjectives.
- **Specific.** Each Key Result names exactly one observable outcome, with an explicit threshold and time horizon. *"Increase AIDE citations"* is not a Key Result; *"At least 5 third-party citations of the AIDE corpus on Zenodo by 2027-Q4"* is.
- **Time-bound.** Each Key Result has a measurement date or window.
- **Stretch-calibrated.** Like Objectives, KRs are written to require effort; ~70% attainment is good performance.

**Cardinality (Doerr's standard guidance):**
- 3–5 Objectives at any given horizon
- 3–5 Key Results per Objective
- Total OKR set fits on one page

**Transparency:**
Per Doerr, OKRs are public within the operating organization. The canon's OKRs are public (the canon repo is public); this matches Doerr's transparency principle by default.

### 2. SOTA-driven derivation per JD's prior direction

ADR-EA-0007 did not specify how Objectives are *derived*. JD's direction in the 2026-05-22 evening session established the derivation methodology:

> *"research the current state-of-the-art against the current aide architecture - identify what's already in flight, where aide is ahead of, or behind, the game, and what strategies emerge from that - leveraging hermetic and the soon to be deployed AEON as exemplars"*

Operationalized inside Doerr's framework:

- **Where AIDE is behind**, Objectives are *catch-up* shape — close the gap to the named SOTA target. Example shape: *"Establish AIDE's evidence-plane interop story with [named external standard] by [date]."*
- **Where AIDE is ahead**, Objectives are *defend-and-extend* shape — propagate the lead before SOTA catches up. Example shape: *"Drive at least one external adoption of [AIDE-leading construct] before SOTA equivalents mature."*
- **Where work is in flight elsewhere**, Objectives are *converge-or-differentiate* shape — either align with the in-flight convergent direction, or articulate the differentiation explicitly.

The SOTA gap analysis (housed at `vision-strategy/analysis/sota-survey/` — to be created) is the evidence base from which Objectives are written. Key Results are derived from the same evidence base — measurable signals tied to observable SOTA movement.

### 3. Cadence and review

Doerr's standard cadence is quarterly. The canon is not a quarterly-operating enterprise — it is a research program with a 1–3 year horizon. The cadence is therefore adapted:

- **Annual** — full OKR refresh tied to the canon's annual review cycle (December timeframe, pending a separate cadence ADR)
- **Quarterly check-ins** — progress evaluation against Key Results; no rewriting of Objectives unless major recalibration is warranted (e.g., a SOTA shift invalidates the gap analysis)
- **Ad-hoc revision** — when significant new evidence lands (a major SOTA paper, a named external adoption, a paradigm shift), Objectives and Key Results are revised mid-cycle with an in-line revision note

Cadence ADR is queued as a follow-on if needed; the operating discipline above is the initial default.

### 4. Scope of this ADR

This ADR:

- Specifies the methodology for the O and KR slots
- Adds methodology references to `objectives/README.md` and `key-results/README.md` placeholder content
- Does **not** populate the O or KR slots — that is downstream SOTA-driven work
- Does **not** modify the Strategy paper (already populated; methodology-agnostic prose)
- Does **not** modify the Vision README beyond the existing slot-relation table reference

## Consequences

**Positive:**

- A named, widely-understood methodology lets contributors and readers immediately recognize what a well-formed Objective or KR looks like.
- Doerr's qualitative-vs-quantitative split forces honest discipline: vague aspirations stay in Vision, measurable signals land in KRs, no in-between mush.
- Stretch calibration (~70% attainment as "good") matches the canon's research-program character — Objectives should require effort; consistently maxed-out scores signal under-ambition.
- SOTA-driven derivation (per JD's prior direction) is naturally compatible with Doerr's framework; the gap analysis produces the inputs Doerr's Objectives consume.
- Transparency is already met by the canon being public.

**Negative:**

- Doerr's framework is enterprise-operational by default; adapting it for a research corpus with a 1–3 year horizon (rather than quarterly operational cycles) requires the cadence guidance in §3, which is partly judgmental.
- Stretch calibration's 70%-is-good convention conflicts with binary commit-vs-aspire models; readers familiar with other frameworks may misinterpret partial scores as failure.
- The framework gives strong guidance on shape but does not solve the *content* question — what the Objectives *should be* still depends on the SOTA gap analysis and JD/Micah's judgment.

**Neutral:**

- Per-construct methodology (e.g., MxM's five-surface decomposition, OrdSA's seven ordinals) is unaffected. OKR methodology applies specifically to VSOK's O and KR slots at the corpus-strategic altitude.
- Citation: Doerr (2018), *Measure What Matters: How Google, Bono, and the Gates Foundation Rock the World with OKRs*. The framework is widely documented; the canon does not need to redocument it in detail.

## Alternatives considered

1. **No specified methodology (free-form O+KR writing).** Rejected. Without a named methodology, the slots drift in shape across contributors and over time. Readers cannot tell whether an entry is well-formed. The canon's discipline elsewhere (schema-first OAgents, ordinal OrdSA, surface-decomposed MxM) sets a precedent for named methodology over free-form prose.

2. **V2MOM (Salesforce).** Rejected. V2MOM (Vision / Values / Methods / Obstacles / Measures) is a coherent alternative used in some enterprise settings. Rejected on the directive (JD specified Doerr) and because Doerr's O+KR cleanly maps to VSOK's existing four-slot decomposition without introducing the V2MOM-specific Values/Obstacles slots that VSOK does not have.

3. **Balanced Scorecard (Kaplan/Norton).** Rejected. BSC's four perspectives (financial / customer / internal-process / learning-growth) are oriented toward operating enterprises with revenue and customer-facing operations. The canon is a research corpus; the BSC perspectives don't map cleanly.

4. **BHAG (Collins).** Rejected. Big Hairy Audacious Goals are a vision-level construct; they belong in Vision, not in Objectives. The Vision slot already serves that role; using BHAG for Objectives would collapse Vision into Objectives.

5. **MBO (Drucker / classic Management by Objectives).** Rejected. MBO predates OKR and shares conceptual lineage, but its operating discipline (cascading individual goals + annual review) is less suited to the canon's small-author, research-program character. OKR's transparency + stretch-calibration is the modernization Doerr's framework provides over MBO.

6. **Defer methodology selection until O+KR are first populated.** Rejected. Methodology shapes what *count* as valid entries. Authoring O+KR content first and back-fitting methodology would risk content that doesn't satisfy any framework cleanly, then forcing methodology choices to accommodate the content rather than vice versa.

7. **Adopt Doerr but adapt cardinality (more than 5 Objectives).** Rejected at default; left open for later refinement. Doerr's 3–5 cardinality is calibrated for organizational attention; the canon is a research corpus with longer horizons and may eventually warrant a different cardinality. If practice surfaces a strong case for divergence, a follow-on ADR amends. The default for v1 is Doerr's 3–5 standard.

## Related

- [ADR-EA-0007](ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) — Tier 0 / VSOK structural ADR; this ADR specifies the methodology for the O+KR slots ADR-EA-0007 introduced
- [`vision-strategy/vsok/vision/README.md`](../vision-strategy/vsok/vision/README.md) — Vision (1–3 year horizon, AI-speed); this ADR's PR adds the slot-relation references to Doerr methodology
- [`vision-strategy/vsok/objectives/README.md`](../vision-strategy/vsok/objectives/README.md) — Objectives slot placeholder; updated by this PR to reference Doerr methodology
- [`vision-strategy/vsok/key-results/README.md`](../vision-strategy/vsok/key-results/README.md) — Key Results slot placeholder; updated by this PR to reference Doerr methodology
- Doerr, J. (2018). *Measure What Matters: How Google, Bono, and the Gates Foundation Rock the World with OKRs.* Portfolio. ISBN 9780525536222.
