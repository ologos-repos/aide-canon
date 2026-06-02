# Standards body — ISO/IEC JTC 1/SC 42 (AI)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Cadence: **slow** (annual/quarterly SC 42 deliverables) — but the *certification ecosystem* around ISO/IEC 42001 is moving fast in 2026, so treat adoption signals as a dated snapshot.

## 1. What it is

**ISO/IEC JTC 1/SC 42** is the joint ISO/IEC subcommittee responsible for international AI standardization — the formal, internationally-recognized standards body for AI, organized into five working groups (foundational standards, big data, trustworthiness, use-cases/applications, computational approaches). Its deliverables are the de jure governance reference the rest of the field anchors to. This entry surveys the four load-bearing SC 42 deliverables for the canon plus the 2026 agentic-AI direction-of-travel:

- **ISO/IEC 42001:2023** — *AI Management System (AIMS)*. The world's **first certifiable** AI management-system standard: organization-level requirements to establish, implement, maintain, and continually improve an AIMS (policy, lifecycle, risk treatment, controls in Annex A). It is the de jure analogue of ISO 27001 for AI — **auditable and ISO-certifiable** by accredited bodies. This is the altitude-defining deliverable for the canon's comparison.
- **ISO/IEC 22989:2022** — *AI concepts and terminology*. The reference vocabulary (AI system, lifecycle stages, roles, AI properties) that underpins the rest of the SC 42 corpus.
- **ISO/IEC 23053:2022** — *Framework for AI systems using machine learning (ML)*. Conceptual framework + shared terminology for ML-based AI systems.
- **ISO/IEC 23894:2023** — *Guidance on risk management* for AI. The AI-specific companion to ISO 31000.

> **Version / status header (REQUIRED).**
> | Deliverable | Edition analyzed | Status (2026-06-01) | Successor / note |
> |---|---|---|---|
> | ISO/IEC 42001 | **:2023** (publ. Dec 2023) | **Published, certifiable.** Certification ecosystem operationalized in 2026 (e.g. BSI accredited via UKAS; ANAB and RvA accreditations live). Certification is **voluntary**. | **EN ISO/IEC 42001:2026** is a CEN/CENELEC European adoption of the same text. *Not* yet an OJEU-listed EU AI Act harmonized standard. |
> | ISO/IEC 22989 | **:2022** | Published | Foundational terminology; stable |
> | ISO/IEC 23053 | **:2022** | Published | ML framework; stable |
> | ISO/IEC 23894 | **:2023** | Published | Risk-management guidance |
> | Agentic-AI deliverable | — | **No ratified SC 42 agentic-AI standard found as of 2026-06-01.** Direction-of-travel only. | US positions feed SC 42 via the **NIST CAISI AI Agent Standards Initiative** (announced 2026-02-17), whose international-engagement pillar coordinates ISO/IEC JTC 1 input. |

**Altitude, stated precisely.** ISO/IEC 42001 governs the **organization's AI management system** — process, policy, lifecycle, risk treatment, documented controls, continual improvement — and is certifiable at that org level. It does **not** specify a per-action behavioral envelope, nor ordinal authority over a *running* AI-aide. It is management-system governance, not runtime governance. This altitude distinction is the load-bearing axis of §3–§4.

## 2. Source links

