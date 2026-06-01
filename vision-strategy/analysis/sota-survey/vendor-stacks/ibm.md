# Vendor stack — IBM watsonx

> SOTA-survey finding. Shape per [`../README.md`](../README.md) → [`sota-survey/README.md`](../../sota-survey/README.md). Cadence: **fast** (the watsonx product line renames and reorganizes frequently — "watsonx.governance" / "watsonx Orchestrate" surface specifics are a dated snapshot, not a fixed spec). **This is the most nuanced vendor entry to date: watsonx.governance is the one surveyed stack that genuinely contests AIDE's *governance* altitude.**

## 1. What it is

**IBM watsonx** is IBM's enterprise AI platform — a *build-govern-and-run* substrate, not a governance/architecture corpus. Three surfaces are in scope here, plus the model family:

- **watsonx.ai** — the model dev/runtime studio: foundation-model library, prompt lab, fine-tuning, and the **AI Gateway** for multi-provider model routing (Granite, plus OpenAI, Anthropic, Google Gemini, Mistral, Ollama — explicit no-lock-in framing).
- **watsonx Orchestrate** — the enterprise agentic surface. As of IBM Think 2026 (May 2026) it is positioned as an **agentic control plane**: a centralized place to "run, manage and govern an organization's agentic estate." Includes the no-code **AI Agent Builder**, an **Agent Development Kit (ADK)**, **Langflow** visual prototyping, an **Agentic Workflow Builder** (structured multi-step guidance), **AgentOps** (built-in observability + policy-based controls), pre-built **domain agents** (Finance, Supply Chain), and multi-agent interop including native, Langflow, LangGraph, and open **A2A**-protocol agents.
- **watsonx.governance** — a genuine **AI-governance product**, not a feature bolt-on. Three core components: **AI lifecycle management** (use-case → dev → validation → production monitoring), **compliance accelerators** (EU AI Act, ISO 42001, NIST AI RMF), and **agentic AI governance**. Carries **AI factsheets** ("nutritional labels" — automatic model-fact logging across performance, fairness, explainability, compliance status), the **Risk Atlas** (now extended with agentic risks: function-calling hallucination, redundant actions, confidential-data leakage, attacks on an agent's external resources), an **AI Agent object type** with onboarding workflows, a **Governed Agentic Catalog**, and continuous agentic monitoring with threshold alerts.
- **Granite** — IBM's open-weight (Apache-2.0) model family; the Granite 4.x generation spans dense LLMs (3B/8B/30B), plus speech/vision/embedding/**Guardian** (safety) models, cryptographically signed, optimized for vLLM/SGLang/llama.cpp.

The enterprise value proposition is an **integrated, governed, multi-vendor AI estate** — the plumbing of building, governing, and running agents in production. In aide-canon terms it is a **Means-layer implementation substrate** — the altitude AIDE explicitly is *not* — **except** that watsonx.governance reaches partway up into the governance altitude AIDE claims as distinctive. That partial overlap is the entire interest of this entry.

## 2. Source links

- Official: `ibm.com/products/watsonx-governance`, `ibm.com/products/watsonx-orchestrate`, `ibm.com/products/watsonx-ai`, `ibm.com/granite`, `research.ibm.com` (Granite 4.x), `dataplatform.cloud.ibm.com/docs` (Risk Atlas, AI-governance planning), IBM Think 2026 announcements (`ibm.com/new/announcements/…`).
- In-canon prior research: the LangChain entry [`langchain.md`](langchain.md) establishes the per-axis "different-altitude" method this entry extends; the vendor-vocab discipline derives from [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md).
- (Product naming is rebrand-prone — IBM renamed/reorganized the watsonx line repeatedly; "watsonx Orchestrate as agentic control plane" is the May-2026 framing. Verify surface names at read time. **Note also IBM's own collision: it calls watsonx Orchestrate a "control plane," which is *not* the canon's Control plane = AEON — see §3 vocab note.**)

## 3. Map against AIDE

### Against the four AIDE planes

| AIDE plane | watsonx equivalent | Position |
|---|---|---|
| **Control** (AEON governance) | watsonx Orchestrate "agentic control plane" + **watsonx.governance** lifecycle/risk governance | *In-flight / partial-parity* on governance (the one vendor that contests this altitude); *AIDE ahead* only on ordinal-authority + per-action behavioral-envelope (see below) |
| **Runtime** | watsonx Orchestrate runtime + ADK + Agentic Workflow Builder; watsonx.ai serving | *AIDE behind* on realized runtime (shipping, scaled, multi-agent) |
| **Experience** (AIDEX) | AI Agent Builder / Langflow (a *builder/admin* UX) + AgentOps console | *AIDE ahead* — a build/ops console, not an HCAE operator-as-curator experience model |
| **Capability** (OAAD) | Foundation-model library, domain agents, tool/skill integrations, Granite | *In flight elsewhere* (mature breadth; deep model+agent catalog) |

### Against the six AEON service planes

| AEON plane | watsonx equivalent | AIDE position |
|---|---|---|
| **Identity** | Agent onboarding + **AI Agent object type** (governed agent registry); platform auth | *In flight elsewhere* — agents are first-class governed objects, but no principal-altitude identity model |
| **Authority** | Policy-based controls (AgentOps); RBAC; lifecycle approval gates | *AIDE ahead* — **OrdSA O0–O6 authority-down/evidence-up** ordinal layering is absent; IBM has policy + RBAC, not authority-*altitude* |
| **Evidence** | **AI factsheets**, Risk Atlas, continuous monitoring, AgentOps observability, compliance accelerators (EU AI Act / NIST AI RMF / ISO 42001) | **AIDE behind** — factsheets + lifecycle audit are built, mature, evidence-rich and regulator-mapped; AIDE's evidence trail is emit-only spec |
| **Integration** | AI Gateway (multi-provider), MCP/A2A, Langflow/LangGraph interop | *In flight elsewhere* — broad, mature, open-protocol |
| **Capability composition** | Agentic Workflow Builder; multi-agent collaboration; domain agents | *In flight elsewhere* — strong; but no **envelope-refinement** composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | watsonx Orchestrate (agentic control plane) | **AIDE behind** on realized orchestration runtime; *converging* via the workflow-orchestration pattern |

*(Inference is AEON's 7th plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md): watsonx.ai's AI Gateway is model-provider-agnostic, and Granite is open-weight — but model-agnosticism is an integration convenience here, not a first-class **governance** property the way the Inference plane frames it.)*

### Vocabulary collision

- IBM's **"control plane"** (watsonx Orchestrate) ≠ the canon's **Control plane = AEON**. IBM's is an estate-management runtime console; AEON is the governance plane. Direct surface collision — flag on every read.
- watsonx **"AI Agent"** (a governed object type / running organizational entity under a principal) is the canon's **AI-aide** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)), **not** the OAgents `Agent` primitive (a typed object inside a behavioral envelope). Use **AI-aide** when referring to IBM's running agents under a principal; reserve casual "agent" usage.
- watsonx **"AgentOps"** = ops/observability tooling ↦ maps to the Evidence + Means layers, not to MxM **Morals** (deontic constraints).
- IBM's compliance/governance vocabulary is **model/risk-lifecycle** governance — distinct from the canon's **agent behavioral-envelope + authority-altitude** governance. The two words "governance" name different altitudes; do not let the shared word imply parity (see §4).

## 4. Classification

**Mixed — "in flight elsewhere," at a different altitude — but with one sharp caveat that makes this the canon's hardest vendor call.** watsonx is a **build-govern-and-run platform**; aide-canon is a **governance/architecture corpus**. Per-axis:

- **AIDE ahead** — **only on two specific constructs**: (1) **OrdSA ordinal authority** (O0–O6 authority-down / evidence-up altitude layering — IBM has policy + RBAC + lifecycle gates, but not authority-*altitude*), and (2) the **OAgents per-action behavioral envelope** over a *running* agent (OAgents §10 names this as the layer that sits "above any framework"; IBM governs the model/agent *object* and its *lifecycle*, not each in-flight action against a deontic envelope). Also ahead on HCAE operator-as-curator and on vendor-neutral conformance criteria.
- **In-flight / partial-parity — and this is the load-bearing nuance** — on the **governance / Authority / Evidence** axes. **watsonx.governance is the one surveyed stack that approaches AIDE's governance altitude.** It does genuine **model/risk-lifecycle governance**: AI factsheets, Risk Atlas (with agentic risks), lifecycle approval, EU-AI-Act/NIST-RMF/ISO-42001 compliance accelerators, continuous monitoring with threshold alerts, and a governed agent registry. On *model-governance and regulatory compliance*, **IBM is strong and AIDE is not cleanly ahead** — likely behind on shipped, regulator-mapped evidence tooling. The distinction that preserves AIDE's distinctive: IBM governs **what an agent/model is and whether its lifecycle is compliant**; AIDE's claim is governing **what an agent is permitted to do, per action, at a given authority altitude** (envelope + ordinal authority). That is a real difference — but it is *narrow*, and it is honest to say IBM contests the broader governance ground.
- **AIDE behind** — realized runtime (watsonx Orchestrate), observability/eval (AgentOps + factsheets), regulatory-compliance tooling (the EU-AI-Act/NIST-RMF accelerators have no AIDE equivalent), open-weight model supply (Granite), and — decisively — **it is a shipping, adopted, IBM-backed product** where AIDE is design-first research with enforcement largely unbuilt.
- **In flight elsewhere** — orchestration (Orchestrate ↔ AEON Composition/Orchestration + the workflow-orchestration pattern), integration breadth (AI Gateway, MCP/A2A), capability composition.

**The synthesis:** they **compose, not compete** — but the seam is subtler than with a pure build-and-run substrate. aide-canon supplies the layer one would wrap *around* a watsonx deployment: **OAgents' per-action envelope + OrdSA authority-altitude + MxM Morals** over watsonx Orchestrate as the Means/runtime, *consuming* watsonx.governance's factsheets/Risk-Atlas as the **Evidence plane** rather than re-inventing them. Unlike LangChain (which lacks any governance layer), IBM already occupies the *lower* governance tier (model/risk/compliance lifecycle); AIDE's defensible distinctive narrows to the **behavioral-envelope + ordinal-authority** tier that sits above it. This is the OAgents "above any framework" thesis made concrete — and it is the same canon-spec ↔ platform-substrate relationship the canon documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/) — but stated with full credit to the one vendor that already does serious governance.

*(Entity note: watsonx is IBM's commercial estate-management stack; do not conflate it with the Ologos ecosystem, the OlogosAI operator, or NG-AIDE-01. IBM's "agentic estate" is its customers' agents, not any Ologos deployment.)*

## 5. Objective implication

Three Doerr-style Objective shapes follow — sharpened by the partial-parity finding:

1. **Defend-and-extend (narrow the claim, then hold it).** Because watsonx.governance contests the broad governance ground, the defensible AIDE lead must be stated *precisely*: per-action **behavioral envelope** + **ordinal authority altitude** over a running agent, distinct from model/risk-lifecycle compliance. KR shape: a published "AIDE-vs-watsonx.governance governance-altitude map" that names exactly which governance work IBM already does well (concede it) and the specific envelope/authority constructs that remain AIDE-distinctive.
2. **Catch-up (evidence + compliance tooling).** watsonx.governance's factsheets, Risk Atlas, and EU-AI-Act/NIST-RMF accelerators are materially ahead of AIDE's emit-only evidence spec and have no AIDE compliance-mapping equivalent. KR shape: adopt a regulator-mappable evidence shape (OTel-GenAI + a factsheet-analogue) and demonstrate Risk-Atlas-grade agentic-risk coverage on an AIDE exemplar.
3. **Converge-or-differentiate (orchestration + compose-over-govern).** Position the **workflow-orchestration pattern** ([ADR-EA-0027](../../../../patterns/workflow-orchestration.md)) over Orchestrate-class runtimes, and prototype **consuming** watsonx.governance factsheets as the AIDE Evidence plane — convergent on orchestration + evidence, differentiated by the envelope-refinement composition law and ordinal-authority layering IBM does not enforce.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Calibrated against IBM Think 2026 (May 2026) announcements and current watsonx.governance / Orchestrate / Granite 4.x docs. Revisit on the next watsonx product shift (rebrand-prone) or at OKR refresh — and re-examine the governance partial-parity call specifically, as IBM is actively extending agentic governance.
