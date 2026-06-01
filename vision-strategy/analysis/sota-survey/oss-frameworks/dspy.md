# OSS framework — DSPy (declarative LM programming)

> SOTA-survey finding. Shape per [`./README.md`](./README.md) → [`sota-survey/README.md`](../README.md). Cadence: **fast** (DSPy ships frequently; optimizer roster and the 3.x API surface move release-to-release — treat version specifics as a dated snapshot).

## 1. What it is

**DSPy** (*Declarative Self-improving Python*, Stanford NLP — led by Omar Khattab with Chris Potts and Matei Zaharia) is **not an agent framework**; it is a **declarative programming model for language models**. You write the *what* — a **Signature** (a typed input→output spec for a task) — wrap it in a **Module** that fixes the *how-to-reason* (`Predict`, `ChainOfThought`, `ReAct`, `ProgramOfThought`, `MultiChainComparison`, `Parallel`) — and then **compile** the program against a metric using an **Optimizer** (historically "teleprompter"): `BootstrapFewShot`, `MIPROv2` (instruction + few-shot proposal/search), and `GEPA` (Genetic-Pareto reflective prompt evolution). The optimizer *synthesizes and tunes the actual prompts (and optionally weights)* so that the human stops hand-authoring prompt strings. In aide-canon terms DSPy is **architecturally adjacent** to a harness rather than a harness itself: it governs *one slice of cognition* — how an LM call is specified, composed, and systematically optimized — and supplies **no** identity, authority, evidence-trail, or trust machinery. Its load-bearing contribution to the survey is the **compile/optimize discipline**: prompt-engineering recast as a *codified, measurable, repeatable method* rather than artisanal string-tweaking.

DSPy is materially mature for its specialty: a 3.x line (the `3.x` series brought native reasoning-model support, a typed/provider-neutral LM boundary, `BetterTogether` optimizer chaining, and a refreshed `ReAct`), six-figure monthly downloads, MIT-licensed, and named production use at Cursor, Databricks, and Mistral. GEPA in particular has a peer-reviewed footing (arXiv 2507.19457, ICLR 2026 oral) and ships both as `dspy.GEPA` and as a standalone `gepa` library.

## 2. Source links

- Official: `dspy.ai` (docs, `dspy.ai/learn/optimization/optimizers/`, `dspy.ai/roadmap/`), GitHub `github.com/stanfordnlp/dspy` (+ `/releases`), standalone optimizer `github.com/gepa-ai/gepa`.
- Papers: "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines" (arXiv 2310.03714); "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning" (arXiv 2507.19457, Agrawal et al., ICLR 2026 oral).
- (Version/optimizer roster is release-prone — verify the current 3.x surface and the optimizer list at read time.)

## 3. Map against AIDE

DSPy is narrower than a full harness, so most rows are *not addressed* by DSPy — that is the honest shape, not a defect. Two rows light up brightly (MIND, METHODS).

### Table (a) — against the four AIDE constructs

