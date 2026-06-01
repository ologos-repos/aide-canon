# OSS framework — Inspect AI (UK AISI evaluation harness)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Cadence: **fast** (Inspect ships frequent point releases — treat version/feature specifics as a dated snapshot). **Governance-adjacent special case:** Inspect is an *evaluation harness*, not an agent-build framework — it does not build AI-aides, it **evaluates** the capability and safety of models and agent systems. It is therefore mapped primarily against the **Evidence plane** and **OAgents conformance testing**, and the central finding is a *catch-up / adopt* opportunity rather than a competition.

## 1. What it is

**Inspect AI** (PyPI `inspect-ai`, GitHub `UKGovernmentBEIS/inspect_ai`) is the open-source (MIT) LLM-evaluation framework built and maintained by the **UK AI Security Institute (AISI)** — a government body — with contributions from Meridian Labs. It is the harness behind nearly all of AISI's own automated evaluations and has been adopted by frontier labs (Anthropic, Google DeepMind, xAI and others) for capability and safety evals. It is mature and actively released (v0.3.233, 2026-06-01 at survey time).

Its architecture is a small, composable set of primitives:

- **Task** — the evaluation unit: binds a `Dataset` + one or more `Solver`s + a `Scorer`.
- **Dataset** — labeled samples, each with an `input` (the prompt) and a `target` (correct answer or grading guidance).
- **Solver** — the Python abstraction that elicits behavior and carries task state to a scorable form: from a plain `generate()` model call up to multi-turn prompt engineering, self-critique, and full agent scaffolding (built-in **ReAct** and **Deep** agents, plus custom).
- **Scorer** — judges whether the solver hit the target, and by how much: text comparison, model-graded, or custom.
- **Tool**, **Sandbox**, **Agent Bridge** — `Tool`s are Python functions a model can call (built-in bash/python/text-editor/web-search/computer, plus MCP); `Sandbox` isolates model-generated code (Docker, Kubernetes, Modal, Proxmox); **Agent Bridge** wraps *external* agents (OpenAI Agents SDK, **LangChain**, PydanticAI) so they run inside Inspect's logging/scoring/observability.

Inspect spans both **capability** evals (coding, agentic tasks, reasoning, knowledge, multi-modal) and **safety/security** evals (e.g. evaluating agents against the OWASP Top 10 for Agentic Applications 2026 — memory poisoning, autonomy hijacking, data exfiltration). The companion `inspect_evals` repo carries 200+ community-contributed evals. In aide-canon terms it is a **Means-layer evaluation substrate** — it measures *what a model/agent does*; it does not confer authority altitude or a behavioral envelope.

## 2. Source links

