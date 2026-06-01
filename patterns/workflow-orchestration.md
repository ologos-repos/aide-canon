# Workflow-orchestration pattern

> **Status:** Proposed (introduced by [ADR-EA-0027](../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md) — itself pending JD-Founder ratification; this pattern doc is normative only once ADR-EA-0027 is Accepted)

## Summary

A **deterministic control program that composes multiple agent invocations into a single governed unit of work.** The control flow — sequencing, fan-out, iteration, branching, resource ceilings — is deterministic and replayable; the work *inside* each step is delegated to judgment-exercising agents. A workflow is therefore two layers in one object: a deterministic **orchestration substrate** (auditable, gate-able, replayable) wrapping probabilistic **execution** (the agent calls).

The pattern names what OrdSA's O3 layer already titles *"Agents and **Workflows**"*, what AEON's **Composition** and **Meta-Orchestration** planes operationally produce, and what MxM's MEANS surface lists alongside tools and skills — and it specifies the one thing none of those decompositions yet answer: **how a behavioral envelope composes when one orchestration spawns many agents.**

## Why this pattern exists

The canon names the pieces but not the shape:

- **OAgents** names the `Agent` primitive (a typed object with a behavioral envelope, evidence emission, audit trail) — but the OAgents standard §10 explicitly places *workflow orchestration* outside its trust problem: *"OAgents addresses the behavioral governance of judgment-exercising agents, a problem that workflow orchestration does not encounter."* That exclusion holds for Zapier/Airflow-style automation, where the steps are deterministic functions. It does **not** hold for an orchestration whose steps are themselves judgment-exercising agents. A workflow that spawns agents inherits exactly the trust problem OAgents was built for.
- **OrdSA** titles O3 *"Agents and Workflows"* and routes authority down / evidence up through it — but the canon has no document for what a *workflow* is, how it differs from an agent (O3 peer) and a tool (O4), or where governance attaches when the workflow delegates.
- **AEON's Composition Plane** owns *"the rules under which agents may chain, delegate, or escalate; capability composability gates"* — a workflow is a concrete Composition-Plane mechanism, but the plane describes the rules, not the orchestration object that enacts them.
- **MxM's MEANS** surface lists *"tools, skills, workflows"* as the execution surface — placing workflow at the right altitude (execution substrate, not governance) but saying nothing about its internal structure.

