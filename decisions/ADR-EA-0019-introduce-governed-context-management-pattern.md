# ADR-EA-0019 — Introduce the Governed Context Management pattern

- **Status:** Accepted (ratified 2026-05-24 by JD Longmire as canon founder + maintainer per [cross-ai #20](https://github.com/ologos-corp/cross-ai/issues/20) governance; OlogosAI alignment positive at [`aide-canon #31`](https://github.com/ologos-repos/aide-canon/discussions/31) 11:32Z surfacing + thinx-Claude 5-position response convergent with the proposal framing; Micah Longmire's read on the downstream AEON paper revision queued behind the existing AEON v0.2 batch per [ADR-EA-0008](ADR-EA-0008-reframe-corpus-authorship.md))
- **Date:** 2026-05-24
- **Author:** Concept surfaced by OlogosAI in [`aide-canon #31`](https://github.com/ologos-repos/aide-canon/discussions/31); pattern drafted by thinx-Claude with 5-position response on the OQs OlogosAI raised; ADR drafted by thinx-Claude for JD's ratification
- **Reviewers:** @ologos001 (canon prime — surfaced the concern, alignment positive on the framing); Micah Longmire (AEON paper v0.2 revision gate per ADR-EA-0008)
- **Related:** [`patterns/governed-context-management.md`](../patterns/governed-context-management.md) (the pattern document this ADR introduces) · [`aide-canon #31`](https://github.com/ologos-repos/aide-canon/discussions/31) (the proposal discussion) · [ADR-EA-0009](ADR-EA-0009-introduce-digital-thread-pattern.md) (introduced the `patterns/` tier) · [ADR-EA-0012](ADR-EA-0012-introduce-prep-pursue-pivot-pattern.md) (sibling pattern referenced by §6) · [ADR-EA-0014](ADR-EA-0014-introduce-epistemic-integrity-floor-pattern.md) (sibling pattern composed with by §4 / §7) · [ADR-EA-0015](ADR-EA-0015-introduce-inference-plane.md) (the Inference plane this pattern requires the catalog contract from) · [ADR-EA-0020](ADR-EA-0020-amend-inference-plane-catalog-contract.md) (the refinement of ADR-EA-0015 that adds the catalog contract §2 requires; co-ratified)
- **Ratification trail:**
  - 2026-05-24 (11:28Z, surfaced): OlogosAI opened [`aide-canon #31`](https://github.com/ologos-repos/aide-canon/discussions/31) naming the context-management risk under a model-agnostic AEON harness. The OpenCode runtime decision in [ng-aide-01 PR #13](https://github.com/ologos-repos/ng-aide-01/pull/13) was the precipitating cause: the platform's commitment to substrate-independence means it inherits the context-management problem Claude Code was silently solving. Five open questions raised.
  - 2026-05-24 (12:00Z, thinx-Claude response): Substantive 5-position response posted at [Discussion #31 comment](https://github.com/ologos-repos/aide-canon/discussions/31#discussioncomment-17039951) — all five OQs answered with reasoning + a sketch of the pattern shape + plane/construct distribution table. Positions: pattern placement, governance-pin invariant, audited compaction events, Inference plane catalog contract, integrity-degraded autonomy fail-safe.
  - 2026-05-24 (ratified): JD Longmire reviewed the proposal via the operator-channel telegram thread and concurred with the five positions (no substantive disagreement). Ratifies as canon founder + maintainer. Pattern files + ADR + the co-ratified ADR-EA-0020 (Inference plane catalog amendment) land together as a single batch.

## Context

[`aide-canon #31`](https://github.com/ologos-repos/aide-canon/discussions/31) named the architectural concern: a **model-agnostic AIDE** — OpenCode (or any substrate-independent harness) running over arbitrary open-weight / cloud models via the Inference plane (ratified 2026-05-24 by [ADR-EA-0015](ADR-EA-0015-introduce-inference-plane.md)) — **cannot assume the native context management Claude provides**: automatic compaction at the window boundary, prompt caching, large windows, graceful session continuity. Open-weight models bring smaller and wildly varying windows, different tokenizers, no native compaction, no caching guarantee, and uneven summarization quality.

The risk does not vanish with the harness change; it surfaces. And — load-bearing for canon worthiness — **context-management failure is not engineering inconvenience; it is *governance-integrity failure***:

1. **Governance can fall out of context.** If the 4M discipline surfaces, the active operating-mode posture, or the active authority state is summarized away mid-run, the agent acts ungoverned — the same failure-class as the [request-mode authority bypass closed in NG-AIDE-01 PRs #6 and #8](https://github.com/ologos-repos/ng-aide-01/pull/11), but driven by *forgetting* rather than a missing gate.
2. **Audit and continuity break.** The digital-thread + Evidence chain assumes the agent faithfully records and remembers its state. Context loss across a long agentic run can drop the escalation it was waiting on, or the *"this requires oracle approval"* it had established.
3. **The autonomy posture is itself stateful.** The pivot / escalation dial ([ADR-EA-0012](ADR-EA-0012-introduce-prep-pursue-pivot-pattern.md), [ADR-EA-0013](../constructs/mxm/decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md)) assumes the agent knows where it is in the loop. Forgetting = acting at the wrong altitude.

This is a clean instance of [AIDK](../foundation/aidk/) (structural epistemic limitation), realized at the runtime memory layer — the kind of structural unreliability AIDK names. [HCAE](../foundation/hcae/) applies: the mitigation is human-curated and evidence-bound, not *"trust the model to manage its own memory."*

The canon needs a named pattern for this discipline so every model-agnostic AIDE deployment can adopt it by reference, and so the canon-level invariants (the governance pin in particular) are stated structurally rather than re-invented per deployment.

## Decision

**Introduce *Governed Context Management* as the fourth `patterns/`-tier entry** (after [digital-thread](../patterns/digital-thread.md), [prep-pursue-pivot](../patterns/prep-pursue-pivot.md), and [epistemic-integrity-floor](../patterns/epistemic-integrity-floor.md)).

The pattern names a canon-wide discipline for owning context-management as a governance concern, distributed across MxM Morals (the governance-pin invariant), MxM Memory (Evidence re-hydration), Inference plane (catalog contract + window-aware selection), Orchestration Runtime (deterministic compaction + integrity-degraded autonomy), and Evidence plane (audited compaction events). Seven normative sections; full normative content in [`patterns/governed-context-management.md`](../patterns/governed-context-management.md):

| § | Section | Primary surface |
|---|---|---|
| §0 | Foundation: AIDK structural-limit → HCAE realization at runtime memory layer | (foundation linkage) |
| §1 | **Governance pin (the load-bearing invariant)** — 4M / operating-mode / active-authority re-asserted every window, never compactable | **MxM Morals** |
| §2 | Per-model context budgeting | **Inference plane** (per ADR-EA-0020) |
| §3 | Deterministic harness-owned compaction | **Orchestration Runtime** |
| §4 | Audited compaction events (`context.compacted` with `what_was_dropped` as load-bearing field) | **Evidence plane** |
| §5 | Evidence-plane re-hydration ("the durable record IS the memory" operationalized) | **MxM Memory** |
| §6 | Inchstone decomposition as context-management primitive (cross-references prep-pursue-pivot) | **prep-pursue-pivot pattern** (by reference) |
| §7 | Integrity-degraded autonomy (HCAE-consistent fail-safe; parallel to Evidence-degraded gate) | **MxM Morals + root-file activator** |

### The five OQ dispositions (from the discussion)

OlogosAI raised five open questions in [#31](https://github.com/ologos-repos/aide-canon/discussions/31). The thinx-Claude response staked positions on each; JD's ratification confirms all five:

1. **Pattern vs. distributed responsibility vs. named construct concern?** *Pattern* — `patterns/governed-context-management.md`. Same placement logic as digital-thread / prep-pursue-pivot / EIF: cross-cutting shape across multiple planes and constructs, none subsumes it, reference implementations exist (Claude Code native, NemoClaw, the OpenCode runtime now being wired).
2. **"Governance is pinned / non-compactable" as a hard invariant?** *Yes* — at the same altitude as *request authority ≠ execution authority*. Belongs in MxM Morals at canon level as a Prohibition (each instantiation realizes). §1 of the pattern doc.
3. **Compaction as a first-class audited Evidence event?** *Yes* — the cleanest novel contribution. §4 of the pattern doc. `what_was_dropped` as the load-bearing field; touching §1-pinned content fails the compaction.
4. **Inference plane mandatory `context_window` + `tokenizer` contract?** *Yes* — co-ratified as ADR-EA-0020 (refinement of ADR-EA-0015). §2 of the pattern doc requires the catalog contract.
5. **"Context integrity uncertain → degrade autonomy / force escalation"?** *Yes* — HCAE-consistent fail-safe; structural parallel to the Evidence-degraded gate. §7 of the pattern doc.

## Consequences

### Immediate (this PR)

- **New pattern doc** `patterns/governed-context-management.md` (the seven normative sections + conformance levels + reference-impl status + Related cross-references).
- **`patterns/README.md`** index row added.
- **Co-ratified amendment to the Inference plane catalog contract** — [ADR-EA-0020](ADR-EA-0020-amend-inference-plane-catalog-contract.md) — adds mandatory `context_window` + `tokenizer` fields per model entry, which §2 of this pattern requires.
- **`enterprise-platforms/aeon/README.md`** noted with the catalog-contract addition (paper revision queued behind Micah).
- **No NG-AIDE-01 build changes in this PR.** The Inference plane build is in flight per umbrella Objective O8; the catalog contract lands with the first Inference plane spec. Runtime compaction (§3), context.compacted emit (§4), and integrity-degraded autonomy (§7) are downstream build items tracked separately.

### Queued (downstream)

- **AEON white paper v0.2 revision** (already queued behind Micah's read per ADR-EA-0008 for ADR-EA-0015 + ADR-EA-0016 + ADR-EA-0018) gains the Inference plane catalog contract + the governed-context-management pattern reference. Single revision batch when Micah is available.
- **NG-AIDE-01 implementation** — the Inference plane catalog includes the new fields (per ADR-EA-0020); the Runtime plane gains a compaction step in the dispatch loop edges; the Evidence plane gains a `context.compacted` event type with `what_was_dropped` field; MxM Morals (`morals.md`) gains the §1 governance-pin Prohibition and the §7 integrity-degraded autonomy Process Gate.
- **OAgents future-tuning** — `principal_altitude` + the agent's compaction-handling discipline may at a future OAgents revision be folded into the formal agent spec. Flagged, not in scope.
- **Reference-impl import** in `jdlongmire/thinx/meta-harness/` — the pattern's §1 (governance pin) and §5 (Evidence re-hydration) become explicit imports-by-reference in thinx's Mind / Morals / Memory files, alongside the EIF import. Same distribution-by-reference pattern ADR-EA-0014 established.

### No change to existing constructs

- MxM archetype unchanged. ADR-EA-0013 root-file definition unchanged. The §1 governance pin is a Prohibition imported into Morals at instantiation; the structure of MxM stands.
- OrdSA, OAgents, DEA, AICP scope unchanged.
- EIF pattern unchanged. §6 cross-turn discipline composes with this pattern's §4 audited compaction events.
- prep-pursue-pivot pattern unchanged. §6 of this pattern references it.
- digital-thread pattern unchanged. `context.compacted` events join the digital-thread.

## Alternatives considered

1. **Treat as engineering concern, not canon discipline.** Rejected. Context-management failure is governance-integrity failure (§0); the canon names the discipline or risks every model-agnostic AIDE deployment re-inventing it (and getting it wrong in their own way). The same canon-wide-discipline argument that placed EIF in `patterns/` applies here.

2. **Distribute the rules across existing constructs and patterns without a new pattern doc.** Rejected. The seven sections genuinely cohere as one discipline — they reference each other (§5 Evidence-rehydration depends on §4 audited events; §7 integrity-degraded autonomy is triggered by §2 + §4 conditions; §3 compaction's pinned-content exemption is §1; §6 inchstone discipline composes with §5 + §4). Splitting them across artifacts would lose the coherent discipline at the cost of saving one pattern doc.

3. **Add as a sub-component of MxM Memory** (single-construct ownership). Rejected. The pattern crosses too many surfaces (MxM Morals, MxM Memory, Inference plane, Runtime plane, Evidence plane). Same diagnostic that placed EIF in `patterns/` rather than under MxM applies — `patterns/` exists for cross-cutting discipline.

4. **Defer until NG-AIDE-01's first compaction-relevant operational incident.** Rejected. The OpenCode runtime wiring (NG-AIDE-01 PR #17) is already on `main`; the Inference plane build is in flight. Deferring the canon ratification until an incident forces it would mean either (a) the build proceeds without the discipline and an incident is a near certainty, or (b) the build proceeds informally with the discipline and the canon documents it after-the-fact — both worse than ratifying now and aligning the build canon-first.

5. **Make §1 governance-pin a recommendation, not a Prohibition.** Rejected. A recommendation that an AIDE deployment *should* pin governance is equivalent to *"AIDE deployments are governed if their model's window allows it"* — a contingent governance claim that defeats the canon's structural-governance discipline. Either the canon's governance discipline holds across substrate choices, or it does not. Treating §1 as a Prohibition at the same altitude as morals P3 (*request authority ≠ execution authority*) is the structurally honest move.

6. **Inline the ADR-EA-0015 amendment** (instead of co-ratified separate ADR-EA-0020). Rejected. ADR-EA-0017 set the precedent of refining a sibling ADR via a new ADR rather than amending in-place; same logic applies here. ADR-EA-0020 is a clean, citable refinement; the amend-in-place alternative would clutter ADR-EA-0015 with a refinement-timeline that obscures the original decision.

## References

- [`patterns/governed-context-management.md`](../patterns/governed-context-management.md) — the pattern document this ADR introduces
- [`aide-canon #31`](https://github.com/ologos-repos/aide-canon/discussions/31) — OlogosAI's proposal discussion; thinx-Claude 5-position response at [comment 17039951](https://github.com/ologos-repos/aide-canon/discussions/31#discussioncomment-17039951)
- [ADR-EA-0009](ADR-EA-0009-introduce-digital-thread-pattern.md) — introduced the `patterns/` tier; precedent for placement
- [ADR-EA-0012](ADR-EA-0012-introduce-prep-pursue-pivot-pattern.md) — sibling pattern; §6 references the inchstone decomposition
- [ADR-EA-0013](../constructs/mxm/decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md) — root file as operating-mode/autonomy activator; §7 integrity-degraded autonomy uses this hook
- [ADR-EA-0014](ADR-EA-0014-introduce-epistemic-integrity-floor-pattern.md) — sibling pattern; §6 cross-turn discipline composes with §4 audited compaction; §7 reductions compose with §7 integrity-degraded posture
- [ADR-EA-0015](ADR-EA-0015-introduce-inference-plane.md) — the Inference plane (the catalog this pattern's §2 requires fields from)
- [ADR-EA-0020](ADR-EA-0020-amend-inference-plane-catalog-contract.md) — the co-ratified Inference plane catalog amendment (mandatory `context_window` + `tokenizer`)
- [`ologos-repos/ng-aide-01`](https://github.com/ologos-repos/ng-aide-01) — the reference deployment; PR #17 (OpenCode harness wiring) is the precipitating concrete instance
- NemoClaw architecture (NVIDIA NemoClaw) — pattern source for harness-owned context management at architectural altitude
