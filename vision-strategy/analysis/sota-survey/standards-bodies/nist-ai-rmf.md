# Standards body — NIST AI Risk Management Framework (AI RMF)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Cadence: **slow** (NIST deliverables are annual/quarterly) — but the *agentic* surface is moving fast in 2026 (CAISI AI Agent Standards Initiative), so treat the agent-specific rows as a live snapshot. AIDE-mapping anchor per [`README.md`](README.md) §"AIDE-mapping anchor": **OAgents is an explicit NIST AI RMF implementation profile** — this slice's strongest *AIDE ahead* anchor, because the canon ships a working spec/profile of the framework, not just alignment language.

## 1. What it is

The **NIST AI Risk Management Framework** is the US government's voluntary, consensus-developed framework for managing risks across the AI lifecycle. It is a *governance framework* — outcomes and a process taxonomy, deliberately implementation-agnostic and non-prescriptive about tooling. Its **Core** organizes risk-management activity into four functions — **GOVERN** (cultivate a risk-aware culture; cross-cuts the other three), **MAP** (establish context and identify risks), **MEASURE** (analyze, assess, benchmark, monitor risks), and **MANAGE** (prioritize and act on risks) — each decomposed into categories and subcategories. Organizations apply the framework to a use case via a **Profile**; NIST also ships a **Playbook**, **Crosswalks** to other frameworks (ISO/IEC 42001, EU AI Act-adjacent work), and the AI Resource Center (`airc.nist.gov`). The **Generative AI Profile** (NIST AI 600-1) is the first cross-sectoral companion profile, enumerating 12 GAI-specific risk categories with suggested actions mapped back to the four Core functions. As of 2026 the agentic frontier is led by **CAISI** (the Center for AI Standards and Innovation, the renamed US AI Safety Institute, inside NIST), whose **AI Agent Standards Initiative** is the standards venue most directly relevant to AIDE.

**Version / status header**

| Field | Value |
|---|---|
| **Framework** | AI RMF 1.0 — NIST AI 100-1 |
| **Version / date** | 1.0, released **2023-01-26** ([DOI 10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1)) |
| **Status** | Active, voluntary; no 2.0 announced. Extended by profiles, not superseded. |
| **GenAI Profile** | NIST AI 600-1, released **2024-07-26** — active companion profile (12 GAI risk categories) |
| **Agentic work** | **CAISI AI Agent Standards Initiative** launched **2026-02-17**; an **AI Agent Interoperability Profile** is planned for **Q4 2026** (identity/authorization, security/risk, monitoring/logging). |
| **Adjacent 2026 deliverable** | Concept note for an *AI RMF Profile on Trustworthy AI in Critical Infrastructure*, released **2026-04-07**. |
| **Successor / supersession** | None. AI RMF 1.0 remains the authoritative framework; the agentic Profile (Q4 2026) will be a *companion*, not a replacement. |
| **Geography** | **US** (NIST, Dept. of Commerce). Voluntary, not regulation. CAISI's 2025 rebrand narrowed emphasis toward security/national-security risk over "safety" framing — material to how the agentic profile will read. International alignment is pursued via crosswalks + ISO/IEC JTC 1/SC 42. |

## 2. Source links

