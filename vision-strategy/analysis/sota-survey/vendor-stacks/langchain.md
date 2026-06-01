# Vendor stack — LangChain (Enterprise)

> SOTA-survey finding. Shape per [`../README.md`](../README.md) → [`sota-survey/README.md`](../../sota-survey/README.md). Cadence: **fast** (LangChain rebrands frequently — treat product specifics as a dated snapshot, not a fixed spec).

## 1. What it is

**LangChain Enterprise** is the commercial tier of the LangChain stack — a *build-and-run* platform for agentic systems, not a governance corpus. Five surfaces compose it:

- **LangChain** — the OSS framework (chains, model/tool integrations, the original abstraction layer).
- **LangGraph** — OSS stateful, graph-based agent orchestration: durable execution, persistence, human-in-the-loop, cyclic control flow.
- **LangGraph Platform** — the commercial deployment runtime: one-click/scaled agent deployment, persistence, task queues, cron, hybrid/self-hosted.
- **LangSmith** — the commercial observability + eval layer: tracing, datasets, evaluators, annotation queues, prompt management, production monitoring. Enterprise adds SSO/SAML, RBAC, self-hosting, SOC2/HIPAA.
- **Fleet / Agent Builder** (rebrand, ~March 2026) — persistent "organizational agents" with stable identity, memory, and tool/skill access, exposed through channels (a no/low-code agent-building surface).

The enterprise value proposition is **deployment flexibility (cloud / hybrid / self-hosted), security & compliance (SSO, RBAC, SOC2), mature observability, and support/SLA** — the plumbing of running agents in production at an organization. It is, in aide-canon terms, a **Means-layer implementation substrate** — the altitude AIDE explicitly is *not*.

## 2. Source links

- Official: `langchain.com`, `docs.langchain.com`, `www.langchain.com/langsmith`, LangGraph docs (`langchain-ai.github.io/langgraph`), LangGraph Platform docs.
- In-canon prior research: the LangChain rows of [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md) and the SOTA-vocabulary synthesis in [ng-aide-01 PR #59 §5.1](https://github.com/ologos-repos/ng-aide-01/pull/59) (the `Agent`/`Skill`/`Tool`/`Sub-agent` mapping, surveyed 2026-05-29).
- (Product naming is rebrand-prone — the "Fleet"/Agent-Builder rename is the latest example; verify surface names at read time.)

## 3. Map against AIDE

### Against the four AIDE planes

| AIDE plane | LangChain Enterprise equivalent | Position |
|---|---|---|
| **Control** (AEON governance) | LangGraph Platform orchestration + LangSmith monitoring — but **no authority/trust governance layer** | *AIDE ahead* on governance; *behind* on operability |
| **Runtime** | **LangGraph / LangGraph Platform** — durable, persistent, scaled | *In flight elsewhere* (strong overlap) / *AIDE behind* on realized runtime |
| **Experience** (AIDEX) | Fleet / Agent Builder (a *builder* UX, not an operator-as-curator console) | *AIDE ahead* — no HCAE operator-curation experience model |
| **Capability** (OAAD) | LangChain tool/integration ecosystem | *In flight elsewhere* (mature integration breadth) |

### Against the six AEON service planes

| AEON plane | LangChain equivalent | AIDE position |
|---|---|---|
| **Identity** | Platform auth / SSO; agents have "stable identity" (Fleet) | *In flight elsewhere* — identity primitives exist, no principal-altitude model |
| **Authority** | RBAC at the enterprise tier; no ordinal authority concept | **AIDE ahead** — OrdSA O0–O6 authority-down/evidence-up is absent |
| **Evidence** | **LangSmith** — tracing, datasets, evals, annotation queues, monitoring | **AIDE behind** — LangSmith is built + mature; AIDE's evidence trail is emit-only spec |
| **Integration** | LangChain integrations + MCP support | *In flight elsewhere* — broad, mature |
| **Capability composition** | LangGraph graphs; Skills/Tools; deepagents sub-agents | *In flight elsewhere* — strong; but no **envelope-refinement** composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | **LangGraph Platform** | **AIDE behind** on realized runtime; *converging* via the workflow-orchestration pattern |

*(Inference is AEON's 7th plane, ADR-EA-0015: LangChain is model-provider-agnostic at the integration level, but model-agnosticism is not a first-class **governance** property the way the Inference plane frames it.)*

### Vocabulary collision (already mapped)

LangChain's **`Agent`** = "persistent organizational entity with stable identity, memory, tools and skills" — this is the canon's **AI-aide** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)), **not** the OAgents `Agent` primitive (a typed object inside a behavioral envelope). LangChain **`Skill`** (modular shareable knowledge package, `SkillsMiddleware`, progressive disclosure) maps to MxM **Means**; **`Tool`** = atomic invocation (convergent across the field). The collision is documented in the vocabulary map; this entry inherits that discipline.

## 4. Classification

**Mixed — "in flight elsewhere," at a different altitude.** This is the load-bearing finding: aide-canon and LangChain Enterprise are *different categories* — a **governance/architecture corpus** vs a **build-and-run platform** — so the classification is per-axis, not global:

- **AIDE ahead** — Authority (OrdSA), behavioral envelope / trust layer (OAgents §10 names LangChain explicitly as a framework whose *"behavioral trustworthiness during execution is outside their scope"*), deontic constraints (MxM Morals), HCAE operator-curation, vendor-neutral conformance criteria.
- **AIDE behind** — realized runtime (LangGraph Platform), observability/eval (LangSmith), enterprise plumbing (SSO/RBAC/SOC2/self-host), and — decisively — **adoption, funding, and the fact that it is a shipping product** where AIDE is design-first research with enforcement still largely unbuilt.
- **In flight elsewhere** — orchestration (LangGraph ↔ AEON Composition/Meta-Orchestration + the workflow-orchestration pattern); integration/capability breadth.

**The synthesis:** they **compose, not compete**. aide-canon is the governance layer one would wrap *around* a LangChain Enterprise deployment — LangGraph Platform as the Means/runtime, LangSmith as the Evidence/eval plane, with OAgents' envelope + OrdSA authority + MxM Morals supplying the trust/governance the framework structurally lacks. This is the OAgents §10 thesis made concrete, and the same canon-spec ↔ platform-substrate relationship the canon already documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/).

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance lead).** Propagate the OAgents-envelope / OrdSA-authority position as the trust layer that sits *above any agent framework* — LangChain Enterprise is the canonical example of a mature substrate with no such layer. KR shape: a documented "govern-a-LangChain-deployment" mapping (envelope + authority + Morals over LangGraph/LangSmith).
2. **Catch-up (evidence tooling).** LangSmith is materially ahead of AIDE's emit-only evidence spec. KR shape: adopt OTel-GenAI as the canonical evidence shape (already begun — see the workflow-orchestration v0.1.2 shared evidence object) and demonstrate LangSmith-grade trace/eval/annotation on an AIDE exemplar.
3. **Converge-or-differentiate (orchestration).** Position the **workflow-orchestration pattern** (ADR-EA-0027) as the governing spec over LangGraph-class runtimes — convergent on orchestration mechanics, differentiated by the envelope-refinement composition law LangGraph does not enforce.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Inherits the 2026-05-29 LangChain vocabulary mapping (vocabulary-map / ng-aide-01 PR #59 §5.1). Revisit on the next LangChain product shift (rebrand-prone) or at OKR refresh.