- Official committee: ISO/IEC JTC 1/SC 42 — `iso.org/committee/6794475.html`.
- ISO/IEC 42001:2023 — `iso.org/standard/42001`; "ISO 42001 explained" — `iso.org/home/insights-news/resources/iso-42001-explained-what-it-is.html`.
- ISO/IEC 22989:2022 — `iso.org/standard/74296.html`; ISO/IEC 23053:2022 — `iso.org/standard/74438.html`; ISO/IEC 23894:2023 — `iso.org/standard/77304.html`.
- Certification ecosystem (2026): BSI ISO 42001 (`bsigroup.com`), DNV, ANAB/RvA accreditation notes; Microsoft Learn offering page (`learn.microsoft.com/en-us/compliance/regulatory/offering-iso-42001`).
- EU adoption / AI Act harmonization: EN ISO/IEC 42001:2026 (CEN catalog via iteh.ai); EC "Standardisation of the AI Act" (`digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation`); the separately-commissioned AI Act QMS standard **prEN 18286**.
- Agentic direction: NIST CAISI AI Agent Standards Initiative (announced 2026-02-17) — international-engagement pillar coordinates US positions into ISO/IEC JTC 1.
- In-canon: the SC 42 / NIST AI RMF rows of [`aide-vocabulary-map.md`](../../aide-vocabulary-map.md); the standards-mapping anchor in [`standards-bodies/README.md`](README.md) (NIST AI RMF ↔ OAgents).

## 3. Map against AIDE

### Mapping table — OAgents + AEON planes

| ISO/IEC deliverable | AIDE construct / AEON plane | Alignment status |
|---|---|---|
| **ISO/IEC 42001** (AIMS, org-level, certifiable) | OAgents conformance construct (per-action envelope) + AEON **Authority** plane (OrdSA O0–O6) | **AIDE ahead** on per-action behavioral envelope + authority-altitude; **AIDE behind** on certifiable org-level management-system maturity + international recognition |
| **ISO/IEC 42001 Annex A controls** | OAgents conformance **levels** | *In flight elsewhere / consume* — map OAgents levels ↔ 42001 controls; 42001 is the org-management wrapper, OAgents the runtime behavioral floor inside it |
| **ISO/IEC 23894** (AI risk management) | AEON **Evidence** plane + MxM Morals (deontic risk treatment) | *In flight elsewhere* — convergent on risk identification; AIDE differentiates with **authority-up/evidence-up** provenance rather than a generic risk register |
| **ISO/IEC 22989** (concepts/terminology) | The canon vocabulary map ([ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) | *Consume / align* — adopt 22989 terms as the international anchor; reconcile against AI-aide vocabulary (see collision note) |
| **ISO/IEC 23053** (ML framework) | AEON **Inference** plane ([ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md)) — model-agnostic framing | *In flight elsewhere* — 23053 frames ML-system components; AIDE frames model-agnosticism as a first-class governance property 23053 does not |
| **SC 42 agentic-AI work** (none ratified) | OAgents (behavioral envelope) + AEON **Authority** + **Orchestration** planes | **AIDE ahead** — no ratified international agentic-AI behavioral standard exists; the canon's envelope + ordinal authority occupies open ground |

### Vocabulary-collision note (ADR-EA-0016)

ISO/IEC 22989 defines **"AI system"** and a lifecycle/roles vocabulary at the *system* altitude — this is mostly orthogonal to the casual-"agent" collision the canon polices, which is a benefit: 22989 does **not** overload "agent" the way vendor stacks do. Where collision risk does live: 22989's **"AI system"** is a system-of-record notion that must not be silently equated with the canon's **AI-aide** (the persistent governed entity) *or* with the OAgents **`Agent`** primitive (a typed object inside a behavioral envelope) — three distinct altitudes. ISO 42001's **"organization"** subject is the AIMS scope holder and maps to neither; it is the *management-system* altitude above all three. The canon should adopt 22989 terminology as the international anchor in the vocabulary map while preserving the AI-aide / OAgents-`Agent` / AI-system distinction explicitly — never collapse them, and never let "AI system" stand in for "AI-aide."

## 4. Alignment classification

**Mixed — different altitude, honestly behind on recognition.** ISO/IEC 42001 and aide-canon are *different categories*: a **certifiable organizational management-system standard** vs a **per-action governance/architecture corpus**. The classification is per-axis, not global:

- **AIDE ahead** — *per-action behavioral envelope* (OAgents conformance, governing a *running* AI-aide, which 42001 does not specify); *authority-altitude* (OrdSA O0–O6 authority-down / evidence-up — there is no ordinal-authority concept anywhere in the SC 42 corpus); deontic per-action constraints (MxM Morals); and the **open agentic-AI ground** — no ratified international agentic-behavioral standard exists, so the envelope + ordinal authority occupy uncontested de jure territory.
- **AIDE behind** — *certifiable org-level management-system maturity*: ISO/IEC 42001 is a published, accredited, internationally-recognized, auditable standard with a live 2026 certification ecosystem (BSI/UKAS, ANAB, RvA) and vendor uptake. **This is honest and decisive: ISO 42001 is THE recognized AI-governance standard; OAgents is a research spec with enforcement largely unbuilt.** AIDE has no certification scheme, no accreditation, no international recognition.
- **In flight elsewhere / consume** — risk management (23894 ↔ Evidence plane + Morals), terminology (22989 ↔ vocabulary map), ML framing (23053 ↔ Inference plane). These are surfaces to *consume and align with*, not contest.

**Synthesis — they compose, not compete (and the canon should say so plainly).** ISO/IEC 42001 is the **organizational management-system wrapper**; OAgents + OrdSA + MxM Morals are the **per-action runtime governance** that lives *inside* an AIMS scope. The right canon posture is **CONSUME 42001 at the org altitude and EXTEND below it**: an organization running AIDE-governed AI-aides would seek ISO/IEC 42001 certification for its *management system*, then satisfy 42001's behavioral-control intent with OAgents conformance + OrdSA authority as the per-action floor 42001 leaves unspecified. Concretely: **map OAgents conformance levels onto ISO/IEC 42001 Annex A controls** (OAgents as the auditable evidence that the AIMS's behavioral controls are operationally realized at runtime), and **adopt ISO/IEC 22989 terminology** as the international anchor in the vocabulary map. This mirrors the consume-substrate / extend-governance relationship the canon already documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/) — here the "substrate" is a *governance standard* rather than a runtime platform.

