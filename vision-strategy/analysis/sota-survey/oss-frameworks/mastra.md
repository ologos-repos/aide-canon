# OSS framework — Mastra

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Mapping anchor: the [`oss-frameworks/README.md`](README.md) two-table anchor (AIDE constructs + the six AEON service planes), which **differs** from the vendor-stacks single-table (planes-only) anchor. Cadence: **fast** (weekly releases; 1.0 shipped Jan 2026 — treat version specifics as a dated snapshot).

## 1. What it is

**Mastra** is an open-source, full-stack **TypeScript/JavaScript** agent framework from the team behind Gatsby. It is a *build-and-run* substrate for agentic applications — not a governance corpus. Its named building blocks are:

- **Agents** — LLM-plus-tools units that reason about a goal, select tools, and iterate internally until a final answer or stopping condition.
- **Workflows** — a graph/step orchestration engine with explicit control-flow syntax (`.then()`, `.branch()`, `.parallel()`), human-in-the-loop pauses, and **durable execution** (a workflow can pause indefinitely and resume).
- **Tools** — atomic typed invocations, also exposable through MCP servers.
- **RAG** — a full retrieval pipeline: chunking, embeddings, vector storage, similarity search, reranking; works across Pinecone, Qdrant, ChromaDB, pgvector, etc.
- **Memory** — conversation history, working memory, and semantic recall.
- **Evals / Scorers** — model-graded, rule-based, and statistical evaluation (relevance, faithfulness, toxicity, tone, custom metrics).
- **MCP support** — authors MCP servers exposing its agents, tools, and resources to any MCP-speaking client.
- **Deployment + observability** — standalone server or serverless (Vercel, Netlify, Cloudflare); built-in tracing/logging/metrics; integrates with React/Next.js/Node and is built atop Vercel's AI SDK for the low-level model layer.

Maturity is real and rising: launched Oct 2024, **1.0 in Jan 2026**, ~24K GitHub stars and ~300K weekly npm downloads by early 2026, a **$22M Series A (Apr 2026)**, and named production adopters (Brex, Sanity, Factorial). License is **dual** — Apache-2.0 core plus a source-available Mastra Enterprise License for `/ee/` directories. Mastra's distinctive position is being the notable **TS-native** option in a field where the heavyweight frameworks (LangGraph, CrewAI, AutoGen, LlamaIndex) are Python-first — its reach into the TypeScript/web ecosystem is the differentiator. In aide-canon terms it is a **Means-layer implementation substrate** — the altitude AIDE explicitly is *not*.

## 2. Source links

- Official: `mastra.ai`, `mastra.ai/ai-agent-framework`, docs at `mastra.ai/docs`.
- Repo + releases: `github.com/mastra-ai/mastra` (Apache-2.0 core + Enterprise license for `/ee/`), `github.com/mastra-ai/mastra/releases`.
- Funding / adoption signal: Series A announcement (Spark Capital, Apr 2026); 1.0 release notes (Jan 2026).
- In-canon prior research: the SOTA-vocabulary discipline of [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md) and the sibling [`vendor-stacks/langchain.md`](../vendor-stacks/langchain.md) finding (the `Agent`/`Skill`/`Tool` mapping, surveyed 2026-05-29 — the same collisions recur here).
- (1.0 is recent; surface names and license boundary are version-sensitive — verify at read time.)

## 3. Map against AIDE

The oss-frameworks anchor uses **two** tables.

### Table (a) — against the four AIDE constructs

| AIDE construct | Mastra equivalent | AIDE position |
|---|---|---|
| **DEA** (deployable enterprise architecture) | No architecture-corpus equivalent — Mastra is a code framework, not a governance/architecture spec | **AIDE ahead** — different altitude; Mastra has no DEA-class corpus |
| **OrdSA** (O0–O6 ordinal authority) | No authority-altitude concept; optional endpoint auth only | **AIDE ahead** — authority-down/evidence-up ordinals are absent |
| **MxM** (5-surface harness: Mission/Mind/Morals/Memory/Methods) | Agent config + Memory + (no Morals/deontic surface) | *In flight elsewhere* — comparable component decomposition (agent/memory/workflow), **no Morals/deontic surface**, different vocabulary |
| **OAgents** (typed agent envelope / behavioral-trust layer) | Mastra `Agent` = a typed code object, but no behavioral-trust *envelope* spec | **AIDE ahead** on the envelope — OAgents §10's "behavioral trustworthiness during execution" sits *above any framework*, Mastra included |

### Table (b) — against the six AEON service planes

