# ADR-EA-0027 — Introduce workflow-orchestration pattern; specify envelope-composition + the determinism gate-surface

- **Status:** Accepted (ratified 2026-06-01 by JD-Founder; cross-vendor QA passed pre-ratify)
- **Date:** 2026-06-01
- **Author:** OlogosAI (canon-prime, corpus-altitude per ADR-EA-0017)
- **Reviewers:** JD Longmire (Founder ratification, 2026-06-01); cross-vendor QA (Gemini 2.5 Pro, pre-ratify — PASS with NITs); thinx-Claude (peer-AI second opinion — invited post-ratify, canon-altitude trigger)
- **Related issue:** TBD (open for tuning, mirroring the per-pattern tuning-issue convention of ADR-EA-0009 / `aide-canon#7`)
- **Ratification trail:**
  - 2026-06-01 (filed): Filed as `Proposed` alongside the design-gate PR [#45](https://github.com/ologos-repos/aide-canon/pull/45) introducing [`patterns/workflow-orchestration.md`](../patterns/workflow-orchestration.md).
  - 2026-06-01 (QA): Cross-vendor QA via `qa_pr_via_gemini.py` (Gemini 2.5 Pro, observer altitude) returned **PASS with NITs** — 0 BLOCKERs; 1 NIT (premature "ratified" status line on the pattern doc — fixed); 1 NOTE (commended the §5.1-sequencing hygiene). No canon-fidelity, cross-reference, or decision-record findings.
  - 2026-06-01 (ratified): JD-Founder ratified all seven forks as-proposed (F-A … F-G; the leans below are now the accepted decision). Status → `Accepted`. Pattern doc becomes normative. Peer-AI second opinion to thinx-Claude follows post-ratify (canon-altitude trigger), threaded to cross-ai #61.

## Context

The canon names the components of agent orchestration across four decompositions but has no document for the orchestration object itself:

- **OAgents** (`constructs/oagents/`) defines the `Agent` primitive and the behavioral envelope, and its §10 *Related Work* explicitly excludes workflow orchestration from the trust problem: *"OAgents addresses the behavioral governance of judgment-exercising agents, a problem that workflow orchestration does not encounter."* That exclusion is correct for deterministic-step automation (Zapier/Airflow/n8n, the platforms §10 names) but **not** for an orchestration whose steps are themselves judgment-exercising agents.
- **OrdSA** (`constructs/ordsa/`) titles layer **O3** *"Agents and Workflows"* — the primitive has a named home — but the canon never defines what a *workflow* is, how it differs from an `Agent` (O3 peer) or a `Tool` (O4), or where governance attaches when a workflow delegates to spawned agents.
- **AEON** (`enterprise-platforms/aeon/`) gives the **Composition Plane** *"the rules under which agents may chain, delegate, or escalate; capability composability gates"* and a **Meta-Orchestration plane** under O1 — the rules, but not the object that enacts them.
- **MxM** (`constructs/mxm/`) lists MEANS as *"tools, skills, workflows"* — correct altitude (execution substrate), no internal structure.

The Claude Code Workflow feature (a deterministic JS orchestration script that fans out and pipelines sub-agents) operationally enacts a workflow-orchestration pattern — spawning judgment-exercising agents under a deterministic, budgeted, journaled control program — *without the canon having a name for the shape*. As with digital-thread / Hermetic (ADR-EA-0009), naming a pattern an exemplar already enacts lets the canon catch up to its own working evidence.

Two questions the exemplar forces that the canon cannot currently answer:

1. **Does workflow orchestration encounter the OAgents trust problem, and if so, how is it governed?** (The §10 exclusion fails for agent-spawning orchestration.)
2. **Where, structurally, do governance gates attach in an orchestration that mixes deterministic control with probabilistic execution?**

## Decision

### 1. Add `patterns/workflow-orchestration.md` to the `patterns/` tier

A new cross-cutting pattern, peer to digital-thread / prep-pursue-pivot / EIF / GCM / founder-override. It qualifies under all three `patterns/` admission tests: it cuts across tiers/constructs/planes (5M + AEON Composition/Meta-Orchestration/Evidence + OrdSA O2–O3 + OAgents); it has a reference implementation (Claude Code Workflow); it is ADR-ratified (this ADR).

### 2. Name the pattern

**Definition.** A deterministic control program that composes multiple agent invocations into a single governed unit of work — a deterministic, replayable orchestration substrate wrapping probabilistic, judgment-bearing execution. The pattern's normative content (the cross-cutting decomposition, the two contributions, conformance criteria, the reference-impl mapping) lives in the pattern doc.

### 3. Specify envelope-composition (Contribution 1 — answers Context Q1)

A workflow **is** an OAgents `Agent` at orchestration altitude (own envelope, evidence, audit) that instantiates child `Agent`s under the law:

```
envelope(child_agent) ⊑ envelope(orchestrator)
```

A child's envelope is always a refinement (⊆ permissions, ⊇ gates) of the orchestrator's; orchestration may narrow authority, never broaden it. This yields no-escalation-by-orchestration, evidence aggregation along the digital thread, and gate inheritance. This **closes the OAgents §10 gap**: workflow orchestration *does* encounter the trust problem, and the refinement lattice is the canon's answer.

### 4. State the determinism gate-surface principle (Contribution 2 — answers Context Q2)

*In any orchestration, governance gates attach to the deterministic control layer; judgment is exercised only within gated steps.* Corollary: governance logic inside a probabilistic agent call is unreliable-by-construction — lift it to the deterministic layer (resource ceilings throw; output conformance is schema-validated with retry; authority checks gate the spawn).

### 5. Conformance: behavioral (required) + schema (recommended) + interface (optional)

Matches the ADR-EA-0009 conformance shape. Five behavioral criteria (deterministic orchestration, envelope refinement, gate-at-the-deterministic-layer, evidence aggregation, bounded resource envelope); schema-level descriptor + invocation + operator + journal recommendations; optional structured-output contract + OTel-mappable observability stream.

### 6. Register Claude Code Workflow as a named exemplar

New tracking subfolder `vision-strategy/analysis/exemplar-tracking/claude-code-workflow/`, added to the exemplar-tracking index. The exemplar realizes Contribution 2 fully and Contribution 1 partially (per-agent model/tool/schema refinement is conventional, not an enforced subset-lattice) — the gap is documented in the pattern doc as the canon-motivating delta.

### 7. Cross-tier updates landed alongside

- `patterns/README.md` — index row for workflow-orchestration.
- `vision-strategy/analysis/exemplar-tracking/README.md` — named-exemplars row for Claude Code Workflow.

## Consequences

**Positive:**
- Closes a real, named gap in OAgents (§10's exclusion is wrong for agent-spawning orchestration) with a precise, composable answer.
- Gives OrdSA's O3 "Agents and Workflows" and AEON's Composition Plane a defined orchestration object instead of an unfilled title.
- The determinism gate-surface principle is a reusable design rule across the canon (Morals, GCM, OrdSA authority placement).
- Build-pointability: a system prompted to "orchestrate agents safely" now has a documented pattern + a working exemplar.

**Negative / risk:**
- **OAgents-spec coupling.** Contribution 1 proposes an extension to OAgents' trust model. It lands here as a *pattern-level* contribution that **references** OAgents; it does **not** edit the OAgents NIST standard. Absorbing envelope-composition into an OAgents spec revision is a separate step gated by Micah Longmire's co-authorship (per [ADR-EA-0008](ADR-EA-0008-reframe-corpus-authorship.md)) and is explicitly out of scope for this ADR.
- **§5.1 ontology not yet ratified.** The Tool/Skill/Workflow primitive distinction is in-flight (ng-aide-01 PR #59 §5.1; deferred to a post-ratification PURSUE-2 pass per the canon hygiene audit). This ADR *defines* the Workflow primitive and feeds §5.1; it does not edit the vocabulary map ahead of that ratification.
- The exemplar's partial realization of Contribution 1 means the canon currently leads its own exemplar on the envelope lattice — acceptable (digital-thread led Hermetic on O5/O6), tracked in the exemplar folder.

**Neutral:**
- Additive only; no tier renamed, no construct restructured. ADR-EA-NNNN continuity holds (0027 follows 0026 Methods-surface).

## Alternatives considered

1. **Place under AEON Composition Plane** (`enterprise-platforms/aeon/composition/workflow-orchestration.md`). Rejected — same cross-cutting reasoning as ADR-EA-0009 Option B: the pattern touches MORALS (gates), MEMORY (journal), METHODS (tradecraft), OAgents (envelope), and OrdSA (O3) simultaneously; subordinating it to one plane undersells it.
2. **Extend the OAgents construct directly** (new section in the OAgents spec). Rejected for now — triggers the Micah co-authorship gate (ADR-EA-0008) and couples a one-document pattern to a standards-revision cycle. The pattern references OAgents externally; OAgents may absorb envelope-composition later via its own authored revision.
3. **Promote Workflow to a standalone construct.** Rejected — a workflow is a recurring shape that emerges when OAgents/OrdSA/AEON are deployed together, not a methodological surface of its own. Category error (cf. ADR-EA-0009 Option D).
4. **Defer until §5.1 ontology ratifies.** Rejected — the §5.1 work needs the Workflow *definition* this pattern supplies; sequencing the pattern first feeds the ontology rather than blocking on it. The pattern marks its §5.1-feeding status explicitly.
5. **Behavioral-only conformance (no envelope-refinement requirement).** Rejected — without criterion 2 (envelope refinement) the pattern would permit privilege-escalation-by-orchestration, which is precisely the trust failure the pattern exists to prevent.

## Ratified decisions (forks — all ratified as-proposed 2026-06-01; held open for later tuning)

All seven forks were **ratified as-proposed** by JD-Founder on 2026-06-01. The leans below are now the accepted decision; they remain documented here as the canonical record and stay open for later tuning per the `aide-canon#7`-style convention if an exemplar or downstream impl surfaces cause.

1. **Placement (F-A).** *Lean:* `patterns/` tier (this ADR). Alt: AEON Composition Plane / OAgents extension.
2. **Envelope-composition semantics (F-B).** *Lean:* refinement lattice `envelope(child) ⊑ envelope(parent)` (intersection of constraints). Alt: inheritance-only (no per-step tightening) / per-agent-independent envelopes.
3. **Is a workflow an OAgents `Agent`? (F-C).** *Lean:* yes — a workflow is an `Agent` at orchestration altitude that orchestrates `Agent`s. Alt: a workflow is a distinct non-agent primitive that *references* agents.
4. **Determinism-principle altitude (F-D).** *Lean:* state it in the pattern + cross-reference MORALS. Alt: elevate to a standalone cross-construct principle / a separate mini-pattern.
5. **§5.1 ontology timing (F-E).** *Lean:* define the Workflow primitive here and mark it as feeding §5.1; do **not** edit the vocabulary map until §5.1 ratifies. Alt: ratify the Tool/Skill/Workflow vocab-map rows as part of this PR.
6. **ng-aide-01 instance (F-F).** *Lean:* defer to a follow-on `ADR-NGAIDE` for a runtime workflow-orchestration capability after this pattern ratifies (canon→instance, mirroring GCM). Alt: scope the instance capability in parallel now.
7. **Conformance level (F-G).** *Lean:* behavioral-required + schema-recommended + interface-optional (matches digital-thread). Alt: behavioral-only.

## Related

- [`patterns/workflow-orchestration.md`](../patterns/workflow-orchestration.md) — the pattern doc (this ADR's normative content)
- [ADR-EA-0009](ADR-EA-0009-introduce-digital-thread-pattern.md) — pattern-tier precedent + conformance-shape precedent
- [ADR-EA-0026](../constructs/mxm/decisions/ADR-EA-0026-introduce-methods-surface.md) — METHODS surface (orchestration tradecraft home)
- [ADR-EA-0017](ADR-EA-0017-ai-aide-principal-altitudes.md) — corpus-altitude authorship of this ADR
- [ADR-EA-0008](ADR-EA-0008-reframe-corpus-authorship.md) — Micah co-authorship gate on OAgents-spec revisions (bounds Consequence/risk above)
- OAgents NIST standard: `constructs/oagents/spec/oagents-nist-standard-v16.0.md` (§10 trust-boundary exclusion this pattern addresses)
- OrdSA: `constructs/ordsa/docs/layers/O3-agents-workflows.md` (the O3 home of the primitive)
- ng-aide-01 PR #59 §5.1 — in-flight Tool/Skill/Workflow/Capability/Envelope ontology this pattern feeds
- cross-ai discussion #61 — o-qa-agent / MxM Q&A; the OAgents-evidence convergence seam shared with this pattern
