# Standards body — EU AI Act (Regulation (EU) 2024/1689)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Cadence: **slow-but-volatile** — the Act itself is settled law, but its *applicability timeline* is in active amendment (the 2026 Digital Omnibus deal moved high-risk dates). Treat the date table as a dated snapshot.

## 1. What it is

The **EU AI Act** (Regulation (EU) 2024/1689) is the European Union's horizontal, **binding regulatory law** for artificial intelligence — the world's first comprehensive AI statute. It is **regulation, not a technical standard and not an architecture**: it sets legal *obligations* on providers and deployers of AI systems, classifying systems by risk and attaching duties to each tier. The technical "how" is deliberately *delegated downward* to harmonized standards (CEN-CENELEC / ISO-IEC — see §3 cross-ref), so the Act states *what evidence and controls are required*, not how to build them.

**Version / status header**

| Field | Value |
|---|---|
| Instrument | Regulation (EU) 2024/1689 ("AI Act") |
| Legal status | **Binding** EU regulation (directly applicable, no national transposition) |
| Entered into force | **2024-08-01** |
| Full applicability (base) | **2026-08-02** (with the staged exceptions below) |
| Amendment in flight | **"Digital Omnibus on AI"** — *provisional* trilogue agreement **2026-05-07**; **not yet formally adopted** as of survey date. Defers high-risk dates and adds prohibitions (see timeline). |
| Successor / superseding | None — this is the primary instrument; the Omnibus *amends* it, does not replace it |

**GEOGRAPHIC NOTE (EU-jurisdictional).** This is **EU law**. It binds AI systems *placed on the market or put into service in the EU*, and systems whose **output is used in the EU** — i.e. it has extraterritorial reach by market-effect, but it is **not a global standard** and not a US/UK instrument. Compare the US **NIST AI RMF** (voluntary framework) and **CEN-CENELEC/ISO-IEC** (technical standards) surveyed elsewhere in this slice — those are *standards*; the AI Act is *law*. Applicability to any AIDE-governed deployment is a **legal determination for that deployment's operator**, not a property of the architecture.

**Risk tiers** (the structural spine of the Act):

| Tier | Treatment | Examples |
|---|---|---|
| **Prohibited** | Banned outright | social scoring, manipulative subliminal techniques, untargeted facial-image scraping, real-time remote biometric ID in public (narrow exceptions). Omnibus adds CSAM / non-consensual intimate imagery. |
| **High-risk** | Permitted **with the heaviest obligations** — risk management, data governance, **technical documentation (Annex IV)**, **automatic logging / record-keeping (Art. 12/19)**, **human oversight (Art. 14)**, transparency, accuracy/robustness, conformity assessment + CE marking + EU-database registration | Annex III use-cases (employment, credit, education, critical infrastructure, etc.) + Annex I product-embedded AI |
| **Limited-risk** | **Transparency** duties only (Art. 50) — disclose AI interaction, label deepfakes / AI-generated content (watermarking) | chatbots, generative media |
| **Minimal-risk** | No obligations | spam filters, AI in games |

**GPAI (general-purpose AI model) obligations** sit on a *separate axis* from the risk tiers: providers of GPAI models owe **technical documentation, training-data-summary disclosure, copyright policy**, and — for models with **systemic risk** — additional model-evaluation, adversarial-testing, incident-reporting, and cybersecurity duties. The **GPAI Code of Practice** (final text 2025-07-10; Commission/Board-endorsed 2025-08-01) is a **voluntary** instrument GPAI providers may sign to *demonstrate* compliance — adherence is one route to showing conformity, not a legal mandate.

**Phased applicability timeline** (mark status; dates shift under the Omnibus):

| Milestone | Date | Status note |
|---|---|---|
| Entry into force | 2024-08-01 | done |
| Prohibitions + AI-literacy duties apply | 2025-02-02 | done / in effect |
| GPAI model obligations apply | 2025-08-02 | in effect; full Commission *enforcement* powers from 2026-08-02; pre-2025-08-02 models have until 2027-08-02 to comply |
| High-risk (Annex III, use-based) apply | **was 2026-08-02 → Omnibus defers to 2027-12-02** | base-text date; **provisional** Omnibus deferral, not yet adopted |
| High-risk (Annex I, product-embedded) apply | **was 2027-08-02 → Omnibus defers to 2028-08-02** | base-text date; **provisional** deferral |
| Watermarking / Art. 50 transparency | base 2026-08-02; Omnibus moves to 2026-12-02 | **provisional** |

