# Vendor stack — Microsoft (enterprise agentic platform)

> SOTA-survey finding. Shape per [`../README.md`](../README.md) → [`sota-survey/README.md`](../../sota-survey/README.md). Cadence: **fast** (Microsoft rebrands aggressively — Azure AI Studio → Azure AI Foundry → Microsoft Foundry in ~18 months; Semantic Kernel + AutoGen → Microsoft Agent Framework; treat every product name here as a dated snapshot, not a fixed spec).

## 1. What it is

**Microsoft's enterprise agentic platform** is a *build-and-run* substrate for AI systems — not a governance corpus. As of mid-2026 it composes from several surfaces at two altitudes (pro-code developer and low-code business):

- **Microsoft Foundry** (the January-2026 rebrand of *Azure AI Foundry*, itself ex *Azure AI Studio*) — the unified developer platform: model catalog, the **Foundry Agent Service** (fully managed agent hosting on the Responses API, replacing the Assistants API retiring 2026-08-26), and the **Foundry Control Plane** (observability, runtime controls, evaluation, security integration).
- **Microsoft Agent Framework** — the open-source SDK (.NET + Python) that GA'd 2026-04-03 as the *convergence of Semantic Kernel and AutoGen* (both now in maintenance mode): single- and multi-agent orchestration, explicit workflows, session state, telemetry, type safety. This is the canon's interest-point — it is the framework altitude.
- **Semantic Kernel** — the prior-generation pro-code SDK, now superseded by Agent Framework; historically significant for the **"skill" → "plugin" rename** (2023, embracing the OpenAI plugin spec).
- **Copilot Studio** — the low-code agent-building surface, with tenant-level agent governance (April-2026 governance updates; Analytics Viewer role).
- **Microsoft 365 Copilot / declarative agents** — the M365-embedded surface: **declarative agents** (instructions + actions + knowledge over the shared M365 orchestrator and foundation models), built via low-code **Agent Builder** or the pro-code **M365 Agents Toolkit**.
- **Agent 365** — the IT/security control plane (agent registry, identity governance, access control, org-wide policy) — distinct from Foundry Control Plane, which is the developer-facing operations layer.

The enterprise value proposition is **breadth-of-surface (pro-code to low-code), deep M365/Entra/Azure integration, GA observability + evaluation + tracing, and a two-tier governance story (Foundry Control Plane for developers, Agent 365 for IT)** — the plumbing of building, running, and managing AI systems at enterprise scale. It is, in aide-canon terms, a **Means-layer implementation substrate** — the altitude AIDE explicitly is *not*.

## 2. Source links

- Official: `azure.microsoft.com/en-us/products/ai-foundry`, Foundry Agent Service docs (`learn.microsoft.com/en-us/azure/foundry/agents/overview`), Foundry Control Plane + Observability (`azure.microsoft.com/en-us/products/ai-foundry/control-plane`, `.../observability`), Microsoft Agent Framework (`learn.microsoft.com/en-us/agent-framework/overview/`, `devblogs.microsoft.com/agent-framework/`), Copilot Studio blog (`microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/`), declarative agents (`learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/overview-declarative-agent`), Agent 365 (`techcommunity.microsoft.com/.../agent-365-blog/`), Brand kit + OAL (`support.microsoft.com/.../create-and-manage-official-brand-kits-...`, `learn.microsoft.com/en-us/copilot/microsoft-365/enterprise-brand-manager`).
- In-canon prior research: the `AI copilot (Microsoft and generalized)` row of [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md) (mapping-type *partial* — *copilot* implies peer altitude, *AI-aide* is subordinate; trademark adjacency makes it an external-mapping term). "MS Foundry" is already listed there as a vendor stack pending full mapping; this entry supplies the per-surface mapping.
- (Product naming is **acutely** rebrand-prone — three Foundry names in 18 months, two predecessor SDKs folded into one — verify surface names at read time.)

## 3. Map against AIDE

### Against the four AIDE planes