**EU AI Act harmonization angle.** EN ISO/IEC 42001:2026 is the CEN/CENELEC European adoption, but ISO 42001 is **not yet an OJEU-listed harmonized standard** and the EU has commissioned a *separate* AI Act QMS standard (prEN 18286) because 42001's goals/definitions don't fully align with the Act's quality-management requirement — so 42001 alone confers no presumption of conformity (cross-ref the forthcoming `eu-ai-act.md` entry in this slice).

## 5. Objective implication

Three Doerr-style Objective shapes follow (per [`sota-survey/README.md`](../README.md) → [ADR-EA-0010](../../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md), feeding [`vsok/objectives/`](../../../vsok/objectives/)):

1. **Defend-and-extend (per-action authority lead).** Position OAgents + OrdSA as the per-action behavioral floor that sits *inside and below* an ISO/IEC 42001 AIMS — the altitude 42001 structurally does not reach. KR shape: a published **"OAgents conformance levels ↔ ISO/IEC 42001 Annex A controls"** crosswalk, showing AIDE as the runtime evidence an AIMS's behavioral controls are realized.
2. **Catch-up (recognition + certifiability).** AIDE is behind on certifiable, internationally-recognized management-system maturity — honestly and decisively. KR shape: define an OAgents conformance-assessment scheme expressible as auditable evidence *against* a 42001-certified management system, rather than competing with the certification itself.
3. **Converge-or-differentiate (terminology + risk).** Adopt ISO/IEC 22989 as the international vocabulary anchor and align ISO/IEC 23894 risk treatment with the Evidence plane + Morals — converging on the de jure terms while differentiating with authority-up/evidence-up provenance. KR shape: a 22989-reconciled vocabulary-map revision and a 23894 ↔ Evidence/Morals mapping.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Standard numbers/editions/statuses verified against ISO/IEC and certification-body sources at survey time; the agentic-AI line is direction-of-travel (NIST CAISI initiative announced 2026-02-17), **no ratified SC 42 agentic-AI standard as of this date**. Revisit on: a ratified SC 42 agentic-AI deliverable, OJEU listing of EN ISO/IEC 42001:2026 (or publication of prEN 18286), or at OKR refresh.