- Official docs: `inspect.aisi.org.uk` (architecture, [Scorers](https://inspect.aisi.org.uk/scorers.html), agents, Agent Bridge, sandboxing).
- Code + releases: [`github.com/UKGovernmentBEIS/inspect_ai`](https://github.com/UKGovernmentBEIS/inspect_ai) (`CHANGELOG.md`), [`inspect-ai` on PyPI](https://pypi.org/project/inspect-ai/) (v0.3.233, 2026-06-01, MIT).
- Eval corpus: [`github.com/UKGovernmentBEIS/inspect_evals`](https://github.com/UKGovernmentBEIS/inspect_evals) + [Inspect Evals listing](https://ukgovernmentbeis.github.io/inspect_evals/) (200+ evals; AISI + Arcadia Impact + Vector Institute).
- Adjacent AISI work: [Autonomous Systems Evaluation Standard](https://ukgovernmentbeis.github.io/as-evaluation-standard/).
- In-canon adjacency: the OAgents conformance/evidence model in [`OAgents-v1.0 §6`](../../../../constructs/oagents/spec/versions/OAgents-v1.0.md) (evidence-by-artifact, three verification levels) and the shared evidence object in [`patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md).

## 3. Map against AIDE

### Against the four AIDE constructs (DEA / OrdSA / MxM / OAgents)

| AIDE construct | Inspect AI equivalent | AIDE position |
|---|---|---|
| **DEA** (deployable enterprise architecture) | (none — Inspect evaluates artifacts, it does not architect a deployment) | *AIDE ahead* — Inspect is construct-unaware |
| **OrdSA** (O0–O6 authority altitudes) | (none — a `Scorer` measures behavior; it confers no authority) | **AIDE ahead** — authority altitude is outside Inspect's scope entirely |
| **MxM** (5-surface harness) | the `Task`/`Solver`/`Scorer`/`Sandbox` decomposition is a *test* harness, not an *operating* harness | *In flight elsewhere* — comparable rigor of decomposition, orthogonal purpose |
| **OAgents** (typed envelope + conformance) | Inspect is a **candidate engine for the conformance/evidence tier** — Tasks/Scorers can probe behavioral-envelope properties; Agent Bridge can wrap an OAgent | **AIDE behind** on eval-harness maturity; **complementary, not competing** — see §4 |

### Against the six AEON service planes

| AEON plane | Inspect AI equivalent | AIDE position |
|---|---|---|
| **Identity** | (none — Inspect has no principal/identity model) | *AIDE ahead* — out of scope for an eval harness |
| **Authority** | (none) | **AIDE ahead** — OrdSA O0–O6 authority-down/evidence-up is absent |
| **Evidence** | **the core of Inspect** — Tasks/Solvers/Scorers, logs, eval datasets, model-graded scoring, viewer/observability | **AIDE behind** — Inspect is a built, government-grade, adopted eval harness; AIDE's evidence trail is emit-only spec with no harness to *generate or grade* the evidence |
| **Integration** | model providers (OpenAI/Anthropic/Google/xAI/Bedrock/Azure/vLLM/Ollama/…), MCP tools, **Agent Bridge** (LangChain/OpenAI-SDK/PydanticAI) | *In flight elsewhere* — broad, mature provider + agent integration |
| **Capability composition** | `Solver` chains, ReAct/Deep agent scaffolds, `Tool` composition | *In flight elsewhere* — strong; but Inspect composes *to test*, not to enforce an **envelope-refinement** composition law (cf. [`patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | the eval-run loop + `Sandbox` execution (Docker/K8s/Modal/Proxmox) | *In flight elsewhere* — a test-time runtime, not an operating runtime |

*(Inference is AEON's 7th plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md): Inspect is model-provider-agnostic at the integration level — one interface over many providers — but model-agnosticism is a convenience here, not a first-class **governance** property the way the Inference plane frames it.)*

### Vocabulary collision note

Inspect's **`Agent`** is a *test scaffold* — a `Solver` combining planning, memory, and tool use (ReAct/Deep) to drive a longer-horizon task to a scorable state. This is **neither** the canon's **AI-aide** (an AI acting under a principal, per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) **nor** the OAgents **`Agent`** primitive (a typed object inside a behavioral envelope); collapsing them is exactly the casual-"agent" error the canon prohibits — name it an *Inspect Solver/agent-scaffold*. Inspect's **`Tool`** = atomic model-callable function — convergent with the canon's **Tool**. Inspect's **`Solver`/`Scorer`** are Means-layer test tradecraft with no governance-layer counterpart; do not map them to MxM **Means** wholesale (a framework **Skill** maps to Means — a `Scorer` is a measurement device, a different category). Flag on read: the most load-bearing collision is **Evidence** — Inspect *produces and grades* evidence; OAgents *requires* evidence as conformance proof. Same word, two altitudes — and that gap is the opportunity in §4.

## 4. Classification

**Mixed — "AIDE behind on the eval slice; ahead on governance altitude," and the two are complementary.** Inspect is an evaluation harness and aide-canon is a governance corpus — *different categories at different altitudes* — so the classification is per-axis, not global:

- **AIDE ahead** — Authority (OrdSA O0–O6), behavioral envelope / trust layer (OAgents — Inspect measures *whether* a model behaves, it does not *constrain* behavior at runtime or assign an authority altitude), deontic constraints (MxM Morals), and the principal/Identity model. Inspect is, by design, construct-unaware: it has no opinion on who may do what, only on what was done.
- **AIDE behind** — the **evaluation-harness maturity itself**. This is an honest, decisive gap: Inspect is a real, rigorous, government-grade, broadly-adopted eval tool with 200+ ready evals, sandboxed agent execution, and Agent-Bridge ingestion of external agents — exactly the kind of mature specialty tooling that puts AIDE *behind on that slice*. It is the eval-plane analogue of LangSmith on the observability slice (cf. [`../vendor-stacks/langchain.md`](../vendor-stacks/langchain.md) §4): AIDE's evidence story is emit-only spec, with **no harness to generate or grade the evidence** OAgents conformance requires.
- **In flight elsewhere** — integration breadth (providers, MCP, Agent Bridge) and capability-composition (Solver chains / ReAct / Deep agents); convergent test-time mechanics AIDE can consume rather than rebuild.

**The synthesis — adopt, don't compete.** OAgents §6 establishes that conformance is *evidence by observable artifact*, verified at three levels (self-assessment → documented review → third-party 3PAO-style), but the spec names **no harness** to produce, run, or grade that evidence. Inspect is the obvious candidate to fill that hole: an OAgent can be wrapped via **Agent Bridge**, and behavioral-envelope properties (independent output review present? enforcement gate fires? memory staleness detected?) can be encoded as **Tasks/Scorers** and run reproducibly — turning OAgents' Appendix-C checklist into an executable conformance suite. This is the [`feedback_enforcement_not_documentation`] discipline applied to conformance: an eval harness is enforcement, a checklist is documentation. It also gives the OAgents "first realized lattice" the eval harness it currently lacks. Distinguish clearly: **Inspect evaluates the capability/safety of a model or agent; it does not supply authority altitude or a behavioral envelope** — those remain AIDE-distinctive, and Inspect would sit *beneath* them as the conformance-measurement substrate, the same canon-spec ↔ Means-substrate relation the canon documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/).

## 5. Objective implication

Two Doerr-style Objective shapes follow — both *catch-up/adopt*, not compete:

1. **Catch-up by adoption (the headline).** Adopt Inspect AI as the canonical **OAgents conformance / behavioral-envelope eval harness**. *Objective:* make OAgents conformance executable rather than asserted. KR shape: encode the OAgents §6 / Appendix-C MUST-component checks as an Inspect `Task` suite (Scorers for independent-review-present, enforcement-gate-fires, memory-staleness-detected, state-verified-before-assertion), wrap a reference OAgent via Agent Bridge, and produce a graded conformance report on an AIDE exemplar ([Hermetic](../../exemplar-tracking/hermetic/) / [thinx-aidex](../../exemplar-tracking/thinx-aidex/)). This closes the eval-harness gap the way OTel-GenAI adoption closes the observability gap.
2. **Defend-and-extend (governance altitude over the harness).** Articulate that an Inspect score measures behavior but confers neither authority (OrdSA) nor a runtime envelope (OAgents) — position the canon as the governance layer that *consumes* Inspect output (conformance evidence feeds the OrdSA evidence-up trail) rather than being measured by it. KR shape: a documented "evaluate-an-OAgent-with-Inspect" mapping that explicitly bounds what an eval can and cannot certify, keeping authority-altitude and envelope-enforcement on the AIDE side of the line.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Snapshot against Inspect AI v0.3.233 (2026-06-01). Revisit on a major Inspect release (Agent-Bridge / eval-format shifts) or at OKR refresh; pairs with the LangSmith finding in [`../vendor-stacks/langchain.md`](../vendor-stacks/langchain.md) as the two halves of AIDE's Evidence-plane catch-up.
