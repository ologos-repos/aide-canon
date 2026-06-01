# Vendor stack — Databricks / Mosaic AI

> SOTA-survey finding. Shape per [`../README.md`](../README.md) → [`sota-survey/README.md`](../../sota-survey/README.md). Cadence: **fast** (Databricks rebrands its AI surfaces frequently — "Mosaic AI Gateway" → "Unity AI Gateway" landed in 2026, and Agent Evaluation folded into MLflow 3 — treat product specifics as a dated snapshot, not a fixed spec).

## 1. What it is

**Databricks / Mosaic AI** is the AI tier of the Databricks lakehouse — a *build-evaluate-deploy-govern* platform for agentic systems anchored to data, not a governance corpus. It is, in aide-canon terms, a **Means-layer implementation substrate** — the altitude AIDE explicitly is *not* — with its differentiating bet being **data-and-AI in one governed system of record** (Unity Catalog). Its principal surfaces:

- **Mosaic AI Agent Framework** — the SDK/runtime for authoring agents (RAG, tool-calling, multi-agent) wired to Delta Lake data, Vector Search, Model Serving, and MLflow. The original "Agent Evaluation" companion has migrated into **MLflow 3** (see below).
- **Agent Bricks** — a higher-level, largely no/low-code surface (beta) that auto-generates domain synthetic data + task-aware benchmarks and auto-optimizes agents for cost/quality; positioned as a "unified control plane for your AI agents." Ships a six-dimension quality model (CLEARS: Correctness, Latency, Execution, Adherence, Relevance, Safety).
- **Unity AI Gateway** (*formerly* **Mosaic AI Gateway**) — a model/AI gateway: a proxy over foundation-model providers, OSS, and custom models with permissions, rate limiting, default safety/PII guardrails, traffic routing (fallback/load-balance/A/B), usage tracking, and audit logging captured in Unity Catalog. Beta in 2026.
- **Mosaic AI Model Serving** — auto-scaling REST endpoints for models and agents, with token streaming and request/response (inference-table) logging.
- **MLflow 3 (for GenAI)** — eval + tracing + observability: end-to-end tracing of agent runs, production-scale trace ingestion, LLM-as-judge + custom scorers, human-feedback datasets built from production traces, versioned quality tracking. OSS core, with a managed/governed Databricks tier.
- **Unity Catalog** — the unified data+AI governance layer: namespaces, fine-grained RBAC/ABAC, lineage, and audit across tables, models, functions/tools, and agents — the "single system of record from data to AI."

The enterprise value proposition is **data-proximate agents under one lineage/governance plane** — agents see only authorized data, with traceability for compliance, eval baked into the lifecycle, and serving/gateway plumbing managed.

## 2. Source links

- Official: `databricks.com/product/artificial-intelligence`, `.../agent-bricks`, `.../ai-gateway` (Unity AI Gateway), `docs.databricks.com/.../generative-ai/guide/mosaic-ai-gen-ai-capabilities`, MLflow 3 GenAI docs (`docs.databricks.com/.../mlflow3/genai`, `mlflow.org/releases/3`), Unity Catalog docs.
- Announcements: Agent Bricks launch (Databricks newsroom, 2026); MLflow 3.0 blog ("Build, Evaluate, and Deploy Generative AI with Confidence"); Constellation Research coverage of Agent Bricks / Lakeflow Designer.
- (Product naming is **rebrand-prone**: "Mosaic AI Gateway" → "Unity AI Gateway"; "Agent Evaluation" absorbed into MLflow 3; "Mosaic AI" itself is an umbrella over surfaces that move — verify surface names at read time.)

## 3. Map against AIDE

### Against the four AIDE planes

| AIDE plane | Databricks / Mosaic AI equivalent | Position |
|---|---|---|
| **Control** (AEON governance) | Unity Catalog (data+AI governance, system of record) + Unity AI Gateway (model-access guardrails) — but **data/RBAC governance, not authority/trust governance** | *AIDE ahead* on authority/trust governance; *behind* on data-lineage governance + operability |
| **Runtime** | **Model Serving** + Agent Framework runtime — auto-scaling, logged, production-grade | *In flight elsewhere* (strong overlap) / *AIDE behind* on realized runtime |
| **Experience** (AIDEX) | Agent Bricks (a *builder/optimizer* UX) + MLflow review/annotation UI | *AIDE ahead* — no HCAE operator-as-curator experience model |
| **Capability** (OAAD) | Agent Framework tools, Vector Search, Unity-Catalog functions, MCP support | *In flight elsewhere* (mature, data-proximate breadth) |

### Against the six AEON service planes

| AEON plane | Databricks equivalent | AIDE position |
|---|---|---|
| **Identity** | Unity Catalog principals + workspace identity; agents are governed catalog objects | *In flight elsewhere* — identity primitives exist, no principal-altitude (AI-aide-under-a-principal) model |
| **Authority** | RBAC/ABAC in Unity Catalog; no ordinal authority concept | **AIDE ahead** — OrdSA O0–O6 authority-down/evidence-up is absent; fine-grained data ACLs are *not* ordinal authority |
| **Evidence** | **MLflow 3 tracing/eval** + Unity Catalog lineage/audit + inference tables | **AIDE behind** — MLflow trace/eval/lineage is built + mature; AIDE's evidence trail is emit-only spec |
| **Integration** | Agent Framework integrations, Vector Search, MCP, external-model gateway | *In flight elsewhere* — broad, mature, data-native |
| **Capability composition** | Agent Bricks multi-agent (Supervisor), Agent Framework composition | *In flight elsewhere* — strong; but no **envelope-refinement** composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | Agent Framework + Model Serving | **AIDE behind** on realized runtime; *converging* via the workflow-orchestration pattern |

