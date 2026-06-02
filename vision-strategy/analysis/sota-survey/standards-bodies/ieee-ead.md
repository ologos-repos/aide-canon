# Standards body — IEEE AI ethics & governance (EAD + P7000 series + CertifAIEd)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Maps to the [standards-bodies AIDE-mapping anchor](README.md#aide-mapping-anchor). Cadence: **slow** (annual/multi-year deliverables) — treat version/status table as the dated snapshot.

## 1. What it is

> **Version / status header (surveyed 2026-06-01).** IEEE's AI-ethics work is *not one document* but a family. Verified statuses (IEEE Xplore / standards.ieee.org as of survey date):
>
> | Effort | Number / status | What it covers |
> |---|---|---|
> | **Ethically Aligned Design** | **EAD1e** — published 2019 (First Edition; the foundational vision doc, not a numbered standard) | General Principles (human rights, well-being, data agency, effectiveness, transparency, accountability, awareness of misuse, competence) for autonomous & intelligent systems (A/IS) |
> | **IEEE 7000** | **7000-2021** published (also **ISO/IEC/IEEE 24748-7000:2022**) | Model *process* for addressing ethical concerns during system design — value-based engineering (VBE) lifecycle |
> | **IEEE 7001** | **7001-2021** published | **Transparency of autonomous systems** — measurable, testable transparency *levels* per stakeholder group (users, public/bystanders, certifiers, investigators, expert witnesses) |
> | **IEEE 7002** | **7002-2022** published | Data privacy *process* (privacy-by-design lifecycle; PIA-driven) |
> | **IEEE 7003** | **7003-2024** published (Jan 2025) | Algorithmic bias considerations (lifecycle bias process; validation-set criteria; application-boundary communication) |
> | **IEEE 7007** | **7007-2021** published | Ontological standard for ethically driven robotics & automation — shared ethics *vocabulary/ontology* |
> | **IEEE 7010** | **7010-2021** published | Well-being metrics for ethical A/IS |
> | **P7008 / P7009 / P7011 / P7012 / P7014** | in development (drafts) | Nudging / fail-safe design / news-source trustworthiness / machine-readable privacy terms / emulated empathy |
> | **IEEE CertifAIEd** | program (not a numbered standard); current | Conformity-assessment + professional certification on four ethics pillars: **transparency, accountability, algorithmic bias, privacy** |
>
> *Calibration note:* **IEEE 2089-2021** (and **2089.1-2024**) is an *age-appropriate-digital-services / online-age-verification* framework (5Rights, children), **not** a general AI-ethics standard — the parent [`standards-bodies/README.md`](README.md) groups it under IEEE but it is a different problem domain; treated here as out-of-scope-for-AI-ethics and flagged for that README to disambiguate.

The IEEE corpus is the recognized authority on **ethics-by-design**: how to *embed ethical considerations into the system-design lifecycle* (7000's VBE process), how to *make autonomous-system behavior transparent and assessable* (7001's transparency levels), and how to certify that an organization or product did so (CertifAIEd). It is **values/ethics-oriented and predominantly design-time + conformity-assessment** — a *process and taxonomy* authority, not a runtime control plane. In aide-canon terms it occupies the **ethics-process and transparency-taxonomy** altitude: it tells you *how to deliberate about values and how to expose system behavior*, not *what an AI-aide is deontically forbidden to do at execution time*.

## 2. Source links