- **Framework hub:** [`nist.gov/itl/ai-risk-management-framework`](https://www.nist.gov/itl/ai-risk-management-framework) · core doc [NIST AI 100-1 (PDF)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), [DOI 10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1).
- **GenAI Profile:** [NIST AI 600-1 (PDF)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) · [publication page](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) (2024-07-26).
- **Playbook + AI Resource Center:** [AI RMF Playbook](https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook) · [`airc.nist.gov`](https://airc.nist.gov).
- **CAISI agentic work:** [Announcing the AI Agent Standards Initiative](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure) (2026-02-17) · [CAISI rename background](https://fedscoop.com/trump-administration-rebrands-ai-safety-institute-aisi-caisi/) (2025-06-03).
- **In-canon profile (the load-bearing reference):** OAgents — [`constructs/oagents/`](../../../../constructs/oagents/), spec [`spec/oagents-nist-standard-v16.0.md`](../../../../constructs/oagents/spec/oagents-nist-standard-v16.0.md) (self-described "pre-standardization draft **profile**" referencing NIST AI 100-1 + AI 600-1; maps its control taxonomy to GOVERN/MAP/MEASURE/MANAGE in §"AI RMF function alignment" + Appendix A), [`10.5281/zenodo.19425021`](https://doi.org/10.5281/zenodo.19425021).
- **Candidate eval harness for the MEASURE/conformance angle:** [`../oss-frameworks/inspect-ai.md`](../oss-frameworks/inspect-ai.md) (UK AISI's Inspect — the harness that could execute OAgents conformance evidence).

## 3. Map against AIDE

The framework maps most cleanly to **OAgents** (an explicit profile of it) and to AEON's **Authority**, **Evidence**, **Integration**, and **Identity** planes. Alignment status uses the survey's three-way classification ([`sota-survey/README.md`](../README.md)).

### NIST AI RMF Core function → OAgents profile control → AEON plane

| AI RMF Core function | OAgents profile control (the implementing mechanism) | AEON plane | Alignment status |
|---|---|---|---|
| **GOVERN** (risk-aware culture; cross-cutting) | Behavioral-envelope components as *executable* governance: session protocols, deontic constraints (MxM Morals), incident governance, enforcement gates that **prevent** non-compliant actions rather than discourage them | **Authority** (OrdSA O0–O6 authority-down / evidence-up) | **AIDE ahead** — OAgents instantiates GOVERN as runtime enforcement, and OrdSA adds an authority-altitude semantics NIST does not specify |
| **MAP** (establish context; identify risk) | Knowledge-injection + context-classification components (operationalize context-establishment as a precondition to action) | **Integration** (context/capability assembly) | *In flight elsewhere* — convergent intent; OAgents has a concrete envelope mechanism, NIST has the function requirement |
| **MEASURE** (analyze, benchmark, monitor) | Quality-gate components + observable evidence criteria (3 conformance levels: self → documented → 3PAO-style) | **Evidence** | **AIDE behind on the harness** — OAgents *requires* evidence as conformance proof but names no harness to generate/grade it (candidate: [Inspect](../oss-frameworks/inspect-ai.md)); **ahead on the conformance model** |
| **MANAGE** (prioritize; act on risk) | Enforcement mechanisms, incident-lifecycle tracking, lessons-learned pipeline | **Evidence** + **Authority** | **AIDE ahead** — OAgents operationalizes MANAGE as a closed enforcement+lessons loop tied to the authority trail |
| **GOVERN 1.x** (accountability; who-is-responsible) | OAgent role split: AI operator implements/maintains the envelope under operator-determined risk tolerance | **Identity** (principal-altitude / AI-aide-under-principal) | **AIDE ahead** — the principal/AI-aide accountability split is first-class in the canon, named only abstractly in the framework |
| GenAI Profile (NIST AI 600-1) GAI risk categories | Anti-Hallucination control set (explicitly addresses the AI 600-1 "Confabulation" category; full 12-category mapping in spec Appendix A) | **Evidence** | *In flight elsewhere* — partial coverage shipped, full mapping in progress |
| CAISI AI Agent Interoperability Profile (Q4 2026 — identity/authz, security, logging) | Not yet published; OAgents envelope + AEON Identity/Integration are the canon's pre-positioned answer | **Identity** + **Integration** | *In flight elsewhere* — **converge-or-differentiate**; OAgents is offered as a community contribution aligned with this initiative (spec §Introduction) |

### Vocabulary collision (flag on read)

The framework speaks of **"AI systems"** and **"AI actors"** — process-level roles, not the canon's principal model. NIST's **Profile** = "an application of the Core functions to a use case"; **OAgents `Profile`** uses the term in exactly this NIST sense (good — no collision, deliberate inheritance). The collision to watch is **"agent"**: NIST/CAISI's emerging "AI agent" is a *system that takes autonomous action* — neither the canon's **AI-aide** (an AI acting under a principal, per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) nor the OAgents **`Agent`** primitive (a typed object operating inside a behavioral envelope). When the CAISI Agent Interoperability Profile lands, map its "agent" to **OAgent + AI-aide** explicitly; never let the casual "agent" reading stand. **"Risk"** is convergent. NIST's **GOVERN/MAP/MEASURE/MANAGE** are *functions* (process verbs); do not conflate with OrdSA's **O0–O6** *authority altitudes* (governance-layer constructs) — they sit at different layers and the OAgents profile maps the former onto mechanisms that the latter authorizes.

## 4. Alignment classification

**Per-axis — the canon *consumes and extends* the framework; it does not compete with it.** AI RMF is a governance framework and aide-canon is a governance/architecture corpus that ships a profile *of* it, so the relation is alignment, not category-rivalry:

- **AIDE ahead — "we ship a profile implementation."** This is the slice's strongest anchor: OAgents is an explicit NIST AI RMF implementation profile ([`spec/oagents-nist-standard-v16.0.md`](../../../../constructs/oagents/spec/oagents-nist-standard-v16.0.md)) that maps a behavioral-envelope control taxonomy onto all four Core functions and addresses an AI 600-1 GAI risk category through executable controls. The canon turns RMF's *outcome statements* into *runtime enforcement mechanisms* — the [`feedback_enforcement_not_documentation`] discipline applied to a national framework. OrdSA further extends the GOVERN function with an **authority-altitude** semantics (O0–O6 authority-down / evidence-up) the framework leaves unspecified, and the canon's principal / AI-aide split sharpens GOVERN's accountability requirement.
- **AIDE behind — the *authority* of the framework, and the MEASURE harness.** Honest caveat: **NIST AI RMF is the authoritative, government-issued framework; OAgents is one (pre-standardization, draft, self-issued) profile of it** — un-adopted, un-ratified, single-author. NIST has institutional consensus weight, broad adoption, crosswalks, a Playbook, and an Agent Standards Initiative with NSF co-investment; OAgents has none of that reach yet. And RMF's MEASURE function exposes the canon's standing evidence-harness gap (cf. [`../oss-frameworks/inspect-ai.md`](../oss-frameworks/inspect-ai.md), [`../vendor-stacks/langchain.md`](../vendor-stacks/langchain.md) §4): the conformance model is specified, the harness to run it is not.
- **In flight elsewhere — the agentic profile.** The **CAISI AI Agent Standards Initiative** (launched 2026-02-17) and its **AI Agent Interoperability Profile** (Q4 2026: identity/authorization, security/risk, monitoring/logging) occupy ground the canon already holds via OAgents + AEON Identity/Integration. This is the converge-or-differentiate frontier: OAgents is explicitly positioned as a community contribution aligned with this initiative.

**The synthesis:** the canon **aligns with and extends** AI RMF — RMF supplies the authoritative function taxonomy and the legitimacy surface; OAgents supplies the working profile that makes those functions executable for *operational, high-consequence AI-aides*, a setting the spec notes no prior RMF profile has addressed. The relationship is the same canon-spec ↔ substrate pattern documented for [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/): NIST is the framework, OAgents is the realized profile, and AEON's Authority/Evidence/Identity/Integration planes are where it runs.

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (profile lead).** Propagate "OAgents is a working NIST AI RMF profile for operational AI-aides" as the canon's flagship standards-alignment claim — RMF is the most-cited US AI governance framework and the canon already implements it. KR shape: complete the **full AI 600-1 12-category → OAgents-control mapping** (Appendix A) and publish a one-page GOVERN/MAP/MEASURE/MANAGE → envelope-component crosswalk as a canonical artifact.
2. **Catch-up (MEASURE harness).** RMF's MEASURE function exposes the evidence-harness gap; OAgents conformance is specified but not executable. KR shape: stand up an **OAgents conformance suite on [Inspect](../oss-frameworks/inspect-ai.md)** — encode behavioral-envelope properties as Tasks/Scorers so MEASURE-function conformance is produced and graded reproducibly, not asserted.
3. **Converge-or-differentiate (CAISI agentic profile).** The CAISI **AI Agent Interoperability Profile** (Q4 2026) is the convergence event to track. KR shape: pre-position a **OAgents-vs-CAISI-profile delta map** keyed to identity/authorization (AEON Identity), security/risk (the envelope), and monitoring/logging (Evidence) — submitting OAgents as a community contribution where convergent, articulating the OrdSA authority-altitude differentiation where not.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Grounds on official NIST sources (AI 100-1 2023-01-26, AI 600-1 2024-07-26, CAISI Agent Standards Initiative 2026-02-17, Critical-Infrastructure profile concept note 2026-04-07) and the in-canon OAgents spec (`oagents-nist-standard-v16.0.md`). Revisit on the **CAISI AI Agent Interoperability Profile** release (expected Q4 2026), any AI RMF 2.0 signal, or at OKR refresh.
