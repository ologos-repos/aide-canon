# OSS framework — LlamaIndex

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Mapping anchor: the **two-table** form declared in [`oss-frameworks/README.md`](README.md) (AIDE constructs *and* the AEON service planes) — this differs from the vendor-stacks single-table form, because OSS frameworks carry a construct-comparable component model. Cadence: **fast** (LlamaIndex ships weekly; treat package names and version specifics as a dated snapshot).

## 1. What it is

**LlamaIndex** is an open-source (MIT) Python/TypeScript framework for building **agentic, retrieval-grounded LLM applications** — it began as a data/indexing framework ("GPT Index") and has reorganized, by 2026, around three pillars: **agentic retrieval** (LLM-routed search over indexed data, framed by the project as the successor to "naive top-k RAG"), **Workflows** (an event-driven, step-based orchestration framework), and a serving/deployment path (`llama-deploy` / LlamaAgents). The repo describes itself as "an open-source framework to build agentic applications" / "the leading document agent and OCR platform" (~50k GitHub stars). Its strongest and most differentiated surface remains **knowledge work over documents**: connectors (LlamaHub), indexing, query/retrieval engines, structured extraction, and document-centric agent workflows.

Two surfaces matter most for this survey:

- **Workflows** — reached **1.0 on 2025-06-30** and was extracted into a standalone, framework-independent package (`llama-index-workflows` on PyPI; `@llamaindex/workflow-core` on npm). It is an event-driven model: an application is divided into **Steps** triggered by **Events**, which themselves emit Events that trigger further Steps; async-first, with typed workflow **state/Context**, resource injection, optional observability via `llama-index-instrumentation` (OpenTelemetry / Arize Phoenix), human-in-the-loop, and streaming. It is positioned as a "general-purpose orchestration framework for LLM-powered systems," usable outside LlamaIndex.
- **AgentWorkflow** — a multi-agent orchestration system built *on top of* Workflows: named agent classes **`FunctionAgent`** (function-calling LLMs) and **`ReActAgent`** (any LLM), with **agent handoff**, shared **Context**/state across agents, and tool-calling. Agentic retrieval adds an **`auto_routed`** mode — a lightweight agent that selects among retrieval strategies (chunk / files-via-metadata / files-via-content) per query.

In aide-canon terms LlamaIndex is a **Means-layer execution substrate** with unusually deep **Capability** (retrieval/knowledge) reach — the altitude aide-canon explicitly is *not*.

## 2. Source links

