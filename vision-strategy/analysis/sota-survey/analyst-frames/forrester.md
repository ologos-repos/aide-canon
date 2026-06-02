# Analyst frame — Forrester (Waves, AEGIS, Data & AI Governance Model, TEI)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Slice: **analyst-frames** (medium cadence — annual flagship Waves + quarterly notes; treat report quarters as dated snapshots). Mapping anchor: the four analyst-frame questions in [`README.md`](README.md) (category-definition, maturity placement, maturity-model dimensions vs. AEON planes, named-vendor coverage).

## 1. What it is

**Forrester** is a tier-1 industry analyst house whose enterprise-AI output in 2026 spans four instrument types relevant to this survey:

- **The Forrester Wave™** — vendor-comparison reports scoring a defined market on three axis-groups (**current offering**, **strategy**, **market presence**), plotting vendors as Leaders / Strong Performers / Contenders / Challengers. The 2026 Waves touching agentic ground are category-specific, not a single "AI agents" Wave: **GRC (Governance, Risk, And Compliance) Platforms, Q2 2026** (12 vendors); **Conversational AI Platforms For Customer Service, Q2 2026**; **Customer Service Solutions, Q1 2026**. No standalone "agentic AI platform" or "AI foundation model" Wave was found published as of this survey date — "agentic" enters as a *scoring criterion* inside existing market Waves rather than as its own market.
- **AEGIS** — *Agentic AI Enterprise Guardrails For Information Security*: a security-architecture framework (not a Wave) defining six dimensions for deploying agents safely, with a four-phase, 12-month-plus adoption maturity arc.
- **The Forrester Data And AI Governance Model** — a governance reference model framing data and AI assets as products, organized around five strategic outcomes (security, privacy, compliance, self-service, discovery).
- **Total Economic Impact™ (TEI)** — vendor-commissioned ROI studies (e.g., Microsoft's agentic AI solutions / Foundry; Cognite; WRITER; Glean; boost.ai), reporting payback periods and multi-year ROI/NPV for *named vendor products*.

The unifying 2026 Forrester thesis is governance-forward and ROI-skeptical: AI "moves from hype to hard hat work," enterprises will defer ~25% of planned AI spend to 2027, and ~60% of Fortune 100 will appoint a head of AI governance. In aide-canon terms Forrester is a **market-cartography instrument**, not a governance corpus or a substrate — it maps which *vendors* are winning which *markets*, the altitude aide-canon is explicitly *not* at.

**Paywall note:** All flagship Forrester reports (every Wave, the Data & AI Governance Model `RES184942`, AEGIS detail, full TEI PDFs) are paywalled. This entry is built from Forrester's own public announcement blogs/press, vendor redistributions (flagged below), and press summaries — verbatim figures and Leader names are attributed to those public sources, not the gated reports.

## 2. Source links

Public / freely accessible (primary-public, attributed):

- Forrester blog — *Announcing The Forrester Wave™: GRC Platforms, Q2 2026* — `forrester.com/blogs/announcing-the-forrester-wave-governance-risk-and-compliance-platforms-q2-2026/` (12 vendors; "system of record to a system of action"; agentic-AI claims outrunning delivery). **Full Wave paywalled** (`forrester.com/report/...RES194652`).
- Forrester — *AEGIS Framework* overview — `forrester.com/technology/aegis-framework/` (six dimensions; four-phase maturity).
- Forrester blog — *Agentic AI Enters Its Enterprise Execution Era* — `forrester.com/blogs/agentic-ai-enters-its-enterprise-execution-era/` ("risk shifts from incorrect outputs to real-world consequences"; "inspectable and user-controlled").
- Forrester blog — *Predictions 2026: AI Moves From Hype To Hard Hat Work* — `forrester.com/blogs/predictions-2026-ai-moves-from-hype-to-hard-hat-work/`; press release `forrester.com/press-newsroom/forrester-tech-security-2026-predictions/` (25% spend deferral; head-of-AI-governance prediction).
- **Paywalled (flagged):** *The Forrester Data And AI Governance Model* — `forrester.com/report/the-forrester-data-and-ai-governance-model/RES184942` (login-gated; five strategic outcomes visible in preview only).

Vendor redistributions / commissioned (secondary — flag the redistributor):

- TEI (Microsoft-commissioned, hosted on `tei.forrester.com/go/microsoft/`) — Microsoft agentic AI / Foundry: payback "as few as six months," up to 35% technical-team productivity. Microsoft Azure blog redistribution.
- Vendor "named a Leader" press (NiCE Cognigy, Kore.ai, Omilia — Conversational AI; Salesforce, Microsoft, Pegasystems, ServiceNow — Customer Service Solutions Q1 2026; Diligent, Optro — GRC Q2 2026). Treat as redistributor-sourced Leader claims.

In-canon prior research: the vendor-stack entries cross-referenced in §3 ([`../vendor-stacks/microsoft.md`](../vendor-stacks/microsoft.md), [`../vendor-stacks/salesforce.md`](../vendor-stacks/salesforce.md), [`../vendor-stacks/ibm.md`](../vendor-stacks/ibm.md), [`../vendor-stacks/google-cloud.md`](../vendor-stacks/google-cloud.md)).

## 3. Map against AIDE

### Category-definition: match / supplement / diverge

Forrester's working category for autonomous AI is **"agentic AI"** — systems that "don't just respond, but take action across real workflows." This is a **vocabulary collision** the canon already flags: Forrester's "agent" / "agentic AI" denotes a deployed organizational actor, which in canon vocabulary is an **AI-aide** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) — *not* the OAgents `Agent` primitive (a typed object inside a behavioral envelope). Forrester's "agentic" is also a market-adjective collision: it bundles autonomy + tool-use + orchestration under one label, where the canon separates capability composition (OAgents), authority (OrdSA), and deontic constraint (MxM Morals). **Verdict: diverge** — Forrester's category is broader and less precise; the canon's vocabulary *supplements* it with governance-altitude distinctions Forrester collapses.

### Wave / maturity placement vs. AIDE exemplar status

aide-canon **does not appear in any Forrester Wave** — and correctly so: a Wave scores *vendors with shipping products and market presence*, and aide-canon is a **governance CORPUS at research/exemplar stage, not a market product**. There is no honest cell for it on a Wave grid; its absence is a category fact, not a ranking. Against Forrester's own maturity read ("hype to hard hat," 60% of F100 appointing a head of AI governance, governance-maturity-must-precede-scale), the canon's *exemplar status* — design-first spec with enforcement largely unbuilt, demonstrated operationally only via [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/) — places it **upstream of Forrester's production-readiness frame**: it articulates the governance layer Forrester says the market now needs but has not yet bought.

### Maturity-model dimensions vs. the six AEON planes

The sharpest mapping is **AEGIS's six dimensions** against the six AEON service planes. (Inference is AEON's 7th plane per [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md); AEGIS has no analogue.)

