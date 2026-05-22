# ADR-EA-0004 — Add Mx-Modes as a corpus construct at the agent-orientation altitude

- **Status:** Accepted
- **Date:** 2026-05-22
- **Author:** JD Longmire
- **Reviewers:** @jdlongmire
- **Ratification note:** Comment-out period waived by explicit maintainer ratification (JD Longmire, 2026-05-22). The non-waivable-clause rule from CONTRIBUTING.md is preserved as the default; the maintainer's prerogative to override the default by ratification was exercised here for the spine-promotion decision, after the bundling reframe (allied → spine) was settled in conversation. The override is recorded so future readers of the ADR see that the period was deliberately collapsed, not silently skipped.
- **See also:** [ADR-EA-0005](ADR-EA-0005-clarify-mxm-archetype.md) — refines this ADR's positioning of MxM ("agent-orientation altitude" → harness archetype across altitudes). The bundling decision (Mx-Modes as spine, not allied) is unchanged.

## Context

On 2026-05-22 a new architectural construct, **Mx-Modes** (architecturally designated **MxM** — multi-mode meta-harness), was authored jointly by JD Longmire (principal) and Micah Longmire as a Technical Architecture Reference. The framework structures AI operation through five governing surfaces — **MIND, MORALS, MISSION, MEMORY, MEANS** — and rests on the architectural claim that *AI behavior should be oriented before it is executed*.

