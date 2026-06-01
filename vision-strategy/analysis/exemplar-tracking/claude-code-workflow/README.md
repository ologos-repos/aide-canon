# claude-code-workflow/

Tracking the **Claude Code Workflow** exemplar — the orchestration feature of Anthropic's Claude Code agent harness: a tool that executes a deterministic JavaScript orchestration script which spawns, fans out, and pipelines sub-agents under a budgeted, journaled control program.

## Exemplar role

Claude Code Workflow is the canon's **reference implementation of the [workflow-orchestration pattern](../../../../patterns/workflow-orchestration.md)** ([ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)).

| Role | Anchor |
|---|---|
| **Workflow-orchestration reference implementation** | [ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md) + [`patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md) — deterministic JS orchestration over agent invocations, with structured-output evidence, deterministic resource ceilings, and run-journaled replay |

This is an **out-of-tree** exemplar: Claude Code is Anthropic's product, on its own release cycle. The canon cites its observable behavior as the conformance reference, the way Hermetic is cited for digital-thread — citation, not ownership.

## Cross-construct touch-points

The workflow-orchestration pattern is cross-cutting; the exemplar instantiates pieces of multiple constructs at once:

| Construct / plane | Claude Code Workflow counterpart | Position |
|---|---|---|
| **OAgents** `Agent` + behavioral envelope | `agent(prompt, {schema})` spawns a child agent; `schema` forces a validated structured output (evidence emission) | Partial — child model/tools/schema are refined per spawn, but no enforced `envelope(child) ⊑ envelope(parent)` subset-lattice yet (see gap below) |
| **AEON Composition Plane** | `pipeline` / `parallel` / loop-until-dry composition operators | Solid — direct enactment of "rules under which agents chain, delegate, iterate" |
| **AEON Meta-Orchestration plane** | the orchestration script + pure-literal `meta` | Solid |
| **AEON Evidence Plane** | `phase()` / `log()` progress + the run journal | Solid — maps to OTel GenAI `invoke_workflow` / `invoke_agent` spans |
| **MxM MORALS** | `budget {total, spent(), remaining()}` — `agent()` throws at ceiling | Solid — deterministic-layer resource gate (pattern Contribution 2, fully realized) |
| **MxM MEMORY** | `runId` + `resumeFromRunId` (longest unchanged prefix cached) | Solid — journaled replay; digital-thread parent record |
| **MxM METHODS** | documented orchestration tradecraft (adversarial-verify, judge-panel, loop-until-dry, multi-modal-sweep, completeness-critic) | Solid |
| **MxM MEANS** | `isolation: 'worktree'` per-agent sandbox | Solid |

## Conformance assertions

Against the six behavioral criteria in [`patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md) (criteria sharpened by the 2026-06-01 thinx refinement):

1. **Deterministic orchestration** — ✅ `resumeFromRunId` returns cached results for the unchanged prefix; same script + same args → 100% cache hit. Date/random are blocked in scripts precisely to preserve replay determinism.
2. **Per-limb envelope refinement** — ⚠️ **partial.** Per-spawn refinement of model (`opts.model`), tools (`opts.agentType`), and output (`opts.schema`) is supported and conventional, but the harness does not *enforce* a child's authority as a provable subset on every limb — in particular post-execution verification is not held at-least-as-strong. This is the canon-motivating gap (see below).
3. **Multi-level closure** — ⚠️ **partial.** Nesting is one level by construction (`workflow()` inside a child throws), which sidesteps deep recursion, but the harness does not enforce transitive `⊑` for the nesting it does allow.
4. **Gate-at-the-deterministic-layer** — ✅ `budget` throws in the control program; schema validation retries at the tool layer; concurrency is capped at `min(16, cores−2)`; a lifetime agent cap backstops runaway loops.
5. **Evidence aggregation (enforced FK)** — ⚠️ **partial.** Per-agent transcripts + the run journal are recoverable and structured-output schemas make per-step evidence machine-readable, but `parent_evidence_id` / `orchestration_run_id` and the gate-decision record are not enforced fields — aggregation is recoverable-by-convention, not FK-guaranteed.
6. **Bounded resource envelope** — ✅ token budget (`budget.total`), concurrency cap, and lifetime agent cap.

## The canon-motivating gap

The exemplar realizes **Contribution 2** (determinism gate-surface) fully but **Contribution 1** (envelope-composition lattice) only partially: refinement of a child's model/tools/schema is *by convention*, not enforced as `envelope(child) ⊑ envelope(parent)`. The canon currently **leads** its exemplar here — the same situation digital-thread had with Hermetic's O5/O6 conflation. This is the intended function of exemplar tracking: the exemplar demonstrates the shape and surfaces exactly what a conformant implementation would need to add (a checkable subset-lattice on spawned-agent authority).

## Tracking artifacts to maintain

| File | Purpose |
|---|---|
| `milestones.md` (TBD) | Workflow-feature capability changes that affect conformance (e.g., if Anthropic adds enforced per-agent permission scoping → criterion 2 upgrades) |
| `signals.md` (TBD) | Observable signals — adoption in Ologos workflows, ng-aide-01 instance work, downstream citation |
| (this README) | Current state + conformance assertions (updated when the feature's governing behavior shifts) |

## Cadence

Track when Claude Code's Workflow capability materially changes (especially anything that closes the envelope-refinement gap), and when the ng-aide-01 instance ADR (per ADR-EA-0027 fork F-F) lands.

## Status

Scaffolding established 2026-06-01 alongside ADR-EA-0027 (design-gate). Conformance assertions are against the Workflow tool behavior as of that date; revisit on feature change.