- Official: `llamaindex.ai`, docs at `developers.llamaindex.ai`, repo `github.com/run-llama/llama_index` (MIT).
- Workflows 1.0 announcement (2025-06-30): `llamaindex.ai/blog/announcing-workflows-1-0-a-lightweight-framework-for-agentic-systems`; standalone repos `run-llama/workflows-py` / `run-llama/workflows-ts`.
- AgentWorkflow: `llamaindex.ai/blog/introducing-agentworkflow-a-powerful-system-for-building-ai-agent-systems`.
- Agentic retrieval position: `llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval` (the `auto_routed` mode + composite retrieval).
- In-canon prior research: the workflow-orchestration pattern [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md) and [ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md) (the convergence point cited in §3–§4); the vocabulary discipline of [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md).
- (Adjacent commercial pieces — **LlamaCloud**, **LlamaParse**, **LlamaExtract** — are mentioned here for completeness but **not surveyed**; they are managed parse/extract/index services, not the OSS framework's architectural surface.)

## 3. Map against AIDE

### Table A — against the AIDE constructs (DEA / OrdSA / MxM / OAgents)

| AIDE construct | LlamaIndex equivalent | AIDE position |
|---|---|---|
| **DEA** (digital-thread evidence architecture) | Workflows' Context/state + `llama-index-instrumentation` (OTel/Phoenix spans); per-step typed events | *In flight elsewhere* — real, OTel-aligned emission; but no governed digital-thread / lineage contract above it |
| **OrdSA** (O0–O6 authority layering) | (not addressed) — handoff is peer-to-peer agent routing, no authority altitude | **AIDE ahead** — authority-down / evidence-up has no analogue; AgentWorkflow handoff is lateral, not ordinal |
| **MxM** (5-surface harness) | The framework *is* a MEANS substrate (Workflows ↦ MEANS workflows; tools ↦ MEANS); no Mind/Morals/Memory/Methods governance surfaces | *In flight elsewhere* on MEANS decomposition; **AIDE ahead** on the four governance surfaces it does not author |
| **OAgents** (typed `Agent` envelope + behavioral trust) | `FunctionAgent` / `ReActAgent` as interface types; no pre-gate / post-verify / operational-discipline envelope, no envelope lattice | **AIDE ahead** — OAgents §10's thesis applies verbatim: behavioral trustworthiness during execution is outside the framework's scope |

### Table B — against the six AEON service planes

| AEON plane | LlamaIndex equivalent | AIDE position |
|---|---|---|
| **Identity** | (no first-class principal/identity model) | **AIDE ahead** on the principal-altitude model — though neither ships enterprise identity integration as a governance property |
| **Authority** | (none — lateral agent handoff only) | **AIDE ahead** — OrdSA ordinal authority is absent |
| **Evidence** | Workflows events + `llama-index-instrumentation` OTel/Phoenix tracing | *In flight elsewhere* / **AIDE behind on realized tooling** — built and shipping; AIDE's evidence trail is emit-only spec |
| **Integration** | LlamaHub connectors; broad, mature data/tool integration; MCP-compatible | **AIDE behind** — integration breadth (esp. document/data connectors) is materially deeper |
| **Capability composition** | **Workflows** Step/Event composition + **AgentWorkflow** handoff; retrieval/query-engine composition | *In flight elsewhere* — strong; but **no envelope-refinement composition law** (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | **Workflows 1.0** (standalone, durable-ish, async) + `llama-deploy` serving | **AIDE behind** on realized runtime; *converging* — see §4 |

*(Inference is AEON's 7th plane, ADR-EA-0015: LlamaIndex is model-provider-agnostic at the integration layer, but model-agnosticism is not framed as a first-class **governance** property the way the Inference plane does.)*

### Vocabulary-collision note

- LlamaIndex **`Agent`** (`FunctionAgent`/`ReActAgent` — an LLM-under-tools interface object acting under a developer/operator) is, in canon terms, an **AI-aide** ([ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) — **never** casual "agent" — and it is **not** the OAgents `Agent` primitive (a typed object *inside* a behavioral envelope). Flag the collision on read.
- LlamaIndex **`Tool`** = atomic invocation — convergent with the canon's `Tool` (OrdSA O4 / OAgents atomic).
- LlamaIndex **`Workflow`** (Step/Event control program) maps to the canon's **workflow-orchestration pattern** object and to MxM **MEANS** (which lists "tools, skills, workflows") — convergent on shape, see §4.
- LlamaIndex carries no "Skill" surface of LangChain's kind; where it speaks of reusable capability packs, that maps to **Means**, not to a governance surface.

## 4. Classification

**Mixed — "in flight elsewhere," at a different altitude.** aide-canon is a **governance CORPUS**; LlamaIndex is a **Means-layer build substrate** — different categories, so the classification is per-axis, not global.

- **AIDE ahead** — Authority (OrdSA O0–O6; LlamaIndex handoff is lateral, no altitude), the behavioral **envelope / trust layer** (OAgents — its §10 exclusion applies directly: workflow steps that are judgment-exercising agents inherit the trust problem the framework does not address), the deontic surface (MxM Morals), and the four non-MEANS MxM surfaces generally. OAgents' envelope sits *above any framework*; LlamaIndex is a clean example of a substrate with no such lattice.
- **AIDE behind** — realized orchestration **runtime** (Workflows 1.0 is shipped, standalone, versioned), **evidence tooling** (OTel/Phoenix instrumentation is built where AIDE's is spec), **integration/retrieval breadth** (the document/knowledge-work surface is best-in-class), and — decisively — **adoption and the fact that it is a shipping framework** (~50k stars, MIT, weekly cadence) where AIDE is design-first research with enforcement largely unbuilt.
- **In flight elsewhere** — Capability composition and orchestration: LlamaIndex **Workflows** (event-driven Step/Event control program) and the canon's **workflow-orchestration pattern** ([ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)) **converge on the same shape** — a deterministic-ish control substrate sequencing/branching probabilistic agent work. **The convergence is genuine and worth naming.** But **neither enforces an envelope lattice**: ADR-EA-0027's load-bearing contribution is the envelope-refinement law `envelope(child) ⊑ envelope(orchestrator)`, per-limb and transitively closed across nesting depth; LlamaIndex AgentWorkflow handoff (like LangGraph) passes control and shared Context with **no envelope-refinement gate** on the spawned agent. The canon itself records that this `⊑` is unbuilt across *all* known implementations — so the honest reading is: the field (LlamaIndex Workflows + LangGraph + Claude Code Workflow) has converged on the orchestration *object*; the canon's differentiation is the *composition law* over it, and that law is still a target, not a realized guarantee on either side.

**Synthesis:** they **compose, not compete.** aide-canon is the governance layer one would wrap *around* a LlamaIndex deployment — Workflows/AgentWorkflow as the Means/orchestration runtime, `llama-index-instrumentation` as the Evidence plane, LlamaHub/retrieval as the Capability/Knowledge surface — with OAgents' envelope + OrdSA authority + MxM Morals supplying the trust/governance the framework structurally lacks. This is the same canon-spec ↔ platform-substrate relationship documented for LangChain ([`../vendor-stacks/langchain.md`](../vendor-stacks/langchain.md)) and for the canon's own exemplars (Hermetic, thinx-aidex). LlamaIndex's distinct contribution to that picture is **depth on the Capability + Knowledge/lineage axis** — its agentic-retrieval surface is a stronger Capability substrate than the general-purpose frameworks, and the natural integration target for the canon's Context/Lineage (Knowledge) concerns.

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Converge-or-differentiate (orchestration — the headline finding).** The field has converged on the event-driven workflow object (LlamaIndex Workflows 1.0, LangGraph, Claude Code Workflow). **Objective:** establish the workflow-orchestration pattern (ADR-EA-0027) as the *governing spec* over workflow-class runtimes — convergent on orchestration mechanics, differentiated by the per-limb envelope-refinement law these runtimes do not enforce. KR shape: a "govern-a-LlamaIndex-Workflow" mapping that attaches `⊑` + parent-FK evidence at each AgentWorkflow handoff, and an honest statement that enforcement at the substrate boundary is the open gap on both sides.
2. **Defend-and-extend (Capability/Knowledge lead — and a catch-up edge).** **Objective:** make the canon's Capability + Context/Lineage (Knowledge) surface concrete enough to govern a best-in-class retrieval substrate. LlamaIndex agentic retrieval (`auto_routed`, composite retrieval) is the SOTA target the canon should be able to *wrap and lineage-track*, not reimplement. KR shape: a Knowledge-plane lineage contract that consumes LlamaIndex retrieval evidence.
3. **Catch-up (evidence tooling).** `llama-index-instrumentation` (OTel-GenAI / Phoenix) is ahead of AIDE's emit-only evidence spec. **Objective:** adopt OTel-GenAI as the canonical evidence shape (already begun — workflow-orchestration v0.1.2 shared evidence object) and demonstrate trace/eval parity on an AIDE exemplar.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Inherits the workflow-orchestration convergence framing from ADR-EA-0027 (ratified same day) and the LangChain vocabulary discipline (vocabulary-map / ng-aide-01 PR #59 §5.1). Revisit on the next LlamaIndex Workflows minor release or at OKR refresh.