- **IEEE 7000-2021** — [IEEE Xplore 9536679](https://ieeexplore.ieee.org/document/9536679) · [IEEE SA launch note](https://standards.ieee.org/news/ieee-7000/) · ISO twin [ISO/IEC/IEEE 24748-7000:2022](https://www.iso.org/standard/84893.html).
- **IEEE 7001-2021** (transparency) — [IEEE Xplore 9726144](https://ieeexplore.ieee.org/document/9726144/) · rationale paper [Frontiers / Winfield et al.](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.665729/full).
- **IEEE 7002-2022** (data privacy) — [IEEE Xplore 9760247](https://ieeexplore.ieee.org/document/9760247) · [IEEE SA 7002](https://standards.ieee.org/ieee/7002/6898/).
- **IEEE 7003-2024** (algorithmic bias) — [IEEE Xplore 10851955](https://ieeexplore.ieee.org/document/10851955).
- **IEEE 7007-2021** (ontology) — [IEEE Xplore 9611206](https://ieeexplore.ieee.org/document/9611206/) · [IEEE SA 7007](https://standards.ieee.org/ieee/7007/7070/).
- **Ethically Aligned Design 1e (2019)** — [EAD1e PDF](https://standards.ieee.org/wp-content/uploads/import/documents/other/ead1e-introduction.pdf) · [OCEANIS launch](https://ethicsstandards.org/ieee-launches-ethically-aligned-design-first-edition-delivering-a-vision-for-prioritizing-human-well-being-with-autonomous-and-intelligent-systems/).
- **P7000-series tracker** — [OCEANIS P7000 list](https://ethicsstandards.org/p7000/) (note: this tracker lagged published-status on several efforts at read time — cross-check each against IEEE Xplore).
- **IEEE CertifAIEd** — [IEEE SA CertifAIEd program](https://standards.ieee.org/products-programs/icap/ieee-certifaied/) · [IEEE Spectrum coverage](https://spectrum.ieee.org/two-new-ai-ethics-certifications).
- **In-canon adjacency:** OAgents already names IEEE as a target routing venue for the behavioral-envelope profile (see [`oagents/README.md`](../../../../constructs/oagents/README.md) — "future NIST, NCCoE, **IEEE**, OASIS, IETF … voluntary consensus processes").

## 3. Map against AIDE

### Primary mapping — IEEE ethics-process/transparency → MxM Morals + EIF + HCAE

| IEEE effort | AIDE construct / plane | Alignment status |
|---|---|---|
| **IEEE 7000** (VBE ethics-by-design process) | **MxM Morals** authoring discipline + the canon's [decision/ADR](../../../../decisions/) provenance | *In flight elsewhere / aligned* — 7000 is the design-time process for *deriving* deontic constraints; canon's Morals is the *resulting runtime envelope*. Different lifecycle stage, complementary. |
| **IEEE 7001** (transparency *levels*, measurable, per-stakeholder) | [Epistemic Integrity Floor](../../../../patterns/epistemic-integrity-floor.md) §2/§8 + [AEON Evidence plane](../../../../enterprise-platforms/aeon/) + [digital-thread](../../../../patterns/digital-thread.md) | *In flight elsewhere* — **honest gap: 7001's transparency taxonomy is worth aligning canon evidence/observability to.** Canon emits evidence (confidence labels, defeater triggers, audit log) but has no per-stakeholder *transparency-level* taxonomy. 7001 supplies one. |
| **IEEE 7002** (data-privacy process) | AEON Identity/Evidence planes; not yet a first-class canon surface | *In flight elsewhere* — privacy-by-design process the canon has not separately authored. |
| **IEEE 7003** (algorithmic bias process) | [RLEG](../../../../foundation/rleg/) (training-time calibration) + EIF §3 claim-handling | *In flight elsewhere* — bias process is design/training-time; EIF's runtime calibration is the sibling, not a substitute. |
| **IEEE 7007** (ethics *ontology*) | OAgents typed-object vocabulary + [aide-vocabulary-map](../../aide-vocabulary-map.md) | *In flight elsewhere* — both build shared ethics vocabulary; canon's is envelope/authority-shaped, 7007's is robotics-domain-shaped. |
| **IEEE CertifAIEd** (conformity assessment + cert) | OAgents conformance criteria + [patterns/README conformance levels](../../../../patterns/README.md) + [HCAE](../../../../foundation/hcae/) review loop | *In flight elsewhere* — both define conformity assessment; CertifAIEd is a credential/program, canon's is vendor-neutral spec conformance. |
| **EAD1e General Principles** | [AIDK](../../../../foundation/aidk/) (why governance) + [HCAE](../../../../foundation/hcae/) (human as locus of judgment) | *In flight elsewhere / aligned* — EAD's "human well-being / human rights / accountability" principles motivate the same governance AIDK/HCAE motivate. |

### Against the AEON service planes

The one IEEE effort that touches AEON directly is **7001** → **Evidence plane** (and the digital-thread / EIF telemetry that plane carries). 7001's *measurable, testable, per-stakeholder transparency levels* are a taxonomy the AEON Evidence plane and EIF §2 confidence labels could be classified *against* — the canon currently emits evidence without a stakeholder-graded transparency scale. The other planes (Authority/OrdSA, Inference, Orchestration) have **no IEEE counterpart** — IEEE provides no runtime authority model.

### Vocabulary collision note (ADR-EA-0016)

IEEE texts use **"autonomous and intelligent systems (A/IS)"** and **"autonomous systems,"** generally *avoiding* the casual "agent" — so the [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md) collision is *milder* here than in vendor stacks. Where IEEE does say "agent" it means an A/IS actor (≈ the canon's **AI-aide**), **not** the OAgents `Agent` primitive (a typed object inside a behavioral envelope). IEEE 7007's *ontology* terms ("responsibility," "accountability," "transparency") are domain-scoped to robotics; when cross-referencing, bind them to canon meanings explicitly rather than importing 7007 senses wholesale.

## 4. Alignment classification

**Per-axis, not global — IEEE and aide-canon are complementary at different mechanism layers** (ethics *process + transparency taxonomy* vs runtime *deontic envelope + authority model*):

- **AIDE ahead** — **runtime-enforceable deontic constraints.** IEEE 7000 is a *design-time process* for surfacing and reasoning about ethical values; it produces no executable, runtime-evaluated permission/prohibition envelope. The canon's **MxM Morals** (deontic constraints — permissions/prohibitions/obligations/process-gates, see [`mxm/README.md`](../../../../constructs/mxm/README.md)) + **OrdSA** authority model + **OAgents** behavioral envelope supply exactly that runtime mechanism. IEEE is *ethics-by-design*; the canon is *ethics-at-execution*. This is the load-bearing differentiation.
- **In flight elsewhere / aligned** — **ethics-by-design process and transparency framing.** IEEE is the *recognized consensus authority* on the ethics-deliberation process (7000/VBE) and on transparency taxonomy (7001). The canon does not contest this ground and should cite it: IEEE 7000 is the design-time process that *feeds* what ends up in Morals; the canon adds the runtime envelope IEEE does not specify.
- **AIDE behind (honest)** — **per-stakeholder transparency levels.** IEEE 7001 provides a *measurable, testable, stakeholder-graded* transparency taxonomy. The canon's evidence/observability (EIF confidence labels, AEON Evidence plane, digital-thread) is emit-shaped but ungraded. Aligning canon observability to a 7001-style level taxonomy is a genuine catch-up opportunity, not a gap to wave away.

**The synthesis:** IEEE supplies the **ethics-deliberation process + transparency taxonomy** (design-time, values-oriented, the consensus authority); aide-canon supplies the **runtime deontic envelope + ordinal authority model** (execution-time, enforcement-oriented). They are *different mechanisms at different lifecycle stages* — a 7000-conformant VBE process is the natural front-end that *produces* the values a canon deployment then *enforces* at runtime via Morals/OrdSA/OAgents, with **HCAE** human-curation as the shared locus-of-judgment both frameworks demand. Same composition relationship the canon documents elsewhere (spec ↔ substrate, governance ↔ platform): IEEE as the ethics-process authority *upstream* of the canon's runtime envelope, with 7001's transparency taxonomy adopted *into* the canon's evidence shape.

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (runtime deontic lead).** Position MxM Morals + OrdSA + OAgents as the *runtime enforcement* layer that sits downstream of a 7000-class ethics-by-design process — IEEE is the named consensus authority for the design-time front-end the canon does not duplicate. KR shape: a documented "IEEE-7000-process → MxM-Morals-envelope" hand-off mapping (VBE-derived values → enforced deontic constraints).
2. **Catch-up (transparency taxonomy).** IEEE 7001 is materially ahead on *graded, per-stakeholder* transparency. KR shape: classify the AEON Evidence plane + EIF §2 confidence/observability outputs against a 7001-style transparency-level taxonomy, and surface the levels at AIDEX operator surfaces.
3. **Converge (ethics-process citation).** Cite IEEE 7000/7001/EAD as the recognized ethics-by-design + transparency authorities in OAgents' standards-routing (OAgents already names IEEE as a target venue) — converge on the design-time framing, differentiate on the runtime envelope.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Version/status table verified against IEEE Xplore + standards.ieee.org as of survey date (the OCEANIS P7000 tracker lagged on several published statuses — cross-checked each individually). Revisit on next P7000-series ratification (P7008/P7009/P7012/P7014 in development) or at OKR refresh.
