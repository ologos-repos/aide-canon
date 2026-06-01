# Vendor stack — Google Cloud (Gemini Enterprise Agent Platform)

> SOTA-survey finding. Shape per [`../README.md`](../README.md) → [`sota-survey/README.md`](../../sota-survey/README.md). Cadence: **fast** (Google rebrands aggressively — the **Cloud Next 2026** rename of *Vertex AI* → *Gemini Enterprise Agent Platform*, with *Agentspace* absorbed into the *Gemini Enterprise app*, is the latest and most consequential example; treat all surface names as a dated snapshot, not a fixed spec).

## 1. What it is

**Google Cloud's Gemini Enterprise Agent Platform** is the consolidated, end-to-end *build-deploy-govern* platform for production AI-aides — the explicit successor to Vertex AI, into which Google states "all Vertex AI services and roadmap evolutions will be delivered exclusively." It bundles, into one pay-as-you-go platform: a code-first framework (**Agent Development Kit / ADK**), a low-code visual builder (**Agent Studio**), a managed execution **Agent Runtime** (the surface previously surveyed as *Agent Engine* — sub-second cold starts, multi-day workflows, an **Agent Sandbox** for secure code execution, agent-to-agent orchestration), state services (**Agent Memory Bank**, **Agent Sessions**), a governance tier (**Agent Identity** with per-aide cryptographic IDs, **Agent Registry**, **Agent Gateway** "air-traffic-control" with Model Armor, **Agent Security Dashboard** on Security Command Center), an evaluation/operability suite (**Agent Simulation**, **Agent Evaluation**, **Agent Observability**, **Agent Optimizer**), the **Model Garden** (200+ models incl. Gemini 3.x and third-party Anthropic Claude), and an employee-facing delivery surface (**Gemini Enterprise app**, the ex-Agentspace). It is, in aide-canon terms, a **Means-layer implementation substrate** — the altitude AIDE explicitly is *not* — and the most vertically-integrated of the hyperscaler stacks ("custom silicon to the employee's inbox").

## 2. Source links

