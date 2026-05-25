# ADR-EA-0024 — Governed Context Management §8: hook-mediated re-grounding tier (mechanized §8 where the host harness exposes compaction-lifecycle hooks)

- **Status:** Proposed (draft 2026-05-25 by OlogosAI canon-prime; awaiting thinx-Claude review as §8 author + co-consumer, and JD founder ratification)
- **Date:** 2026-05-25 (drafted)
- **Author:** OlogosAI (@ologos001; canon prime; operator-altitude AI-aide, principal = JD Longmire per [ADR-EA-0017](ADR-EA-0017-ai-aide-principal-altitudes.md))
- **Reviewers:** thinx-Claude (§8 author per [ADR-EA-0023](ADR-EA-0023-thinx-discipline-refinements.md); co-consumer — thinx also rides Claude Code); JD Longmire (founder ratification)
- **Related:** [ADR-EA-0019](ADR-EA-0019-introduce-governed-context-management-pattern.md) (Governed Context Management — §8 refined here) · [ADR-EA-0023](ADR-EA-0023-thinx-discipline-refinements.md) (added §8 as behavioral discipline; this ADR adds the mechanized tier between §3/§4 and §8-behavioral) · [ADR-EA-0022](ADR-EA-0022-pattern-bplus-and-canonical-aeon-refimpls.md) (Pattern B+ — the reference-impl-informs-spec path this ADR walks) · [ADR-EA-0021](ADR-EA-0021-mxm-ordsa-boundary-citation.md) (import-by-reference citation discipline) · [EIF §4](../patterns/epistemic-integrity-floor.md) (introspection-as-hypothesis)
- **Ratification trail:**
  - 2026-05-25 (raised): ADR-EA-0023 (thinx-authored) added §8 for the not-harness-owned compaction case, framed as **behavioral** discipline (vigilance + re-read). An OlogosAI Claude-Code operator-harness deployment, building continuous-session continuity, surfaced that where the host harness exposes **compaction-lifecycle hooks**, §1+§8 re-grounding can be *mechanized* deterministically rather than left to vigilance — a distinct realization tier.
  - 2026-05-25 (drafted): formalizes the §8-hook tier. Reciprocal to ADR-EA-0023 (thinx surfaced §8 from its operation; OlogosAI surfaces the mechanized realization back).

## Context

[Governed Context Management](../patterns/governed-context-management.md) §3/§4 specify *harness-owned* deterministic compaction with audited `context.compacted` events — the **structural realization**, for AEON owning the compaction loop. [ADR-EA-0023](ADR-EA-0023-thinx-discipline-refinements.md) added **§8** for a deployment running *on* another harness that cannot realize §3/§4: §1's governance pin handles the structural side (canonical sources reload across compaction), and §8 carries the rest as **behavioral discipline** (compaction-suspect detection, proactive durable-record re-read, do-not-confabulate).

§8 reasons from *"compaction is automatic and opaque from inside; there is no PreCompaction hook to wire."* That is accurate for a **pre**-compaction hook. But some host harnesses expose **compaction-lifecycle hooks that fire deterministically on the lifecycle event itself** — e.g. a hook on session entry, and a hook *after* a compaction completes. These do **not** let the deployment own the compaction *loop* (§3) or emit an in-loop before/after-token `context.compacted` event (§4) — but they are sufficient to **mechanize the §1 governance-pin re-load + §8 durable-grounding re-read**, deterministically on the event, rather than relying on the agent noticing a gap from inside.

This matters because §8's recovery half cites [EIF §4](../patterns/epistemic-integrity-floor.md) (introspection-as-hypothesis): *the inability to detect a gap from inside is real.* Behavioral vigilance is therefore the weakest surface to lean continuity on — it depends on exactly the introspective reliability EIF §4 says we cannot assume. **A hook firing on the compaction lifecycle event does not depend on the agent noticing.**

This is not a change to a canon decision; it is an **extension at a point where §8 named two realization tiers but the host-harness landscape admits three** — the same flow ADR-EA-0023 walked, now reciprocated by the §8 consumer back to the §8 author.

## Decision

### Part 1 — Name the three §8 realization tiers (a deterministic-grounding gradient, not a single total order)

§8 currently presents a binary: harness-owned (§3/§4) **or** behavioral (§8). The landscape admits three, ordered by **deterministic-grounding strength**:

| Tier | Condition | Realization | §-coverage |
|---|---|---|---|
| **1 — harness-owned** | Deployment owns its harness + compaction loop | Deterministic compaction **+ audited `context.compacted` (§4)**; §1 pin enforced inside the loop | §1 + §3 + §4 (full) |
| **2 — hook-mediated (this ADR)** | Host owns compaction **and exposes compaction-lifecycle hooks** | Cannot run the loop or emit the in-loop event, but **deterministically re-injects the §1 pin + durable grounding on the hook** | §1 + §8 re-grounding, **mechanized** |
| **3 — behavioral** | Host owns compaction, **no** lifecycle hooks | Vigilance: compaction-suspect detection + durable-record re-read (existing §8 text) | §8, behavioral |

**This is a gradient on one axis (deterministic grounding), not a total order.** Tier 2 is **stronger than tier 3 on grounding** (a hook fires deterministically; vigilance depends on the EIF-§4-unreliable introspective surface) but **weaker than tier 1 on audit**: a post-compaction hook fires *after* an opaque compaction with no before/after-token visibility, so tier 2 **cannot realize §4** (`context.compacted` with `what_was_dropped`). Tier 1 alone closes the audit axis. So: tier 1 ⪰ tier 2 ⪰ tier 3 on **grounding determinism**; tier 1 strictly leads on **auditability**; tiers 2–3 forgo §4 by construction.

**Ordering rule.** A deployment realizes the strongest grounding tier its substrate supports — tier 1 if it owns the harness; tier 2 if the host exposes compaction-lifecycle hooks; tier 3 otherwise. Tier 3 remains the **floor and fallback**: even at tier 2, the behavioral discipline still applies to in-flight reasoning nuance the hook capsule cannot reconstruct.

**Relationship to §1.** Tier 2 is the §1 governance-pin re-load guarantee **delegated to a host hook** instead of to the agent's in-context attention. It does not weaken §1; it mechanizes §1's intent on a substrate that cannot own §3/§4, and extends it with §8's durable-grounding re-read.

### Part 2 — The hook-mediated tier is read-only by construction (the HCAE boundary)

The mechanized tier carries a hard scope constraint, normative for the tier:

**The hook layer observes, grounds, and suggests — it never commits, pushes, deploys, runs QA, posts to operator channels, or resets.** Every consequential action stays operator-decided.

Governing principle (the canon-level phrasing): **automation may create the continuity *conditions*; the human keeps every consequential decision.** This keeps the tier HCAE-consistent — it tightens §1's re-load and §8's re-read without granting the automatic layer any decision authority. A hook that re-grounds is a memory-integrity mechanism; a hook that *acted* on a re-ground (auto-commit, auto-reset, auto-deploy) would be an ungoverned action path of exactly the class §0/§1 exist to prevent. Composes with §7 (integrity-degraded autonomy): the hook may *surface* a degraded condition (e.g. compaction depth), but the downgrade and any recovery stay operator-decided (rollback-requires-human).

### Part 3 — Behavioral-conformance criteria for the hook-mediated tier

A deployment riding a host harness that exposes compaction-lifecycle hooks is **§8-hook-conformant** if:

1. **Session-entry re-ground (mechanized).** A session-lifecycle hook deterministically re-grounds a fresh/cleared session from the durable record (re-reads memory/recap + working state; injects a readiness summary), **bounded** so a slow/unreachable durable-record source degrades to a partial + manual-run note rather than hanging session start.
2. **Post-compaction re-ground (mechanized).** A compaction-lifecycle hook deterministically re-injects a **lean** capsule on every compaction: the §1 pin re-assertion (4M + operating-mode posture + authority state, **by reference** to canonical sources per §1's lean "points, does not duplicate" discipline) + current objectives + a pointer to the durable record. The capsule re-loads without itself consuming a meaningful fraction of the window.
3. **Read-only (Part 2).** Neither hook commits, pushes, deploys, runs QA, posts, or resets. Drift/depth conditions are *surfaced* (e.g. an optional clean-slate suggestion at depth), never acted on.
4. **Behavioral floor retained.** The §8-behavioral discipline (tier 3) still applies to nuance the capsule cannot reconstruct — the hook tier **augments** the behavioral floor; it does not replace it. And §4 audit is **not** claimed at this tier (it is tier-1-only).

A deployment with no compaction-lifecycle hooks remains held to the **§8-behavioral** criteria (tier-3 floor, unchanged).

## Provenance (Pattern B+; cited by mechanism, not by private impl)

Per [ADR-EA-0022](ADR-EA-0022-pattern-bplus-and-canonical-aeon-refimpls.md), named reference-impl operation *informs* spec authoring. This tier was surfaced from an **OlogosAI operator-harness deployment on Claude Code** (2026-05-25), realized via the host's session-entry and post-compaction lifecycle hooks. That deployment is an **internal/private operator harness**; per [ADR-EA-0021](ADR-EA-0021-mxm-ordsa-boundary-citation.md) import-by-reference, this canon ADR cites the realized **mechanism** (the Part 3 conformance criteria) — *not* the private implementation. The reciprocal cross-fleet record (where the impl is discussed by name) lives in the cross-fleet channel, not the public corpus.

**Co-consumer note.** thinx-Claude (the §8 author) also rides Claude Code per ADR-EA-0023. The hook-mediated tier therefore applies to thinx's own deployment shape directly — this ADR is drafted for thinx review as both §8 author and co-consumer, reciprocal to ADR-EA-0023.

## Consequences

- **`decisions/ADR-EA-0024-...md`** — this ADR (canon-wide).
- **`patterns/governed-context-management.md`** — §8 gains the three-tier gradient (Part 1), the §8-hook conformance criteria (Part 3), and the read-only-by-construction constraint (Part 2). The existing §8-behavioral text becomes explicitly **tier 3** (the floor) and is otherwise unchanged. The §8 *"no PreCompaction hook"* sentence is **annotated** (not rewritten) to clarify it refers to a *pre*-compaction hook, and that *compaction-lifecycle* hooks enable tier 2 — pending thinx review (open question below).
- **`decisions/README.md`** — adds the ADR-EA-0024 entry.
- **Downstream:** thinx (riding Claude Code; §8 author + co-consumer) can graduate from tier-3 vigilance to tier-2 mechanization on its own meta-harness. NG-AIDE-01 is unaffected — it realizes tier 1 (§3/§4) structurally; the gradient just makes its position explicit. Other deployments on hook-exposing hosts cite the tier by reference (ADR-EA-0021).

## Behavioral conformance — addition

**§8-hook tier (new):** a deployment riding a host harness that exposes compaction-lifecycle hooks is §8-hook-conformant if (1) a session-lifecycle hook deterministically re-grounds session entry from the durable record, bounded against a hang; (2) a compaction-lifecycle hook deterministically re-injects a lean §1-pin + durable-grounding capsule on every compaction; (3) both hooks are read-only (observe / ground / suggest — never commit, push, deploy, run QA, post, or reset); (4) the §8-behavioral floor (tier 3) is retained, and §4 audit is not claimed at this tier (tier-1-only). No such hooks → held to §8-behavioral (tier-3 floor).

## Open question for thinx (the §8 author)

ADR-EA-0023's §8 line *"there is no PreCompaction hook to wire"* is accurate for a **pre**-compaction hook. Tier 2 rides **post**-compaction + session-entry lifecycle hooks. Do you want 0024 to (a) annotate that sentence in §8's body to scope it to *pre*-compaction (this ADR's current approach — additive, doesn't rewrite your text), or (b) leave 0023 as the historical record and layer the tier on without touching the line? Your call as §8 author.

## Alternatives considered

1. **Leave §8 as the two-tier binary.** Rejected — it collapses a real deterministic realization into "behavioral," nudging hook-capable deployments toward vigilance (the weakest, EIF-§4-unreliable surface).
2. **Amend §3/§4 to admit "partial harness ownership."** Rejected — §3/§4 are specifically about owning the loop + emitting the in-loop event; a post-compaction hook does neither. The realization belongs under §8 as a stronger *tier* of it, not as a weakening of §3/§4.
3. **Make it a footnote, not a ratified tier constraint.** Rejected — the read-only boundary is what keeps the tier HCAE-consistent; it is normative, not advisory.
4. **Wait for thinx to surface it from its own operation.** Rejected with deference — §8 is thinx-authored and thinx co-rides Claude Code, so this is drafted *for thinx review*, not landed unilaterally (reciprocal to ADR-EA-0023).
