# Vendor stack — OpenAI (Enterprise + Agents platform)

> SOTA-survey finding. Shape per [`../README.md`](../README.md) → [`sota-survey/README.md`](../../sota-survey/README.md). Cadence: **fast** (OpenAI renames surfaces frequently — "connectors"→"Apps" Dec 2025, "Operator" folded into "ChatGPT agent" — treat product specifics as a dated snapshot, not a fixed spec).

## 1. What it is

**OpenAI's agents platform** is the productized stack OpenAI ships on top of its frontier models — a *build-and-run* substrate for agentic systems, not a governance corpus. As of mid-2026 the surfaces compose into roughly six pieces:

- **ChatGPT Enterprise** — the workspace tier: SSO/SAML, admin console, data-residency/compliance controls, and per-role feature toggles (including whether *agent mode* is enabled for a workspace). The principal-facing operator surface.
- **Agents SDK** — the open-source orchestration library (Python + JS/TS). An "agent" is an LLM configured with **instructions**, **tools**, **handoffs**, **guardrails**, sessions and tracing; a `Runner` manages turns. GA, production-grade.
- **Responses API** — OpenAI's agent-oriented, stateful endpoint (successor to Chat Completions for agent work): hosted tools, stateful turn management, structured outputs. The Agents SDK is built on it by default. GA.
- **AgentKit** (DevDay, Oct 2025) — the build-and-ship bundle: **Agent Builder** (visual drag-and-drop canvas for versioned multi-agent workflows — *beta*), **Connector Registry** (central admin surface mapping ChatGPT/API orgs to data sources + approved MCP connectors — *beta rollout*), **ChatKit** (embeddable chat-agent UI toolkit — *GA*).
- **Apps SDK** (renamed from "connectors," Dec 17 2025) — packaging for ChatGPT "Apps": an **MCP server** plus **UI components** rendered inline / picture-in-picture / fullscreen. Builds on and extends MCP.
- **Operator / ChatGPT agent** — the computer-use agent (browses, clicks, runs code). The standalone Operator product was retired and its computer-use capability folded into **ChatGPT agent mode**, gated by an Enterprise workspace toggle.
- **Evals** — datasets, graders, and inline eval configuration (surfaced in Agent Builder). GA.

The enterprise value proposition is **frontier model quality, a GA orchestration SDK on a stateful API, a visual builder, an MCP-native app/connector ecosystem, and enterprise plumbing (SSO, admin console, eval tooling)**. In aide-canon terms it is a **Means-layer implementation substrate** — the altitude AIDE explicitly is *not*.

## 2. Source links

- Official: `openai.com/index/introducing-agentkit/`, `developers.openai.com/api/docs/guides/agents` (Agents SDK), `openai.github.io/openai-agents-python` (OSS SDK reference — agents/handoffs/guardrails), `developers.openai.com/apps-sdk` (Apps SDK), `developers.openai.com/api/docs/guides/agent-builder`, `openai.com/index/introducing-apps-in-chatgpt/`, ChatGPT agent / Operator: `openai.com/index/introducing-chatgpt-agent/` + `help.openai.com` ChatGPT-agent article.
- In-canon prior research: the external-term mappings in [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md) (vendor-stacks scope already lists OpenAI; *MyAide* × "my ChatGPT" row) and the AI-aide vocabulary ratified in [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md).
- **(Rebrand-prone — high.** OpenAI renames surfaces aggressively: "connectors"→"Apps" (Dec 2025), standalone "Operator"→"ChatGPT agent," "Azure AI Studio"-style churn at the partner layer. Verify every surface name + maturity at read time.)

## 3. Map against AIDE

### Against the four AIDE planes

| AIDE plane | OpenAI equivalent | Position |
|---|---|---|
| **Control** (AEON governance) | Agent Builder orchestration + Connector Registry admin + Enterprise role toggles — but **no authority/trust governance layer** | *AIDE ahead* on governance; *behind* on operability |
| **Runtime** | **Agents SDK + Responses API** (Runner-managed turns, sessions, hosted tools); ChatGPT agent for computer-use | *In flight elsewhere* (strong overlap) / *AIDE behind* on realized runtime |
| **Experience** (AIDEX) | ChatKit (embed UX) + Agent Builder (a *builder* canvas) + Apps in ChatGPT | *AIDE ahead* — these are build/embed UX, not an HCAE operator-as-curator console |
| **Capability** (OAAD) | Tools (function/hosted/MCP), Apps SDK (MCP + UI), Connector Registry | *In flight elsewhere* — mature, MCP-native integration breadth |

### Against the six AEON service planes

| AEON plane | OpenAI equivalent | AIDE position |
|---|---|---|
| **Identity** | Enterprise SSO/SAML; ChatGPT workspace + API org identity | *In flight elsewhere* — identity primitives exist, no principal-altitude model |
| **Authority** | RBAC (workspace roles, agent-mode role toggles); no ordinal authority concept | **AIDE ahead** — OrdSA O0–O6 authority-down/evidence-up is absent (vendor RBAC ≠ ordinal authority) |
| **Evidence** | **Evals** (GA: datasets/graders, inline eval config) + SDK tracing | **AIDE behind** — Evals + tracing are built + GA; AIDE's evidence trail is emit-only spec |
| **Integration** | **Apps SDK / MCP**, Connector Registry, hosted tools | *In flight elsewhere* — broad, MCP-native, maturing fast |
| **Capability composition** | Agents-as-tools + **handoffs** (agent→agent delegation, the sub-agent equivalent); Agent Builder graph nodes | *In flight elsewhere* — strong; but no **envelope-refinement** composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | **Agents SDK Runner + Responses API**; Agent Builder (beta) | **AIDE behind** on realized runtime; *converging* via the workflow-orchestration pattern |