*(Inference is AEON's 7th plane, ADR-EA-0015: **Unity AI Gateway** is the closest analogue — an Inference-plane-adjacent model gateway with provider fallback/routing — but model-access governance is framed as data/security governance, not as a first-class **Inference governance** property the way the canon's Inference plane frames it.)*

### Vocabulary collision

Databricks' **"agent"** (Agent Framework / Agent Bricks) = an AI system acting under a principal against governed data — the canon's **AI-aide** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)), **not** the OAgents `Agent` primitive (a typed object inside a behavioral envelope); never carry the casual "agent" through. Databricks **"Tool"** = atomic invocation (convergent across the field; here often a Unity-Catalog-governed function). Databricks **"control plane"** (Agent Bricks "unified control plane") names operational/data-governance control, **not** the canon's Control plane (AEON authority/trust governance) — a direct altitude collision to flag. There is no Databricks "Skill" surface to map; capability packaging lives in Unity-Catalog functions/tools (↦ MxM **Means**).

## 4. Classification

**Mixed — "in flight elsewhere," at a different altitude.** As with every vendor stack, aide-canon and Databricks / Mosaic AI are *different categories* — a **governance/architecture corpus** vs a **data-proximate build-and-run platform** — so the classification is per-axis, not global:

- **AIDE ahead** — Authority (OrdSA O0–O6 ordinal authority vs Unity Catalog's RBAC/ABAC — data ACLs are not ordinal authority), behavioral envelope / trust layer (OAgents §10: trustworthiness *during execution* sits "above any framework"; Databricks governs *data access*, not behavioral envelope), deontic constraints (MxM Morals), HCAE operator-as-curator experience, vendor-neutral conformance criteria.
- **AIDE behind** — **data+AI governance/lineage** (Unity Catalog is genuinely strong and a real differentiator — honest credit here), evidence tooling (MLflow 3 trace/eval/observability is built + mature where AIDE is emit-only spec), realized runtime (Model Serving), model-gateway plumbing (Unity AI Gateway), and — decisively — **adoption, funding, and being a shipping product** where AIDE is design-first research with enforcement largely unbuilt.
- **In flight elsewhere** — orchestration (Agent Framework ↔ AEON Composition/Orchestration-runtime + the workflow-orchestration pattern); integration/capability breadth.

**Calibration note on Unity Catalog specifically:** it is *strong* on data governance, lineage, and access control (a defensible best-in-class claim) and *weak/absent* on **ordinal AUTHORITY** and the **behavioral envelope** — those are not the same axis. Crediting its data-governance lead while holding the authority/trust lead for AIDE is the precise read; conflating "governance" wholesale would be miscalibrated in either direction.

**The synthesis:** they **compose, not compete**. aide-canon is the governance layer one would wrap *around* a Databricks deployment — Agent Framework/Model Serving as the Means/runtime, MLflow 3 as the Evidence/eval plane, Unity Catalog as the data-governance substrate, Unity AI Gateway at the Inference boundary — with OAgents' envelope + OrdSA ordinal authority + MxM Morals supplying the *behavioral* trust/authority governance the platform structurally lacks (it governs data, not conduct). This is the same canon-spec ↔ platform-substrate relationship the canon already documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/).

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (authority + envelope lead).** Propagate the OrdSA-ordinal-authority + OAgents-envelope position as the *behavioral* governance layer above a data-governance platform — Databricks is the canonical example of mature **data** governance (Unity Catalog) with no **ordinal-authority or behavioral-envelope** layer. KR shape: a documented "govern-a-Databricks-deployment" mapping (envelope + O0–O6 authority + Morals layered over Unity Catalog's RBAC + Agent Framework runtime).
2. **Catch-up (evidence tooling + data lineage).** MLflow 3 tracing/eval and Unity Catalog lineage are materially ahead of AIDE's emit-only evidence spec. KR shape: adopt OTel-GenAI as the canonical evidence shape (already begun — workflow-orchestration v0.1.x shared evidence object) and demonstrate MLflow-grade trace/eval plus lineage-of-record on an AIDE exemplar.
3. **Converge-or-differentiate (orchestration + inference gateway).** Position the **workflow-orchestration pattern** (ADR-EA-0027) over Agent-Framework-class runtimes, and articulate the Inference plane (ADR-EA-0015) as the governance frame for model-gateway capability that Unity AI Gateway implements as data/security governance — convergent on mechanics, differentiated by ordinal authority + envelope-refinement.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Snapshot reflects the 2026 "Mosaic AI Gateway" → "Unity AI Gateway" rebrand and Agent-Evaluation-into-MLflow-3 consolidation. Revisit on the next Databricks AI product shift (rebrand-prone) or at OKR refresh.
