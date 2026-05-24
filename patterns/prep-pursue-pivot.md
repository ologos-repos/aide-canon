# Prep-Pursue-Pivot pattern

> **Status:** Proposed (ratified by [ADR-EA-0012](../decisions/ADR-EA-0012-introduce-prep-pursue-pivot-pattern.md))

## Summary

A three-faculty model of governed agent cognition across the lifecycle of a single piece of work: **prep** (before action — research, plan, decompose), **pursue** (during action — drive toward the objective under a decoupled evaluator), **pivot** (at the inflection — a governed decision to stay the course or change it). The three are a *before / during / after* triad, and each carries a distinct **governance posture**, which is what makes the pattern AIDE-native rather than a generic agent loop.

The pattern names what an agentic system does *cognitively* as it works, and binds each faculty to the canon's governance: prep's plan-approval is the [HCAE](../foundation/hcae/) human-curation moment, pursue's decoupled evaluator is [OrdSA](../constructs/ordsa/) evidence-up, and pivot is where OrdSA's authority modes are *exercised* — a human-or-policy decision at the moment of change. The work the triad operates on is a two-tier hierarchy of **milestones** (macro) decomposed into **inchstones** (micro); the inchstone trail is the orchestration layer of the [digital-thread](digital-thread.md).

## Why this pattern exists

The canon describes the agentic control plane *structurally* — AEON's six service planes, OrdSA's ordinal layers, MxM's governing surfaces. It does not name the **temporal cognitive loop** an agent runs *as it does a piece of work*: how it thinks before acting, how it drives while acting, and how it changes course after learning. Production agent platforms run some version of this loop; naming it lets the canon govern it.

Crucially, the pattern's value is not the loop itself (every agent framework has one) but the **governance gradient** mapped onto it. An ungoverned agent loop is a liability under [AIDK](../foundation/aidk/) (AI is structurally unreliable). The prep-pursue-pivot pattern places a human-curation or policy decision at each load-bearing inflection, so the loop is auditable and steerable — HCAE made operational in the runtime.

## The triad (normative)

| Faculty | Phase | What it does | Governance posture |
|---|---|---|---|
| **prep** | before | Research the problem; produce a structured plan; decompose the plan into trackable **inchstones**. | **Approve** — the plan passes a human-curation gate before execution tools unlock (HCAE front gate). |
| **pursue** | during | Drive toward the stated objective across turns; burn down the inchstones; a **separate evaluator**, in its own context, judges whether the completion condition holds and feeds reasons back. | **Bounded autonomy** — the agent acts autonomously toward the objective, but an evidence-up evaluator (decoupled from the actor) gates "done." |
| **pivot** | after / at inflection | Surface a decision point — *stay the course or change it* — informed by consolidated experience; resolve it by human choice or by policy; revise the inchstones accordingly. | **Governed decision** — resolved by human curation *or* by pre-declared autonomy rules; dialable per deployment. |

### Behavioral conformance (required)

An implementation is prep-pursue-pivot-conformant if:

1. **prep gate.** Before write/effecting actions execute, the system produces an inspectable plan and decomposition (inchstones), and a principal (human or policy) can approve, refine, or reject it. Plan-then-act, not act-then-explain.
2. **pursue evaluator decoupling.** The judgment of whether the objective is met is made by an evaluator that is *separate from the actor's reasoning context* (a distinct model invocation / context window), so completion is not self-certified. The evaluator's verdict + reason is recorded.
3. **pivot as governed decision.** When the system detects a course-change inflection (objective unmet, recurring failure, changed conditions), it does not silently self-modify its course or its durable memory. It either (a) surfaces the decision for human resolution, or (b) self-resolves strictly within pre-declared autonomy rules, escalating outside them. The decision and its resolver are recorded.
4. **work hierarchy.** Work is tracked as **milestones** (macro, cross-session) decomposed into **inchstones** (micro, session-level, status-tracked). Inchstone state changes are emitted as evidence.
5. **evidence.** Every gate (prep approval, pursue verdict, pivot decision) and every inchstone state change emits to an audit record (the digital-thread).

### The governance gradient

```
   prep            pursue             pivot
   ────            ──────             ─────
   APPROVE         BOUNDED AUTONOMY   GOVERNED DECISION
   (human gate     (act, but a        (human-choose OR
    before          decoupled judge    policy-authorized
    execution)      gates "done")      self-pivot; dialable)

   HCAE front      OrdSA evidence-up   OrdSA authority modes,
   gate            evaluation          exercised at the inflection
```

