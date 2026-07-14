# ADR-EA-0028 — Introduce MxH-P synthesis pattern (MxM · Hermetic · P/G/E)

- **Status:** Accepted (ratified 2026-07-14 by JD-Founder)
- **Date:** 2026-07-13
- **Author:** ologos-grok (operator-altitude synthesis, filed into canon per JD direction)
- **Reviewers:** JD Longmire (Founder ratification, 2026-07-14)
- **Related:** Hermetic discussions [#38](https://github.com/ologos-repos/Hermetic/discussions/38)–[#40](https://github.com/ologos-repos/Hermetic/discussions/40); [ADR-EA-0022](ADR-EA-0022-pattern-bplus-and-canonical-aeon-refimpls.md); [ADR-EA-0027](ADR-EA-0027-introduce-workflow-orchestration-pattern.md); [ADR-EA-0005](../constructs/mxm/decisions/ADR-EA-0005-clarify-mxm-archetype.md)
- **Ratification trail:**
  - 2026-07-13 (filed): Pattern + ADR landed as `Proposed` on PR [#61](https://github.com/ologos-repos/aide-canon/pull/61) (`patterns/mxh-p-synthesis.md`, root README, cross-indexes).
  - 2026-07-14 (merged): PR #61 squash-merged to `main` (`2711268`).
  - 2026-07-14 (ratified): JD-Founder accepted as-proposed. Status → `Accepted`. Pattern doc becomes normative. Hermetic#40 pointer comment authorized.

## Context

The AIDE corpus has three strong, partially overlapping answers to “how do agents work safely and usefully?”:

1. **MxM** — the harness archetype: orient before execute; Mind/Morals/Mission/Memory/Methods/Means ([ADR-EA-0005](../constructs/mxm/decisions/ADR-EA-0005-clarify-mxm-archetype.md), [ADR-EA-0026](../constructs/mxm/decisions/ADR-EA-0026-introduce-methods-surface.md)).
2. **Hermetic** — a production multi-agent orchestration runtime (tasks, roster, oracle L0–L3, signal/gate, Nous, Eidolon, federation), cited as Pattern B+ AEON reference impl ([ADR-EA-0022](ADR-EA-0022-pattern-bplus-and-canonical-aeon-refimpls.md)).
3. **P/G/E** — Planner / Generator / Evaluator as *claimable* delivery for substantial work, with artifact-only explicitly prohibited (operator homes such as ologos-grok Morals P13 + `pge_gate`).

Engagement work already showed:

- Hermetic *enacts* MxM concerns under function-grouped packages, but **folder renames are not the unlock** (Hermetic#40; OlogosAI: orientation packet first).
- Workflow orchestration needs **envelope refinement** and gates on the deterministic layer ([ADR-EA-0027](ADR-EA-0027-introduce-workflow-orchestration-pattern.md)).
- Operator primes risk either **under-orchestrating** (single agent self-grades) or **over-ceremonializing** (always-on swarm + always-on P/G/E).

Without a named composition pattern, teams:

- treat Hermetic as a substitute for morals,
- treat MxM as wallpaper over a swarm,
- or claim “P/G/E” from three files written in one context.

That is a framework-level gap: not a missing construct, but a missing **cross-tier deployment shape**.

## Decision

### 1. Add `patterns/mxh-p-synthesis.md` to the `patterns/` tier

A new cross-cutting pattern, peer to digital-thread, workflow-orchestration, EIF, GCM, etc. Admission tests:

| Test | Satisfied? |
|---|---|
| Cuts across tiers/constructs/planes | Yes — MxM + Hermetic/AEON means + OAgents-style roles + OrdSA oracle altitude + digital-thread evidence |
| Reference implementation(s) citable | Yes — fragmentary but real: MxM homes, Hermetic, ologos-grok P/G/E bag, Claude Code Workflow as control-plane supertype |
| ADR-ratified | This ADR (Accepted 2026-07-14) |

### 2. Name the pattern

**MxH-P** (MxM · Hermetic · P/G/E) — *oriented multi-agent claimable delivery*.

**Definition.** Compose three altitudes without fusion:

- **MxM** orients and constrains (constitution + orientation packet).
- **Hermetic** schedules and coordinates (swarm means; Pattern B+ out-of-tree).
- **P/G/E** proves substantial packages were planned, built, and skeptically accepted under dispatched role isolation and a fail-closed gate.

Normative one-liner:

> MxM orients and constrains · Hermetic schedules and coordinates · P/G/E proves substantial work was planned, built, and skeptically accepted.

### 3. Normative contributions (live in the pattern doc)

1. **Orientation packet** — every delegated worker/role boots with an MxM-shaped structured envelope; this is the Hermetic#40 operational unlock (not package rename).
2. **P/G/E as signal/gate workflow** — three role-isolated dispatches with access asymmetry; ledger `mode=dispatched-agents` only is claimable; specialization of workflow-orchestration under envelope refinement.
3. **Unified escalation table** — ordinal oracle for judgment under uncertainty; deontic DENY/CONFIRM/P1 for irreversible and out-of-scope; no laundering the second through the first; no silent full-auto without time-boxed grant.

### 4. Conformance levels

- **Behavioral (required)** — seven criteria in the pattern doc (orientation, refinement, claim discipline, access asymmetry, escalation split, proportionality, prime independence for multi-prime).
- **Partial labels** — `MxH-P/core` | `MxH-P/swarm` | `MxH-P/full` so operator primes can claim honesty before Hermetic is in the path.
- **Schema (recommended)** / **Interface (optional)** — as specified in the pattern doc.

### 5. Phased adoption is part of the decision

Land **packet + P/G/E gate + DAG** before multi-worker Hermetic. Do not require full Hermetic for `MxH-P/core` conformance. Pattern B+ for Hermetic remains: out-of-tree, cited, not absorbed into the canon or soft-linked as runtime law into peer primes.

### 6. Cross-tier index updates landed alongside

- `patterns/README.md` — index row  
- `decisions/README.md` — this ADR  
- `vision-strategy/analysis/hermetic-engagement/README.md` — pointer to MxH-P as composition answer post-#40  
- `constructs/mxm/README.md` — related pattern citation  
- `vision-strategy/analysis/README.md` and exemplar-tracking hermetic notes as needed  

## Consequences

**Positive:**

- Gives a single citeable answer to “how do MxM, Hermetic, and P/G/E fit?”
- Prevents three failure modes: wallpaper morals, fake P/G/E, rename-only MxM.
- Aligns Hermetic#40 contingency (packets before reorg) with a canon-level pattern.
- Composes cleanly with ADR-EA-0027 (P/G/E as specialized workflow) and ADR-EA-0022 (Hermetic Pattern B+).
- Allows operator primes (e.g. ologos-grok) to implement `MxH-P/core` without adopting Hermetic immediately.

**Negative / risk:**

- **Pattern lead vs realization.** No single system is `MxH-P/full` today; the pattern stays honest about partial conformance (same honesty as the envelope lattice in ADR-EA-0027).
- **Name collision.** “Hermit” (org/brand) vs “Hermetic” (product) vs cashapp hermit toolchain — the pattern doc uses **Hermetic** for the runtime and **MxH-P** as the short name to reduce confusion.
- **Ceremony pressure.** Misread as “always run Hermetic + P/G/E”; the proportionality rule and partial labels exist to counter this.
- **OAgents / Micah co-authorship.** Envelope refinement remains pattern-level; absorbing into OAgents NIST text stays out of scope (ADR-EA-0008).

## Alternatives considered

| Alternative | Why not chosen |
|---|---|
| **Docs-only mapping under hermetic-engagement/** | Useful trail, but not discoverable as a canon pattern peers cite for deployment. |
| **Absorb Hermetic into aide-canon** | Violates Pattern B+; collapses independent release/governance (ADR-EA-0022). |
| **Rename Hermetic internals to MxM surfaces** | Hermetic#40 risk: churn without operational meaning; packets first. |
| **Treat P/G/E as Hermetic-only** | Blocks `MxH-P/core` on single-prime homes that already have `delegate.py` / `pge_*`. |
| **New construct instead of pattern** | MxH-P does not define a new methodological surface; it composes existing ones — correct `patterns/` altitude. |
| **Extend only workflow-orchestration** | Workflow-orchestration is the control-plane supertype; it does not name Hermetic’s swarm means or MxM orientation packets. Specialization needs a named pattern. |

## References

- [`patterns/mxh-p-synthesis.md`](../patterns/mxh-p-synthesis.md) — normative pattern text  
- [`patterns/workflow-orchestration.md`](../patterns/workflow-orchestration.md)  
- [`vision-strategy/analysis/hermetic-engagement/`](../vision-strategy/analysis/hermetic-engagement/)  
- [Hermetic#40 MxM refactor discussion](https://github.com/ologos-repos/Hermetic/discussions/40)  
- ologos-grok: `construct/morals.md` P13, `docs/pge.md`, `scripts/pge_gate.py`  
- [ADR-EA-0009](ADR-EA-0009-introduce-digital-thread-pattern.md) digital-thread  
