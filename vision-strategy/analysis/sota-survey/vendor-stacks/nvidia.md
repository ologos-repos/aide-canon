# Vendor stack — NVIDIA (NIM / NeMo / Blueprints / AI Enterprise)

> SOTA-survey finding. Shape per [`../README.md`](../README.md) → [`sota-survey/README.md`](../../sota-survey/README.md). Cadence: **fast** (NVIDIA rebrands aggressively — the AIQ → NeMo Agent Toolkit rename and the GTC/Computex 2026 NemoClaw/OpenShell naming churn are recent examples; treat product specifics as a dated snapshot, not a fixed spec).

## 1. What it is

**NVIDIA's enterprise-AI stack is, first and above all, an *infrastructure* substrate** — accelerated inference and the model/agent-serving plumbing on top of it. It is **not** a governance corpus, and (unlike LangChain Enterprise) it is not primarily a build-and-orchestrate platform either; the agentic surfaces are recent additions layered on a substrate that is fundamentally about *running models fast and safely on GPUs*. Five surfaces compose the relevant slice:

- **NIM (NVIDIA Inference Microservices)** — portable, optimized, containerized inference microservices: a model (or guardrail, or retriever) packaged as a standard API endpoint, GPU-accelerated, deployable cloud/hybrid/on-prem. This is the load-bearing surface — the **inference-serving substrate** the rest of the stack consumes.
- **NeMo** — described by NVIDIA (2026) as an *"agent-first, open suite of libraries with skills for accelerating AI agent specialization, optimization, and governance."* It spans **build** (Curator, Data Designer, Evaluator), **deploy** (Guardrails, Auditor, NIM), and **optimize** (Customizer, Framework, RL, Relay observability) phases.
  - **NeMo Guardrails** (OSS, v0.20.x, Jan 2026) — a *programmable* guardrail layer: topic control, PII detection, RAG grounding, jailbreak prevention, multimodal content safety. Integrates with LangChain/LangGraph/LlamaIndex; also shipped as a NIM. **Output/interaction validation**, not an authority model.
  - **NeMo Agent Toolkit** (OSS; *formerly the AIQ / "Agent Intelligence" toolkit*) — a framework-agnostic *"conductor"* for connecting, profiling, evaluating, and optimizing teams of AI-aides across LangChain, LlamaIndex, CrewAI, Semantic Kernel, Agno, etc. The emerging orchestration/observability piece.
- **NVIDIA Blueprints** — reference workflows (partner microservices + AI-aide reference code + customization docs + Helm chart) for common agentic patterns; e.g. the open **AI-Q Blueprint** for enterprise-data agents.
- **NVIDIA AI Enterprise** — the commercial software platform/license tier (support, SLA, security, supported NIM/NeMo builds) wrapping the above for production.

The value proposition is **performance, portability, and a safe inference substrate** — the GPU-accelerated plumbing under an agentic system. In aide-canon terms this is a **Means-layer implementation substrate**, and specifically the *deepest* Means layer: the **INFRASTRUCTURE / inference** altitude AIDE explicitly is *not*.

## 2. Source links

- Official: `nvidia.com/en-us/ai-data-science/products/nemo/`, `developer.nvidia.com/nemo-agent-toolkit`, `developer.nvidia.com/nemo-guardrails`, `docs.nvidia.com/nemo/guardrails/`, `build.nvidia.com/blueprints` (NIM/Blueprints catalog), `docs.nvidia.com/ai-enterprise/`.
- OSS: `github.com/NVIDIA/NeMo-Agent-Toolkit`, `github.com/NVIDIA-NeMo/Guardrails`, `github.com/NVIDIA-AI-Blueprints/aiq`.
- Announcements (2026): agentic-AI Blueprints launch, NIM guardrail microservices, GTC/Computex 2026 NemoClaw + OpenShell secure-runtime + Nemotron/Agent Toolkit bundling.
- **Rebrand-prone:** product names churn hard here — *AIQ → NeMo Agent Toolkit*; the GTC-2026 "NemoClaw" orchestration-blueprints framing and "OpenShell" runtime-policy naming are very fresh and may not stick. Verify surface names at read time.