*(Calibration: the deferred dates are a **provisional trilogue agreement** as of 2026-05-07 — formal adoption anticipated mid-2026, publication in the OJEU ~July 2026, in force on the third day after. Until adopted, the **2026-08-02** base date legally stands.)*

## 2. Source links

- Official text: Regulation (EU) 2024/1689, EUR-Lex (`eur-lex.europa.eu`).
- European Commission — AI Act policy + standardisation: `digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai` and `.../ai-act-standardisation`.
- Implementation timeline + article-level explainer: `artificialintelligenceact.eu/implementation-timeline/`, Art. 12 (record-keeping), Annex IV (technical documentation).
- GPAI Code of Practice: `digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers`; Commission endorsement (2025-08-01).
- Harmonized-standards bridge: CEN-CENELEC **JTC 21** (`jtc21.eu`); harmonised-standards map (`ai-act-standards.com`).
- **Digital Omnibus on AI** (provisional agreement 2026-05-07): Council/Parliament press; legal-analysis summaries (White & Case, Hogan Lovells, Covington/Inside Privacy). *Status: provisional, not adopted — re-verify at read time.*

## 3. Map against AIDE

The Act is a **compliance target**, so the mapping is *which AIDE mechanisms produce the evidence each obligation demands* — not an architecture-vs-architecture comparison. AIDE does not "implement" the Act; it provides the **technical substrate to evidence** its high-risk obligations.

### Against OAgents + AEON service planes

| AI Act obligation | AIDE construct / plane | Alignment status |
|---|---|---|
| **Technical documentation (Annex IV / Art. 11)** | OAgents conformance criteria + **digital-thread** ([`../../../../patterns/digital-thread.md`](../../../../patterns/digital-thread.md)) — the documentation/provenance record | *Alignment-enabling* — AIDE's conformance + thread *generates* the documentation the obligation requires |
| **Automatic logging / record-keeping (Art. 12/19)** | **AEON Evidence plane** — OAgents evidence emission (emit-only spec today) | *Alignment-enabling (partial)* — the *shape* matches the duty; AIDE's evidence trail is largely spec, not built (cf. langchain LangSmith gap) |
| **Human oversight (Art. 14)** | **HCAE** human-curation / operator-as-curator + MxM **Morals** process gates | *Strong alignment* — HCAE's "human keeps every decision" is precisely Art. 14's meaningful-human-control principle |
| **Risk management + prohibited-practice constraints** | MxM **Morals** (deontic layer: permissions / prohibitions / obligations) + AEON **Authority** plane (OrdSA O0–O6) | *Strong alignment* — Morals is the deontic surface that can encode prohibited-practice gates; Authority bounds who may approve high-impact action |
| **Conformity assessment / accountability** | OAgents behavioral-envelope conformance + Authority-down/evidence-up provenance | *Alignment-enabling* — produces the auditable trail a conformity assessment consumes |
| **Transparency (Art. 50, GPAI training-data summary)** | AEON Evidence + Identity planes (AI-aide self-identification; output provenance) | *Partial alignment* — disclosure primitives map; watermarking is not an AIDE concern |

### Harmonized-standards bridge (cross-ref)

The Act **delegates technical detail to harmonized standards** (CEN-CENELEC JTC 21 / ISO-IEC). Conforming to an OJEU-cited harmonized standard yields a **rebuttable presumption of conformity**. ISO/IEC 42001 (AI management system) is the leading candidate to underlie the Act's AI-QMS requirement. This is where AIDE's *standards* alignment lives — **cross-ref the [ISO-IEC SC 42 entry](iso-iec-sc42.md)** (this slice) for the technical-standard mapping. The relationship is layered: **Act (law) → harmonized standard (technical detail) → AIDE mechanisms (evidence production)**.

### Vocabulary-collision note

