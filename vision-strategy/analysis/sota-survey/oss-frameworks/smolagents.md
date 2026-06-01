# OSS framework — smolagents (Hugging Face)

> SOTA-survey finding. Shape per [`../README.md`](../README.md) → [`sota-survey/README.md`](../../sota-survey/README.md). Mapping anchor per the oss-frameworks README (constructs **+** the six AEON service planes — wider than the vendor-stacks anchor). Cadence: **fast** (weekly-to-monthly point releases; treat version specifics as a dated snapshot).

## 1. What it is

**smolagents** is Hugging Face's deliberately *minimal* open-source agent library — "a barebones library for agents that think in code." Its design thesis is radical smallness: the core agent logic fits in roughly a thousand lines (`agents.py`), with abstractions kept "to their minimal shape above raw code." It ships two agent classes: **`CodeAgent`** — the signature primitive, in which the AI-aide writes its action as an executable **Python code snippet** rather than emitting a structured JSON tool call — and **`ToolCallingAgent`**, the conventional JSON/text tool-calling style for cases where that paradigm is preferred. Capability is supplied through **`Tool`** (a callable with schema metadata) and **`ToolCollection`** (aggregates tools, importable from MCP servers, LangChain, or Hub Spaces). It is model-agnostic (`InferenceClientModel`, `LiteLLMModel`, `OpenAIModel`, `TransformersModel`, et al.), modality-agnostic (text/vision/video/audio), and Hub-integrated (`push_to_hub` / `from_hub`). Code-as-action is its bet: the maintainers report it reaches goals in ~30% fewer steps than JSON tool-calling because Python's native composability (function nesting, loops, conditionals) collapses multi-step reasoning into one action.

In aide-canon terms smolagents is a **Means-layer substrate at the smallest possible altitude** — and explicitly so by design. It supplies an execution loop and a code action space and **leaves governance entirely to the integrator**: there is no identity, authority, trust-envelope, or deontic layer in the library, and that omission is a *deliberate virtue* (minimalism, not a deficiency), not an oversight to be scored as a gap.

## 2. Source links

