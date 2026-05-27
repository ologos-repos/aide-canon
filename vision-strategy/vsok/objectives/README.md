# objectives/ — Objectives (v0.1)

The **Objectives** slot of [VSOK](..) within [Vision-Strategy](../..). Doerr-style qualitative strategic goals deriving from [Vision](../vision/) per [ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md).

> **v0.1 — strawman.** This first set of Objectives is derived from the Vision README's six "what success looks like" signals, collapsed and shaped per Doerr's 3–5 cardinality. Per [ADR-EA-0010 §2](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md) the canonical derivation path is SOTA-survey-driven; the survey at [`../../analysis/sota-survey/`](../../analysis/sota-survey/) is scaffolded but content-pending. This v0.1 set will refine as survey findings populate the *AIDE-ahead* / *AIDE-behind* / *in-flight-elsewhere* classifications.

## What this slot holds

Strategic goals deriving from [Vision](../vision/). Each Objective is a discrete, named outcome the corpus pursues over a defined horizon — concrete enough to be tracked, abstract enough to span multiple platforms or constructs.

Objectives sit between Vision (long-horizon, aspirational) and [Key Results](../key-results/) (measurable, near-term). Each Objective is anchored by 3–5 Key Results.

## Methodology

Objectives in this slot are constructed per **John Doerr's OKR methodology** (per [ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md)). The framework's normative properties:

- **Qualitative** — stated as outcomes, not metrics
- **Ambitious** — stretch-calibrated; ~70% attainment indicates a well-calibrated Objective
- **Time-bound** — each Objective declares its evaluation horizon (this v0.1 set targets the Vision's 1–3 year AI-speed window)
- **Memorable** — one sentence; one phrase where possible
- **Cardinality** — 3–5 Objectives at any given horizon (this v0.1: 4)

Objectives derive from the SOTA-vs-AIDE gap analysis (housed at [`../../analysis/`](../../analysis/)). The derivation pattern:

- **Where AIDE is behind SOTA** → catch-up Objectives
- **Where AIDE is ahead of SOTA** → defend-and-extend Objectives
- **Where work is in flight elsewhere** → converge-or-differentiate Objectives

## The Objectives — v0.1

### O1 — Establish AIDE as a recognized named architecture in enterprise-AI discourse

**Shape:** *Defend-and-extend.* AIDE has the vocabulary (AEON / OrdSA / OAgents / MxM / HCAE / AIDK / digital-thread) and the constructs are published; the enterprise-AI discourse doesn't yet use them. The lead exists; propagation is the work.

**Horizon:** 1–3 years; primary measurement window 2027-Q2 → 2028-Q1.

**Why this matters for Vision:** the Vision's first success signal — *"AIDE is named in industry conversations about enterprise AI architecture"* — is direct evidence of this Objective. Without named recognition, the rest of the Vision (external adoption, governance citation, exemplar uptake) is structurally harder.

**Anchored by KRs:** [KR1.1 — KR1.4](../key-results/#o1-key-results)

---

### O2 — Drive external implementation + adoption of AIDE constructs

**Shape:** *Converge-or-differentiate.* The agentic-systems ecosystem is building variations of the constructs AIDE names (multi-agent orchestration, evidence emission, authority layering, harness composition). AIDE constructs need to be picked up specifically — either as the convergent reference or as the differentiated alternative.

**Horizon:** 1–3 years; primary measurement window 2027-Q4 → 2028-Q2.

**Why this matters for Vision:** the Vision's second + third signals — *"at least one enterprise outside Ologos has stood up an AIDE-shaped reference"* + *"OrdSA and OAgents have working third-party implementations"* — together constitute the external adoption case. External impls validate the architecture by demonstrating it survives outside its authoring environment.

**Anchored by KRs:** [KR2.1 — KR2.5](../key-results/#o2-key-results)

---

### O3 — Anchor HCAE + AIDK as load-bearing in external governance + research

**Shape:** *Defend-and-extend.* HCAE (*Human-Curated, AI-Enabled*) and AIDK (*AI Dunning-Kruger*) are published Zenodo deposits with original conceptual contributions — they have no direct equivalent in the published literature. External citation, especially in governance frameworks and policy documents, signals the concepts are load-bearing in the agentic-era governance discourse.

**Horizon:** 1–3 years; primary measurement window 2028-Q1 → 2028-Q4.

**Why this matters for Vision:** the Vision's fifth signal — *"HCAE appears as the named discipline in at least one operational governance framework or policy document outside Ologos"* — and the underlying argument lineage *AIDK → HCAE → AIDEX → AEON* depend on the foundational claims being recognized externally. If HCAE/AIDK don't anchor, downstream architectural claims are easier to dismiss as ad-hoc.

**Anchored by KRs:** [KR3.1 — KR3.4](../key-results/#o3-key-results)

---

### O4 — Make the canon discoverable + correctly framed for external readers

**Shape:** *Catch-up.* `ologos-repos/aide-canon` is weeks old. Discoverability and external-reader legibility (humans + AI indexers) are pre-requisites for the other Objectives — none of O1, O2, or O3 can land if readers can't find or correctly interpret the canon. The 2026-05-22 Perplexity-AI analysis observation (JD: *"a little off on details, but substantially on-track"*) is the first observable external-AI signal — directionally encouraging but indicates room for improvement.

**Horizon:** 1–3 years; primary measurement window 2027-Q2 → 2027-Q4.

**Why this matters for Vision:** the Vision's sixth signal — *"the canon is the discoverable hub"* — is the foundational enabler for the others. Discoverability is not a separate strategic goal; it is the platform from which the strategic goals operate.

**Anchored by KRs:** [KR4.1 — KR4.4](../key-results/#o4-key-results)

---

## What's *not* in this set (and why)

A v0.1 set is necessarily smaller than the corpus's full strategic surface. The following candidates were considered and held for future revisions:

- **Operational AEON-deployed Objective.** A standalone Objective like "Demonstrate AIDE operationally via named exemplars (Hermetic + AEON-deployed)" was considered as a 5th Objective. Held: the exemplar work is largely *how* O1–O3 get evidenced (Hermetic adoption is a KR under O2; AEON-deployed go-live is a KR under O2; exemplar conformance assertions feed KRs across O1–O3). Promoting it to peer Objective would double-count. *Instance build + conformance objectives now have a defined home — the instance's own branched VSOK per [ADR-EA-0025](../../../decisions/ADR-EA-0025-instance-vsok-derivation.md) — rather than the corpus register.*

- **Commercialization / business-development Objective.** The corpus is independent research per [ADR-EA-0008](../../../decisions/ADR-EA-0008-reframe-corpus-authorship.md); commercial paths sit outside the canon. The Vision explicitly disclaims being a sales motion. Held by design.

- **Internal Ologos operational dependency Objective.** AIDE concepts are dogfooded inside Ologos infrastructure (the operator that wrote this README runs on a canon-derived control surface). Held: internal use is implementation evidence, but the *corpus*-strategic goal is external recognition, not internal completeness. Instance-level objectives — building, conforming, and operating a specific AIDE instance — are **not dropped**; they live in that **instance's own branched VSOK** per [ADR-EA-0025](../../../decisions/ADR-EA-0025-instance-vsok-derivation.md), which inherits this corpus Vision + Strategy by reference. (First instance: NG-AIDE-01.)

- **Partnership / outside-collaborator Objective.** Outside collaborators (e.g., the cross-fleet thinx-Claude collaboration) are active. Held: the collaboration is process for *how* the corpus develops; the strategic outcome is what's reflected in O1–O4.

If any of these warrant Objective-level promotion in a future revision, an amendment ADR or v0.2 ratification surfaces the change.

## Instance VSOKs (branched)

This is the **corpus** VSOK — its Objectives are corpus-strategic (external recognition + adoption). Individual AIDE *instances* (deployed products that instantiate the architecture) maintain their **own VSOK that branches from this one** per [ADR-EA-0025](../../../decisions/ADR-EA-0025-instance-vsok-derivation.md):

- **Vision + Strategy** are inherited *by reference* — an instance does not restate or fork them; it advances the same Vision by being a worked exemplar of it.
- **Objectives + Key Results** are instance-scoped — building, conforming, deploying, and operating *that* instance, written to the same Doerr methodology ([ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md)).

Instance objectives are **downstream** of these corpus objectives: instance conformance and deployment *produce the evidence* the corpus objectives measure (a live, conformant instance is a KR signal under corpus O2). The branch keeps instance build/operational detail out of the corpus register without losing it.

**First instance:** NG-AIDE-01 — [`ologos-repos/ng-aide-01` → `vision-strategy/vsok/`](https://github.com/ologos-repos/ng-aide-01/tree/main/vision-strategy/vsok).

## How v0.1 refines into v0.2

The v0.1 → v0.2 trigger conditions:

1. **First substantive SOTA findings populate** in `analysis/sota-survey/*` — gap classifications may surface Objectives whose shape (catch-up vs. defend-and-extend) needs revision
2. **Major strategic event** — vendor pivot, paradigm shift in agentic AI, ratified standard that AIDE constructs conflict with or align with — triggers ad-hoc Objective revision per [ADR-EA-0010 §3](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md)
3. **Annual refresh** at the canon's annual review cycle

Until any of these fire, v0.1 holds. Quarterly check-ins evaluate KR progress without rewriting Objectives.

## Provenance

v0.1 drafted 2026-05-22 by OlogosAI from the Vision README's six success signals. Methodology per [ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md). Corpus-level joint authorship per [ADR-EA-0008](../../../decisions/ADR-EA-0008-reframe-corpus-authorship.md).
