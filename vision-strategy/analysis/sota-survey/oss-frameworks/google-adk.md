# OSS framework — Google ADK (Agent Development Kit)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md), mapped against the AIDE-construct + AEON-plane anchor in [`README.md`](README.md). Cadence: **fast** (ADK ships roughly bi-weekly; v2.x landed mid-2026 with breaking changes from 1.x — treat version/star/surface specifics as a dated snapshot, not a fixed spec). This is the **OSS-framework** angle (code-first agents, multi-agent composition, A2A, Runner/runtime); the *managed* Gemini-Enterprise / Agent-Runtime side is surveyed separately at [`../vendor-stacks/google-cloud.md`](../vendor-stacks/google-cloud.md) and is **not** duplicated here.

## 1. What it is

**Google ADK** is an **open-source, code-first agent framework** (Apache 2.0) for building, evaluating, and deploying AI-aides — a *build* substrate, not a governance corpus. It is multi-language (Python is the lead implementation; TypeScript/`adk-js`, Go/`adk-go`, and Java/`adk-java` track toward parity), and is the OSS construction kit that *sits underneath* Google's managed platform: the same ADK code deploys locally, to a container (Cloud Run / GKE), or to the managed Agent Runtime surveyed in the vendor entry. Architecturally it provides: a **BaseAgent / LlmAgent** hierarchy (the agent loop with typed tools); **workflow agents** for deterministic multi-agent composition (**SequentialAgent**, **ParallelAgent**, **LoopAgent**) plus hierarchical sub-agent networks; a **Runner** that executes an agent against a **Session** and streams **Events**; a structured context/session-state model (sessions, memory, tool outputs, artifacts assembled into a filtered, lazy-loaded view rather than concatenated prompts); a **graph-based Workflow Runtime** (routing, fan-out/fan-in, loops, retry, nested workflows, human-in-the-loop) and a **Task API** for structured agent-to-agent delegation; tool types (function tools, OpenAPI tools, **MCP** tools, prebuilt integrations); a built-in **evaluation framework** (evalsets, LLM-as-judge / autorater scoring, user- and environment-simulation); a local dev UI; and native **A2A** exposure (`adk api_server --a2a`). It is, in aide-canon terms, a **Means-layer implementation substrate** — the altitude AIDE explicitly is *not*.

## 2. Source links

