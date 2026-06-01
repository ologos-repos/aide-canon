# OSS framework — AutoGen

> SOTA-survey finding. Shape per [`../README.md`](../README.md) → [`sota-survey/README.md`](../../sota-survey/README.md). Cadence: **fast** (OSS frameworks ship weekly) — but AutoGen is now **maintenance-mode**, so the live direction-of-travel is its successor (see [`../vendor-stacks/microsoft.md`](../vendor-stacks/microsoft.md)). Treat product specifics here as a dated snapshot.

## 1. What it is

**AutoGen** is Microsoft's open-source framework for building **multi-agent conversational systems** — applications composed of multiple LLM-backed agents that solve tasks by *talking to each other* (and to tools, code executors, and humans) in a message-passing loop. Its signature idea is the **conversation as the orchestration primitive**: rather than a static graph or pipeline, behavior emerges from agents exchanging messages, with a manager deciding turn order.

As of the 2026 survey it is in a clearly declared posture:

> **"⚠️ Maintenance Mode: AutoGen is now in maintenance mode. It will not receive new features or enhancements and is community managed going forward."**

Microsoft has converged AutoGen and Semantic Kernel into the **Microsoft Agent Framework (MAF)**, which GA'd **2026-04-03** as "the enterprise-ready successor to AutoGen." AutoGen continues to receive bug fixes and critical security patches only; new capability flows to MAF, and existing users are pointed at an AutoGen → Agent Framework migration guide. This entry therefore surveys AutoGen as **prior art / a paradigm**, and cross-references the MAF convergence and enterprise side in [`../vendor-stacks/microsoft.md`](../vendor-stacks/microsoft.md).

AutoGen's own architecture (post the v0.4 rewrite) is three-layered:

- **`autogen-core`** — the event-driven message-passing runtime: actor-style agents, local/distributed execution, cross-language support (.NET + Python).
- **`autogen-agentchat` (AgentChat)** — the higher-level, opinionated API for rapid multi-agent prototyping (two-agent chat, group chats, teams); built on Core. The recommended starting point.
- **`autogen-ext`** — first/third-party extensions: LLM clients (OpenAI, AzureOpenAI), code executors, capabilities.