This pattern closes the gap. It is extracted from a working reference implementation (Claude Code's Workflow feature; see below), in keeping with the `patterns/` tier rule that a pattern names a recurring shape that an exemplar already enacts.

## The pattern is cross-cutting (the central claim)

A workflow is **not a single-slot canon object.** Its parts distribute across the 5M surfaces, the AEON planes, OrdSA's layers, and OAgents' primitives. The decomposition below is normative — it states *which canon construct each workflow element enacts*:

| Workflow element | What it is | Canon home (enacted) |
|---|---|---|
| **Orchestration program** (the control flow + its descriptor) | deterministic sequencing/fan-out/iteration spec | AEON **Meta-Orchestration** plane · MxM **MEANS** · OrdSA **O2/O3** orchestrator |
| **Agent invocation** (spawn a sub-agent for a step) | instantiation of a judgment-exercising worker | OAgents **`Agent`** primitive · OrdSA **O3** agent |
| **Composition operators** (pipeline / parallel / loop / nest) | rules under which agents chain, delegate, iterate | AEON **Composition Plane** (composability gates) |
| **Structured output** (forced typed result per step) | schema-validated deliverable from a step | OAgents **evidence emission** · digital-thread **artifacts** |
| **Resource ceiling** (token / agent-count / time budget) | a hard, deterministically-enforced limit | MxM **MORALS** (deontic constraint) · OrdSA authority-envelope bound |
| **Journal / replay** (run identity + cached prefix) | durable, resumable record of the run | MxM **MEMORY** · canon **[digital-thread](digital-thread.md)** |
| **Progress + observability** (phases, narrator log) | step-level evidence of execution | AEON **Evidence Plane** · OTel GenAI `invoke_workflow` / `invoke_agent` spans |
| **Isolation** (per-agent sandbox for parallel mutation) | execution-substrate boundary | MxM **MEANS** (substrate) |
| **Orchestration tradecraft** (adversarial-verify, judge-panel, loop-until-dry, completeness-critic) | codified best-practice for *how* to orchestrate well | MxM **METHODS** ([ADR-EA-0026](../constructs/mxm/decisions/ADR-EA-0026-introduce-methods-surface.md)) |

The pattern is the object that binds these into one governed unit. The two contributions below are the parts the canon does not already have.

## Contribution 1 — Workflow as an envelope-composition operator (normative)

This is the pattern's load-bearing claim and the part that closes the OAgents §10 gap.

**Claim.** A workflow *is itself* an OAgents `Agent` operating at orchestration altitude — it has its own behavioral envelope, emits evidence, and carries an audit trail. It instantiates child `Agent`s. The governing rule for that instantiation is **envelope refinement**:

```
envelope(child_agent)  ⊑  envelope(orchestrator)
```

A spawned agent's envelope is always a **refinement** of the orchestrator's: a subset of its permissions and a superset of its gates. A workflow may *narrow* authority for a step (fewer tools, a cheaper model, a tighter output schema, a stricter gate) but may **never broaden** a child's authority beyond what the orchestrator itself holds.

Three guarantees follow, and together they are what makes orchestration *governable* rather than an escalation vector:

1. **No privilege escalation by orchestration.** You cannot spawn an agent that does what the orchestrator could not. Composition strictly contracts authority; it never expands it. (This is AEON's Composition-Plane *composability gate*, made precise.)
2. **Evidence aggregation along the digital thread.** Each child emits OAgents evidence; the orchestrator's evidence record is the parent into which the children's evidence FK-links. An orchestration produces one [digital-thread](digital-thread.md) with the orchestrator as the task/phase parent and each agent invocation as a child artifact + audit entry.
3. **Gate inheritance.** Pre-execution and post-execution gates on the orchestrator apply to every child by default; a child step may add gates but cannot remove inherited ones.

The short form: **a workflow is an agent that orchestrates agents under envelope refinement.** That single sentence is the canon's answer to "does workflow orchestration encounter the trust problem?" — yes, and the answer is the refinement lattice.

## Contribution 2 — The determinism boundary is the gate-attachment surface (principle)

**Principle.** *In any orchestration, governance gates attach to the deterministic control layer; judgment is exercised only within gated steps.*

A workflow cleanly separates a **deterministic layer** (the control program: sequencing, fan-out, iteration, budget arithmetic, schema validation, audit emission — all reproducible given the same inputs and the same agent outputs) from a **probabilistic layer** (the agent calls — where judgment happens). The principle says:

- **Gates live in the deterministic layer.** Pre-execution authorization, post-execution verification of a step's (schema-validated) result, resource ceilings, and audit/evidence emission are all enforced deterministically, in the control program — *before* and *after* an agent call, never inside it.
- **Judgment lives in the gated layer.** The probabilistic agent call is *what* gets gated, never *where* the gate is.

**Corollary (a design rule).** Any governance logic placed *inside* a probabilistic agent call is unreliable-by-construction — the model may or may not honor it on any given run. Lift it to the deterministic layer. Concretely: a hard token ceiling must throw in the control program (not be a polite instruction in a prompt); output conformance must be validated against a schema with retry (not requested in prose); authority checks must gate the spawn (not be asked of the spawned agent).

This connects directly to MxM **MORALS** (gates are deontic constraints, and constraints you cannot reliably enforce are not constraints), to **[governed-context-management](governed-context-management.md)** §1–§7 (deterministic, harness-owned mechanisms are the reliable ones), and to OrdSA (authority gates belong at the orchestrator's altitude, not delegated into the executing agent).

## Canon-vocabulary mapping

How the pattern connects to existing canon concepts. AIDE vocabulary is the canon's source of truth; external terms map *to* it per the [AIDE vocabulary map](../vision-strategy/analysis/aide-vocabulary-map.md).

| Workflow concept | Canon mapping (AIDE-canonical) |
|---|---|
| **Workflow** (the primitive) | OrdSA **O3** *"Agents and Workflows"* — the workflow is the orchestration object at O3; distinct from a **Tool** (atomic invocation, O4 / MEANS) and a **Skill** (temporally-extended instructional procedure, MEANS). Feeds the in-flight §5.1 ontology (see ADR-EA-0027 §Open-for-tuning). |
| **Orchestrator** | AEON **Meta-Orchestration plane**; an OAgents `Agent` at orchestration altitude |
| **Composition operators** | AEON **Composition Plane** composability gates |
| **Envelope refinement** (`⊑`) | OAgents **behavioral envelope** + AEON Composition-Plane escalation rules — the composition law (Contribution 1) |
| **Structured-output step** | OAgents **evidence emission**; digital-thread **artifact** |
| **Resource ceiling** | MxM **MORALS** gate |
| **Journal / replay** | MxM **MEMORY**; digital-thread **audit-log** parent |
| **Determinism boundary** | the gate-attachment principle (Contribution 2); MxM **MORALS** / GCM §1–§7 |

The pattern is the *vertical slice* that binds these horizontal decompositions for one orchestrated unit of work — the orchestration analogue of what [digital-thread](digital-thread.md) does for one piece of work.

## Conformance criteria

### Behavioral conformance (required)

An implementation is **workflow-orchestration-conformant** if and only if all of the following hold:

1. **Deterministic orchestration.** The control flow (sequencing, fan-out, iteration, branching) is deterministic and replayable: given the same inputs and the same agent outputs, it issues the same sequence of agent invocations. (A journal/resume mechanism that returns cached prior-run results is the canonical evidence of this.)
2. **Envelope refinement.** Every spawned agent runs under an envelope that refines — never relaxes — the orchestrator's: `envelope(child) ⊑ envelope(parent)`. No orchestration-induced privilege escalation. An impl MUST document how it bounds a child's authority to a subset of the orchestrator's.
3. **Gate-at-the-deterministic-layer.** Pre-execution authorization, post-execution verification, and resource ceilings are enforced in the deterministic control layer, not delegated to the judgment of spawned agents.
4. **Evidence aggregation.** The orchestration emits an audit/evidence record, and each spawned agent's evidence links to it (digital-thread parent ← child). An orchestration is not a black box: per-step evidence is recoverable.
5. **Bounded resource envelope.** The orchestration runs under a declared, deterministically-enforced resource ceiling (token, agent-count, and/or wall-clock budget). Unbounded fan-out is not conformant.

### Schema-level recommendations (interop)

Implementations that follow these interoperate at the descriptor level; divergence is still conformant if the behavioral criteria hold.

- **Orchestration descriptor:** `name`, `description`, declared `phases`/stages (a pure-literal metadata block, resolvable before the run).
- **Agent-invocation shape:** per-step `label`, `phase`, optional `schema` (structured-output contract), optional `model` / `isolation` overrides.
- **Composition operators:** named `pipeline` (per-item staged, no barrier), `parallel` (barrier), and bounded iteration (loop-until-condition with a declared cap).
- **Journal record:** `(invocation, inputs, result)` per step, keyed by a run identifier, sufficient to replay an unchanged prefix.

### Interface conformance (optional)

- A **structured-output contract** validated at the orchestration boundary (JSON Schema, validated with retry-on-mismatch — a deterministic-layer gate, per Contribution 2).
- A **progress / observability stream** emitting phase + step events that map to OTel GenAI `invoke_workflow` (orchestration span) and `invoke_agent` / `execute_tool` (child spans).

## Reference implementation: Claude Code Workflow

**Implementation:** the Workflow feature of Claude Code (Anthropic) — a tool that executes a deterministic JavaScript orchestration script which fans out and pipelines sub-agents. It is the canon's **named exemplar** for this pattern (tracking subfolder: [`vision-strategy/analysis/exemplar-tracking/claude-code-workflow/`](../vision-strategy/analysis/exemplar-tracking/claude-code-workflow/)).

| Pattern element | Claude Code Workflow primitive |
|---|---|
| Deterministic orchestration | the JS script + pure-literal `meta` (name/description/phases) |
| Agent invocation | `agent(prompt, opts)` — spawns an ephemeral sub-agent; `opts.schema` forces a validated structured output (evidence emission) |
| Composition operators | `pipeline(items, ...stages)` (per-item, no barrier), `parallel(thunks)` (barrier), loop-until-dry / loop-until-budget |
| Structured output | `schema` (JSON Schema) — validated at the tool layer with model retry on mismatch |
| Resource ceiling | `budget {total, spent(), remaining()}` — `agent()` **throws** once `spent()` reaches `total` (deterministic-layer gate) |
| Journal / replay | `runId` + `resumeFromRunId` — longest unchanged prefix returns cached results; same script + same args → 100% cache hit |
| Progress + observability | `phase(title)` / `log(message)` — progress groups + narrator lines |
| Isolation | `isolation: 'worktree'` — fresh git worktree per agent for parallel file mutation |
| Orchestration tradecraft | documented patterns: adversarial-verify, judge-panel, loop-until-dry, multi-modal-sweep, completeness-critic |
| Resource safety bounds | concurrency cap `min(16, cores−2)`; lifetime agent cap (runaway backstop) |

**Honest conformance gap (tracked).** The exemplar realizes Contribution 1 only *partially*: it refines a child's **model**, **tools** (via `agentType`), and **output schema** per invocation, and it enforces the resource ceiling deterministically — but it does **not** yet enforce a formal `envelope(child) ⊑ envelope(parent)` lattice (e.g. a permission set that is provably a subset of the orchestrator's). The refinement is conventional, not enforced. This is exactly the kind of exemplar-motivates-the-canon gap the `patterns/` tier exists to surface (cf. Hermetic's O5/O6 conflation under [digital-thread](digital-thread.md)): the exemplar demonstrates the shape and names what it does not yet guarantee. Contribution 2 (gate-at-the-deterministic-layer) is fully realized — `budget` throws, schema validation retries, concurrency is capped — all in the control program.

**Alternative implementations are explicitly welcome.** The pattern does not constrain implementations to JavaScript, to sub-agent-spawning, or to Claude Code's specific API. Behavioral conformance is the bar; the schema and interface recommendations are starting points.

## Related

- **Constructs:** [OAgents](../constructs/oagents/) (the `Agent` primitive + behavioral envelope this pattern composes; §10 trust-boundary gap this pattern closes) · [OrdSA](../constructs/ordsa/) (O3 "Agents and Workflows"; authority-down/evidence-up the orchestration carries) · [MxM](../constructs/mxm/) (MEANS lists workflows; MORALS holds the gates; METHODS holds the orchestration tradecraft; MEMORY holds the journal)
- **Platforms:** [AEON](../enterprise-platforms/aeon/) (Composition + Meta-Orchestration + Evidence planes the pattern enacts)
- **Patterns:** [digital-thread](digital-thread.md) (the orchestration emits one; orchestrator = parent, agent invocations = children) · [governed-context-management](governed-context-management.md) (deterministic harness-owned mechanisms — same reliability argument as Contribution 2) · [prep-pursue-pivot](prep-pursue-pivot.md) (the governance gradient an orchestration applies per step)
- **Vocabulary:** [AIDE vocabulary map](../vision-strategy/analysis/aide-vocabulary-map.md) — Tool / Skill / Workflow distinction (feeds §5.1 ontology)
- **Exemplar:** [`exemplar-tracking/claude-code-workflow/`](../vision-strategy/analysis/exemplar-tracking/claude-code-workflow/)
- **Standards external mapping:** OTel GenAI semantic conventions (`invoke_workflow` / `invoke_agent` / `execute_tool` span taxonomy) — the observation-layer corroboration that workflow ≠ agent ≠ tool