| AIDE plane | Microsoft equivalent | Position |
|---|---|---|
| **Control** (AEON governance) | Foundry Control Plane (dev ops/observability) + Agent 365 (IT registry/identity/policy) — but **no authority-altitude or behavioral-envelope governance** | *AIDE ahead* on authority/trust governance; *AIDE behind* on shipped operations/policy control |
| **Runtime** | **Foundry Agent Service** (managed hosting, Responses API) + Agent Framework (durable workflows, session state) | *AIDE behind* on realized runtime (GA, managed, at scale) |
| **Experience** (AIDEX) | Copilot Studio + Agent Builder (a *builder* UX; M365 Copilot is a *chat* surface) — not an operator-as-curator console | *AIDE ahead* — no HCAE operator-curation experience model |
| **Capability** (OAAD) | Foundry model catalog + plugins/tools + connectors + MCP support | *In flight elsewhere* — mature catalog + integration breadth |

### Against the six AEON service planes

| AEON plane | Microsoft equivalent | AIDE position |
|---|---|---|
| **Identity** | Entra-backed agent identity; Agent 365 registry + identity governance | *AIDE behind* — agent-identity primitives are GA and Entra-integrated; AIDE's principal-altitude identity model is design-spec |
| **Authority** | Entra RBAC + tenant policy; **no ordinal authority concept** | **AIDE ahead** — OrdSA O0–O6 authority-down/evidence-up is absent (RBAC is access-control, not authority-altitude) |
| **Evidence** | **Foundry Observability** — tracing, evaluation, monitoring (GA March 2026); OpenTelemetry traces from Agent Framework | **AIDE behind** — Foundry's evidence tooling is built + GA; AIDE's evidence trail is emit-only spec |
| **Integration** | Connectors, plugins/tools, MCP support, M365/Graph surface | *In flight elsewhere* — broad, deeply integrated into the M365/Azure estate |
| **Capability composition** | Agent Framework workflows + multi-agent orchestration; plugins; declarative-agent actions | *In flight elsewhere* — strong; but no **envelope-refinement** composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | **Agent Framework** workflows + **Foundry Agent Service** | **AIDE behind** on realized runtime; *converging* via the workflow-orchestration pattern |

*(Inference is AEON's 7th plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md): Foundry's model catalog is multi-model and Agent Framework is model-flexible, but model-choice is a deployment configuration, not the first-class **governance** property the Inference plane frames — per-principal substrate binding is absent.)*

### Vocabulary collision

Microsoft's **`agent`** (Foundry Agent Service / Copilot Studio / declarative agent — "an AI system with instructions, actions, and knowledge serving a business scenario") is the canon's **AI-aide** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) — **not** the OAgents `Agent` primitive (a typed object inside a behavioral envelope). Three vendor-specific collisions worth flagging:

- **`Copilot`** — the marquee brand — maps *partial* to **AI-aide** (per the vocabulary-map row): *copilot* implies peer altitude; AI-aide is explicitly subordinate-with-evidence-upward. The canon does not adopt *copilot* as a source-of-truth term (trademark adjacency, authority-flattening).
- **Semantic Kernel `plugin`** (renamed from `skill` in 2023) maps to MxM **Means** — the same target the canon maps LangChain's `Skill` to. Note the asymmetry: **Copilot Studio has no `Skill` noun at all** (its equivalents are *topics*, *actions*, *tools*, *connectors*), so the LangChain-style `Skill ↦ Means` mapping has *no Microsoft surface to attach to* on the low-code side and attaches via `plugin` on the pro-code side. This entry records that split; it is a refinement to fold into the vocabulary map.
- **`Tool`** = atomic invocation (convergent across the field; maps cleanly).

**Entity-distinction note:** Microsoft's Foundry Control Plane markets "fleet management" across agents. Do **not** read this as the canon sense of *fleet* — Microsoft's "fleet" is a tenant's population of vendor-hosted agents, not an entity in the canon's cross-entity federation (Ologos ecosystem / NG-AIDE-01 / thinx). Keep the terms separate.

## 4. Classification

**Mixed — "in flight elsewhere," at a different altitude.** This is the load-bearing finding: aide-canon and Microsoft's platform are *different categories* — a **governance/architecture corpus** vs a **build-and-run platform** — so the classification is per-axis, not global:

- **AIDE ahead** — Authority (OrdSA O0–O6 vs Entra RBAC), behavioral envelope / trust layer (OAgents §10's "trust layer above any agent framework" — Microsoft ships no such layer; Foundry/Agent 365 govern access, identity, and policy, not behavioral-envelope conformance during execution), deontic constraints (MxM Morals), HCAE operator-as-curator, vendor-neutral conformance criteria.
- **AIDE behind** — realized runtime (Foundry Agent Service + Agent Framework, GA), observability/eval (Foundry Observability, GA March 2026), identity governance (Entra + Agent 365 registry), enterprise plumbing (M365/Azure/Entra integration, SOC-grade controls), and — decisively — **adoption, distribution, and the fact that it is a shipping, GA product portfolio recognized as a Leader in the 2026 IDC MarketScape for unified AI governance** where AIDE is design-first research with enforcement still largely unbuilt. On *operationalized governance* specifically, Microsoft is ahead: it has two GA control planes; the canon has ADRs.
- **In flight elsewhere** — orchestration (Agent Framework workflows ↔ AEON Composition/Orchestration-runtime + the workflow-orchestration pattern); integration/capability breadth; identity primitives.

**The synthesis:** they **compose, not compete** — but with a sharper caveat than LangChain. aide-canon is the governance layer one would wrap *around* a Microsoft Foundry deployment — Foundry Agent Service + Agent Framework as the Means/runtime, Foundry Observability as the Evidence/eval plane, Agent 365 as an existing identity/policy substrate to *map onto* (not replace), with OAgents' envelope + OrdSA authority + MxM Morals supplying the **behavioral-trust and authority-altitude governance the platform structurally lacks**. The caveat: Microsoft already occupies the "governance platform" *marketing* position (Agent 365, Foundry Control Plane, IDC-Leader), so the canon must articulate its differentiation as **governance-of-behavior-and-authority** vs Microsoft's **governance-of-access-identity-and-policy** — not claim governance ground Microsoft has already shipped product into. This is the OAgents §10 thesis made concrete against the most credible vendor governance story in the field. Same canon-spec ↔ platform-substrate relationship the canon documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/).

**α1 template/brand note:** Microsoft's two-layer model — **OAL (Organizational Asset Library)** as the asset/template source-of-truth + **Brand Kit** as the brand-enforcement layer that complements OAL — is the concrete vendor exemplar the canon's α1 (template-and-brand) sub-design references: a clean separation of *asset library* (templates live where they already are) from *brand enforcement* (colors/fonts/voice/rules applied over generated output). Worth tracking as prior art for α1.

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance lead — sharpened).** Propagate the OAgents-envelope / OrdSA-authority position as the **behavioral-and-authority** trust layer that sits *above any agent framework*, explicitly differentiated from Microsoft's access/identity/policy control planes (Agent 365, Foundry Control Plane). KR shape: a documented "govern-a-Foundry-deployment" mapping (envelope + OrdSA authority + Morals over Agent Framework / Foundry Agent Service / Foundry Observability), with the differentiation claim stated as *behavior+authority* vs *access+identity+policy* so the canon does not collide with shipped Microsoft governance marketing.
2. **Catch-up (evidence + identity tooling).** Foundry Observability (GA tracing/eval/monitoring, OTel-native) and Entra/Agent-365 identity governance are materially ahead of AIDE's emit-only evidence spec and design-stage identity model. KR shape: adopt OTel-GenAI as the canonical evidence shape (already begun — workflow-orchestration v0.1.2 shared evidence object) so an AIDE exemplar can emit *into* Foundry Observability, and map the principal-altitude identity model onto Entra/Agent-365 primitives rather than reinventing them.
3. **Converge-or-differentiate (orchestration).** Position the **workflow-orchestration pattern** ([ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)) as the governing spec over Agent-Framework-class runtimes — convergent on workflow/orchestration mechanics (Agent Framework's explicit-workflow direction aligns), differentiated by the envelope-refinement composition law Agent Framework does not enforce.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Inherits the vocabulary-map `AI copilot` row; contributes the Semantic-Kernel-`plugin` / Copilot-Studio-no-`Skill` split and the OAL+Brand-Kit α1 prior-art note for fold-back into [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md). Revisit on the next Microsoft product shift (acutely rebrand-prone) or at OKR refresh.
