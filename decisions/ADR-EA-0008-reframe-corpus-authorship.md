# ADR-EA-0008 — Reframe corpus authorship as JD Longmire and Micah Longmire (co-authored)

- **Status:** Accepted
- **Date:** 2026-05-22
- **Authors:** JD Longmire, Micah Longmire
- **Reviewers:** @jdlongmire
- **Refines:** [ADR-EA-0004](../constructs/mxm/decisions/ADR-EA-0004-add-mx-modes-as-spine-construct.md) §Decision item 2 (principal-author-led + per-construct attribution). The per-construct attribution discipline is preserved; the corpus-level identity is broadened from sole-principal to joint co-authorship.
- **Ratification note:** Comment-out period waived by explicit maintainer ratification (JD Longmire, 2026-05-22). Same override pattern as ADR-EA-0003 / 0004 / 0005 / 0007 ratified earlier today. Basis: sole-maintainer status, in-session directive from JD to give Micah equal corpus-level credit, and the refinement being a positioning correction rather than a new construct or scope expansion.

## Context

[ADR-EA-0004 §Decision item 2](../constructs/mxm/decisions/ADR-EA-0004-add-mx-modes-as-spine-construct.md) codified the corpus's authorship pattern as principal-led with per-construct attribution:

> "Authorship is per-construct, principal-led. The corpus identity remains **JD Longmire-led**: he is principal author of all constructs in the spine, including Mx-Modes. Mx-Modes is specifically marked as co-authored with Micah Longmire wherever it appears. The other constructs remain sole-authored. The corpus README's intro continues to name JD as principal author; the per-construct attribution carries the joint-authorship signal where it applies."

That framing reflected the visible artifact-authorship at the time: JD as sole-author of DEA / AEON / AIDEX / OAAD; JD + Micah jointly on Mx-Modes; Micah sole-author of Theseus (allied, not spine).

The framing was correct at the artifact level. **It was incomplete at the corpus level.**

In practice, the corpus's intellectual content emerges from continuous collaboration between JD and Micah — concepts and ideation are joint, with JD as the principal generator of the AIDE-specific artifacts. Treating Micah as "co-author of one construct" understates the collaborative nature of the corpus's identity as a whole. A reader citing the corpus as "Longmire 2026" rather than "Longmire & Longmire 2026" misrepresents the source of the work.

This ADR refines the corpus-level identity to match the working reality without disturbing the per-artifact authorship that ADR-EA-0004 correctly established.

## Decision

**The corpus's identity is jointly authored by JD Longmire and Micah Longmire.** Specifically:

1. **Corpus-level authorship is joint.** The canon README intro, citation block, and any other corpus-identity surface (e.g., LICENSE attribution lines, citation files when added) name both authors. Standard citation form: *Longmire, J. D., & Longmire, M. (2026). AI-enabled Digital Ecosystem (AIDE) canon …*

2. **Per-artifact authorship is preserved as-is.** Existing artifacts retain their established author attribution at the artifact level (see e.g. `constructs/mxm/` which records the joint authorship at the construct README; foundation artifacts which cite the upstream Zenodo DOIs with their own author records). The corpus-level joint-authorship does **not** retroactively claim joint authorship of artifacts that were sole-authored by one of the co-authors.

3. **ADR-EA-0004 §Decision item 2 is refined, not superseded.** The principal-author + per-construct attribution pattern remains the *artifact-level* discipline. The *corpus-level* identity broadens to joint. ADR-EA-0004 stays Accepted; this ADR sits alongside as a positioning refinement, the same pattern ADR-EA-0005 used to refine ADR-EA-0004's altitude characterization.

4. **Future artifact authorship is recorded per-artifact at the artifact's location.** Some future artifacts may be JD-sole-authored, some Micah-sole-authored, some jointly authored. The corpus-level identity does *not* presume any particular per-artifact authorship pattern.

### Scope: ADR + canon README + citation block

This ADR's PR carries:

- ADR-EA-0008 itself + `decisions/README.md` index entry
- Canon README intro paragraph reframed to name both authors at the corpus level
- Canon README citation block reframed to standard joint-author form
- Canon README footnote pointing readers at this ADR for the corpus-vs-artifact authorship discipline

It does **not**:

- Modify ADR-EA-0004 (artifact-level discipline preserved; ADR remains immutable)
- Edit per-artifact authorship blocks (those are recorded at the artifact level; corpus-level change does not propagate downward)
- Edit existing published artifacts (Zenodo deposits keep their original author records; this is corpus-level identity, not retroactive per-artifact reattribution)
- Edit retirement banners on archived `osa-ai-org/*` source repos (historical; sole-principal framing was correct at the time the retirement banner was authored)

A **follow-on audit task** is queued: walk every artifact in the canon (foundation, constructs, enterprise-platforms, mode-alpha, vision-strategy) where author attribution appears, and add Micah where the working pattern was joint. Medium priority; tracked via the canon's issue tracker after this PR merges.

## Consequences

**Positive:**

- The corpus's identity matches the working reality: collaborative concepts and ideation between JD and Micah, with the corpus's artifacts representing their joint research program.
- Citations of the corpus correctly credit both authors.
- The corpus-vs-artifact authorship distinction is explicit: corpus-level identity is joint; per-artifact attribution remains specific to each artifact's actual authorship.
- ADR-EA-0004's principal-author + per-construct attribution pattern remains operative at the artifact level — no governance churn for the per-artifact discipline.

**Negative:**

- A reader skimming only the canon README without reading individual artifact READMEs may assume joint authorship of every artifact. Mitigated by the README's citation block footnote pointing at this ADR + the explicit "per-artifact authorship recorded at the artifact's location" rule.
- The corpus's prior published prose (in archived `osa-ai-org/*` repos and existing Zenodo deposits) names JD as principal author. That historical record is not updated retroactively; only forward-going corpus identity is joint. Some discontinuity in author attribution between the source-archive identity and the canon's identity is unavoidable.
- A follow-on audit pass is needed to surface Micah's co-authorship in artifacts where it applies but wasn't explicitly noted under the old principal-author framing. Tracked as a queued task (medium priority).

**Neutral:**

- Per-artifact authorship records are unchanged.
- License (CC BY 4.0) is unchanged.
- ADR-EA-NNNN numbering continuity holds.
- The independent-research disclaimer broadens from "the author" to "the authors"; both publish in personal capacity.

## Alternatives considered

1. **Keep sole-principal corpus identity (ADR-EA-0004 §Decision item 2 unchanged).** Rejected. JD explicitly directed (2026-05-22) that Micah should receive equal corpus-level credit because they collaborate continuously on concepts and ideation. Maintaining the sole-principal framing would understate the collaborative reality.

2. **Retroactively claim joint authorship of every per-artifact record.** Edit foundation/, constructs/, and enterprise-platforms/ artifact READMEs (and ideally Zenodo deposit metadata) to add Micah as co-author of artifacts that were JD-sole-authored. Rejected. Per-artifact authorship is a per-artifact fact — some artifacts are genuinely sole-authored even when the corpus identity is joint. Conflating corpus identity with per-artifact authorship would misrepresent specific artifact provenance.

3. **Add Micah as "Contributor" at corpus level (lighter than co-author).** Rejected. JD explicitly directed *equal credit*. "Contributor" frames Micah as supporting JD's lead, not as a co-author of equivalent standing. The directive is for the latter.

4. **Defer the corpus-level reframing until per-artifact audit completes.** Rejected. The corpus-level identity is the most-visible attribution surface (canon README, citation block). Updating it immediately gives Micah correct credit now; the per-artifact audit can land as follow-on work without blocking the corpus identity correction.

5. **Fold into ADR-EA-0007 instead of authoring a separate ADR.** Rejected. ADR-EA-0007 is about tier shape (Vision-Strategy / Mode Alpha); authorship reframing is structurally distinct. Folding two unrelated decisions into one ADR would obscure both. Separate ADR with cross-references is cleaner.

## Related

- [ADR-EA-0004](../constructs/mxm/decisions/ADR-EA-0004-add-mx-modes-as-spine-construct.md) — refined §Decision item 2 (principal-author + per-construct attribution); the artifact-level discipline is preserved.
- [ADR-EA-0005](../constructs/mxm/decisions/ADR-EA-0005-clarify-mxm-archetype.md) — precedent for refinement-grade ADRs that sit alongside an earlier ADR rather than superseding it.
- [ADR-EA-0006](ADR-EA-0006-migrate-corpus-to-aide-canon.md) — umbrella migration ADR; predates this authorship reframe (its prose references "JD Longmire" alone, which was correct at the time of authoring; not edited retroactively).
- [ADR-EA-0007](ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) — Tier 0 / Mode Alpha structural amendment; lands in the same PR but is structurally separate from this ADR.
