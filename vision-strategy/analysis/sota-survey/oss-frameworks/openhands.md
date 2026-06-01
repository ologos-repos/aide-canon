# OSS framework — OpenHands (formerly OpenDevin)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Mapping anchor is the **OSS-frameworks** one (constructs + six AEON service planes), *not* the vendor-stacks "4 AIDE planes" table. Cadence: **fast** (weekly releases; V0→V1 SDK split is recent — treat component names as a dated snapshot).

## 1. What it is

**OpenHands** (renamed from **OpenDevin** in early 2024) is the leading open-source **autonomous coding AI-aide / harness** — a platform whose AI-aides do real engineering work (modify code, run shell commands, drive a headless browser, call APIs) rather than only suggesting completions. It is MIT-licensed (the core; an `enterprise/` directory carries separate licensing), maintained by OpenHands (ex-All Hands AI), and is by far the most-adopted framework in this slice (~75k GitHub stars; reported SWE-bench ~77 at survey time).

The late-2025 **V1 Software Agent SDK** refactored the project from a single-agent tool into a composable framework with three cleanly separable modules:

- **Agent logic** — the **CodeAct** agent, where the AI-aide expresses actions as executable code in a single action space, over an **event-stream** architecture (action → observation → logged event).
- **Execution environment** — a pluggable sandboxed **Runtime**: `LocalRuntime` (action server on the host), the default **Docker** sandbox (its own bash shell, Jupyter kernel, headless browser, optional tokenized VS Code Web), and `RemoteRuntime` for scaled container infrastructure.
- **Interface** — CLI, local GUI, REST API, and a hosted cloud tier.

In aide-canon terms OpenHands is a **Means-layer build substrate** — the altitude AIDE explicitly is *not*. The SDK composes an AI-aide from an `LLM` plus a list of `Tool` objects inside a `Conversation`; **what it leaves to the user** is the governance altitude entirely: custom `Tool`s, MCP integrations, and `Skill`s are developer-authored; there is **no authority-altitude model, no deontic constraint layer, and no behavioral-trust envelope** around what the AI-aide is permitted to do. Sandboxing supplies *containment* (blast-radius limiting), not *governance* (principled permission). The cloud tier adds RBAC and multi-user collaboration, but that is enterprise plumbing, not an ordinal-authority or envelope construct.

## 2. Source links