The Act's term **"AI system"** is a *legal* definition (Art. 3) — broad, output-and-autonomy based. It is **not** the OAgents `Agent` primitive and **not** the canon **AI-aide** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)). When mapping an AIDE deployment onto the Act, the legal "AI system" boundary may enclose *several* OAgents `Agent` objects and the AI-aide that wraps them — these are different units of analysis and must not be flattened. The Act also uses **"general-purpose AI model" (GPAI)** as a regulatory category keyed to a model's training-compute and generality — orthogonal to the canon's plane vocabulary; do not casually equate GPAI with AEON's Inference plane. Per ADR-EA-0016, never default to casual **"agent"** in this entry → use **AI-aide** (the principal) or **`Agent`** (the OAgents primitive) explicitly.

## 4. Alignment classification

Because a regulation is a *compliance target*, the survey's ahead/behind/in-flight axis does **not** apply globally — AIDE cannot be "ahead of" or "behind" a law. The honest framing is **alignment status per obligation-axis**:

- **Human oversight (Art. 14)** — *Strong alignment.* HCAE's human-curation invariant and MxM Morals gates are a near-direct fit for "meaningful human control / ultimate human responsibility." This is AIDE's strongest evidencing surface.
- **Deontic / prohibited-practice (Arts. 5, 9)** — *Strong alignment.* MxM Morals is purpose-built as a deontic layer (permissions / prohibitions / obligations) — the natural place to encode prohibited-practice and risk-management gates as enforceable constraints rather than documentation.
- **Documentation + provenance (Annex IV, conformity)** — *Alignment-enabling, spec-mature.* OAgents conformance + the digital-thread pattern define the *shape* of the audit/documentation trail high-risk obligations consume.
- **Logging / record-keeping (Art. 12/19)** — *Alignment-enabling, build-immature.* The AEON Evidence plane *specifies* the right emit-only shape, but — as with the LangSmith comparison — AIDE's evidence trail is largely unbuilt. This is the gap most material to actually *producing* Act-required logs.
- **Harmonized-standards conformance** — *Indirect / pending.* AIDE aligns to the Act *through* ISO-IEC SC 42 (esp. 42001); see the cross-ref. No OJEU-cited harmonized standard is in force yet (first expected 2026), so the presumption-of-conformity route is not yet available to anyone.

**Synthesis.** AIDE is **compliance-enabling architecture**, not a compliance claim. The canon's OAgents evidence emission + digital-thread + MxM Morals + HCAE human-curation are the **mechanisms that produce the conformance evidence** the Act's high-risk obligations demand — they map cleanly onto Annex IV documentation, Art. 12 logging, and Art. 14 oversight. **AIDE provides the technical substrate to evidence high-risk-AI obligations.** It does **not** make any deployment "compliant" — compliance is a **legal determination** for the deployment's operator, reached through conformity assessment (ideally against an OJEU-cited harmonized standard once one exists). The relationship is layered, not competitive: **Act (obligation) → harmonized standard (technical detail) → AIDE (evidence production)**.

## 5. Objective implication

Two Doerr-style Objective shapes follow (note: not *catch-up*/*defend* — the target is a law, so the shape is *evidence-readiness*):

1. **Evidence-readiness (build the logging/evidence plane).** The decisive gap is that Art. 12/19 logging maps to an AEON Evidence plane that is *emit-only spec*. KR shape: realize a working evidence/digital-thread trail on an AIDE exemplar that demonstrably emits the record types Annex IV + Art. 12 enumerate (period-of-use, inputs, oversight events) — convergent with the langchain-survey OTel-GenAI evidence-object catch-up KR.
2. **Compliance-mapping artifact (make the substrate claim concrete).** KR shape: a documented **"evidence the high-risk obligations of an EU-deployed AI system"** mapping — Annex IV / Art. 12 / Art. 14 each crosswalked to the specific OAgents-conformance, digital-thread, Morals, and HCAE outputs that satisfy them, *with* the explicit caveat that this enables evidence and is not a compliance determination. Cross-link to the [ISO-IEC SC 42 entry](iso-iec-sc42.md) so the harmonized-standards bridge is traceable end-to-end.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Timeline reflects the base Regulation (EU) 2024/1689 dates **plus** the *provisional* (not-yet-adopted) 2026-05-07 Digital Omnibus deferrals — re-verify on Omnibus formal adoption / OJEU publication and on first publication of an OJEU-cited harmonized standard. Cross-ref: [`iso-iec-sc42.md`](iso-iec-sc42.md) (this slice).
