# ADR-EA-0012 — Introduce the prep-pursue-pivot agent-cognition pattern

- **Status:** Proposed
- **Date:** 2026-05-23
- **Author:** JD Longmire (framing + naming: prep / pursue / pivot, the governance gradient, pivot-as-governed-decision, inchstones; drafted by OlogosAI)
- **Reviewers:** @ologos001 (canon prime), Micah Longmire, Tracy Norrell
- **Related:** [`patterns/prep-pursue-pivot.md`](../patterns/prep-pursue-pivot.md) · [ADR-EA-0009](ADR-EA-0009-introduce-digital-thread-pattern.md) (introduced the `patterns/` tier) · [`patterns/digital-thread.md`](../patterns/digital-thread.md)

## Context

The canon describes the agentic control plane *structurally* — AEON's six service planes, OrdSA's ordinal layers, MxM's governing surfaces, OAgents' behavioral envelope. None of these names the **temporal cognitive loop** an agent runs *as it does a single piece of work*: forethought before acting, steering while acting, and a governed change of course after learning.

Production agent platforms run some version of this loop. Three publicly-documented mechanisms exemplify its parts:
- **planning** — Claude Code *plan mode* (read-only research → structured plan → approval gate) + the *todo* decomposition/tracking mechanism;
- **goal-pursuit** — Claude Code `/goal` (stop-hook loop + transcript-only evaluator) and Managed-Agents *Outcomes* (rubric + separate-context grader);
- **self-evolution** — Managed-Agents *Dreaming* (between-session memory consolidation, with a review-before-changes-land gate); nearest open reference is *sleep-time compute* (arXiv 2504.13171).

Under [AIDK](../foundation/aidk/) (AI is structurally unreliable), an *ungoverned* version of this loop is a liability. The canon needs a named, governed cognition pattern — one that places a human-curation or policy decision at each load-bearing inflection — that platforms can be measured against.

## Decision

Introduce **prep-pursue-pivot** as a `patterns/`-tier pattern (the second entry, after digital-thread). The pattern names a three-faculty governed cognition loop:

- **prep** (before) — research, approval-gated plan, decompose into inchstones. Posture: **approve** (HCAE front gate).
- **pursue** (during) — drive toward the objective, burn down inchstones, with a **decoupled evaluator** (separate context) gating "done." Posture: **bounded autonomy** (OrdSA evidence-up).
- **pivot** (at inflection) — a **governed decision** to stay the course or change it, resolved by human choice or by pre-declared autonomy rules, revising the inchstones. Posture: **governed decision** (OrdSA authority modes, dialable).

The pattern further defines a two-tier work hierarchy — **milestones** (macro, cross-session) decomposed into **inchstones** (micro, session-level, status-tracked) — whose trail is the orchestration layer of the digital-thread.

Conformance is **behavioral** (five required properties: prep gate, pursue evaluator-decoupling, pivot-as-governed-decision, milestone/inchstone hierarchy, evidence emission), with **schema** recommended and **interface** unspecified. See the pattern document for the normative detail.

The pattern is placed in `patterns/` (not a construct, not a platform) because it is a recurring cross-cutting shape that emerges when AEON, OrdSA, MxM, and HCAE are deployed together — it traverses them rather than living inside any one.

## Consequences

- **New pattern doc** `patterns/prep-pursue-pivot.md` and an Index row in `patterns/README.md`.
- **Foundation linkage:** the pattern makes explicit that pivot's experiential self-improvement is a *runtime/between-session* sibling of RLEG (training-time) and HCAE (practice-time) — a third calibration layer. This is a framing addition, not a change to those foundation entries.
- **Construct linkage:** OrdSA gains an operational locus — pivot is where its authority modes are exercised in the cognitive loop. No change to OrdSA's spec; a reciprocal cross-reference is added.
- **Reference implementation:** NG-AIDE-01 is the intended AIDE reference impl (it instantiates prep→Mind, pursue→Orchestration Runtime, pivot→Memory+Authority). The pattern is reproduced from public source concepts + an AIDE-original governance wrapper; provenance is cited honestly in the pattern doc.
- **No migration burden** — additive; nothing prior depends on the absence of this pattern.

## Alternatives considered

**A. Document it inside MxM (a construct) rather than as a pattern.** Rejected: the loop traverses MxM's Mind/Means/Memory *and* OrdSA's authority *and* AEON's planes *and* HCAE's curation. Per the `patterns/` placement rule, a shape that cuts across multiple constructs/platforms belongs in `patterns/`, not inside one construct.

**B. Keep the three faculties as three separate patterns.** Rejected: their value is the *unified governance gradient* across the before/during/after loop and the shared milestone/inchstone artifact. Split apart, the gradient (the AIDE-original contribution) is lost.

**C. Adopt Anthropic's names (plan mode / goal / dreaming) directly.** Rejected: (1) the AIDE pattern is a *governed* reproduction, not the proprietary features; (2) "dreaming" names the mechanism, not the governed decision — the pivot framing (human-or-policy choice at the inflection) is the load-bearing AIDE addition; (3) AIDE-native naming keeps the pattern portable across the open-source substrate the canon mandates.

**D. Defer until a reference implementation exists.** Rejected: the source-concept impls are public and citable now, NG-AIDE-01 is actively building toward the reference impl, and naming the pattern first gives that build a conformance target. (Status remains Proposed until ratified + an impl lands, per the digital-thread precedent.)

## References

- [`patterns/prep-pursue-pivot.md`](../patterns/prep-pursue-pivot.md) — the pattern document
- [ADR-EA-0009](ADR-EA-0009-introduce-digital-thread-pattern.md) — introduced the `patterns/` tier (digital-thread, first entry)
- Source concepts: Claude Code plan mode + todos (code.claude.com/docs/permission-modes); `/goal` (code.claude.com/docs/goal); Managed-Agents Outcomes + Dreaming (claude.com/blog/new-in-claude-managed-agents); sleep-time compute (arXiv 2504.13171, repo github.com/letta-ai/sleep-time-compute)
- Foundation: [AIDK](../foundation/aidk/), [HCAE](../foundation/hcae/), [RLEG](../foundation/rleg/) · Constructs: [OrdSA](../constructs/ordsa/), [MxM](../constructs/mxm/)
