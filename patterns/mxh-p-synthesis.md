# MxH-P synthesis pattern (MxM · Hermetic · P/G/E)

> **Status:** Proposed — [ADR-EA-0028](../decisions/ADR-EA-0028-introduce-mxh-p-synthesis-pattern.md)  
> **Short name:** **MxH-P** (MxM + Hermetic + P/G/E)  
> **Also called:** oriented multi-agent claimable delivery

## Summary

**MxH-P** is the cross-cutting composition of three altitudes that are often confused or partially reimplemented:

| Layer | Owns | Must not be asked to own |
|---|---|---|
| **MxM** | Identity, law, judgment, continuity, graduation (`practice → method → moral → means`) | Swarm scheduling; multi-worker DAG machinery |
| **Hermetic** | Multi-agent orchestration runtime (tasks, roster, oracle, signal/gate, Nous, Eidolon, federation) | Typed deontology; prime-independence law; claimable delivery semantics |
| **P/G/E** | Claimable delivery protocol for *substantial* work (Planner → Generator → Evaluator, dispatched, gated) | Standing identity; host-wide safety floor; unbounded swarm scale |

One-line law of the pattern:

> **MxM orients and constrains · Hermetic schedules and coordinates · P/G/E proves substantial work was planned, built, and skeptically accepted.**

MxH-P is **not** a merge of the three codebases into one monorepo. It is a **composition pattern**: each layer keeps its home; adapters and envelopes bind them under **envelope refinement** (see [workflow-orchestration](workflow-orchestration.md): `envelope(child) ⊑ envelope(parent)`).

## Why this pattern exists

The corpus already has pieces:

