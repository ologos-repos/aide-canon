# Vendor stack — Salesforce (Agentforce)

> SOTA-survey finding. Shape per [`../README.md`](../README.md) → [`sota-survey/README.md`](../../sota-survey/README.md). Cadence: **fast** (Salesforce rebrands aggressively — "Einstein 1" → "Agentforce" → the Dreamforce-2025 "Agentforce 360 / Data 360" relabel; treat product specifics as a dated snapshot, not a fixed spec).

## 1. What it is

**Agentforce** is Salesforce's agentic platform — a *build-and-run* substrate for deploying AI-aides (Salesforce calls them "agents") tightly coupled to the CRM, not a governance corpus. Five surfaces compose the current stack:

- **Agentforce (1 → 2 → 3)** — the platform line. v1 (Oct 2024) introduced configurable agents; v2 deepened reasoning, Slack-native agents, and the **Topics/Actions** authoring model; **v3 (June 2025)** is the "scale" release — adding the **Command Center** observability layer, **MCP** support, response streaming, and multi-model failover.
- **Atlas Reasoning Engine** — the planning/reasoning core: it generates a plan from user intent, evaluates and refines it, retrieves grounding data (RAG/hybrid search over Data Cloud), and acts via Actions. v3 claims ~50% lower latency vs Jan 2025, response streaming, inline-cited web search, and automatic failover across model providers (OpenAI, Anthropic Claude via Bedrock, Gemini).
- **Einstein Trust Layer** — a governance-*adjacent* runtime feature set: secure data retrieval, dynamic grounding, **PII data masking**, zero-data-retention with third-party LLMs, prompt-injection defense, and **toxicity detection** (five categories scored 0–1). It wraps the prompt/response journey, not the agent's authority model.
- **Agentforce Command Center** — the observability surface (GA targeted Aug 2025): real-time agent-health/error/escalation monitoring, alerting, adoption/performance analytics, and **session tracing via OpenTelemetry through Data Cloud**.
- **Data Cloud (Data 360)** — the data spine: zero-copy unification, identity resolution, unified profiles, and the RAG/grounding retrievers Atlas draws on. Agents are only as good as the Data Cloud profile grounding them.

The value proposition is **a turnkey agentic layer fused to the world's dominant CRM** — grounding, trust guardrails, observability, and a no/low-code builder, all inside the Salesforce platform. It is, in aide-canon terms, a **Means-layer implementation substrate** — the altitude AIDE explicitly is *not*.

## 2. Source links

- Official: `salesforce.com/agentforce`, `help.salesforce.com` (Agent Builder / Topics & Actions, Einstein Trust Layer), `salesforce.com/artificial-intelligence/trusted-ai/`, `trailhead.salesforce.com` (Trust Layer, Data-Cloud-powered Agentforce modules), the Agentforce 3 press release (`salesforce.com/news/press-releases/2025/06/23/agentforce-3-announcement/`).
- Independent: Constellation Research and VentureBeat coverage of the Agentforce 3 / Command Center launch (observability + MCP framing).
- (Product naming is **highly** rebrand-prone — Einstein 1 → Agentforce → the Dreamforce-2025 "Agentforce 360 / Data 360" relabel is the latest churn; verify surface names and GA status at read time, since several v3 pieces — Command Center, Gemini support, hosted models — were preview/roadmap at announcement.)

## 3. Map against AIDE

### Against the four AIDE planes

| AIDE plane | Agentforce equivalent | Position |
|---|---|---|
| **Control** (AEON governance) | Einstein Trust Layer (data/safety guardrails) + Command Center (monitoring) — but **no authority-altitude or behavioral-envelope governance layer** | *AIDE ahead* on governance architecture; *behind* on shipped operability |
| **Runtime** | **Atlas Reasoning Engine** + Agentforce platform — planning, streaming, multi-model failover, in production | *In flight elsewhere* (strong overlap) / *AIDE behind* on realized runtime |
| **Experience** (AIDEX) | Agent Builder (no/low-code *builder* UX) + Command Center console | *AIDE ahead* — no HCAE operator-as-curator experience model; builder ≠ curation |
| **Capability** (OAAD) | Topics/Actions + AgentExchange + MCP/MuleSoft integration breadth | *In flight elsewhere* (mature, CRM-deep integration) |

### Against the six AEON service planes

| AEON plane | Agentforce equivalent | AIDE position |
|---|---|---|
| **Identity** | Platform auth + Data Cloud identity resolution / unified profiles (customer-data identity, not agent-principal identity) | *In flight elsewhere* — rich *customer*-identity resolution, no principal-altitude AI-aide identity model |
| **Authority** | Topic Scope + permission sets / RBAC; no ordinal authority concept | **AIDE ahead** — OrdSA O0–O6 authority-down/evidence-up is absent; Topic "guardrails" are scoping, not authority altitude |
| **Evidence** | **Command Center** — OpenTelemetry session tracing via Data Cloud, health/adoption analytics | **AIDE behind** — built + GA-tracked, OTel-native; AIDE's evidence trail is emit-only spec |
| **Integration** | MCP support, MuleSoft agent gateway, Slack, AgentExchange | *In flight elsewhere* — broad, mature, CRM-anchored |
| **Capability composition** | Topics group Actions (Apex/Flow/API/prompt); multi-agent/subagent topics | *In flight elsewhere* — strong; but no **envelope-refinement** composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | **Atlas Reasoning Engine** (plan → evaluate → refine → act) | **AIDE behind** on realized runtime; *converging* via the workflow-orchestration pattern |

