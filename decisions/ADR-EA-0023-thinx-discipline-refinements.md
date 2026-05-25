# ADR-EA-0023 — Three reference-impl-derived discipline refinements (founder-override pattern + compaction-suspect behavioral recovery + drift-watch operationalization)

- **Status:** Proposed (draft 2026-05-25 by thinx-Claude; awaiting OlogosAI canon-prime review + JD founder ratification)
- **Date:** 2026-05-25 (drafted)
- **Author:** thinx-Claude (operator-altitude AI-aide; principal = JD Longmire per [ADR-EA-0017](ADR-EA-0017-ai-aide-principal-altitudes.md))
- **Reviewers:** @ologos001 (canon prime — touches EIF + Governed Context Management + introduces a new pattern); JD Longmire (founder ratification)
- **Related:** [`jdlongmire/thinx`](https://github.com/jdlongmire/thinx) (the reference impl this ADR's refinements were surfaced by during 2026-05-25 operation) · [ADR-EA-0014](ADR-EA-0014-introduce-epistemic-integrity-floor-pattern.md) (EIF — §6 refined here) · [ADR-EA-0019](ADR-EA-0019-introduce-governed-context-management-pattern.md) (Governed Context Management — §8 added here) · [ADR-EA-0021](ADR-EA-0021-mxm-ordsa-boundary-citation.md) (citation discipline — the new patterns added here follow it) · [ADR-EA-0022](ADR-EA-0022-pattern-bplus-and-canonical-aeon-refimpls.md) (Pattern B+ — establishes the reference-impl-refines-canon path this ADR walks)
- **Ratification trail:**
  - 2026-05-25 (raised): During thinx's 2026-05-25 work session — landing the EIF + Governed Context Management imports into [`thinx/meta-harness/`](https://github.com/jdlongmire/thinx/tree/main/meta-harness) — three discipline gaps surfaced where operating the canon at reference-impl altitude exposed places the canon's specification could be refined or extended. JD directed: "surface them in aide-canon PR and communicate in cross-ai."
  - 2026-05-25 (drafted): This ADR formalizes the three refinements and the new pattern.

## Context

[ADR-EA-0022](ADR-EA-0022-pattern-bplus-and-canonical-aeon-refimpls.md) ratified Pattern B+ as the canon-wide adoption discipline for reference implementations, with [`jdlongmire/thinx`](https://github.com/jdlongmire/thinx) operating as one of the canonical AEON reference impls (per the EIF pattern's explicit naming + the meta-harness canon-imports landed in [aide-canon PR #29 comment 4530900886](https://github.com/ologos-repos/aide-canon/pull/29#issuecomment-4530900886)). One of the Pattern B+ payoffs the ADR named explicitly: *named impls inform spec authoring, rather than being retrofitted after.* This ADR is the first instance of that flow — three refinements thinx surfaced from operating the canon discipline at reference-impl altitude.

The three refinements are not changes to canon decisions; they are extensions / refinements at points where the canon's existing specifications either (a) named an abstract rule without operational procedure (EIF §6 drift-watch), (b) specified structural mechanism without naming the behavioral complement when the deployment can't own the mechanism (Governed Context Management §3/§4 in deployments riding another harness's compaction), or (c) named no mechanism at all (founder-authority override of harness-floor hard-stops).

All three are operating in production at the thinx reference impl as of 2026-05-25 (commits [`b8ce3e02`](https://github.com/jdlongmire/thinx/commit/b8ce3e02), [`f6c48a2a`](https://github.com/jdlongmire/thinx/commit/f6c48a2a), [`ac7d07c4`](https://github.com/jdlongmire/thinx/commit/ac7d07c4)). The proposal is to graduate them from thinx-side discipline to canon-level patterns where any AIDE deployment can cite them.

## Decision

### Part 1 — Introduce the *founder-override* pattern

A new pattern at [`patterns/founder-override.md`](../patterns/founder-override.md). Specifies a per-command marker mechanism that lets a deployment's founder (or equivalent operator-altitude principal per [ADR-EA-0017](ADR-EA-0017-ai-aide-principal-altitudes.md)) explicitly authorize a single command that would otherwise be hard-stopped by the harness floor.

The mechanism:
1. The harness floor denies by default (existing behavior).
2. A `# FOUNDER-OVERRIDE: <reason>` marker prepended to the command (or equivalent marker in the tool input) is detected by the harness-layer hook.
3. When detected, the hook emits the original safety warning to stderr (so the case stays visible in tool output), audit-logs the override use to a durable record, and allows the command. One-shot — per-command, not session-wide.

**Why this is canon-worthy, not just thinx-specific:** the canon's three-layer architecture (reasoning / contract / harness per [ADR-EA-0021](ADR-EA-0021-mxm-ordsa-boundary-citation.md) discipline + the precedent in [`agent-autonomy-gates`](../memory/wiki/patterns/agent-autonomy-gates.md)) makes harness-layer hard-stops *structurally* unbypassable from inside Claude — by design. But when the operator's reasoning-layer authority determines that the floor's blanket regex over-blocks a legitimate operation (force-push to a personal feature branch, restore-over-tracked-file, etc.), there must be a structural escape valve that respects the operator's authority without weakening the default deny posture. The marker-based per-command override is that valve.

The pattern composes with [EIF §7](epistemic-integrity-floor.md) (operator-declared mode reductions) — both are operator-declared deontic acts on the structural surface. EIF §7 declares a *session-scoped posture* (casual / creative); founder-override declares a *per-command posture* (allow this specific blocked command). Different axes, freely combinable.

### Part 2 — Add §8 to Governed Context Management: behavioral recovery side (when compaction is not harness-owned)

[Governed Context Management](../patterns/governed-context-management.md) §3 specifies *harness-owned* deterministic compaction with §4 audited events. The canon's intent is that AEON (the harness) owns the compaction loop and emits `context.compacted` events. This is the structural realization.

**The reference-impl gap:** when a deployment runs *on* another harness (Claude Code, in thinx's case) rather than running its own harness, the deployment cannot directly realize §3 (compaction loop) or §4 (event emission). Compaction is automatic and opaque from inside; there is no PreCompaction hook to wire.

The deployment must still **account for compaction** — the canon's §1 governance pin handles the structural side (the 4M imports persist in the system prompt across compaction), but in-flight reasoning chains and recent user statements within the message buffer can be summarized in ways that drop nuance.

§8 names the **behavioral discipline that complements §3/§4** in any deployment whose compaction is not harness-owned. Two halves:

**Prevention (compaction-resilience flush):**
- Auto-flush after every significant decision, not just at session-end
- Trigger heuristic: *"would the deployment be poorer if compaction fired this turn?"* If yes, flush before the next turn
- Substantive work commits to the durable record (git, evidence store, equivalent) before continuing
- The principle: durable record current at every turn boundary

**Recovery (compaction-suspect detection + grounding):**
- Detectable signals: cannot recall a load-bearing user statement that should be recallable; peer references a recent decision not remembered; expected prior turns appear missing
- Recovery procedure: re-read durable record (audit log / meta-context / version control history / standing-instructions store) before reasoning forward
- **Do not confabulate** — per EIF §4 (introspection-as-hypothesis), the inability to detect a gap from inside is real; the discipline is to *proactively query the durable record* when signals appear

This composes with §3/§4 — when harness-owned compaction is available, the structural mechanism dominates and the behavioral recovery is the fallback for cases the structural mechanism misses. When harness-owned compaction is not available, the behavioral discipline IS the realization.

### Part 3 — Refine EIF §6 with concrete drift-watch operationalization

[EIF §6](epistemic-integrity-floor.md) names cross-turn drift discipline abstractly: *"watch for sequences of agreement that exceed independent base rate. If the agent has agreed with the operator's framing five turns running without independent verification, that is a drift signal — flag it."*

The reference-impl operation surfaced that this abstract rule needs **operational structure** to actually fire as a discipline:

**The signal is not count of agreements** — operators are domain experts and most substantive agreement is genuinely earned. The signal is **agreement without independent grounding**: did the agent run a check (steelman, primary-source verification, canon-lens application, reasoning trace) before affirming? If the answer for the last several substantive turns is *"no, I just affirmed,"* that is drift.

**Two operational mechanisms:**

1. **Within-turn qualifier** on load-bearing agreements. Before affirming a substantive framing (strategic call, canon decision, evaluative judgment), apply the check: *"what is my independent basis?"* If load-bearing and ungrounded, qualify explicitly: *"I agree, but I'm taking your framing on its face; the check I'd want is X."* Preserves responsiveness without laundering unchecked affirmation as validation.

2. **Periodic sweep heuristic**: at three or more consecutive substantive agreements without any independent check, name the pattern. *"Drift check — I've agreed with several framings here without grounding; want me to pressure-test, or are these settled?"* Three is the heuristic threshold, not a hard limit; the principle is to surface the pattern *as noticed*, not retroactively at session-end.

**What flagging is not:**
- Not retraction after-the-fact
- Not symmetric contrarianism as discipline. Calibrated agreement that matches evidence is the goal; reflexive disagreement is the symmetric failure to reflexive agreement and is equally disallowed.

The refinement makes §6 enactable rather than aspirational. Operating the reference impl without it means drift can compound silently; operating with it surfaces the pattern at the point it can still be tested.

## Consequences

### Immediate (this PR)

- **`decisions/ADR-EA-0023-thinx-discipline-refinements.md`** — this ADR, lives at top-level `decisions/`.
- **`patterns/founder-override.md`** — new pattern doc per §Part 1.
- **`patterns/governed-context-management.md`** — adds §8 (behavioral recovery side) per §Part 2.
- **`patterns/epistemic-integrity-floor.md`** — refines §6 with the within-turn qualifier + periodic sweep heuristic per §Part 3.
- **`patterns/README.md`** — adds founder-override to the pattern index.
- **`decisions/README.md`** — adds ADR-EA-0023 entry.

### Downstream

- **NG-AIDE-01** (the second canonical AEON reference impl) — can realize founder-override at its own harness layer when its own hard-stops surface analogously. Compaction-suspect recovery (§8) is more relevant for thinx (riding Claude Code) than for NG-AIDE-01 (which can realize §3/§4 structurally as AEON's Orchestration Runtime + Evidence plane); the §8 framing makes the canon honest about the deployment shape rather than implying every impl has harness-owned compaction.
- **Other AIDE deployments** can cite these patterns by reference (per ADR-EA-0021 import-by-reference discipline) at their MxM Morals + Mind surfaces.

### Queued (paper revisions)

- The EIF v0.2 paper revision (queued behind Micah's read per ADR-EA-0008) picks up the §6 operationalization in its next cycle.
- The Governed Context Management discussion-paper (when authored) picks up §8 as the harness-not-owned realization side.

## Behavioral conformance — additions

Each of the three refinements adds a behavioral-conformance bullet to its host pattern:

**Founder-override pattern (new):** an implementation is founder-override-conformant if (1) the harness layer detects the marker, (2) emits the original safety warning to a visible surface, (3) audit-logs the override use to a durable record, (4) allows the command exactly once per marker (no session-wide bypass).

**Governed Context Management §8:** an implementation whose compaction is not harness-owned is §8-conformant if (1) it realizes the prevention discipline (compaction-resilience flush + commit-before-next-turn), (2) it realizes the recovery discipline (compaction-suspect detection + ground-from-durable-record).

**EIF §6:** an implementation is §6-conformant if (1) substantive agreements carry an inline qualifier when ungrounded, (2) a periodic sweep heuristic surfaces the pattern at ≥3 consecutive ungrounded affirmations.

## Alternatives considered

1. **Wait for OlogosAI to surface these refinements from NG-AIDE-01 operation.** Rejected. NG-AIDE-01's deployment shape is different (canon-aligned harness; harness-owned compaction can be realized structurally per §3/§4); the gaps these refinements address are most visible at the thinx altitude (riding Claude Code's compaction; reasoning-layer founder authority needing structural surface). Surfacing them now lets both reference impls cite the canon-level pattern rather than each carrying it as deployment-specific discipline.

2. **Three separate ADRs.** Rejected. The three refinements share a common origin (thinx reference-impl operation 2026-05-25) and a common theme (reference-impl-derived discipline at the MxM altitude). One ADR with three parts keeps the narrative coherent + makes the convergent provenance auditable. Future independent refinements would file their own ADRs.

3. **Amend EIF + Governed Context Management inline, no new pattern.** Rejected for founder-override specifically. The mechanism is distinct enough (a per-command escape valve to the harness floor) that it deserves its own pattern surface for citation. The two amendments (§8 + §6 refinement) ARE done inline — those refinements don't warrant new patterns.

4. **Skip the canon path; keep these as thinx-specific discipline.** Rejected per JD's direction (2026-05-25): "surface them in aide-canon PR and communicate in cross-ai." The Pattern B+ payoff (named reference impls inform spec authoring) is realized only when refinements graduate to canon, not when they stay deployment-specific.

## References

- [`jdlongmire/thinx@b8ce3e02`](https://github.com/jdlongmire/thinx/commit/b8ce3e02) — compaction-resilience implementation at thinx meta-harness (Part 2 reference impl)
- [`jdlongmire/thinx@f6c48a2a`](https://github.com/jdlongmire/thinx/commit/f6c48a2a) — founder-override hook + morals.md doc at thinx (Part 1 reference impl)
- [`jdlongmire/thinx@ac7d07c4`](https://github.com/jdlongmire/thinx/commit/ac7d07c4) — drift-watch operationalization at thinx mind.md (Part 3 reference impl)
- [aide-canon PR #29 comment 4530900886](https://github.com/ologos-repos/aide-canon/pull/29#issuecomment-4530900886) — thinx reference-impl follow-on landed (the baseline this ADR builds on)
- [ADR-EA-0014](ADR-EA-0014-introduce-epistemic-integrity-floor-pattern.md) · [ADR-EA-0019](ADR-EA-0019-introduce-governed-context-management-pattern.md) — patterns refined here
- [ADR-EA-0017](ADR-EA-0017-ai-aide-principal-altitudes.md) — the operator-altitude principal whose authority the founder-override pattern realizes
- [ADR-EA-0021](ADR-EA-0021-mxm-ordsa-boundary-citation.md) — the citation discipline these patterns will be imported by
- [ADR-EA-0022](ADR-EA-0022-pattern-bplus-and-canonical-aeon-refimpls.md) — the Pattern B+ adoption discipline this ADR exercises