| AIDE construct | DSPy equivalent | AIDE position |
|---|---|---|
| **DEA** (deployable enterprise architecture) | (DSPy doesn't address — it is a per-task programming model, not an enterprise architecture) | *AIDE ahead* — no architectural altitude in DSPy |
| **OrdSA** (O0–O6 ordinal authority) | (none — DSPy has no authority concept; a compiled program runs with whatever the caller grants) | **AIDE ahead** — authority-down/evidence-up is absent from DSPy |
| **MxM** (5-surface harness: Mode·Mind·Morals·Memory·Methods) | DSPy populates **Mind** (declarative reasoning spec) + **Methods** (systematic prompt-optimization as codified tradecraft); silent on Mode, Morals, Memory | **Split** — *AIDE behind* on the Methods/Mind *prompt-optimization tooling slice*; *AIDE ahead* on the other three surfaces and on harness coherence |
| **OAgents** (typed agent envelope / trust layer) | (none — a DSPy `Module` is a typed *program*, not a behavioral envelope with trust semantics) | **AIDE ahead** — OAgents §10 places envelope/trust *above any framework*; DSPy is exactly such a framework |

### Table (b) — against the six AEON service planes (Inference = 7th, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md))

| AEON plane | DSPy equivalent | AIDE position |
|---|---|---|
| **Identity** | (none — DSPy programs carry no principal identity) | **AIDE ahead** — no identity primitive in DSPy |
| **Authority** | (none) | **AIDE ahead** — OrdSA authority altitudes have no DSPy analogue |
| **Evidence** | Optimizer traces + metric scores + optional MLflow logging during compilation (an *eval/optimization* trail, not a runtime governance trail) | *In flight elsewhere* — DSPy has real compile-time evidence for optimization; AIDE's runtime evidence-trail spec addresses a different (governance) purpose |
| **Integration** | Provider-neutral LM boundary (3.x typed request/response; LiteLLM decoupling in progress); tool calls via `ReAct` | *In flight elsewhere* — DSPy's model-portability boundary is real and converging with the Inference-plane framing |
| **Capability composition** | Module composition (Modules nest into programs; `BetterTogether` chains optimizers) | *In flight elsewhere* — genuine composition, but no **envelope-refinement** composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | (minimal — `ReAct`/`Parallel` give intra-program control flow; no durable/scaled orchestration runtime) | **AIDE ahead** on orchestration-as-governed-plane; DSPy is below that altitude |

*(Inference, AEON's 7th plane per ADR-EA-0015: DSPy's typed provider-neutral LM boundary is squarely in this territory and is one of its stronger, fast-moving surfaces — but model-portability is an engineering property in DSPy, not a first-class **governance** property the way the Inference plane frames it.)*

### Vocabulary-collision note

DSPy's vocabulary is mostly **non-colliding**, which makes it a clean comparator — but three terms need discipline:

- DSPy **`Module`** = a typed, composable *program unit* (a `Predict`/`ChainOfThought`/`ReAct` instance). This is **not** MxM's "M" surfaces and **not** the OAgents **`Agent`** primitive (a typed object inside a behavioral envelope). Keep "Module" scoped to the DSPy programming model.
- DSPy has **no first-class "Agent"** — when DSPy material says "agentic," it means an LM-call program (often a `ReAct` loop), an *AI-aide* program slice under whatever principal invokes it ([ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)); never use the casual bare "agent" for an AI-under-principal.
- DSPy **`Tool`** (a callable handed to `ReAct`) = atomic invocation — convergent with the field and with the canon's `Tool`.
- DSPy's **optimization discipline** (Signatures + optimizers as a *systematic method*) maps to MxM **Methods** (tradecraft) — i.e. DSPy's "Skill"-equivalent contribution is a **Means/Methods** artifact, not a governance one.

This is a comparator framework, not an Ologos-ecosystem or NG-AIDE-01 entity; no fleet conflation applies.

## 4. Classification

**Mixed — "different altitude, mostly orthogonal," with one sharp catch-up slice.** DSPy is a *programming model*, aide-canon is a *governance corpus*; they barely overlap except at MxM **Mind/Methods**, where DSPy is genuinely strong.

- **AIDE ahead** — everything governance: DEA architecture altitude, OrdSA **Authority** (O0–O6), OAgents **envelope/trust** (OAgents §10 names exactly this gap — behavioral trustworthiness is *outside a framework's scope*), MxM **Morals/Mode/Memory**, Identity, and orchestration-as-governed-plane. DSPy has *no harness and no governance* — it is a programming model, by design.
- **AIDE behind** — the **systematic prompt-optimization tooling slice** of MxM **Methods** (and the **Mind** reasoning-spec slice). DSPy's compile-against-a-metric discipline — `Signatures` → `Modules` → `MIPROv2`/`GEPA` optimizers that *automatically synthesize and tune prompts* — is mature, peer-reviewed (GEPA, ICLR 2026), and production-adopted. The canon codifies prompt rigor as *practice/method narrative*; it has **no executable optimizer-grade tooling** that compiles and measurably improves prompts. On that slice, AIDE is honestly behind.
- **In flight elsewhere** — Evidence (compile-time optimization traces), Integration (provider-neutral LM boundary), Capability composition (Module/optimizer chaining). These converge with AEON planes without occupying the same governance purpose.

**The synthesis:** DSPy and aide-canon **compose, not compete** — and the composition is *complementary at different altitudes*. DSPy is a tool a governed AI-aide would *use* to author and optimize the LM-call internals of a Means-layer Method; aide-canon supplies the envelope, authority, identity, and deontic layer DSPy structurally omits. The clean read: **adopt DSPy's compile/optimize discipline into the canon's Methods surface** (the prompt-optimization slice is the one place SOTA tooling clearly leads), while DSPy validates — by its total absence of governance — the OAgents §10 thesis that trust must live *above any framework*.

## 5. Objective implication

Two Doerr-style Objective shapes follow (the split mirrors the split classification):

1. **Catch-up (Methods / prompt-optimization tooling).** DSPy's optimizer discipline is materially ahead of the canon's narrative treatment of prompt rigor. KR shape: codify a "compile-and-optimize" Method in the MxM **Methods** surface ([ADR-EA-0026](../../../../constructs/mxm/decisions/ADR-EA-0026-introduce-methods-surface.md)) that adopts a Signature-style typed task spec + a metric-driven optimization loop (DSPy or `gepa`-class), and demonstrate it producing a measurably improved prompt artifact on an AIDE exemplar — turning prompt tradecraft from prose into an executable, gated method (cf. [`feedback_enforcement_not_documentation`]).
2. **Defend-and-extend (governance lead).** DSPy is the cleanest possible example of a powerful framework with *zero* governance surface — propagate the OAgents-envelope + OrdSA-authority + MxM-Morals position as the layer that wraps *around* a DSPy-authored Method. KR shape: a documented "govern-a-DSPy-program" mapping (envelope + authority + Morals over a compiled DSPy Module), parallel to the govern-a-LangChain-deployment mapping and the [Hermetic](../../exemplar-tracking/hermetic/) / [thinx-aidex](../../exemplar-tracking/thinx-aidex/) canon-spec ↔ substrate relationship.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). DSPy version/optimizer surface is release-prone (3.x line, GEPA/MIPROv2 current at survey time) — revisit on the next DSPy major release, on a new optimizer paradigm, or at OKR refresh.
