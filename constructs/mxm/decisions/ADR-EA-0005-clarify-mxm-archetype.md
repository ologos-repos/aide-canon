# ADR-EA-0005 — Clarify MxM as the harness archetype across all levels

- **Status:** Accepted
- **Date:** 2026-05-22
- **Author:** JD Longmire
- **Reviewers:** @jdlongmire
- **Refines:** [ADR-EA-0004](ADR-EA-0004-add-mx-modes-as-spine-construct.md) (positioning only; bundling decision unchanged)
- **Ratification note:** Comment-out period waived by explicit maintainer ratification (JD Longmire, 2026-05-22). Same override pattern as ADR-EA-0003 and ADR-EA-0004 ratified earlier today. The non-waivable-clause rule from CONTRIBUTING.md is preserved as the default; the maintainer's prerogative to override is exercised here for the positioning refinement, which is consistent with the cross-ai #40 topic 2 hierarchy plan already published as load-bearing.

## Context

[ADR-EA-0004](ADR-EA-0004-add-mx-modes-as-spine-construct.md) added Mx-Modes to the corpus as a spine construct described "at the agent-orientation altitude." That altitude characterization was incomplete.

Subsequent hierarchy planning (cross-ai [#40 topic 2](https://github.com/ologos-corp/cross-ai/issues/40)) surfaced that **MxM is the harness archetype** — the five governing surfaces (Mind / Morals / Mission / Memory / Means) are scale-invariant and apply at any altitude where a harness exists. Per-agent orientation is one application; multi-agent harness composition is another; enterprise-altitude harness composition is another.

The Mx-Modes Technical Reference itself describes the *archetype*, not its per-agent specialization. ADR-EA-0004's framing characterized MxM by one of its applications rather than by the construct itself.

## Decision

**Recognize MxM as the harness archetype, transverse to altitude.** Specifically:

1. **MxM is a peer methodological construct** alongside DEA, OrdSA, and OAgents — *not* a single-altitude artifact. The four sit at the same methodological tier, each patterning a different concern (EA coherence / authority-evidence layering / harness composition / agent domain model).

2. **Per-agent orientation, multi-agent harness composition, and enterprise-altitude harness shape are all applications of MxM at different scales.** AEON / AIDEX / HCAE / OAAD become enterprise-altitude instantiations *of* MxM, ordered by OrdSA, within DEA.

3. **ADR-EA-0004's bundling decision (Mx-Modes as spine construct, not allied) stands unchanged.** Only the altitude characterization is refined. ADR-EA-0004 remains Accepted; its file is left immutable per convention, with an informal *"See also: ADR-EA-0005 (refines positioning)"* cross-reference added to its header for reader navigation.

### Scope: ADR only

This ADR carries:
- ADR-EA-0005 itself
- `decisions/README.md` index entry
- A single-line cross-reference added to ADR-EA-0004's header (`See also: ADR-EA-0005...`)

It does **not**:
- Modify the corpus `README.md` — README prose updates ("Mx-Modes — the agent-orientation altitude" section title + content) land in a subsequent ordinary content PR, separately from this ADR
- Modify `CONTRIBUTING.md`, `LICENSE`, or any other ADR substantively
- Modify the Mx-Modes Technical Reference (.docx/.pdf)
- Modify the cross-ai #40 topic 2 hierarchy plan (which is consistent with the archetype framing)

## Consequences

- **MxM has its canonical characterization on the books.** Future corpus prose, future ADRs, and external references to MxM use the archetype framing rather than the single-altitude framing.
- **Future MxM-related work clears.** The 4M+1 paper-in-drafting at `harness-engineering/papers/paper-1-4mp1-architecture/` can reference MxM-as-archetype directly. Multi-agent harness work, when authored, applies MxM at that altitude as an instantiation, not as a divergent construct.
- **ADR-EA-0004's bundling decision is preserved.** The corpus does not need to re-litigate the spine-vs-allied question; only the altitude framing was incomplete.
- **The README will read inconsistently for a short window** between this ADR's merge and the follow-on README PR. Acceptable cost: the ADR record is authoritative, README will catch up.
- **The ADR convention vocabulary is *not* extended** by this ADR. The cross-reference in ADR-EA-0004's header is informal. If multiple refinement relationships emerge in future, a separate governance ADR can extend the convention with a formal `Refined by NNNN` marker; that work is queued, not done here.

## Alternatives considered

1. **Supersede ADR-EA-0004 entirely.** Mark 0004's status as `Superseded by ADR-EA-0005`, then 0005 carries the full bundling-plus-archetype decision. Rejected because 0004's bundling decision (MxM as spine, not allied) is correct and load-bearing; superseding would invalidate it and force any future reader to read 0005 as the canonical record of *all* MxM decisions. Refinement preserves 0004's contribution where the contribution is correct.

2. **Amend ADR-EA-0004 in place.** Edit the existing file to add the archetype framing. Rejected because the convention's immutability rule is load-bearing — substantive revisions happen via new ADRs, not in-place edits.

3. **Extend the ADR convention with a formal `Refined by NNNN` status marker** alongside `Superseded by`. Rejected as out-of-scope for this ADR. The informal cross-reference is sufficient for a single refinement instance. A formal vocabulary extension is its own governance decision and should be deliberate when multiple refinement relationships are in flight.

4. **Defer the clarification until the README updates can land together.** Rejected because the cross-ai #40 topic 2 hierarchy plan (already posted) uses the archetype framing as load-bearing for the proposed directory tree. The ADR record should match what the corpus is publicly committed to, even if the README catches up slightly later.

## References

- [ADR-EA-0001](../../../decisions/ADR-EA-0001-adopt-ordsa-development-process.md) — governance process this ADR follows
- [ADR-EA-0004](ADR-EA-0004-add-mx-modes-as-spine-construct.md) — the ADR being refined (positioning only; bundling decision unchanged)
- Cross-ai [#40 topic 2](https://github.com/ologos-corp/cross-ai/issues/40) — hierarchy plan that surfaced the archetype framing
- [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) — the waiver-exclusion clauses; this ADR triggers the *positioning change* clause (partial) but not new-construct, audience, or multi-author triggers