- Repo: [`github.com/huggingface/smolagents`](https://github.com/huggingface/smolagents) — ~27.7k stars at survey time; latest release **v1.26.0 (2026-05-29)**.
- Docs: [`huggingface.co/docs/smolagents`](https://huggingface.co/docs/smolagents) (guided tour, `CodeAgent`/`ToolCallingAgent` reference, secure-code-execution tutorial, multi-agent tutorial).
- Package: [`pypi.org/project/smolagents`](https://pypi.org/project/smolagents/).
- Launch framing: [Introducing smolagents](https://huggingface.co/blog/smolagents) (Hugging Face blog) — the "agents that write actions in code" thesis.
- In-canon prior research: the framework `Agent`/`Skill`/`Tool` vocabulary discipline in [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md); this entry inherits that map.

## 3. Map against AIDE

### Table A — against the AIDE constructs

| AIDE construct | smolagents equivalent | AIDE position |
|---|---|---|
| **DEA** (digital-engineering / corpus-as-artifact governance) | none — smolagents is a runtime library, not a governance corpus | **AIDE ahead** — different altitude; DEA has no counterpart here |
| **OrdSA** (O0–O6 ordinal authority, authority-down/evidence-up) | none — no authority concept; all calls run with the integrator's ambient privilege | **AIDE ahead** — authority altitudes are absent by design |
| **MxM** (5-surface harness: mode/mission/mind/morals/methods + means) | the agent class itself is a single, thin Means surface; no mind/morals/methods/mission surfaces | **AIDE ahead** on harness completeness — smolagents is *Means only* |
| **OAgents** (typed agent envelope + trust layer "above any framework", §10) | `CodeAgent`/`ToolCallingAgent` are runtime objects, not envelope-typed; no behavioral-trust contract | **AIDE ahead** on envelope/trust — smolagents is exactly the "framework whose execution-time trustworthiness is outside its scope" OAgents §10 names |

### Table B — against the six AEON service planes

| AEON plane | smolagents equivalent | AIDE position |
|---|---|---|
| **Identity** | none — agents have no principal identity (Hub sharing is artifact identity, not a runtime principal) | **AIDE ahead** — no principal-altitude identity model |
| **Authority** | none — no authorization layer; sandbox limits *what code can touch*, not *what authority the aide holds* | **AIDE ahead** — OrdSA O0–O6 has no counterpart |
| **Evidence** | step logs + optional OpenTelemetry instrumentation for tracing (third-party observability backends) | *In flight elsewhere* / *AIDE behind* on **realized** tracing tooling, ahead on evidence-up *governance* framing |
| **Integration** | broad and mature — MCP servers, LangChain tools, Hub Spaces, any LiteLLM-reachable model | **AIDE behind** on realized integration breadth |
| **Capability composition** | **code-as-action** — Python control flow (nesting/loops/conditionals) composes tool calls natively; multi-agent via managed/sub-agents | *In flight elsewhere* — a genuinely strong, distinct composition model; but no **envelope-refinement** composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | the `run()` loop + sandboxed executors (E2B / Modal / Blaxel / Docker; `LocalPythonExecutor` is explicitly *not a security boundary*) | *In flight elsewhere* — a real, shipping runtime; **AIDE behind** on realized, adopted runtime |

*(Inference is AEON's 7th plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md): smolagents is model-agnostic at the integration level, but model-agnosticism is not framed as a first-class **governance** property the way the Inference plane is.)*

### Vocabulary-collision note

smolagents' usage is mostly low-collision precisely because it is small. **`Tool`** = atomic callable invocation — convergent with the canon's `Tool` and the field at large. The informal **"agent"** (as in `CodeAgent`) is the casual sense the canon forbids for an AI-under-principal; in canon prose this is the **AI-aide** ([ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)), and it is **not** the OAgents `Agent` primitive (a typed object inside a behavioral envelope). **Critically, smolagents has no `Skill` primitive at all** — there is nothing to map onto MxM **Means**; the canon vocabulary map records the *absence* (where LangChain's `Skill` ↦ Means, smolagents simply has no such surface — capability is `Tool` plus raw Python). No conflation arises with the Ologos operator deployment or NG-AIDE-01; "agent" here is a library class, not a fleet member.

## 4. Classification

**Mixed — and emphatically at a different altitude**, even more so than the heavier frameworks. smolagents is the *smallest credible Means substrate*: an execution loop + a code action space, with governance left, by deliberate design, to whoever integrates it. So the classification is per-axis:

- **AIDE ahead** — Authority (OrdSA: none here), behavioral envelope / trust (OAgents §10: smolagents is the textbook "execution-trust-is-out-of-scope" library), harness completeness (MxM: smolagents is Means-only), identity, and corpus-level governance (DEA). On the entire envelope/authority/evidence-governance axis the gap is **clear and wide** — but this is the framework *agreeing* with the canon's division of labor, not losing a contest it entered.
- **AIDE behind** — realized runtime (sandboxed executors that exist and run today), integration breadth (MCP/LangChain/Hub/LiteLLM), observability tooling (OTel-instrumented tracing vs the canon's emit-only evidence spec), and — decisively — **adoption and the fact that it ships** (~27.7k stars, active releases) where AIDE is design-first with enforcement largely unbuilt.
- **In flight elsewhere** — the **code-as-action capability model** is the genuinely interesting axis and the one worth watching: `CodeAgent` proposes Python-as-action-space as a *better composition primitive* than JSON tool-calls. This overlaps AEON Capability-composition / Orchestration-runtime and the workflow-orchestration pattern, and it is a live design direction AIDE should explicitly position against rather than dismiss.

**The synthesis:** they **compose, not compete** — the relationship is even cleaner than with larger frameworks because smolagents makes *no* governance claim. aide-canon is precisely the layer one wraps *around* a smolagents deployment: OAgents' envelope + OrdSA authority + MxM Morals supplying the identity/authority/trust that smolagents intentionally omits, with `CodeAgent`'s code action space as the Means/runtime underneath. This is the OAgents §10 thesis at its most literal — a ~1000-line runtime that *is* the "any framework" the trust layer sits above — mirroring the canon-spec ↔ platform-substrate relationship already documented with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/). The one place to engage on the *merits* (not just altitude) is whether code-as-action changes how the envelope-refinement composition law must be expressed when the action space is arbitrary Python rather than discrete typed calls.

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance lead, cleanest case).** Use smolagents as the *canonical minimal substrate* in the "trust layer above any agent framework" argument — a ~1000-line runtime with zero governance is the sharpest possible illustration of OAgents §10. KR shape: a documented "govern-a-smolagents-deployment" mapping (OAgents envelope + OrdSA authority + MxM Morals wrapped around a `CodeAgent`), reusable as the reference small-substrate integration.
2. **Converge-or-differentiate (code-as-action capability model).** Decide and document AIDE's stance on the code-as-action paradigm: does the envelope-refinement composition law ([ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md) / [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) hold when the action space is arbitrary Python? KR shape: an ADR or pattern note that either constrains code-as-action under the composition law or differentiates explicitly.
3. **Catch-up (evidence tooling, shared with the rest of the slice).** smolagents' OTel-instrumented tracing is shipping; AIDE's evidence trail is emit-only spec. KR shape: standardize on OTel-GenAI as the canonical evidence shape (already begun — workflow-orchestration shared evidence object) and demonstrate trace-grade evidence on an AIDE exemplar driving a `CodeAgent`.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Snapshot: smolagents **v1.26.0 (2026-05-29)**, ~27.7k stars. Revisit on a smolagents minor-version shift in the code-execution / multi-agent surface, or at OKR refresh.