- **Repo:** [`OpenHands/OpenHands`](https://github.com/OpenHands/OpenHands) (core) · [`OpenHands/software-agent-sdk`](https://github.com/OpenHands/software-agent-sdk) (V1 SDK) · [`OpenHands/extensions`](https://github.com/OpenHands/extensions) (global skills registry)
- **Docs:** [`docs.openhands.dev`](https://docs.openhands.dev/) · Skills overview: [`docs.openhands.dev/overview/skills`](https://docs.openhands.dev/overview/skills) · Product site: [`openhands.dev`](https://www.openhands.dev/)
- **Sources to re-canvass at refresh:** GitHub release notes (last 90 days), `AGENTS.md` / `skills/README.md` in-repo, SWE-bench leaderboard standing.
- (V0 "microagents" → V1 "Skills" is a live rename with backward-compat reads; verify component names at read time.)

## 3. Map against AIDE

### Against the four AIDE constructs (DEA / OrdSA / MxM / OAgents)

| Construct | OpenHands equivalent | AIDE position |
|---|---|---|
| **DEA** (digital-engineering / digital-thread provenance) | Event-stream log + per-conversation history; no FK-linked lifecycle traceability schema | *AIDE ahead* — DEA's digital-thread provenance (cf. the Hermetic `Eidolon` PLM chain) is a modeled lifecycle, not an append-only run log |
| **OrdSA** (O0–O6 ordinal authority) | (not addressed — cloud RBAC roles only) | **AIDE ahead** — authority altitudes / authority-down-evidence-up are absent; RBAC is flat access control, not ordinal authority |
| **MxM** (5-surface harness) | V1 SDK component model: `Agent` (CodeAct logic) + `Runtime` (sandbox) + `Conversation` + interface layer | *In flight elsewhere* — a comparable harness decomposition, but mission/morals/memory are not first-class surfaces (see synthesis) |
| **OAgents** (typed agent envelope + behavioral-trust layer, §10 "above any framework") | `Agent(llm, tools=[...])` — an ad-hoc construction interface, no schema-first behavioral envelope | **AIDE ahead** — OpenHands has *no* trust/behavioral-envelope layer; this is the exact gap OAgents §10 names |

### Against the six AEON service planes (Inference = 7th, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md))

| AEON plane | OpenHands equivalent | AIDE position |
|---|---|---|
| **Identity** | Cloud GitHub/GitLab account integration; no principal-altitude identity for the AI-aide itself | *AIDE behind* — OpenHands integrates with enterprise VCS identity in a shipping product; *but ahead* on a principled AI-aide-principal model ([ADR-EA-0017](../../../../decisions/ADR-EA-0017-ai-aide-principal-altitudes.md)) |
| **Authority** | Cloud RBAC + permissions; sandbox containment | **AIDE ahead** — OrdSA O0–O6 ordinal authority has no counterpart; RBAC ≠ authority altitude |
| **Evidence** | Event-stream (action/observation log); SWE-bench eval harness | *In flight elsewhere* — strong run-trace + a real eval discipline; AIDE's evidence trail is emit-only spec, so *AIDE behind* on realized eval/trace tooling |
| **Integration** | MCP support; broad `Tool` + Skills marketplace ecosystem | *AIDE behind* — mature, shipping, community-extended integration breadth |
| **Capability composition** | `Agent` + `Tool` list + Skills (keyword-triggered / permanent / org / global) | *In flight elsewhere* — real composition, but no **envelope-refinement** composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | Pluggable Runtime (Local / Docker / Remote) + Agent Server; cloud scale-out | **AIDE behind** on realized runtime — this is OpenHands' specialty and it is shipping at scale |

*(Inference plane, ADR-EA-0015: OpenHands is model-agnostic at the `LLM` config level — any provider/model — but model-agnosticism is an implementation convenience there, not a first-class **governance** property the way the Inference plane frames it.)*

### Vocabulary collision

- OpenHands **`Agent`** = the CodeAct execution unit (an `LLM` + `Tool`s). When OpenHands docs/marketing call the whole running coding assistant an "agent," that referent is the canon's **AI-aide** (an AI system acting under a principal, per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) — **not** the OAgents `Agent` (a *typed object* inside a behavioral envelope). Flag both senses on read.
- OpenHands **`Tool`** = atomic invocation (`TerminalTool`, `FileEditorTool`, …) — convergent with the canon's **Tool** across the field.
- OpenHands **`Skill`** (formerly **microagent**) = a prompt/knowledge package (permanent-context, keyword-triggered, organization, global) that conditions AI-aide behavior — this maps to MxM **Means** (tradecraft/method packaging injected into the harness), *not* to a capability primitive. The V0→V1 `microagents`→`Skills` rename is itself a moving target.
- **`RemoteRuntime` "fleet-scale"** in OpenHands docs means *container scale-out*; do **not** read it as the Ologos fleet or NG-AIDE-01 — no bare "fleet" cross-wiring.

## 4. Classification

**Mixed — "in flight elsewhere," at a different altitude — and the *closest comparator to the canon's Hermetic exemplar*.** OpenHands and aide-canon are different categories (a **build-and-run coding-AI-aide substrate** vs a **governance/architecture corpus**), so classification is per-axis:

- **AIDE ahead** — Authority (OrdSA O0–O6 vs flat RBAC), the behavioral-trust **envelope** (OAgents §10 names *exactly* this class of framework as one whose execution-time behavioral trustworthiness is out of scope — OpenHands has no envelope at all), deontic constraints (MxM Morals), digital-thread provenance (DEA), and a principled AI-aide-principal identity model (ADR-EA-0017).
- **AIDE behind** — realized sandboxed **runtime** (Local/Docker/Remote — OpenHands' specialty, shipping at scale), **integration** breadth (MCP + skills marketplace), **evidence/eval** (a real SWE-bench discipline + event-stream traces vs AIDE's emit-only spec), and — decisively — **adoption, contributor base, and the fact that it is a 75k-star shipping product** where aide-canon is design-first research with enforcement largely unbuilt.
- **In flight elsewhere** — the **harness shape** itself (V1 SDK's `Agent`/`Runtime`/`Conversation` decomposition ↔ MxM's surfaces) and capability composition (skills + tools ↔ AEON Composition / the workflow-orchestration pattern).

**Synthesis — they compose, not compete, and OpenHands is the survey-side mirror of Hermetic.** OpenHands is the autonomous-coding-AI-aide harness aide-canon would govern *from above*: OpenHands supplies the Means/runtime (CodeAct in a sandbox), Skills map to MxM Means, and `Tool`s are atomic capability — while OAgents' envelope + OrdSA authority + MxM Morals + DEA provenance supply the trust/governance the framework structurally lacks. Critically, the canon already has a *resident* coding-harness exemplar — **Hermetic** (tracked at [`../../exemplar-tracking/hermetic/`](../../exemplar-tracking/hermetic/), Pattern B+ AEON reference impl with an L0–L3 ordinal-escalation hierarchy and an `Eidolon` digital-thread). Hermetic is the canon's *exemplar* (proof AIDE's claims realize operationally); **OpenHands is the external SOTA comparator that bounds how far ahead/behind that exemplar is.** Where Hermetic instantiates OrdSA-lineage authority and a digital-thread, OpenHands has neither — confirming the *AIDE-ahead-on-governance* axis. Where OpenHands has a 75k-star adoption curve and a shipping eval/runtime, Hermetic does not — confirming the *AIDE-behind-on-adoption/runtime* axis. The MxM contrast is the sharpest: OpenHands' `Agent`/`Runtime`/`Conversation` is a *capability* harness; MxM's mission/morals/memory surfaces make it a *governance* harness — the same altitude gap the whole survey turns on.

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance lead).** OpenHands is the highest-adoption autonomous-coding harness with *no* authority altitude and *no* behavioral envelope — the canonical OAgents §10 case made concrete on the OSS side. **KR shape:** a documented "govern-an-OpenHands-AI-aide" mapping — OAgents envelope + OrdSA O0–O6 authority + MxM Morals wrapped over a CodeAct-in-sandbox runtime — published as the companion to the Hermetic exemplar mapping.
2. **Catch-up (runtime + eval).** OpenHands' sandboxed runtime and SWE-bench eval discipline are materially ahead of AIDE's design-first runtime/evidence spec. **KR shape:** stand up an AIDE-governed exemplar on a sandboxed coding runtime and demonstrate event-stream-grade traceability + a reproducible eval against a named benchmark (cf. the workflow-orchestration shared evidence object and OTel-GenAI evidence shape).
3. **Converge-or-differentiate (harness shape).** OpenHands' V1 SDK component model converges toward MxM's harness decomposition without its governance surfaces. **KR shape:** position MxM as the governing 5-surface spec over CodeAct-class harnesses — convergent on the `Agent`/`Runtime`/`Conversation` mechanics, differentiated by mission/morals/memory as first-class surfaces a capability harness omits.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Inherits the canon AI-aide / OAgents-Agent / Tool / Skill↦Means vocabulary discipline ([ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)). Cross-references the Hermetic exemplar ([`../../exemplar-tracking/hermetic/`](../../exemplar-tracking/hermetic/)) as the resident coding-harness counterpart. Revisit on the next OpenHands SDK shift (V0→V1 rename still settling) or at OKR refresh.