| AEGIS dimension (Forrester) | Nearest AEON plane | AIDE position |
|---|---|---|
| **IAM** — agents as managed identities, "just-in-time, least-agency authorization" | **Identity** | *In flight elsewhere* — identity primitives convergent; AEGIS has no principal-altitude model |
| **Zero Trust** — "least agency… what decisions it is allowed to make" + GRC **policy-as-code** | **Authority** | **AIDE ahead** — closest market analogue to OrdSA O0–O6 authority-down/evidence-up, but AEGIS frames it as access-control, not *ordinal* authority |
| **Threat Mgmt / SecOps** — "detailed logging of prompts, actions, reasoning steps" | **Evidence** | *In flight elsewhere / AIDE behind* on realized tooling — AEGIS logging is operational; canon evidence trail is emit-only spec |
| **Data Security & Privacy** — "purpose-bounded data access" | **Integration** | *In flight elsewhere* — purpose-bounding overlaps Integration governance |
| **AppSec / DevSecOps** — AI threat modeling, agent-generated-code validation | **Capability composition** | **AIDE ahead** on the composition *law* — no envelope-refinement analogue (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **GRC** — real-time risk/compliance monitoring, policy-as-code guardrails | **Orchestration runtime** + cross-cutting | *In flight elsewhere* — GRC monitoring is the runtime-governance overlap |

Forrester's **Wave evaluation dimensions** (current offering / strategy / market presence) reveal the divergence even more bluntly: **two of the three axes — current offering and market presence — reward shipped capability and adoption**, which is exactly where a research-stage corpus scores zero and a mature substrate scores high. Only **strategy** rewards architectural foresight, and even there Forrester scores a *vendor's* roadmap, not a vendor-neutral governance thesis. **The canon's governance-altitude criteria (authority layering, deontic constraint, conformance-as-property-of-harness) have no column on a Wave** — they are the axes Forrester does not score because they are not market-differentiating *yet*. That gap is the finding.

### Named-vendor coverage (cross-ref `../vendor-stacks/`)

Forrester rates as **Leaders** several vendors with existing canon vendor-stack entries:

- **Microsoft** — Leader, *Customer Service Solutions Q1 2026*; subject of a Microsoft-commissioned **TEI** (Foundry/agentic). Cross-ref [`../vendor-stacks/microsoft.md`](../vendor-stacks/microsoft.md).
- **Salesforce** (Agentforce) — Leader, *Customer Service Solutions Q1 2026*. Cross-ref [`../vendor-stacks/salesforce.md`](../vendor-stacks/salesforce.md).
- GRC Q2 2026 Leaders (Diligent, Optro) and Conversational-AI Q2 2026 Leaders (NiCE Cognigy, Kore.ai, Omilia) have **no** canon vendor-stack entry yet — Forrester is operating in customer-service / GRC sub-markets the canon has not surveyed.
- **IBM watsonx** ([`../vendor-stacks/ibm.md`](../vendor-stacks/ibm.md)) and **Google Cloud** ([`../vendor-stacks/google-cloud.md`](../vendor-stacks/google-cloud.md)) are canon-surveyed but were not surfaced as Leaders in the 2026 agentic-adjacent Waves found here — a coverage gap to revisit if an AI-platform / foundation-model Wave publishes.

### Is AIDE / OrdSA / OAgents / MxM in analyst vocabulary? (Vision-signal check)

**Honest answer: no — not yet.** None of AIDE, OrdSA, OAgents, or MxM appears in any surveyed Forrester report, blog, prediction, Wave, AEGIS material, or TEI study as of 2026-06-01. Forrester's nearest *concepts* — "least agency," policy-as-code, governance-before-scale, agent-as-managed-identity — are convergent with canon positions but reach them under Forrester's own vocabulary, with no attribution to the canon. This is the baseline reading for the **"AIDE is named in industry conversations"** Vision success signal: the conceptual ground is being independently occupied; the canon's *terms* have zero analyst-vocabulary penetration. Track this cell at every Forrester survey pass.

## 4. Relationship + synthesis

**Market-timing + category-formation signal — not a competitor, not a peer instrument.** The classification is per-axis (the survey's three-way scheme):

- **AIDE ahead** — governance altitude. Forrester's *Predictions 2026* ("hype to hard hat," governance-must-precede-scale, head-of-AI-governance appointments) and AEGIS's "least agency… what decisions it is allowed to make" describe, in market language, the exact need the canon's OrdSA authority layer + MxM Morals + OAgents envelope were specified to fill. Forrester is *naming the demand*; the canon already has the *architecture* — but at lower precision in Forrester's framing (access-control, not ordinal authority; guardrails, not deontic constraint).
- **AIDE behind** — everything Forrester actually measures: shipped product, adoption, ROI, market presence. The TEI studies (Microsoft payback in six months, etc.) and Leader placements are evidence of *deployed* substrates; the canon has none of this, by design and stage.
- **In flight elsewhere** — AEGIS's six security dimensions and the Data & AI Governance Model occupy similar governance ground and are actively evolving; the canon should track AEGIS as the most credible *market-vocabulary* mirror of the AEON plane decomposition.

**The synthesis:** Forrester is the canon's **market-readiness barometer**, not a thing to compose with or compete against. Its 2026 turn toward AI governance, "least agency," and policy-as-code is the strongest external validation yet that the canon's thesis is correctly timed — the market is now articulating the demand the canon pre-specified. The honest relationship is therefore **category-formation signal**: when Forrester eventually scores a market the canon's governance criteria define (an "AI governance for agents" Wave, distinct from GRC-platform AI features), *that* is where the canon's thesis lands — and the canon would inform the *evaluation criteria*, not appear as a *vendor*. Until then, the canon's vocabulary remains more precise than any Forrester market-category definition, and that precision-gap is the asset to propagate.

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance-vocabulary lead).** Forrester's 2026 governance turn validates the timing but reaches the ground in coarser terms. KR shape: publish an explicit "AEGIS-six-dimensions ↔ AEON-seven-planes ↔ OrdSA-authority" crosswalk that demonstrates the canon's precision over the analyst category, and seed it where analyst-adjacent audiences read.
2. **Catch-up (evidence + production proof).** Two Wave axes (current offering, market presence) and every TEI study reward shipped, measured capability the canon lacks. KR shape: produce TEI-grade operational evidence on an AIDE exemplar (Hermetic / thinx-aidex) — even a single quantified governance-overhead-vs-risk-avoided figure converts "research-stage" toward "demonstrated."
3. **Converge-or-differentiate (named in the frame).** The Vision-signal check is currently a hard "no." KR shape: a deliberate path to first-mention — target the precise sub-market (AI-governance-for-agents) where the canon's criteria, not a vendor's product, are the differentiator, so the canon shows up as *evaluation-criteria source* rather than as an absent vendor.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Built from public Forrester blogs/press + flagged vendor redistributions; all flagship reports paywalled (no gated content quoted). Revisit on publication of any standalone "AI agents" / "AI foundation models" / "AI governance for agents" Wave, on AEGIS framework updates, or at OKR refresh.