The agent abstractions are **`AssistantAgent`** (LLM-backed worker) and the v0.2-era **`ConversableAgent`** (the base conversational building block), composed into **`GroupChat`** / team patterns where a manager selects the next speaker. Latest official Microsoft release at survey time: **python-v0.7.5**. (Note: a separate community fork, **AG2** — "the open-source AgentOS," formerly carrying the AutoGen name — exists and is *not* Microsoft's `microsoft/autogen`; do not conflate the two when reading release dates or docs.)

It is, in aide-canon terms, a **Means-layer implementation substrate** — the altitude AIDE explicitly is *not*.

## 2. Source links

- Official repo: `github.com/microsoft/autogen` (maintenance-mode banner + three-layer architecture).
- Docs: `microsoft.github.io/autogen/` (AgentChat / Core / Extensions API references).
- PyPI: `autogen-agentchat`, `autogen-core`, `autogen-ext`.
- Successor: Microsoft Agent Framework — see [`../vendor-stacks/microsoft.md`](../vendor-stacks/microsoft.md) §1 (GA 2026-04-03 convergence of Semantic Kernel + AutoGen) and `learn.microsoft.com/en-us/agent-framework/`.
- In-canon prior research: the framework-vocabulary rows of [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md) (the `Agent`/`Skill`/`Tool` mapping discipline this entry inherits).
- (Distinct community fork — not surveyed here — is **AG2**, `ag2ai/ag2`; mind the naming collision when reading third-party "AutoGen 2026" write-ups.)

## 3. Map against AIDE

### Against the four AIDE constructs

| AIDE construct | AutoGen equivalent | AIDE position |
|---|---|---|
| **DEA** (digital-thread enterprise architecture) | (no enterprise-architecture surface — AutoGen is an application framework) | *AIDE ahead* — no DEA-altitude architecture concept exists in AutoGen |
| **OrdSA** (O0–O6 ordinal authority) | (no authority model — a `GroupChat` manager picks speakers, but there is no authority-down/evidence-up altitude) | **AIDE ahead** — see [`../../../../constructs/ordsa/`](../../../../constructs/ordsa/); turn-selection ≠ ordinal authority |
| **MxM** (5-surface harness) | the `autogen-core` runtime + AgentChat component model (a runtime/component decomposition, not a governance harness) | *In flight elsewhere* — comparable decomposition, different vocabulary; AutoGen has no Morals/Memory/Mind governance surfaces |
| **OAgents** (typed agent envelope + trust layer) | `AssistantAgent` / `ConversableAgent` — an ad-hoc conversational interface, no envelope or trust token | **AIDE ahead** — see [`../../../../constructs/oagents/`](../../../../constructs/oagents/); behavioral trustworthiness during execution is outside AutoGen's scope |

### Against the six AEON service planes

| AEON plane | AutoGen equivalent | AIDE position |
|---|---|---|
| **Identity** | none first-class — agents are named objects, no principal-altitude identity (Azure identity arrives only via MAF/Entra) | *AIDE behind* on shipped identity (via the MAF successor), but AutoGen *itself* has no identity model |
| **Authority** | `GroupChatManager` speaker-selection; no ordinal authority concept | **AIDE ahead** — OrdSA O0–O6 authority-down/evidence-up is absent; manager turn-taking is orchestration, not authority |
| **Evidence** | conversation transcripts + optional OpenTelemetry hooks; no datasets/eval/annotation tooling (that lives in the MAF/Foundry successor) | **AIDE behind** on *mature* evidence tooling (via successor), but level on AutoGen's own emit-only traces |
| **Integration** | `autogen-ext` LLM clients + tool/code-executor integrations | *In flight elsewhere* — real integration breadth, convergent direction |
| **Capability composition** | multi-agent `GroupChat` / teams; tool calls; code execution | *In flight elsewhere* — strong conversational composition, but **no envelope-refinement composition law** (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | `autogen-core` event-driven, local/distributed runtime | **AIDE behind** on realized runtime; *converging* via the workflow-orchestration pattern — though AutoGen's runtime is now frozen and the live successor is MAF |

*(Inference is AEON's 7th plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md): AutoGen is model-flexible through `autogen-ext` clients, but model choice is a client-configuration detail, not the first-class **governance** property the Inference plane frames — per-principal substrate binding is absent.)*

### Vocabulary collision (inherits the map discipline)

AutoGen's **`Agent`** (`AssistantAgent` / `ConversableAgent`) is a conversational worker object — when it stands for an AI acting under a principal it is the canon's **AI-aide** ([ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)), and never to be written as a casual bare "agent." It is **not** the OAgents **`Agent`** primitive (a *typed object inside a behavioral envelope*); AutoGen's agent carries no envelope or trust token, so the surfaces look alike and govern differently — flag the collision. AutoGen has **no `Skill` noun** (its capability surface is *tools* + code execution + `autogen-ext`), so the field's `Skill ↦` MxM **Means** mapping has no AutoGen surface to attach to — capability attaches via *tools*/extensions instead. **`Tool`** = atomic invocation (convergent across the field; maps cleanly). Avoid any bare "fleet" framing — AutoGen's multi-agent teams are not, and must not be conflated with, the Ologos operator fleet or NG-AIDE-01.

## 4. Classification

**Mixed — "in flight elsewhere," at a different altitude — and now frozen.** aide-canon and AutoGen are *different categories*: a **governance/architecture corpus** vs an **application-building framework**. The classification is per-axis, not global:

- **AIDE ahead** — Authority (OrdSA O0–O6 vs a turn-selecting `GroupChatManager`); behavioral envelope / trust layer (OAgents' thesis that *"behavioral trustworthiness during execution is outside their scope … OAgents addresses the trust layer that sits above any agent framework"* — AutoGen is a textbook instance of a framework with no such layer); deontic constraints (MxM Morals); HCAE operator-as-curator; vendor-neutral conformance criteria; the DEA enterprise-architecture altitude AutoGen never reaches.
- **AIDE behind** — realized runtime, observability/eval, identity, and enterprise plumbing — but **almost entirely via the successor (MAF/Foundry), not AutoGen itself**; and, decisively, **adoption and the fact that AutoGen shipped, ran in production, and seeded a 75k-star ecosystem** where AIDE is design-first research with enforcement still largely unbuilt. The honest qualifier: AutoGen is in maintenance mode, so this "behind" is against a *frozen* target whose forward motion has migrated to MAF.
- **In flight elsewhere** — conversational orchestration (`GroupChat`/teams ↔ AEON Capability-composition + Orchestration-runtime + the workflow-orchestration pattern); integration breadth via `autogen-ext`.

**The synthesis:** they **compose, not compete** — but the composition target has moved. AutoGen *validated the conversational-multi-agent paradigm* (agents-talking-to-agents as orchestration), and that paradigm now lives on in the Microsoft Agent Framework. aide-canon is the governance layer one would wrap *around* such a runtime: AutoGen-style `GroupChat`/teams as the Means/capability-composition substrate, with OAgents' envelope + OrdSA authority + MxM Morals supplying the behavioral-trust and authority-altitude governance the conversational model structurally lacks (a `GroupChatManager` decides *who speaks next*, never *who may act under whose authority within what envelope*). This is the OAgents §10 thesis made concrete against the framework that most cleanly exhibits the gap — and it is the same canon-spec ↔ platform-substrate relationship the canon documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/). Because AutoGen is frozen, the *live* convergence story is tracked in [`../vendor-stacks/microsoft.md`](../vendor-stacks/microsoft.md); this entry preserves AutoGen as the paradigm-of-record.

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance lead over the conversational paradigm).** Propagate the OAgents-envelope / OrdSA-authority position as the behavioral-and-authority trust layer that sits *above any agent framework* — AutoGen is the cleanest example of a conversational-multi-agent runtime with no envelope, no authority altitude, and a manager that orders speech rather than governing action. KR shape: a documented "govern-a-conversational-multi-agent-system" mapping (envelope + OrdSA authority + Morals over a `GroupChat`/teams runtime), with the contrast stated as *authority-and-envelope governance* vs *turn-selection orchestration*.
2. **Catch-up (runtime + evidence — but aim at the successor).** AutoGen's own runtime/evidence is frozen; its forward motion is in MAF. KR shape: adopt OTel-GenAI as the canonical evidence shape (already begun — workflow-orchestration v0.1.2 shared evidence object) so an AIDE exemplar can emit into the MAF/Foundry observability successor, rather than catching up to a maintenance-mode framework.
3. **Converge-or-differentiate (orchestration).** Position the **workflow-orchestration pattern** ([ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)) as the governing spec over conversational-multi-agent runtimes (AutoGen-class and its MAF successor) — convergent on multi-agent composition mechanics, differentiated by the envelope-refinement composition law the conversation-as-orchestration model does not enforce.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Inherits the framework-vocabulary mapping discipline (aide-vocabulary-map). AutoGen is maintenance-mode as of survey; revisit only on a maintenance-status change — the live successor is tracked in [`../vendor-stacks/microsoft.md`](../vendor-stacks/microsoft.md) (Microsoft Agent Framework), which is where the next material shift will land.