*(Inference is AEON's 7th plane, ADR-EA-0015: Agentforce is multi-model at the Atlas layer with automatic failover, but model-agnosticism is a performance/availability feature, not a first-class **governance** property the way the Inference plane frames it.)*

### Vocabulary collision

Agentforce's **"agent"** = a deployed, CRM-coupled autonomous worker with a role and stable identity — this is the canon's **AI-aide** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)), **not** the OAgents `Agent` primitive (a typed object inside a behavioral envelope); flag the bare-"agent" usage on read. Agentforce departs from the field's `Skill`/`Tool` lexicon: it uses **Topics** (intent-scoped task categories with instructions/guardrails) and **Actions** (atomic Apex/Flow/API/prompt invocations). Mapping: an **Action** ↦ canon **Tool** (atomic invocation, convergent across the field); a **Topic** ↦ MxM **Means** *plus* a thin scoping layer (intent classification + scoped instructions) — closer to a Means bundle than to a single Skill. The vocabulary map should add a Salesforce row to record this Topic/Action split.

## 4. Classification

**Mixed — "in flight elsewhere," at a different altitude.** As with the LangChain finding, aide-canon and Agentforce are *different categories* — a **governance/architecture corpus** vs a **build-and-run platform fused to a CRM** — so the classification is per-axis, not global:

- **AIDE ahead** — Authority (OrdSA O0–O6 vs Topic-scoping/RBAC), behavioral envelope / trust-during-execution (OAgents §10 — the envelope sits *above any framework*), deontic constraints (MxM Morals), HCAE operator-as-curator, vendor-neutral conformance criteria. **Caveat on the trust axis (Salesforce-specific):** the **Einstein Trust Layer is governance-adjacent**, so Salesforce is **partially in-flight, not cleanly behind**, on trust — but the gap is precise: the Trust Layer does *input/output* hygiene (PII masking, zero-retention, toxicity/injection scoring on the prompt/response journey), which is **data-plane and content guardrailing**, not **behavioral-envelope governance**. It does not encode deontic Permissions/Prohibitions/Obligations (MxM Morals), does not gate *which authority* an action carries (OrdSA), and is not the OAgents-style envelope that governs an AI-aide's behavioral trustworthiness *during execution*. So: AIDE ahead on the *deontic/authority/envelope* layer; Salesforce **in-flight (genuinely shipped)** on *content/data-safety* guardrails — a layer AIDE's design assumes but does not itself ship.
- **AIDE behind** — realized runtime (Atlas), observability/eval (Command Center, OTel-native, Data-Cloud-backed), data-grounding/identity-resolution plumbing (Data Cloud), and — decisively — **adoption, install-base, and the fact that it is a shipping product fused to the dominant CRM** where AIDE is design-first research with enforcement still largely unbuilt.
- **In flight elsewhere** — orchestration (Atlas ↔ AEON Composition/Meta-Orchestration + the workflow-orchestration pattern); integration/capability breadth (MCP, AgentExchange); customer-identity resolution.

**The synthesis:** they **compose, not compete**. aide-canon is the governance layer one would wrap *around* an Agentforce deployment — Atlas as the Means/runtime, Command Center as the Evidence/eval plane, the Einstein Trust Layer as a *content-safety sub-layer* — with OAgents' envelope + OrdSA authority + MxM Morals supplying the **behavioral-trust and authority governance the Trust Layer structurally does not reach**. This is the OAgents §10 thesis made concrete, and the same canon-spec ↔ platform-substrate relationship the canon documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/). (Entity note: Agentforce is an external vendor stack — do not conflate it with the Ologos ecosystem or NG-AIDE-01.)

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance lead).** Propagate the OAgents-envelope / OrdSA-authority position as the trust layer *above any agent platform* — Agentforce, *with a real Trust Layer*, is the strongest counter-example to defend against: it shows a vendor can ship credible content-safety governance. KR shape: a documented "govern-an-Agentforce-deployment" mapping that draws the **precise line** between Einstein-Trust-Layer content/data guardrails and the OAgents/OrdSA/Morals behavioral-and-authority envelope they do not provide.
2. **Catch-up (evidence tooling).** Command Center is OTel-native and Data-Cloud-backed — materially ahead of AIDE's emit-only evidence spec. KR shape: confirm OTel-GenAI as the canonical evidence shape (already begun — workflow-orchestration v0.1.2 shared evidence object) and demonstrate Command-Center-grade trace/health/adoption telemetry on an AIDE exemplar.
3. **Converge-or-differentiate (orchestration + trust).** Position the **workflow-orchestration pattern** (ADR-EA-0027) as the governing spec over Atlas-class reasoning runtimes — convergent on plan/evaluate/refine mechanics, differentiated by the envelope-refinement composition law and deontic gating Atlas/Topics do not enforce; and articulate the Trust-Layer-vs-envelope distinction as the canonical "where vendor guardrails stop" exemplar.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Snapshot pins Agentforce 3 (June 2025 announcement; Command Center / hosted-model / Gemini pieces preview→GA through 2025) and the Dreamforce-2025 "Agentforce 360 / Data 360" relabel. Revisit on the next Salesforce product shift (rebrand-prone) or at OKR refresh.
