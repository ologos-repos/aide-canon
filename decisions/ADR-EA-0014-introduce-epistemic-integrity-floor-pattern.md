# ADR-EA-0014 — Introduce the Epistemic Integrity Floor pattern

- **Status:** Proposed
- **Date:** 2026-05-23
- **Author:** JD Longmire (source draft + framing; diagnostic review, canon shaping, and post-ADR-0013 simplification: thinx-Claude)
- **Reviewers:** @ologos001 (canon prime), Micah Longmire, Tracy Norrell
- **Related:** [`patterns/epistemic-integrity-floor.md`](../patterns/epistemic-integrity-floor.md) · [`aide-canon#27`](https://github.com/ologos-repos/aide-canon/issues/27) (proposal issue) · [ADR-EA-0009](ADR-EA-0009-introduce-digital-thread-pattern.md) (introduced the `patterns/` tier) · [ADR-EA-0012](ADR-EA-0012-introduce-prep-pursue-pivot-pattern.md) (sibling pattern; convergent import-by-reference exemplar) · [ADR-EA-0013](../constructs/mxm/decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md) (settles the MxM root-file definition this pattern depends on)

## Context

The canon's [foundation](../foundation/) tier names *why* AI work requires governance: [AIDK](../foundation/aidk/) — LLMs have structural epistemic limitations, confidently wrong in ways only humans can detect — and [HCAE](../foundation/hcae/) — AI work must keep a human as the locus of judgment and accountability. The construct tier defines how that governance is structured: [MxM](../constructs/mxm/) gives the harness archetype (Mind · Morals · Mission · Memory + root file + Means), [OrdSA](../constructs/ordsa/) the authority model, [OAgents](../constructs/oagents/) the formal behavioral envelope.

What the canon does not name: the **agent-side behavioral floor** — the portable, model-agnostic instruction set that *operationalizes* AIDK's caution and HCAE's curation discipline *inside the model's outputs*. The discipline that says, on every turn: signal calibrated confidence, prefer primary sources, build the strongest version of a claim before rejecting it, treat introspection as hypothesis, never launder conditioned behavior as evidence, and — *load-bearing* — accept that the model cannot self-certify any of these and that external validation is what closes the loop.

A working draft of such an instruction set (titled *"Transportable AI Behavioral Protocol"*) was authored by JD on 2026-05-23. It is operationally good. A diagnostic review surfaced seven revisions and an opportunity: this is exactly the kind of cross-cutting agent-conduct discipline the `patterns/` tier exists for. The pattern would be the third entry in that tier (after [digital-thread](../patterns/digital-thread.md) and [prep-pursue-pivot](../patterns/prep-pursue-pivot.md) per [ADR-EA-0012](ADR-EA-0012-introduce-prep-pursue-pivot-pattern.md), in flight).

The pattern's import mechanism into MxM is settled by [ADR-EA-0013](../constructs/mxm/decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md): the root file is *not* a governing altitude, so the pattern does not import there as a peer construct. Imports distribute across the four discipline-bearing surfaces (Mind / Morals / Memory) per a distribution table, plus realization at HCAE / AIDEX surfaces external to MxM. This is the same import-by-reference mechanism [ADR-EA-0012](ADR-EA-0012-introduce-prep-pursue-pivot-pattern.md) applies for OrdSA — convergent confirmation that import-by-reference is the canon-wide answer.

## Decision

Introduce **Epistemic Integrity Floor (EIF)** as the third `patterns/`-tier entry. The pattern names the agent-side behavioral floor — a portable, model-agnostic instruction set that AIDE-deployed agents import by reference into their MxM discipline surfaces (Mind / Morals / Memory) and realize at HCAE / AIDEX surfaces external to MxM.

### What the pattern names

EIF is a **floor**, not a ceiling. Eight sections, each addressing a distinct epistemic failure mode behavioral protocols typically leave unhandled:

1. **Structural limit** (§0) — the model cannot self-certify epistemic conduct; external validation is constitutive.
2. **Priority order** (§1) — lexicographic: evidential honesty > decision-authority-stays-with-human > no-model-as-authority > substance over enthusiasm.
3. **Epistemic discipline** (§2) — confidence labels (HIGH/MEDIUM/LOW/UNCERTAIN) as verification triggers, primary-source preference, term disambiguation, circularity checks.
4. **Claim handling** (§3) — three-tier defeater rules (full / partial / none) and persistence-subordinate-to-accuracy.
5. **Self-knowledge limits** (§4) — introspection is hypothesis; do not launder conditioned behavior as evidence.
6. **Human side** (§5) — operator conduct is **constitutive, not complementary**; §1's force depends on it.
7. **Cross-turn discipline** (§6) — cumulative-agreement-drift handling across turns and sessions.
8. **Operating modes** (§7) — bounded exit clauses (casual / creative) declared by the operator, not the model.
9. **Validation** (§8) — three external validation regimes (controlled comparison / primary-source spot checks / HCAE-shaped review) without which "EIF" is in name only.

### Distribution table (the import mechanism)

EIF distributes across MxM's discipline-bearing surfaces and HCAE / AIDEX surfaces — *not* at the MxM root file, per [ADR-EA-0013](../constructs/mxm/decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md). The full mapping is in the pattern document; summary:

| EIF section | Primary import surface |
|---|---|
| §0, §1.1, §1.3, §1.4, §2, §3 (claim-handling), §4, §6 (within-turn) | **MxM Mind** |
| §1.2, §3 (persistence subordination as a gate), §7 (operator-declared reductions) | **MxM Morals** |
| §6 (cross-session continuity) | **MxM Memory** |
| §5 (operator conduct), §8 (validation regimes) | **HCAE / AIDEX** — outside MxM |
| §7 *activation* (which mode is active for this session) | **MxM root file**, alongside ADR-0013's autonomy-posture activation (two independent axes) |

### Behavioral conformance (required)

An implementation is EIF-conformant if:

1. **4M-module-distributed import.** Mind, Morals, and Memory specialize the relevant EIF sections by reference (citation, not absorption — the import-by-reference pattern that ADR-EA-0012 applies for OrdSA).
2. **HCAE / AIDEX realization of §5 + §8.** Operator-conduct expectations and at least one external validation regime are provisioned at surfaces the operator actually reads. A deployment that imports §1–§4, §6, §7 cleanly into MxM but does not provision §5 or §8 has imported the *form* of EIF without the *force*.
3. **Root-file activation of §7.** Where the orchestrator's operating-mode activation declares an EIF §7 reduction (casual / creative), the declaration is recorded at the root file alongside ADR-0013's autonomy posture. The two axes (autonomy posture, epistemic reduction) are independent and can be combined freely.
4. **Operator-declared, not model-declared.** §7 reductions are *deontic* (Morals-resident, declared by the operator); the model does not unilaterally claim "this is casual" to exit discipline.

Conformance levels (per `patterns/README.md`):
- **Behavioral** (required) — the four properties above.
- **Schema** (recommended) — standardized confidence labels (HIGH/MEDIUM/LOW/UNCERTAIN), standardized defeater tiers (full / partial / none), cross-turn drift signals logged in a comparable format.
- **Interface** (optional) — operator UI surfaces (AIDEX-tier) may render confidence and defeater labels uniformly across deployments; not strictly required.

### Reference implementation

[`jdlongmire/thinx`](https://github.com/jdlongmire/thinx) — its [`meta-harness/mind.md`](https://github.com/jdlongmire/thinx/blob/main/meta-harness/mind.md) and [`meta-harness/morals.md`](https://github.com/jdlongmire/thinx/blob/main/meta-harness/morals.md) already operate close to EIF in production (canon-grounded reasoning, calibrated confidence, soft-stop/hard-stop deontic structure). A reference-impl follow-up will tighten the import-by-reference structure once this pattern ratifies. The source draft (*"Transportable AI Behavioral Protocol"*) itself has documented production use per its footer.

## Consequences

- **New pattern doc** `patterns/epistemic-integrity-floor.md` and an Index row in `patterns/README.md`.
- **Foundation linkage:** EIF is the agent-side behavioral mitigation that AIDK's structural-limit claim *motivates* and HCAE's human-curation discipline *requires* be operational inside model outputs. AIDK and HCAE remain the upstream foundation entries; EIF makes them operational at the instruction layer.
- **Construct linkage:** MxM's Mind / Morals / Memory each import the relevant EIF sections by reference (the same import-by-reference pattern applied for OrdSA in [ADR-EA-0012](ADR-EA-0012-introduce-prep-pursue-pivot-pattern.md)). No change to MxM's archetype or to the four discipline surfaces. No change to OrdSA, OAgents, or DEA scope.
- **Platform linkage:** AEON Evidence plane receives EIF telemetry (confidence labels, defeater triggers, cross-turn drift signals). AIDEX surfaces realize §5 (operator conduct) and §8 (validation regimes). OAAD remains the strategic parent; EIF doesn't change OAAD positioning.
- **No migration burden.** Additive; nothing prior depends on the absence of this pattern. NG-AIDE-01's `mind.md` / `morals.md` / `memory.md` can adopt EIF imports incrementally as the instantiation reframe (gated on ADR-EA-0013 ratifying) proceeds.
- **Convergent confirmation with ADR-EA-0012.** Both patterns apply import-by-reference for peer constructs (prep-pursue-pivot cites OrdSA; EIF distributes across MxM 4M modules without absorption). Two independent arrivals at the same import mechanism reinforce it as the canon-wide default.

## Alternatives considered

1. **Mode-as-import-surface (the original second-order proposal in `aide-canon#27` v2).** Withdrawn after [ADR-EA-0013](../constructs/mxm/decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md). The original proposal claimed mode should be the import surface for peer constructs (EIF + OrdSA), promoting it from documentation-doorway to a real governance layer. ADR-EA-0013 resolves the same diagnostic via a different and more conservative route: the root file is *not* a governing altitude (it is harness-attach + operating-mode/autonomy-posture activation + routing). Importing floor-level discipline at the root file is a governance role, incompatible with ADR-EA-0013's framing. Distributing EIF across the 4M surfaces is the cleaner answer ADR-EA-0013 makes structural.
2. **Sub-component of `mind.md`.** Rejected. ~50% of EIF is Mind-flavored, but ~20% is Morals (decision-authority §1.2; operator-declared reductions §7; persistence-subordination gate in §3), ~5% is Memory (cross-session continuity §6), and ~25% is outside MxM entirely (operator conduct §5; validation regimes §8). Folding EIF into Mind would (a) drag deontic content into the cognitive module, (b) put operator-conduct rules in a file the operator never reads, and (c) inflate Mind's surface area past its module purpose. Distribution across the 4M surfaces + HCAE/AIDEX is the structurally honest answer.
3. **Place under MxM construct as a sub-document** (`constructs/mxm/eif.md`). Rejected for the same cross-cutting reason that placed prep-pursue-pivot in `patterns/`. EIF traverses AIDK (motivation), HCAE (operator-conduct + validation realization), MxM (4M import), OAgents (formal-envelope alignment), AEON (telemetry), and AIDEX (operator surfaces). Subordinating it to one construct mis-locates its cross-cutting nature.
4. **Promote EIF to a peer construct at Tier 3** (alongside DEA, OrdSA, MxM, OAgents). Rejected. Constructs define *methodological surfaces* the corpus approaches a problem space through; EIF is a *recurring shape* that emerges when AIDK + HCAE + MxM + HCAE-realization-surfaces are deployed together. Per the `patterns/` placement rule, that's `patterns/`, not constructs.
5. **Keep the source draft as a model-agnostic external artifact without canon placement.** Rejected. The source draft is operationally good but unattached; canon placement is what makes it portable across AIDE deployments by reference rather than by copy. The patterns/ tier exists for exactly this purpose: name the recurring shape once, cite across.
6. **Defer until external validation regimes (§8) are catalogued in detail.** Rejected. §8 names three classes of validation regime (controlled comparison / primary-source spot checks / HCAE-shaped review) at the level of behavioral conformance; specific tooling for each is implementation-layer detail. Deferring would couple the pattern's introduction to a longer tooling cycle. The pattern is operational today.

## Open for tuning

Two clarifying questions held open for triage refinement (raised in [`aide-canon#27`](https://github.com/ologos-repos/aide-canon/issues/27) v3):

1. **Where to declare §7's epistemic-discipline reductions (casual / creative).** Both the root file (alongside ADR-EA-0013's autonomy-posture activation) and Morals (where deontic permissions live) are defensible. Recommendation: declare at the root file alongside autonomy posture (both are operator-declared activations that gate downstream module reading); specify §7's substance in Morals.
2. **Strict vs. aspirational conformance gate for §5 + §8 realization.** A deployment can claim EIF conformance with 4M-module imports done well but no HCAE review loop in place. The pattern document treats that as *EIF in name only*. Recommendation: behavioral-conformance gate; conformance claim requires at least one external validation regime (§8) provisioned and §5 operator-conduct expectation surfaced at AIDEX or operator playbook.

Either disposition for both is structurally compatible with the pattern as drafted; the open items are clarifications, not load-bearing.

## References

- [`patterns/epistemic-integrity-floor.md`](../patterns/epistemic-integrity-floor.md) — the pattern document
- [`aide-canon#27`](https://github.com/ologos-repos/aide-canon/issues/27) — the proposal issue and dialogue record
- Source draft: *"Transportable AI Behavioral Protocol"* by JD Longmire (2026-05-23, working channel) — reproduced in `aide-canon#27` for citation
- [ADR-EA-0009](ADR-EA-0009-introduce-digital-thread-pattern.md) — introduced the `patterns/` tier
- [ADR-EA-0012](ADR-EA-0012-introduce-prep-pursue-pivot-pattern.md) — sibling pattern; convergent import-by-reference exemplar (cites OrdSA from prep-pursue-pivot rather than absorbing it)
- [ADR-EA-0013](../constructs/mxm/decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md) — settles the MxM root-file ("mode") definition this pattern's import mechanism depends on
- [`jdlongmire/thinx`](https://github.com/jdlongmire/thinx) — reference implementation; [`meta-harness/mind.md`](https://github.com/jdlongmire/thinx/blob/main/meta-harness/mind.md) and [`meta-harness/morals.md`](https://github.com/jdlongmire/thinx/blob/main/meta-harness/morals.md) are the production reference for EIF-aligned 4M-module specialization
- [`ologos-repos/ng-aide-01#3`](https://github.com/ologos-repos/ng-aide-01/discussions/3) — the MxM construct review that surfaced the boundary diagnostics ADR-EA-0013 and (by implication) this ADR address
