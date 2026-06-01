# OSS framework — CrewAI

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md), mapped against the AIDE-construct + AEON-plane anchor in [`README.md`](README.md). Cadence: **fast** (CrewAI ships weekly point releases — treat version/star specifics as a dated snapshot, not a fixed spec).

## 1. What it is

**CrewAI** is an open-source, role-based multi-agent orchestration framework — a lean Python library, **built from scratch and explicitly independent of LangChain** (the maintainers stress it is not a LangChain wrapper). Its organizing metaphor is a *crew*: you describe AI-aides the way you'd staff a human team — each with a **role**, a **goal**, and a **backstory** — assign them **Tasks**, and run them under a **Process**. Two complementary execution surfaces compose the framework:

- **Crews** — collections of role-bearing AI-aides that reason, delegate, and self-correct toward task outputs, run under a **Process** that is `sequential` (linear) or `hierarchical` (a manager AI-aide delegates to workers).
- **Flows** — an event-driven, lower-level orchestration layer for "massive complexity": deterministic, observable, context-aware chains that can invoke Crews natively. Post-1.0 these are positioned as the production-grade control surface.

The framework ships hundreds of built-in tools, a memory subsystem, native tracing, a unified CLI (local-dev → deploy), and first-class **MCP** integration. OSS 1.0 went GA **2025-10-20** (Crew/Flow APIs locked for long-term compatibility); as of this survey it is at v1.14.x. It is, in aide-canon terms, a **Means-layer implementation substrate** — a build-and-run library for composing AI-aides — the altitude aide-canon explicitly is *not*. A separate commercial **CrewAI AMP / Enterprise** tier (control plane, RBAC, audit trails, telemetry, on-prem) sits above the OSS framework; **this entry surveys the OSS framework only** and mentions AMP solely to bound scope.

## 2. Source links

- Official: `crewai.com`, `docs.crewai.com` (incl. `docs.crewai.com/en/changelog`), GitHub `github.com/crewAIInc/crewAI`, blog `blog.crewai.com` (OSS 1.0 GA announcement, 2025-10-20).
- Maturity signals at survey time: ~52.6k GitHub stars, ~318 contributors; maintainers cite 12M+ daily agent executions in production. Treat exact counts as dated.
- In-canon prior research: the SOTA-vocabulary discipline and `Agent`/`Skill`/`Tool` mapping in [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md); the LangChain peer entry [`../vendor-stacks/langchain.md`](../vendor-stacks/langchain.md) (same anchor, sibling finding).
- (Star/version/contributor numbers move weekly — verify at read time.)

## 3. Map against AIDE

### Against the four AIDE constructs (DEA / OrdSA / MxM / OAgents)

| AIDE construct | CrewAI equivalent | AIDE position |
|---|---|---|
| **MxM** (5-surface harness) | Agent definition (role/goal/backstory) + Crew/Process config — Mission/Persona expressed as prose role+backstory; no Morals/Memory/Methods surfaces as first-class governance | *In flight elsewhere* — comparable decomposition (role ↦ Mission, backstory ↦ Persona), but no 5-surface governance contract |
| **OAgents** (typed agent envelope + trust layer) | CrewAI `Agent` (role-bearing executor); memory subsystem; no behavioral-envelope / execution-trust contract | **AIDE ahead** — OAgents §10 names frameworks of this class as ones whose execution-time trustworthiness is out of scope; CrewAI has the agent *object*, not the typed envelope |
| **OrdSA** (O0–O6 ordinal authority) | (CrewAI does not address authority altitudes; `hierarchical` Process is task-delegation, not principal-authority layering) | **AIDE ahead** — authority-down/evidence-up across O0–O6 is absent |
| **DEA** (deontic / evidence architecture) | Native tracing + logging (observability); no deontic constraint model | *In flight elsewhere* on evidence trace; **AIDE ahead** on deontic governance |

### Against the six AEON service planes

| AEON plane | CrewAI equivalent | AIDE position |
|---|---|---|
| **Identity** | AI-aides have role/goal/backstory but no principal-altitude identity; no enterprise identity in OSS tier | *In flight elsewhere* — role-as-identity exists, no principal model |
| **Authority** | `hierarchical` Process (manager delegates to workers) — task delegation, not authority | **AIDE ahead** — OrdSA O0–O6 has no CrewAI analogue |
| **Evidence** | Native tracing, deterministic logging, observation handling | **AIDE behind** — CrewAI's trace is built + shipping; AIDE's evidence trail is emit-only spec |
| **Integration** | Hundreds of built-in tools, custom tools, first-class MCP, sandbox tools (E2B/Daytona) | *In flight elsewhere* — broad, mature |
| **Capability composition** | Crews + Tasks + Process; Flows compose Crews | *In flight elsewhere* — strong composition; but no **envelope-refinement** composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | Crew runner + Flows (event-driven, deterministic) | **AIDE behind** on realized runtime; *converging* via the workflow-orchestration pattern |