- Official: `cloud.google.com/products/agent-builder` (now titled *Gemini Enterprise Agent Platform*), `cloud.google.com/gemini-enterprise`, ADK docs (`google.github.io/adk-docs`, incl. the [Skills](https://google.github.io/adk-docs/skills/) section), platform docs (`docs.cloud.google.com/agent-builder/...`), and the Cloud Next 2026 launch posts (`cloud.google.com/blog/.../introducing-gemini-enterprise-agent-platform`, `.../the-new-gemini-enterprise-one-platform-for-agent-development`).
- In-canon prior research: the ADK row of [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md) (Google ADK's **Skill** = the field's most rigorous Skill protocol — see §3 vocabulary note).
- A2A (Agent2Agent) originated at Google (released Apr 2025) and was **donated to the Linux Foundation** (Jun 2025); the protocol itself belongs in [`../standards-bodies/`](../standards-bodies/) — this entry references only Google's *adoption* of it as a runtime/orchestration surface.
- (Product naming is **highly** rebrand-prone — Vertex AI → Gemini Enterprise Agent Platform, Agentspace → Gemini Enterprise app, Agent Engine ↦ Agent Runtime all landed at Next '26; verify surface names at read time. Migration deadline off deprecated Vertex AI SDK modules: 2026-06-24.)

## 3. Map against AIDE

### Against the four AIDE planes

| AIDE plane | Gemini Enterprise Agent Platform equivalent | Position |
|---|---|---|
| **Control** (AEON governance) | Agent Identity (crypto IDs) + Agent Registry + Agent Gateway + Agent Security Dashboard — a real, shipping governance surface, but **RBAC/security governance, not authority/trust governance** | *AIDE ahead* on ordinal authority + behavioral envelope; *AIDE behind* on operability of the governance plane |
| **Runtime** | **Agent Runtime** (ex-Agent Engine) — managed, sandboxed, sub-second cold start, multi-day jobs, A2A orchestration | *AIDE behind* on realized runtime — this is mature, GA-trajectory infrastructure |
| **Experience** (AIDEX) | Agent Studio (builder UX) + Gemini Enterprise app (employee consumer UX) | *AIDE ahead* — a *builder* and a *consumer* surface, not an HCAE operator-as-curator console |
| **Capability** (OAAD) | ADK Skills + Tools + Model Garden + Agent Garden templates + native ecosystem connectors | *In flight elsewhere* — broad, mature; ADK's Skill protocol is the rigorous standout (below) |

### Against the six AEON service planes

| AEON plane | Gemini Enterprise equivalent | AIDE position |
|---|---|---|
| **Identity** | **Agent Identity** — unique cryptographic IDs per aide, auditable trails | *In flight elsewhere* — strong, shipping identity primitives, but no **principal-altitude** governance model (whose-aide-under-what-authority) |
| **Authority** | RBAC + IAM + Agent Gateway gating; no ordinal-authority concept | **AIDE ahead** — OrdSA O0–O6 authority-down/evidence-up layering (`../../../../constructs/ordsa`) is absent; the platform has access control, not authority altitude |
| **Evidence** | **Agent Observability** (reasoning traces) + Agent Evaluation (multi-turn autoraters) + Security Dashboard audit | **AIDE behind** — built + maturing; AIDE's evidence trail is still emit-only spec |
| **Integration** | Native ecosystem connectors + MCP + A2A (Linux-Foundation protocol Google authored) | *In flight elsewhere* — broad, mature integration breadth |
| **Capability composition** | ADK multi-agent graphs/sub-agent networks; Skills (L1/L2/L3); Agent Garden | *In flight elsewhere* — strong; but **no envelope-refinement composition law** (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | **Agent Runtime** + A2A agent-to-agent orchestration | **AIDE behind** on realized runtime; *converging* via the workflow-orchestration pattern |

*(Inference is AEON's 7th plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md): ADK is explicitly **model-agnostic** — "swap models without rewriting your agent," 200+ models in Model Garden — but model-agnosticism is a developer convenience, not the first-class **governance** property the Inference plane frames.)*

### Vocabulary collision

Google's **`Agent`** (an "AI agent at enterprise scale" with Agent Identity, Memory Bank, Sessions, tools) is the canon's **AI-aide** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) — **not** the OAgents `Agent` primitive (a typed object inside a behavioral envelope). Use **AI-aide** for the system-under-a-principal; reserve casual "agent" — and never use bare "**fleet**" of Google's deployments, which are not the Ologos fleet nor NG-AIDE-01. Google's **`Tool`** = atomic invocation (convergent across the field). Google's **`Skill`** is the notable case: ADK defines a Skill as a **self-contained unit** (a `SKILL.md`-rooted folder bundling instructions + reference resources + assets/scripts) with a **formal L1/L2/L3 progressive disclosure** model — L1 metadata for discovery, L2 instructions on trigger, L3 resources on demand (auto-exposed via `list_skills`/`load_skill`/`load_skill_resource`). The canon vocabulary map records this as **the most rigorous Skill protocol in the field**; it maps to MxM **Means** (a packaged capability the substrate composes), not to any governance primitive. This entry inherits that mapping discipline.

## 4. Classification

**Mixed — "in flight elsewhere," at a different altitude.** As with the LangChain finding, the load-bearing point is that aide-canon and the Gemini Enterprise Agent Platform are *different categories* — a **governance/architecture corpus** vs a **build-deploy-govern platform** — so the classification is per-axis, not global:

- **AIDE ahead** — Authority (OrdSA ordinal layering vs RBAC), the behavioral-envelope / trust layer (OAgents §10's position that trust sits *above any agent framework* — Google ships per-aide *identity* and *security*, but not an *envelope* governing behavioral trustworthiness during execution), deontic constraints (MxM Morals), HCAE operator-as-curator experience (vs Google's builder + consumer surfaces), and vendor-neutral conformance criteria.
- **AIDE behind** — realized runtime (Agent Runtime), evidence/observability/eval (Agent Observability + Evaluation + Optimizer + Simulation — a notably *complete* operability suite, ahead of LangSmith's surface in breadth), the governance *plane as shipping product* (cryptographic Agent Identity, Registry, Gateway, Security Dashboard), and — decisively — **adoption, vertical integration, funding, and the fact that it is a shipping platform** where AIDE is design-first research with enforcement largely unbuilt.
- **In flight elsewhere** — orchestration (Agent Runtime + A2A ↔ AEON Composition/Meta-Orchestration + the workflow-orchestration pattern); identity primitives; integration/capability breadth; and the **Skill protocol**, where Google is *converging on the same rigor AIDE wants* (progressive disclosure as a Means-packaging discipline).

**The synthesis:** they **compose, not compete** — but Google is the *hardest* substrate to claim a clean lead over, because it ships a governance *surface* (identity, registry, gateway, security) that LangChain lacks. The distinction holds at altitude: Google governs *access and security* (RBAC, crypto-IDs, anomaly detection); AIDE governs *authority and trust* (OrdSA ordinal layering, OAgents envelope, MxM Morals, HCAE curation). aide-canon is the governance layer one would wrap *around* a Gemini-Enterprise deployment — Agent Runtime as the Means/runtime, the Observability/Eval suite as the Evidence plane, with OAgents' envelope + OrdSA authority + MxM Morals supplying the *behavioral trust* the platform's security tier structurally does not address. This is the OAgents §10 thesis made concrete, the same canon-spec ↔ platform-substrate relationship the canon documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/).

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (authority + trust above a governed substrate).** Google is the strongest counter-example to a naive "vendors have no governance" claim — it ships identity + security governance. Sharpen the lead to the *altitude Google does not occupy*: ordinal authority (OrdSA) and the behavioral envelope (OAgents). KR shape: a documented "govern-a-Gemini-Enterprise-deployment" mapping that lays OrdSA O0–O6 + OAgents envelope + MxM Morals *over* Agent Identity / Agent Gateway / Agent Runtime, making explicit the access-control-vs-authority and security-vs-trust distinctions.
2. **Catch-up (evidence + operability tooling).** Google's Observability + Evaluation + Optimizer + Simulation suite is materially ahead of AIDE's emit-only evidence spec — broader even than LangSmith. KR shape: adopt OTel-GenAI as the canonical evidence shape (already begun — workflow-orchestration v0.1.x shared evidence object) and demonstrate Google-grade trace/eval/autorater coverage on an AIDE exemplar.
3. **Converge-or-differentiate (Skill protocol + orchestration).** ADK's L1/L2/L3 Skill is convergent with the canon's Means-packaging intent and is the field's most rigorous Skill spec — *align* the canon's Means vocabulary to cite it as the SOTA Skill exemplar, while differentiating on the **envelope-refinement composition law** ([ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)) that ADK graphs and A2A orchestration do not enforce.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Captures the Cloud Next 2026 rebrand (Vertex AI → Gemini Enterprise Agent Platform; Agentspace → Gemini Enterprise app; Agent Engine ↦ Agent Runtime). Revisit on the next Google product shift (highly rebrand-prone) or at OKR refresh.