The corpus to date has positioned itself at the **enterprise altitude**: AEON / AIDEX / HCAE / OAAD are the AI-specialization control-plane constructs, DEA (landing via [ADR-EA-0003](../../dea/decisions/ADR-EA-0003-expand-corpus-to-include-dea.md), in flight as [PR #5](https://github.com/osa-ai-org/enterprise-ai/pull/5)) is the general-EA foundation, and OrdSA provides the layered authority/evidence ordering that those deployments operationalize. All of those work at the level of *how an enterprise composes and governs its agentic systems*.

Mx-Modes sits at a different altitude — the **agent-orientation altitude**: how a single AI instance is structured *before* execution begins. Five governing surfaces (Mind, Morals, Mission, Memory, Means) establish the operating envelope; the model executes within that envelope. The construct formalizes a discipline that is implicit in AEON, AIDEX, and HCAE at enterprise scale but had no named per-agent counterpart in the corpus until now.

Initial framing (in this PR's first revision, since reworked) bundled Mx-Modes as an allied subdirectory under `docs/mx-modes/` following the Theseus thesis precedent. On reflection, that framing understated the construct's role: Mx-Modes is not adjacent research that happens to land in the corpus's neighborhood — it is a **load-bearing construct in the corpus's architectural argument**. The enterprise control plane the corpus describes presumes that individual agents are oriented before execution; Mx-Modes is what that orientation looks like in practice. Treating it as allied-isolated would leave the per-agent altitude unnamed in the spine while explicitly relying on it.

Adding Mx-Modes as a spine construct touches multiple clauses CONTRIBUTING.md flags as **excluded from the maintainer-prerogative waiver**:

- Introduces a new architectural construct (Mx-Modes itself)
- Changes the corpus's stated audience (expands to include agent architects and AI harness engineers)
- Changes the corpus's positioning prose (introduces the *agent-orientation altitude* as a corpus altitude, not just an enterprise-altitude assumption)
- Introduces the corpus's first co-authored construct, surfacing the multi-author question inside the spine

So this requires a regular ADR with the standard one-week comment-out period.

## Decision

**Add Mx-Modes to the corpus as a spine construct at the agent-orientation altitude.** The corpus's stated scope broadens from *"enterprise architecture, with AI specialization"* to *"enterprise architecture, with AI specialization, plus a per-agent orientation construct that the enterprise constructs presume."* Concretely:

1. **Mx-Modes joins the corpus's named constructs.** The four-construct AI-specialization enumeration (AEON / AIDEX / HCAE / OAAD) is preserved; Mx-Modes is added as a separate construct at a different altitude, not as a fifth AI-specialization peer to those four. The README presents the corpus as having three layers:
   - **General-EA foundation:** DEA (per ADR-EA-0003)
   - **AI specialization (enterprise altitude):** AEON, AIDEX, HCAE, OAAD
   - **Agent-orientation altitude:** Mx-Modes

2. **Authorship is per-construct, principal-led.** The corpus identity remains **JD Longmire-led**: he is principal author of all constructs in the spine, including Mx-Modes. Mx-Modes is specifically marked as co-authored with Micah Longmire wherever it appears (document index, citation, in-construct attribution). The other constructs remain sole-authored. The corpus README's intro continues to name JD as principal author; the per-construct attribution carries the joint-authorship signal where it applies.

3. **Filesystem layout follows the spine pattern.** Mx-Modes artifacts live at `docs/` root and `infographics/` root, alongside the DEA papers and the AI-specialization papers — *not* in an allied `docs/mx-modes/` subdirectory. The allied-subdirectory pattern (precedent: `docs/theseus-thesis/`) remains the corpus's mechanism for *adjacent-but-not-spine* work, which Mx-Modes is no longer.

4. **License continuity, with co-author consent acknowledged.** Mx-Modes is licensed CC BY 4.0 consistent with the rest of the corpus. The license file's "JD-authored content" framing is broadened in spirit to "JD-principal-authored corpus content"; both authors of Mx-Modes consent to CC BY 4.0 for their joint work. The license file itself is not edited in this PR (its existing text remains accurate for sole-authored constructs); the README's citation block notes the per-construct co-authorship.

5. **Independent-research disclaimer is per-construct compatible.** Both authors publish in personal capacity. JD's "does not represent any employer" disclaimer continues to apply to corpus content as a whole. Mx-Modes's attribution lists both authors with their employer affiliations for identification only.

### Concrete README changes (this PR carries them)

1. **Document index:** new row for Mx-Modes Technical Reference with both authors' ORCIDs.
2. **New section after the AI-specialization constructs:** *Mx-Modes at the agent-orientation altitude* — describes the construct, names the five surfaces, points to the source document, names both authors and links their ORCIDs.
3. **Suggested reading order:** revised to include Mx-Modes as a later-stage reading once the enterprise-altitude argument is in hand — appropriate for readers who want to descend from enterprise architecture into per-agent operating structure.
4. **Audience expansion:** tertiary audience adds *agent architects and AI harness engineers* who consume the framework at the per-agent level rather than at enterprise architecture scale.
5. **Citation:** broadened to acknowledge the now-multi-altitude corpus — "AEON / AIDEX / HCAE / OAAD + DEA + Mx-Modes" — with the note that Mx-Modes specifically is co-authored.
6. **Related work section:** the Theseus thesis remains allied (sole-authored by Micah, isolated in `docs/theseus-thesis/`). The "this repository's corpus is sole-authored" claim is softened to "JD Longmire is principal author of the corpus's constructs; one construct (Mx-Modes) is co-authored, as noted at the construct."

### Scope: README revision + three new files + ADR

This ADR's PR carries:
- README revisions described above
- `docs/Mx-Modes-Technical-Reference.docx` + `.pdf`
- `infographics/Mx-Modes-Construct-Infographic.jpg`
- ADR-EA-0004 itself + `decisions/README.md` index entry

It does **not**:
- Modify `CONTRIBUTING.md` (the sole-author maintainer-prerogative waiver clause remains in effect; future joint-author work in the spine that needs a waiver path is a follow-on ADR if and when it arises)
- Modify the `LICENSE` file (CC BY 4.0 stands; the per-construct co-author consent is noted in the README and in this ADR, not in the license)
- Modify any other ADR or paper

## Consequences

- **Corpus scope explicitly multi-altitude.** The README now articulates the per-agent altitude as a corpus altitude, not just an enterprise-altitude assumption. Readers who want to descend from the enterprise control plane into per-agent operating envelopes find Mx-Modes as the named construct that fills that descent.
- **Sole-author identity loosens to principal-author identity.** The corpus is no longer strictly sole-authored — but the principal-author framing keeps JD as the corpus's named architect and reserves multi-author surface to the constructs where it applies. The Theseus precedent (allied-isolated sole-author-by-other) continues to serve as the bundling-without-absorbing pattern for adjacent work.
- **The waiver clause is now in tension.** CONTRIBUTING.md's PR #3 sole-author waiver clause was framed around sole-author corpus identity. With Mx-Modes co-authored, the clause is narrower than the corpus is — it cannot waive a Mx-Modes-touching ADR even when JD is the sole maintainer, because the multi-author surface has separate consent semantics. This ADR notes the tension but does **not** edit the clause; resolution is queued for a future targeted ADR. In the meantime, the clause is operative for spine constructs that remain sole-authored.
- **Future joint constructs have a path.** A follow-on joint construct now has a precedent — principal-author + named co-authors + per-construct attribution. Future joint work that wants to enter the spine follows the same pattern without requiring a CONTRIBUTING.md change.
- **The non-waivable-clause rule is now load-bearing across multiple categories.** ADR-EA-0003 exercised the new-construct + audience + positioning triggers; this ADR exercises those plus the multi-author-spine trigger. Both ADRs are sitting out the standard one-week period, demonstrating that the rule operates as written rather than as aspiration.

## Alternatives considered

1. **Bundle Mx-Modes as an allied subdirectory under `docs/mx-modes/`, following the Theseus precedent.** This was the first framing in this PR's history before being reworked. Rejected because Mx-Modes is not adjacent research that happens to be in the neighborhood — it is a load-bearing construct that the enterprise-altitude constructs implicitly rely on. Treating it as allied-isolated leaves the per-agent altitude unnamed in the spine while the spine explicitly presumes that orientation discipline. Allied-isolation is the right pattern for the Theseus thesis (per-agent identity and memory by a different author, sole-authored, not co-developed with the corpus); it is the wrong pattern for Mx-Modes (co-authored, formalizes a discipline the corpus already presumes at enterprise scale).

2. **Publish Mx-Modes as a standalone repository at `osa-ai-org/mx-modes` (or similar).** Treat it as a parallel construct with its own independent presence — like OrdSA's relationship to enterprise-ai, where OrdSA is canonical in `ordsa-ai` and bundled here for navigability. Rejected because OrdSA serves a different role — it is the *layered authority/evidence* construct that the corpus deploys, not the corpus's own architectural object. Mx-Modes is the corpus's own work, co-authored with another principal, naming an altitude the corpus needs. Standing up a separate repo would obscure that the corpus's argument now extends to the per-agent altitude; bundling it as spine makes the multi-altitude scope explicit.

3. **Reframe the corpus as "JD Longmire and co-authors" with broader identity change.** Open the corpus generally to multi-author work; update README intro, citation block, and CONTRIBUTING.md's waiver clause in one move. Rejected because (a) it is heavier than the current work justifies — Mx-Modes is the first joint construct, and the multi-author surface is not yet load-bearing across the spine; (b) it would couple the Mx-Modes addition to a governance overhaul that should be a deliberate, separate decision; (c) keeping JD as principal author of the corpus identity preserves the corpus's voice while the per-construct attribution carries the joint-authorship signal where it applies.

4. **Add Mx-Modes as a fifth AI-specialization construct alongside AEON / AIDEX / HCAE / OAAD.** Restructure "the four constructs" table to "the five constructs," include Mx-Modes inline. Rejected because Mx-Modes is at a different altitude — those four are enterprise control-plane components; Mx-Modes is per-agent operating-envelope orientation. Listing them as peer would either elevate Mx-Modes inappropriately (as if it were enterprise-scale) or demote the enterprise constructs (as if they were per-agent). The honest framing is altitude-stratified: enterprise constructs at one altitude, Mx-Modes at another, both named in the spine.

5. **Defer Mx-Modes's spine entry until a companion AI-EA / Mx-Modes integration paper is written.** Mark Mx-Modes as forthcoming-spine but bundle it allied for now. Rejected because the construct is already in stable form (Technical Architecture Reference v1) and the integration argument — that the enterprise control plane presumes Mx-Modes-style orientation at the agent level — is already implicit in AEON / AIDEX / HCAE. A future integration paper would refine the bridge, not establish it; the bridge is already real. Deferring means the per-agent altitude remains unnamed in the spine while functionally relied on.

## References

- [ADR-EA-0001](../../../decisions/ADR-EA-0001-adopt-ordsa-development-process.md) — the governance process this ADR follows
- [ADR-EA-0002](../../../decisions/ADR-EA-0002-reframe-as-ordsa-exemplar.md) — corpus as canonical enterprise-scale OrdSA deployment (still holds; Mx-Modes operates at a different altitude than OrdSA's enterprise-scale-deployment frame)
- [ADR-EA-0003](../../dea/decisions/ADR-EA-0003-expand-corpus-to-include-dea.md) — DEA expansion (in flight as [PR #5](https://github.com/osa-ai-org/enterprise-ai/pull/5); this ADR is independent of its merge state, except that the top-level README will need to coherently present both DEA and Mx-Modes after both merge)
- [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) — the waiver-exclusion clauses that make this ADR require the standard one-week period
- [`docs/Mx-Modes-Technical-Reference.docx`](../docs/Mx-Modes-Technical-Reference.docx) / [`.pdf`](../docs/Mx-Modes-Technical-Reference.pdf) — the Mx-Modes Technical Architecture Reference introduced by this ADR
- [`infographics/Mx-Modes-Construct-Infographic.jpg`](../infographics/Mx-Modes-Construct-Infographic.jpg) — construct overview infographic
- [`related-work/theseus/`](../../../related-work/theseus/) — the allied-isolated precedent, which remains the pattern for sole-author-by-other adjacent work but is not what Mx-Modes is