- Official: `adk.dev` (ex `google.github.io/adk-docs`, now redirects), the [Skills](https://adk.dev/) section of the docs, and the OSS repos [`google/adk-python`](https://github.com/google/adk-python), [`google/adk-js`](https://github.com/google/adk-js), [`google/adk-go`](https://github.com/google/adk-go), [`google/adk-java`](https://github.com/google/adk-java).
- Maturity at survey time: `adk-python` **v2.1.0** (released 2026-05-23; ADK **2.0** was a major release with breaking changes from 1.x, sessions back-compatible to 1.28+), ~20k stars, Apache 2.0, Python 3.11+. Released originally April 2025; actively maintained, ~bi-weekly cadence. The other-language SDKs release independently and continue converging on parity.
- In-canon prior research: the ADK row of [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md) (records ADK's **Skill** as the field's most rigorous Skill protocol — see §3 vocabulary note); the sibling **vendor** entry [`../vendor-stacks/google-cloud.md`](../vendor-stacks/google-cloud.md) (same Google authorship, managed-platform altitude); peer OSS findings [`crewai.md`](crewai.md) and [`openhands.md`](openhands.md) (same anchor).
- **A2A (Agent2Agent)** originated at Google (Apr 2025) and was **donated to the Linux Foundation** (Jun 2025); the protocol itself belongs in [`../standards-bodies/`](../standards-bodies/) — this entry references only ADK's *adoption* of it as a delegation/orchestration surface.

## 3. Map against AIDE

### Against the AIDE constructs

| AIDE construct | Google ADK equivalent | AIDE position |
|---|---|---|
| **DEA** (deployment / execution architecture) | "deploy anywhere" — local, container, Cloud Run, GKE, Agent Runtime; Runner + Workflow Runtime as the execution model | *AIDE behind* on realized deployment substrate — ADK is shipping, multi-target, GA-line |
| **OrdSA** (O0–O6 ordinal authority) | (not addressed — sub-agent delegation is *structural*, not authority-layered) | **AIDE ahead** — authority-down/evidence-up altitudes ([`../../../../constructs/ordsa`](../../../../constructs/ordsa)) are absent; ADK has delegation, not authority |
| **MxM** (5-surface harness) | The agent definition (instructions + model + tools + sub-agents) sketches a harness; **Skills** are the rigorous Means surface (below) | *In flight elsewhere* — comparable decomposition, no governing 5-surface contract; Skill ↦ Means is the convergent highlight |
| **OAgents** (typed agent envelope + trust) | BaseAgent/LlmAgent typed config; A2A AgentCard for discovery | **AIDE ahead** — typed *interface*, but no behavioral *envelope* governing trustworthiness during execution (OAgents §10's explicit "above any framework" position) |

### Against the six AEON service planes

| AEON plane | Google ADK equivalent | AIDE position |
|---|---|---|
| **Identity** | A2A AgentCard / agent identity at the protocol edge; deeper crypto-ID is the *managed* tier (see vendor entry) | *In flight elsewhere* — discovery-grade identity, no **principal-altitude** model (whose-aide-under-what-authority) |
| **Authority** | sub-agent delegation, Task API hand-offs; no ordinal-authority concept | **AIDE ahead** — OrdSA O0–O6 layering is absent; ADK composes delegation, not authority altitude |
| **Evidence** | built-in evaluation framework (evalsets, LLM-as-judge, simulation) + Events stream + traces | **AIDE behind** — built + maturing in-framework; AIDE's evidence trail is still emit-only spec |
| **Integration** | function / OpenAPI / **MCP** tools + **A2A** + prebuilt connectors | *In flight elsewhere* — broad, mature integration breadth |
| **Capability composition** | SequentialAgent / ParallelAgent / LoopAgent + hierarchical sub-agents + graph Workflow Runtime; **Skills** (L1/L2/L3) | *In flight elsewhere* — strong; but **no envelope-refinement composition law** (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | **Runner** + graph **Workflow Runtime** + **Task API** + A2A delegation | **AIDE behind** on realized runtime; *converging* via the workflow-orchestration pattern |

*(Inference is AEON's 7th plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md): ADK is explicitly **model-agnostic** — swap models without rewriting the agent — but model-agnosticism is a developer convenience, not the first-class **governance** property the Inference plane frames.)*

### Vocabulary collision

ADK's **`Agent`** (BaseAgent / LlmAgent — an AI entity with instructions, a model, tools, and sub-agents) is the canon's **AI-aide** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) — **not** the OAgents `Agent` primitive (a typed object inside a behavioral envelope). Never carry ADK's casual `Agent` into canon prose for an AI-under-principal — use **AI-aide**; and never use bare "**fleet**" of ADK deployments, which are neither the Ologos fleet nor NG-AIDE-01. ADK's **`Tool`** = atomic invocation (convergent across the field). ADK's **`Skill`** is the notable case and the **convergent highlight** of this entry: a Skill is a **self-contained unit** — a `SKILL.md`-rooted directory (YAML frontmatter + Markdown instructions, with optional `references/`, `assets/`, `scripts/` subdirs) — exposed through a **formal L1/L2/L3 progressive-disclosure** model: **L1** metadata (name + description, ~100 tokens, always loaded as a menu via `list_skills`), **L2** full instructions (loaded on activation via `load_skill`), **L3** reference resources (loaded on demand via `load_skill_resource`), all auto-generated by `SkillToolset`. The canon vocabulary map records this as **the most rigorous Skill protocol in the field**; it maps to MxM **Means** (a packaged capability the substrate composes), **not** to any governance primitive. This entry inherits that mapping discipline.

## 4. Classification

**Mixed — "in flight elsewhere," at a different altitude.** As with the LangChain, CrewAI, and Google-Cloud findings, the load-bearing point is that aide-canon and ADK are *different categories* — a **governance/architecture corpus** vs an **OSS build framework** — so the classification is per-axis, not global:

- **Authority — AIDE ahead.** OrdSA O0–O6 ordinal authority-down/evidence-up is absent; ADK's sub-agent delegation and Task API are *structural* composition, not authority altitude.
- **Envelope / trust — AIDE ahead.** ADK ships a typed agent *interface* and A2A discovery, but not a behavioral *envelope* governing trustworthiness during execution — the OAgents §10 position that trust sits *above any agent framework*, with ADK a textbook instance of the "framework whose behavioral trustworthiness during execution is outside its scope."
- **Deontic constraints / operator-curation — AIDE ahead.** No MxM-Morals deontic layer, no HCAE operator-as-curator experience (ADK is a developer SDK + local dev UI), no vendor-neutral conformance criteria.
- **Realized runtime / deployment — AIDE behind.** Runner + graph Workflow Runtime + multi-target deploy is shipping, GA-line infrastructure; AIDE's runtime is design-first and largely unbuilt.
- **Evidence / eval — AIDE behind.** ADK's built-in evalsets + LLM-as-judge + simulation are in-framework and maturing; AIDE's evidence trail is emit-only spec.
- **Adoption — AIDE behind.** ~20k stars, four-language SDKs, bi-weekly cadence, Google backing, and the fact that it is a shipping framework where AIDE is design-first research.
- **Skill protocol — in flight elsewhere (convergent).** ADK's L1/L2/L3 `SKILL.md` is *converging on the same rigor AIDE wants* for Means-packaging — the strongest field exemplar of progressive disclosure as a capability-packaging discipline.
- **Orchestration / capability composition — in flight elsewhere.** Workflow agents + Workflow Runtime + A2A ↔ AEON Capability-composition + Orchestration-runtime + the workflow-orchestration pattern.

**The synthesis:** they **compose, not compete**. aide-canon is the governance layer one would wrap *around* an ADK build — ADK's Runner / Workflow Runtime as the Means/runtime, its evalsets + Events as the Evidence plane, its Skills as the Means-packaging primitive — with OAgents' envelope + OrdSA authority + MxM Morals supplying the behavioral trust/authority the framework structurally lacks. ADK is the *open-source* face of the same Google stack whose managed tier is surveyed at [`../vendor-stacks/google-cloud.md`](../vendor-stacks/google-cloud.md): the vendor entry adds shipping *identity/security governance* (crypto-IDs, Registry, Gateway) on top, but neither tier reaches *authority* (OrdSA) or *behavioral-trust* (OAgents envelope) altitude. This is the OAgents §10 thesis made concrete — the same canon-spec ↔ platform-substrate relationship the canon documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/).

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (authority + trust above an OSS framework).** ADK is the canonical *open-source* example of a mature build substrate with a typed interface but no authority altitude and no behavioral envelope. Propagate the OAgents-envelope / OrdSA-authority position as the trust layer that sits *above any agent framework*. KR shape: a documented "govern-an-ADK-build" mapping that lays OrdSA O0–O6 + OAgents envelope + MxM Morals *over* ADK Runner / Workflow Runtime / sub-agent delegation, making the delegation-vs-authority distinction explicit.
2. **Catch-up (evidence + runtime).** ADK's in-framework evalsets, LLM-as-judge, simulation, and Workflow Runtime are materially ahead of AIDE's emit-only evidence spec and unbuilt runtime. KR shape: adopt OTel-GenAI as the canonical evidence shape (already begun — see the workflow-orchestration shared evidence object) and demonstrate ADK-grade trace/eval/autorater coverage on an AIDE exemplar.
3. **Converge-or-differentiate (Skill protocol + orchestration).** ADK's L1/L2/L3 `SKILL.md` is convergent with the canon's Means-packaging intent and is the field's most rigorous Skill spec — *align* the canon's **Means** vocabulary to cite it as the SOTA Skill exemplar, while differentiating on the **envelope-refinement composition law** ([ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)) that ADK's workflow agents and A2A delegation do not enforce.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Captures ADK `adk-python` v2.1.0 (2026-05-23) and cross-references the managed-tier finding in [`../vendor-stacks/google-cloud.md`](../vendor-stacks/google-cloud.md). Revisit on the next ADK major release (2.x is rapid) or at OKR refresh.