The autonomy is *not* uniform across the loop. prep is human-gated by default; pursue runs autonomously within the approved plan; pivot's autonomy is **dialable** — crank it down and every course-change surfaces to a human (full HCAE); open it up and the agent self-pivots within declared bounds and only escalates at the edges. This dial is set per deployment, per classification, per operator-trust level.

### pivot's three modes (the authority model, exercised)

pivot is where [OrdSA](../constructs/ordsa/)'s authority modes get used inside the cognitive loop:

| Mode | Form | OrdSA mode |
|---|---|---|
| **Surfaced decision** | *"Here's what we're pursuing — stay the course or pivot?"* | request upward → principal decides (HCAE curation) |
| **Collaborative pivot** | *"This didn't work — how shall we pivot?"* | escalate to oracle; principal steers the new direction |
| **Bounded autonomous pivot** | self-pivot within declared autonomy rules; escalate outside them | receive downward authorization / execute-within-scope |

The "autonomy rules" are the Morals/Authority policy that decides which pivots are pre-authorized vs. which must escalate — the same envelope OrdSA defines, applied to the act of changing course.

### Milestones and inchstones

| Tier | Scope | Tracked in |
|---|---|---|
| **Milestone** | Macro objective, cross-session | Backlog / issues / the VSOK Objectives |
| **Inchstone** | Micro step, session-level, status-tracked (pending → in-progress → done) | The agent's live work decomposition (the "todo" surface) |

prep decomposes a milestone into inchstones; pursue burns the inchstones down (objective-met ≈ inchstones-done); pivot revises them at the inflection. The inchstone is the unit of legibility — a human can curate at inchstone granularity, not just at the whole-plan level (fine-grained HCAE). The inchstone trail is the orchestration layer of the digital-thread.

## Reproducibility and source concepts

The three faculties are reproductions of publicly-documented mechanisms, renamed and unified under the AIDE governance gradient. Honest provenance:

| Faculty | Source concept (publicly documented) | Reproducibility |
|---|---|---|
| **prep** | Claude Code *plan mode* (read-only research → structured plan → approval gate) + the *todo* task-list / decomposition mechanism | **High** — mechanism is simple + documented; reimplementable against any reasoning-capable model |
| **pursue** | Claude Code `/goal` (session-scoped stop-hook loop + transcript-only evaluator + reason-feedback) and Managed-Agents *Outcomes* (rubric + separate-context grader) | **High** — the evaluator-decoupling pattern is documented; reproducible with a worker + a cheap judge model |
| **pivot** | Managed-Agents *Dreaming* (between-session memory consolidation / experiential self-evolution, with a "review before changes land" gate). Nearest open reference: *sleep-time compute* (arXiv 2504.13171, open repo) | **Low–medium** — the *idea* reproduces; the consolidation/decision internals are unpublished. The **governance wrapper** (the curation gate + autonomy dial + drift/poisoning safeguards) is the part AIDE designs and owns. |

The AIDE contribution is not the underlying mechanisms (those are public) but **the governance gradient, the pivot-as-governed-decision framing, the milestone/inchstone work hierarchy, and the binding to HCAE / OrdSA / digital-thread.** The intended AIDE reference implementation is NG-AIDE-01 (forthcoming).

## Conformance levels

- **Behavioral** (required) — the five properties above. This is what determines whether a system is prep-pursue-pivot-conformant.
- **Schema** (recommended) — the milestone/inchstone two-tier work record; inchstone status states (pending/in-progress/done); the evidence event shape for gates + state changes.
- **Interface** (optional) — not specified; the pattern does not require a particular API between faculties, only the behavioral gates.

## Related

- **Foundation:** [AIDK](../foundation/aidk/) (why the governance gradient is necessary — AI is structurally unreliable) → [HCAE](../foundation/hcae/) (prep's approval gate + pivot's curation are the human-curation moments). [RLEG](../foundation/rleg/) and pivot's experiential self-improvement are sibling answers to "how the agent stays calibrated" — RLEG at training time, pivot at runtime/between-sessions.
- **Constructs:** [OrdSA](../constructs/ordsa/) (pivot exercises the authority modes; pursue's evaluator is evidence-up). [MxM](../constructs/mxm/) (prep ↔ Mind, pursue ↔ Means/runtime, pivot ↔ Memory + Morals).
- **Enterprise-platforms:** [AEON](../enterprise-platforms/aeon/) (prep → Mind/Orchestration; pursue → Orchestration Runtime + evaluator; pivot → Memory + Authority planes; all gates → Evidence). [AIDEX](../enterprise-platforms/aidex/) (the surface where pivot decisions are presented to the operator).
- **Patterns:** [digital-thread](digital-thread.md) (the inchstone trail + the gate decisions are the digital-thread's orchestration + review + audit layers for a working session).