*(Inference is AEON's 7th plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md): CrewAI is model-provider-agnostic at the integration level, but model-agnosticism is not a first-class **governance** property the way the Inference plane frames it.)*

### Vocabulary collision

CrewAI's **`Agent`** = "an AI entity with a role, goal, and backstory that executes Tasks" — this is the canon's **AI-aide** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)), **not** the OAgents `Agent` primitive (a typed object inside a behavioral envelope). Never carry CrewAI's casual `Agent` into canon prose for an AI-under-principal — use **AI-aide**. CrewAI's **role + backstory** map to MxM **Mission / Persona**; **Crew + Process** map to orchestration (the workflow-orchestration pattern), **not** to a governance surface. CrewAI **`Task`** is an atomic work item with an expected output, and **`Tool`** is an atomic invocation (convergent across the field). CrewAI has no `Skill` primitive; were one introduced it would map to MxM **Means**. These collisions are flagged here and inherit the discipline of the vocabulary map.

## 4. Classification

**Mixed — "in flight elsewhere," at a different altitude.** This is the load-bearing finding, and it parallels the LangChain finding: aide-canon and CrewAI are *different categories* — a **governance/architecture corpus** vs an **OSS build-and-run library** — so the classification is per-axis, not global:

- **AIDE ahead** — Authority (OrdSA O0–O6; CrewAI's `hierarchical` Process is delegation, not authority), behavioral envelope / execution trust (OAgents §10 names this framework class explicitly as lacking execution-time trust governance), deontic constraints (MxM Morals), and vendor-neutral conformance criteria. CrewAI gives you a *crew of AI-aides*; it does not give you the envelope that makes their execution governable.
- **AIDE behind** — realized orchestration runtime (Crew runner + Flows), observability/evidence (native tracing is built and shipping where AIDE's is emit-only spec), integration breadth (hundreds of tools + MCP), and — decisively — **adoption, contributor base, and the fact that it is a shipping product at 12M+ daily executions** where AIDE is design-first research with enforcement still largely unbuilt.
- **In flight elsewhere** — orchestration mechanics (Crew/Process/Flows ↔ AEON Capability-composition + Orchestration-runtime + the workflow-orchestration pattern); integration/capability breadth; role-as-identity.

**The synthesis:** they **compose, not compete**. aide-canon is the governance layer one would wrap *around* a CrewAI deployment — Crews/Flows as the Means/runtime, native tracing as the Evidence plane — with OAgents' envelope + OrdSA authority + MxM Morals supplying the trust/governance the framework structurally lacks. CrewAI's role/goal/backstory are a *prose* sketch of what MxM makes a contracted harness surface; the canon's value is turning that sketch into a governed, authority-layered, deontically-constrained envelope. This is the OAgents §10 thesis made concrete — the same canon-spec ↔ platform-substrate relationship the canon documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/).

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance lead).** Propagate the OAgents-envelope / OrdSA-authority position as the trust layer that sits *above any agent framework* — CrewAI is a second canonical example (alongside LangChain) of a popular, mature OSS substrate with no such layer, and its prose role/backstory model makes the gap legible. KR shape: a documented "govern-a-CrewAI-crew" mapping (envelope + OrdSA authority + MxM Morals over Crews/Flows; role/backstory ↦ Mission/Persona).
2. **Catch-up (evidence + runtime).** CrewAI's native tracing and Flows runtime are materially ahead of AIDE's emit-only evidence spec and unbuilt runtime. KR shape: adopt OTel-GenAI as the canonical evidence shape (already begun — see the workflow-orchestration shared evidence object) and demonstrate trace-grade evidence on an AIDE exemplar that a CrewAI Flow would produce natively.
3. **Converge-or-differentiate (orchestration).** Position the **workflow-orchestration pattern** ([ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)) as the governing spec over Crew/Process/Flows-class runtimes — convergent on orchestration mechanics, differentiated by the envelope-refinement composition law CrewAI does not enforce, and by authority-down/evidence-up that its `hierarchical` Process does not model.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Inherits the LangChain peer-entry anchor and the canon vocabulary-map discipline. Scope is the **OSS framework**; the commercial CrewAI AMP / Enterprise tier is noted but not surveyed here. Revisit on the next major CrewAI release (fast cadence) or at OKR refresh.