## 3. Map against AIDE

### Against the four AIDE planes

| AIDE plane | NVIDIA equivalent | Position |
|---|---|---|
| **Control** (AEON governance) | NeMo Guardrails + Blueprint policy templates — **no authority/trust governance model** | *AIDE ahead* on governance/authority; NVIDIA carries policy-as-config, not authority-altitude |
| **Runtime** | **NIM** (inference runtime) + NeMo Agent Toolkit orchestration | *In flight (infrastructure)* — strongest at the inference-serving layer; *AIDE behind* on realized runtime |
| **Experience** (AIDEX) | Build-portal / blueprint reference UX; no operator-as-curator console | **AIDE ahead** — no HCAE operator-curation experience model (NVIDIA is light here by design) |
| **Capability** (OAAD) | NIM microservice catalog + Blueprints + tool/agent plugins | *In flight elsewhere* — broad, mature catalog of deployable capability units |

### Against the six AEON service planes

| AEON plane | NVIDIA equivalent | AIDE position |
|---|---|---|
| **Identity** | Container/service identity; no principal-altitude model | *AIDE ahead* — no AI-aide-under-a-principal identity concept |
| **Authority** | Blueprint/OpenShell runtime *policy controls* (config-level) | **AIDE ahead** — OrdSA O0–O6 authority-down/evidence-up is wholly absent |
| **Evidence** | NeMo Agent Toolkit profiling/observability; NeMo Relay; Auditor | *In flight (infrastructure)* — real telemetry/profiling exists; not an emit-only spec but not an authority-grounded evidence trail either |
| **Integration** | NIM standard APIs; MCP support; framework plugins | *In flight elsewhere* — broad, mature, portability-first |
| **Capability composition** | Agent Toolkit "conductor" + Blueprints (task decomposition, delegation, tool invocation) | *In flight (infrastructure)* — composes across frameworks; but **no envelope-refinement composition law** (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | **NeMo Agent Toolkit** (the emerging conductor) over NIM | *In flight (infrastructure)* / *AIDE behind* on shipping runtime; *converging* via the workflow-orchestration pattern |

*(Inference is AEON's **7th** plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md). This is NVIDIA's single strongest map: **NIM is the canonical realized Inference plane** — model-agnostic, portable, GPU-accelerated serving as a first-class deployable unit. Where AIDE frames Inference as a *governance* plane (substrate-swappable by design), NVIDIA ships the actual swappable substrate. On Inference, **AIDE is behind on realization** and NVIDIA is the reference infrastructure AIDE's Inference plane would sit atop.)*

### Vocabulary collision

- NVIDIA **"agent"** (NeMo Agent Toolkit, "teams of AI agents") = the canon's **AI-aide** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) — an AI system acting under a principal — **not** the OAgents `Agent` primitive (a typed object inside a behavioral envelope). Never carry NVIDIA's bare "agent" into canon prose.
- NVIDIA **"Skill"** (NeMo "libraries with skills", "agent skills" in CUDA-X) maps to MxM **Means** — a packaged capability, not a governance primitive.
- NVIDIA **"Tool"** = atomic invocation (convergent across the field).
- NVIDIA **"Guardrails"** ≠ the OAgents behavioral envelope (see §4). It is output/interaction validation, not an authority or envelope model.
- **Entity distinction:** NVIDIA's "agents"/"teams of agents" must not be conflated with the Ologos operator fleet or NG-AIDE-01; no bare "fleet" reading of NVIDIA marketing copy.

## 4. Classification

**Mixed — "in flight (infrastructure)," at a *deeper* altitude than LangChain.** The load-bearing finding: aide-canon and NVIDIA's stack are *different categories* at *different altitudes* — a **governance/architecture corpus** vs an **inference/infrastructure substrate** — so classification is per-axis, not global:

- **Inference plane** — *AIDE behind on realization; NVIDIA is the reference infrastructure.* **NIM** is the strongest single map in the whole survey: a shipping, portable, model-agnostic inference substrate that *is* what AIDE's Inference plane (ADR-EA-0015) abstracts as governance. AIDE governs substrate-swappability; NVIDIA *is* the swappable substrate.
- **AIDE ahead** — **Authority** (OrdSA O0–O6 is entirely absent — NVIDIA has runtime *policy config*, not authority altitude); **Identity** (no AI-aide-under-principal model); **Experience/AIDEX** (no HCAE operator-as-curator console); **behavioral envelope / trust layer** (see the Guardrails assessment below); **deontic constraints** (MxM Morals); vendor-neutral conformance criteria.
- **NeMo Guardrails vs the OAgents envelope — assessed precisely:** Guardrails is a *programmable, mostly POST-execution output-validation* layer (topic control, PII, grounding, jailbreak, content safety). It is a **partial envelope component** — it overlaps the OAgents POST-execution gate slice, and is real, shipping, and GPU-optimized (a genuine *behind*-on-realization point for that one slice). But it is **not** the full OAgents behavioral envelope: no typed-object model, no PRE/authority gating tied to a principal, no ordinal authority, no trust-during-execution guarantee across composition. Per OAgents §10, behavioral trustworthiness sits *above any framework* — Guardrails is a configurable safety filter inside the framework, not the envelope around it. So: **AIDE ahead on the envelope/authority model; behind on the realized output-validation slice.**
- **In flight (infrastructure)** — **NeMo Agent Toolkit** orchestration (the emerging "conductor"; converging with the AEON orchestration-runtime / workflow-orchestration pattern); **Blueprints/NIM catalog** capability breadth; **profiling/observability** evidence telemetry; integration/portability.

**The synthesis:** they **compose, not compete — and NVIDIA sits *below* even LangChain in the stack.** aide-canon is the governance layer one wraps *around* an agentic deployment; NVIDIA is the **inference/infrastructure floor** that deployment runs *on*. The clean picture: **NIM as the AEON Inference plane**, NeMo Agent Toolkit as a Means-layer runtime, NeMo Guardrails as one configurable POST-execution gate inside the envelope — with OAgents' full envelope + OrdSA authority + MxM Morals + HCAE supplying the trust/authority/experience the infrastructure structurally does not (and by design does not try to) provide. This is the OAgents §10 "above any framework" thesis applied one altitude deeper than the LangChain entry: the trust/authority layer sits above *both* the framework (LangChain) *and* the inference substrate (NVIDIA).

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance/authority lead).** NVIDIA is the canonical example of a *mature, shipping infrastructure substrate with zero authority/identity/experience governance* — by design. Propagate the OrdSA-authority + OAgents-envelope + HCAE position as the trust/authority/curation layer above the inference floor. KR shape: a documented "govern-an-NVIDIA-NIM/NeMo-deployment" mapping (envelope + OrdSA authority + Morals over NIM/Agent-Toolkit/Guardrails).
2. **Catch-up / adopt-the-floor (Inference plane realization).** NIM is the reference realization of the Inference plane (ADR-EA-0015) — AIDE specs it as governance but ships no substrate. KR shape: name NIM (and equivalents) as the canonical Inference-plane substrate the AEON Inference plane abstracts, and demonstrate a substrate-swap against an AIDE exemplar to prove the governance claim holds over a real serving layer.
3. **Converge-or-differentiate (orchestration + guardrails).** Position the **workflow-orchestration pattern** ([ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)) as the governing spec over NeMo-Agent-Toolkit-class conductors, and frame NeMo Guardrails as an *implementable POST-execution gate* inside the OAgents envelope — convergent on the safety-filter mechanic, differentiated by the authority/envelope model Guardrails does not carry.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Naming captured at the AIQ → NeMo Agent Toolkit rename and the GTC/Computex 2026 NemoClaw/OpenShell announcements; rebrand-prone — revisit on the next NVIDIA product shift or at OKR refresh.