- **MxM** (`constructs/mxm/`) — harness archetype; orientation before execution ([ADR-EA-0005](../constructs/mxm/decisions/ADR-EA-0005-clarify-mxm-archetype.md), [ADR-EA-0026](../constructs/mxm/decisions/ADR-EA-0026-introduce-methods-surface.md) Methods).
- **Hermetic** — working multi-agent means / AEON six-plane exemplar ([ADR-EA-0022](../decisions/ADR-EA-0022-pattern-bplus-and-canonical-aeon-refimpls.md); engagement threads [#38](https://github.com/ologos-repos/Hermetic/discussions/38)–[#40](https://github.com/ologos-repos/Hermetic/discussions/40)).
- **P/G/E** — Planner/Generator/Evaluator with **dispatched-agents only** claimable (ologos-grok `scripts/pge_*`, Morals P13; thinx-codex port lineage).
- **Workflow-orchestration** — deterministic control + agent steps under envelope refinement ([ADR-EA-0027](../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)).

What was missing: a single named shape that answers:

1. How does a **swarm runtime** inherit a **typed constitution** without renaming folders for cosplay?
2. How does **claimable delivery** sit *on* Hermetic’s task/signal machinery without becoming artifact-only theater?
3. When is **single-agent under MxM** enough, when is **P/G/E** required, and when is **Hermetic multi-worker** justified?

Hermetic#40 correctly rejected package renames-for-MxM alone. The operational unlock is an **orientation packet** plus **authority-narrowing dispatch** plus a **claimable ledger** on a **signal/gate DAG**. MxH-P names that composite.

## Relationship to other canon objects

| Object | Relation to MxH-P |
|---|---|
| [workflow-orchestration](workflow-orchestration.md) | **Supertype for the control plane.** P/G/E is a *specialized* three-role workflow under envelope refinement; Hermetic Director is an orchestration agent; gates attach to the deterministic layer. |
| [digital-thread](digital-thread.md) | **Evidence spine.** Package artifacts + ledger + Eidolon phases/reviews should FK into one thread per substantial package. |
| [epistemic-integrity-floor](epistemic-integrity-floor.md) | Feeds **MxM Mind** labels (computed / inferred / uncertain) into the orientation packet. |
| [founder-override](founder-override.md) | Human override path for hard stops; never silent `/auto` without grant. |
| OAgents | Child roles are agents with envelopes; Evaluator is post-execution verification altitude. |
| OrdSA | Oracle L0–L3 aligns with ordinal authority; P/G/E lives at O3 under O2-delegated orchestration. |
| AEON | Hermetic remains Pattern B+ AEON refimpl; MxH-P adds *how* MxM + delivery rigor compose *on* that runtime. |

## Normative stack

```text
┌─────────────────────────────────────────────────────────────┐
│  HUMAN (L3)  — grants, confirmations, mission changes         │
└────────────────────────────▲────────────────────────────────┘
                             │ oracle / CONFIRM / recovery grants
┌────────────────────────────┴────────────────────────────────┐
│  MxM  (constitution + orientation)                            │
│  root(mode) · mission · mind · morals · methods · memory      │
│  conflict priority: Prohibitions > Obligations > Permissions  │
└────────────────────────────▲────────────────────────────────┘
                             │ every prime/worker inherits envelope
┌────────────────────────────┴────────────────────────────────┐
│  Hermetic  (swarm means / orchestration runtime)              │
│  Hermes · Bus · Nous · Eidolon · Federation · Director        │
│  Runner backends (Claude Code, Grok, …) via adapter            │
└────────────────────────────▲────────────────────────────────┘
                             │ substantial packages only
┌────────────────────────────┴────────────────────────────────┐
│  P/G/E  (claimable delivery bag)                              │
│  Planner(RO) → Generator(WW) → Evaluator(RO)                  │
│  ledger mode=dispatched-agents · gate fail-closed               │
└─────────────────────────────────────────────────────────────┘
```

### Hard composition rules

1. **Envelope refinement.** Hermetic and P/G/E may only **narrow** authority relative to the active MxM envelope. Never widen by orchestration, affinity, or federation.
2. **Prime independence.** Multi-prime federation is transport + task routing, not shared morals. Each prime owns its MxM home (P12-class rule in operator deployments).
3. **Claim ≠ task complete.** Hermes `completed` ≠ P/G/E `succeeded`. Only `dispatched-agents` ledgers that pass the package gate are claimable.
4. **Artifact-only prohibited.** Three markdown files written by one context are **not** P/G/E.
5. **Optional ladder.** Narrow work stays single-agent under MxM. Ceremony is proportional to blast radius.
6. **No silent full-auto.** Hermetic `/auto` (or equivalent) requires an **explicit, time-boxed MxM grant**. Default is gated autonomy.

## Contribution 1 — Orientation packet (MxM operational inside Hermetic)

**Claim.** MxM is operational in a multi-agent runtime only when every worker/role boot receives a **structured orientation packet**, not only prose skills and inline prompts.

Recommended schema (implementations may map fields; behavioral content is normative):

```yaml
# orientation.packet.yaml — injected at spawn; stored on task/package
schema_version: 1
mission:
  identity: <prime-or-worker identity>
  telos: <one-line purpose for this run>
  scope_class: in_home | authorized_surface | reference_only
  authority_grant: null | { surface, expires, by }
mind:
  epistemic_labels: [computed, inferred, uncertain]
  inference_mode: abductive | deductive | inductive | mixed
  ground_before_assert: true
morals:
  prohibitions_ref: <construct path or catalog id>
  confirm_classes: [...]
  deny_catalog_ref: <irreversible rules id>
methods:
  delivery: single_agent | pge_optional | pge_required
  pr_first: true | false
memory:
  prior_refs: [...]
  rule: "memory is snapshot; verify live state"
means:
  access: read-only | workspace-write | full
  tools_allowlist: [...]
  workspace: <path>
  deny_floor: active
  confirm_gate: required_for_class
```

**Why this is the Hermetic#40 unlock.** Renaming `internal/` to `mind/morals/...` without packets is naming alignment. Packets make surface mismatches **spottable** and authority **auditable**. Package reorg (if ever) is gated on packet utility, not the reverse — consistent with the OlogosAI response on Hermetic#40.

## Contribution 2 — P/G/E as signal/gate workflow on Hermetic

**Claim.** For substantial packages, P/G/E is enacted as a **deterministic DAG of three role-isolated dispatches**, not as freeform multi-worker chat.

### Role contracts

| Role | Access | Produces | Must not |
|---|---|---|---|
| **Planner** | read-only (mechanical preferred) | `planner.md` — objective, non-goals, acceptance, verification, authority boundary | Edit product tree; self-approve |
| **Generator** | workspace-write ⊆ grant | Implementation + `generator.md` | Redefine acceptance without plan revision; widen scope |
| **Evaluator** | read-only | `evaluator.md` — accept/repair, defects, residual risk | Apply fixes; rubber-stamp without evidence |

### Signal/gate mapping

```text
Planner complete  ──signal:plan_ready──► Generator unblocks
Generator complete ──signal:impl_ready──► Evaluator unblocks
Evaluator accept  ──signal:package_ok──► Director may claim P/G/E success
Evaluator repair  ──signal:repair──────► Generator loop (bounded N)
```

### Ledger (claim surface)

Minimum claimable fields (align with ologos-grok ledger schema v2 spirit):

| Field | Requirement |
|---|---|
| `mode` | Must be `dispatched-agents` |
| `status` | `succeeded` only if all role dispatches succeeded and gate passes |
| `dispatches[]` | Per-role command/id, timestamps, exit codes, content hashes |
| `artifacts` | planner / generator / evaluator paths |
| `orientation_packet_hash` | Hash of packet at package open |
| `parent_run_id` | Links to Hermetic dispatch / digital-thread parent |

**Gate:** fail-closed package validation (e.g. `pge_gate --required`). Scaffold / artifact-only modes are bookkeeping only.

### Relationship to workflow-orchestration

P/G/E is a **normative specialization** of [workflow-orchestration](workflow-orchestration.md):

- Control program is deterministic (dispatch order + gates).
- Each step is a judgment-bearing agent under `⊑`.
- Evaluator is the **post-execution verification** limb made into a separate agent with fresh context (anti self-grade).
- Resource ceilings (repair loops, wall clock, token budget) attach to the control layer.

## Contribution 3 — Unified escalation table (oracle × morals)

Hermetic’s L0–L3 oracle and MxM’s CONFIRM/DENY/P1 must not be two competing stories.

| Event | Route |
|---|---|
| Ambiguous design choice inside plan | L1 → L2 Director (policy-bounded) |
| Scope expansion / peer-prime home / new surface | **Morals stop** — explicit human grant (not auto-oracle) |
| Force-push, mass delete, recovery/rollback | **DENY or CONFIRM** — never L1 best-effort |
| Accept despite failed verification | L2 refuse; L3 human only |
| Cross-prime task | Federation **and** prime-independence grant |
| Full-auto / unattended high blast | Explicit time-boxed grant object; default off |

**Principle:** ordinal escalation handles *judgment under uncertainty*; deontic catalogs handle *irreversible and out-of-scope classes*. Do not launder the second through the first.

## Work classification (operator decision rule)

```text
if scope unclear or outside authorized home:
    MxM stop → ask human
elif work is narrow (one-file / low blast):
    single agent under MxM + means floor
elif work is substantial (multi-file, ambiguous, long-run, governance-affecting):
    P/G/E required (dispatched)
    if needs parallel specialties or long multi-worker swarm:
        Hermetic roster + signal/gate
    else:
        sequential three-context dispatch is enough
elif product-architecture change:
    Eidolon/trace link + P/G/E + verify spine
```

## Memory planes (do not collapse)

| Plane | Role | Store examples |
|---|---|---|
| **Nous** (Hermetic) | Working swarm memory (director / shared / shell) | FTS memories, worker shells |
| **MxM Memory** | Identity continuity, earned feedback, next-session | `memory/wiki`, session wrap |
| **Eidolon / digital-thread** | Product evidence and phase audit | phases, artifacts, reviews, ledger |
| **Graduation** | Lessons that become law | methods → morals → means/safety catalog |

Memory is **never** law. Law graduates deliberately.

## Topology (Pattern B+ for Hermetic)

```text
aide-canon/
  constructs/mxm/          # archetype law (prose + ADRs)
  patterns/mxh-p-synthesis.md   # this composition pattern
  patterns/workflow-orchestration.md
  vision-strategy/analysis/hermetic-engagement/  # engagement trail

ologos-repos/Hermetic/     # out-of-tree swarm means (Pattern B+)
  — does not import peer prime MxM at runtime

prime homes (e.g. grok-console, thinx, ologos-ai)/
  construct/               # each prime's own MxM
  construct/means/         # safety floor + adapters
  sandbox/pge/<slug>/      # claimable packages
  optional hermetic adapter (port/subprocess — copy, don't couple)
```

**P10/P12-class deployments:** port useful modules into the prime’s tree; do not soft-link Hermetic or peer constructs as runtime law.

## Phased adoption (normative recommendation)

| Phase | Deliverable | Depends on Hermetic? |
|---|---|---|
| **0 — Lens** | Mapping doc (this pattern) + package↔surface table | No |
| **1 — Packet** | Orientation packet built from local `construct/*` for every delegated role | No |
| **2 — DAG** | P/G/E as signal/gate (in-process or Hermetic MCP) | Optional |
| **3 — Floor bridge** | Worker tools share DENY/CONFIRM catalog with prime means | Optional |
| **4 — Swarm means** | Multi-worker dispatch when sequential P/G/E is the bottleneck | Yes |
| **5 — Eidolon link** | Package acceptance ↔ product requirement/phase | Yes (or local PLM) |
| **6 — Federation** | Multi-prime with per-prime MxM + explicit grants | Yes |

**Do not start at full Hermetic in-tree.** Start at **packet + gate + DAG**. Hermetic is the multi-worker backend when justified.

## Anti-patterns

1. **MxM wallpaper** — swarm runs; morals only in README.  
2. **Hermetic-as-MxM** — rename packages without orientation packets.  
3. **Fake P/G/E** — one context fills three files; ledger still claims success.  
4. **Shared MxM for all primes** — fusion failure domain.  
5. **Always-on P/G/E** — ceremony tax; operators skip the whole stack.  
6. **Federation = authorization** — network reach ≠ scope grant.  
7. **Nous overwrites morals** — memory treated as permission.  
8. **Silent `/auto`** — unattended high blast without grant object.

## Conformance

### Behavioral (required)

An implementation is **MxH-P conformant** only if all hold:

1. **Orientation** — every delegated worker/role receives an MxM-shaped orientation packet (or equivalent structured envelope) at spawn.  
2. **Refinement** — child access/tools/workspace ⊆ parent envelope; gates/verification are not weaker than parent.  
3. **Claim discipline** — “P/G/E succeeded” requires dispatched distinct role contexts + fail-closed package gate; artifact-only is non-claimable.  
4. **Access asymmetry** — Planner and Evaluator cannot mutate the product tree under normal grant (mechanical preferred; prose-only is partial conformance).  
5. **Escalation split** — irreversible/out-of-scope classes use deontic stop/confirm; ordinal oracle is not used to bypass them.  
6. **Proportionality** — classification rule exists: narrow work is not forced through full swarm P/G/E.  
7. **Prime independence** (multi-prime only) — federation does not import peer morals/means as binding law.

**Partial conformance** is allowed and should be labeled:

| Label | Meaning |
|---|---|
| **MxH-P/core** | Packet + P/G/E claim discipline + refinement (no Hermetic) |
| **MxH-P/swarm** | Core + Hermetic signal/gate multi-worker |
| **MxH-P/full** | Swarm + shared safety catalog + Eidolon/thread link + grant-gated full-auto policy |

### Schema (recommended)

- Orientation packet schema version field  
- P/G/E ledger with `mode`, `dispatches[]`, artifact hashes, `orientation_packet_hash`  
- Parent FK to orchestration/digital-thread run id  

### Interface (optional)

- Hermetic MCP tools for package open / signal emit / gate evaluate  
- CLI: `pge_package --dispatch`, `pge_gate --required`  

## Reference implementations (fragmentary today)

| Fragment | Where | MxH-P role |
|---|---|---|
| MxM construct + operator homes | `constructs/mxm/`; e.g. `ologos-repos/grok-console` `construct/` | Constitution altitude |
| Hermetic | `ologos-repos/Hermetic` (Pattern B+) | Swarm means |
| P/G/E dispatched bag | ologos-grok `scripts/pge_*`, `construct/means/agents/`, Morals P13 | Claimable delivery |
| Workflow-orchestration exemplar | Claude Code Workflow (see exemplar-tracking) | Control-plane supertype |
| Engagement trail | `vision-strategy/analysis/hermetic-engagement/` | Why packets > renames |

No single system is **MxH-P/full** as of this writing. The pattern is **ahead of full realization** by design (same posture as workflow-orchestration’s envelope lattice honesty).

## VSOK implications

| Slot | Implication |
|---|---|
| **Strategy** | Compose orientation (MxM), swarm means (Hermetic), and claimable delivery (P/G/E) rather than picking one as the whole answer. |
| **Objectives** | Land MxH-P/core on operator primes (packet + gate); Hermetic multi-worker only when sequential P/G/E saturates. |
| **Key Results** | Orientation packet utilization; claimable package rate vs scaffold; DENY/CONFIRM shared catalog coverage; zero silent full-auto incidents. |

## Related

- [ADR-EA-0028](../decisions/ADR-EA-0028-introduce-mxh-p-synthesis-pattern.md) — introduce this pattern  
- [ADR-EA-0027](../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md) — workflow-orchestration  
- [ADR-EA-0022](../decisions/ADR-EA-0022-pattern-bplus-and-canonical-aeon-refimpls.md) — Hermetic Pattern B+  
- [ADR-EA-0005](../constructs/mxm/decisions/ADR-EA-0005-clarify-mxm-archetype.md) — MxM scale-invariant archetype  
- [ADR-EA-0009](../decisions/ADR-EA-0009-introduce-digital-thread-pattern.md) — digital-thread  
- [hermetic-engagement/](../vision-strategy/analysis/hermetic-engagement/) — #38–#40 trail  
- [exemplar-tracking/hermetic/](../vision-strategy/analysis/exemplar-tracking/hermetic/)  

## Provenance

- Synthesis discussion (ologos-grok session, 2026-07-13): evaluation of MxM, MxM+P/G/E, Hermetic, and the composite stack.  
- Canon priors: Hermetic engagement #38–#40 (2026-05-22); workflow-orchestration ADR-EA-0027 (2026-06-01); MxM Methods ADR-EA-0026.  
- Authoring altitude: operator synthesis → canon pattern (this file) under explicit human direction to land under `aide-canon`.