| AEON plane | Mastra equivalent | AIDE position | State |
|---|---|---|---|
| **Identity** | Optional endpoint authentication "using your identity system" — no principal-altitude model | *Behind* on enterprise-identity wiring; **AIDE ahead** on the principal concept | in-flight |
| **Authority** | RBAC/ordinals absent; Guardrails (prompt-injection/sanitization) ≠ authority | **AIDE ahead** — OrdSA O0–O6 is unique | ahead |
| **Evidence** | **Evals/Scorers + observability** — model-graded/rule-based/statistical, tracing, metrics; built and shipping | **AIDE behind** — Mastra's eval/observability is real product where AIDE's evidence trail is emit-only spec | behind |
| **Integration** | Broad RAG/vector/tool integrations + MCP authoring | *In flight elsewhere* — broad, mature, TS-native | in-flight |
| **Capability composition** | **Workflows** (graph/step, `.then()`/`.branch()`/`.parallel()`, durable, HITL) | *In flight elsewhere* — strong; but no **envelope-refinement** composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) | in-flight |
| **Orchestration runtime** | Durable-execution workflow runtime + serverless/standalone deploy | **AIDE behind** on realized runtime; *converging* via the workflow-orchestration pattern | behind / in-flight |

*(Inference is AEON's 7th plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md): Mastra is model-provider-agnostic via the Vercel AI SDK, but model-agnosticism is an integration convenience, not a first-class **governance** property the way the Inference plane frames it.)*

### Vocabulary collision note

- Mastra's **`Agent`** ("LLM that reasons about goals, decides tools, iterates") is an AI-acting-under-a-principal — in canon that is an **AI-aide** ([ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)), and it must **not** be read as the OAgents **`Agent`** primitive (a typed object inside a behavioral envelope). Never carry Mastra's casual "agent" into canon prose.
- Mastra **`Tool`** = atomic invocation — convergent with canon/`Tool` across the field.
- Mastra has no first-class "Skill" surface; where a framework's **`Skill`** would appear it maps to MxM **Means**, not to a construct.
- Mastra **`Workflow`** ↦ the workflow-orchestration pattern ([ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)); it is a *Means*-layer realization of that pattern, not a governing spec.
- Mastra **`Guardrails`** (prompt-injection / output sanitization) is input/output hygiene — it is **not** OrdSA authority and **not** MxM Morals; flag the temptation to read it as deontic governance.
- **Entity distinction:** Mastra is an external OSS project. It has no relationship to the Ologos ecosystem or to NG-AIDE-01, and nothing here implies any "fleet." Mastra's adopters (Brex/Sanity/Factorial) are third parties, not collaborators.

## 4. Classification

**Mixed — "in flight elsewhere," at a different altitude.** As with the LangChain finding, aide-canon and Mastra are *different categories* — a **governance/architecture corpus** vs a **build-and-run framework** — so classification is per-axis, not global.

- **AIDE ahead** — **Authority** (OrdSA O0–O6, with no Mastra analogue), the **behavioral envelope / trust layer** (OAgents §10 names exactly this class of framework as one whose execution-time trustworthiness is "outside their scope"), **deontic constraints** (MxM Morals — Mastra's Guardrails are I/O hygiene, not deontics), the **principal/identity-altitude** concept, and **vendor-neutral conformance criteria** / the DEA corpus altitude itself.
- **AIDE behind** — **Evidence/observability** (Mastra's Evals/Scorers + tracing are built and shipping where AIDE's evidence trail is emit-only spec), **realized runtime** (durable-execution workflows + serverless deploy), and — decisively — **adoption, funding, and shipping-product status**, plus a slice AIDE has no equivalent for: **TS-native ecosystem coverage** (the honest specialty lead). AIDE remains design-first research with enforcement largely unbuilt.
- **In flight elsewhere** — **orchestration** (Mastra Workflows ↔ AEON Composition / Orchestration-runtime + the workflow-orchestration pattern) and **integration/RAG/MCP breadth**.

**Synthesis:** they **compose, not compete.** aide-canon is the governance layer one would wrap *around* a Mastra deployment — Mastra Workflows as the Means/runtime realizing ADR-EA-0027, Mastra Evals/observability as the Evidence plane, with OAgents' envelope + OrdSA authority + MxM Morals supplying the trust/governance the framework structurally lacks. This is the OAgents §10 thesis (trust layer *above any framework*) made concrete in the **TypeScript** stack specifically — the same canon-spec ↔ platform-substrate relationship the canon documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/), now extended to a TS-native substrate.

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance lead, language-agnostic).** Propagate the OAgents-envelope / OrdSA-authority / MxM-Morals position as the trust layer that sits *above any agent framework regardless of language* — Mastra is the canonical **TypeScript** example of a maturing substrate with no such layer. KR shape: a documented "govern-a-Mastra-deployment" mapping (envelope + authority + Morals over Mastra Workflows/Evals), demonstrating the canon is not Python-coupled.
2. **Catch-up (evidence tooling).** Mastra's Evals/Scorers + observability are materially ahead of AIDE's emit-only evidence spec. KR shape: adopt OTel-GenAI as the canonical evidence shape (already begun — workflow-orchestration shared evidence object) and demonstrate Mastra-grade scorer/trace evidence on an AIDE exemplar.
3. **Converge-or-differentiate (orchestration).** Position the **workflow-orchestration pattern** ([ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)) as the governing spec over Mastra-class durable-workflow runtimes — convergent on graph/step/HITL/durable mechanics, differentiated by the envelope-refinement composition law Mastra does not enforce.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Inherits the 2026-05-29 framework-vocabulary discipline (vocabulary-map / sibling LangChain finding). Revisit on the next Mastra minor/major release (fast cadence) or at OKR refresh.