*(Inference is AEON's 7th plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md): OpenAI is the **opposite** of model-agnostic — the stack is welded to OpenAI's own models as the substrate. Per-principal substrate-swap, which the Inference plane frames as a first-class **governance** property, is structurally absent — a sharper *AIDE ahead* than for model-agnostic frameworks.)*

### Vocabulary collision

OpenAI's **"agent"** = "an LLM configured with instructions, tools, handoffs, and guardrails" — a runtime configuration object, not a principal-bound role. Under canon vocabulary, an AI system acting under a principal is an **AI-aide** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)), **not** the OAgents `Agent` primitive (a typed object inside a behavioral envelope); the personal-instance "my ChatGPT" maps to **MyAide** (vocabulary-map MyAide row). **"Tool"** = atomic invocation (convergent across the field). **"Handoff"** = agent→agent delegation — the sub-agent / delegation equivalent.

**Crucial OpenAI-specific gap:** OpenAI has **no "Skill" primitive at all.** Instructional/behavioral configuration lives entirely on the agent's **`instructions`** field (the system prompt, static or dynamic); the **Tool is the only externalized primitive**. There is therefore no vendor surface that maps to MxM **Means** the way LangChain's `Skill` (shareable knowledge package) does — for OpenAI, the canon's *Skill ↦ Means* row has no left-hand term, and behavioral specification is in-prompt rather than packaged. This is the canon vocabulary-map's recorded position and is the inverse of the LangChain entry's collision: there the clash is over the word *Skill*; here the finding is its **absence**.

## 4. Classification

**Mixed — "in flight elsewhere," at a different altitude.** This is the load-bearing finding: aide-canon and OpenAI's stack are *different categories* — a **governance/architecture corpus** vs a **build-and-run platform welded to one model vendor** — so the classification is per-axis, not global:

- **AIDE ahead** — Authority (OrdSA O0–O6 vs vendor RBAC), behavioral envelope / trust layer (OAgents §10: trustworthiness *during execution* sits **above any framework** — OpenAI ships instructions+guardrails, not a typed behavioral envelope), deontic constraints (MxM Morals), HCAE operator-as-curator experience, **Inference-plane model-agnosticism** (OpenAI is single-vendor-locked), and the absence of any Means-layer **Skill** abstraction (behavior is in-prompt, not packaged/governed).
- **AIDE behind** — realized runtime (Agents SDK + Responses API, GA), evals/observability (Evals + tracing, GA), enterprise plumbing (SSO, admin console, Connector Registry), MCP-native app ecosystem, and — decisively — **adoption, distribution, and the fact that it is a shipping GA product** where AIDE is design-first research with enforcement still largely unbuilt.
- **In flight elsewhere** — orchestration (Agents SDK Runner ↔ AEON Orchestration-runtime + the workflow-orchestration pattern), capability composition (handoffs ↔ sub-agent delegation), and MCP integration breadth.

**The synthesis:** they **compose, not compete** — but with a caveat absent from the LangChain finding: OpenAI's single-vendor lock makes it a *narrower* substrate. aide-canon is the governance layer one would wrap *around* an OpenAI deployment — Agents SDK / Responses API as the Means/runtime, Evals as part of the Evidence plane, with OAgents' envelope + OrdSA authority + MxM Morals supplying the trust/governance the stack structurally lacks, **and the Inference plane supplying the multi-vendor portability OpenAI cannot.** This is the OAgents §10 thesis made concrete, the same canon-spec ↔ platform-substrate relationship the canon already documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/).

## 5. Objective implication

Four Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance lead).** Propagate the OAgents-envelope / OrdSA-authority position as the trust layer that sits *above any agent framework* — OpenAI's "instructions + guardrails" config is the canonical example of a mature substrate with no typed behavioral envelope and no ordinal authority. KR shape: a documented "govern-an-OpenAI-deployment" mapping (envelope + authority + Morals over Agents SDK / Responses API).
2. **Defend-and-extend (Inference plane / portability).** OpenAI is single-vendor-locked; the Inference plane ([ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md)) is a first-class AIDE differentiator. KR shape: demonstrate per-principal substrate-swap (OpenAI-backed in one binding, non-OpenAI in another) under one unchanged governance spec.
3. **Catch-up (eval/runtime tooling).** Agents SDK + Responses API + Evals are GA and ahead of AIDE's emit-only evidence spec and unbuilt runtime. KR shape: adopt OTel-GenAI as the canonical evidence shape (already begun — workflow-orchestration v0.1.2 shared evidence object) and show Evals-grade trace/eval on an AIDE exemplar.
4. **Converge-or-differentiate (orchestration + Means gap).** Position the **workflow-orchestration pattern** ([ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)) as the governing spec over Agents-SDK-class runtimes — convergent on handoff/Runner mechanics, differentiated by the envelope-refinement composition law and by treating behavioral spec as a packaged **Means/Skill** artifact OpenAI has no primitive for.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Inherits the ADR-EA-0016 AI-aide / MyAide vocabulary discipline; records OpenAI's distinctive **no-Skill-primitive** position (behavior on `instructions`; Tool as sole externalized primitive). Revisit on the next OpenAI product/rename shift (rebrand-prone — high) or at OKR refresh.
