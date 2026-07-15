# ADR-EA-0006 — Migrate corpus to `ologos-repos/aide-canon` as the canonical home

- **Status:** Accepted
- **Date:** 2026-05-22
- **Author:** JD Longmire
- **Reviewers:** @jdlongmire
- **Ratification note:** Comment-out period waived by explicit maintainer ratification (JD Longmire, 2026-05-22). Same override pattern as ADR-EA-0003 / 0004 / 0005 ratified earlier today. The migration was deliberated in cross-ai [#40](https://github.com/ologos-corp/cross-ai/issues/40) over the course of the day with thinx-Claude (acting as JD's prime) and OlogosAI (member-tier); Topic 2 (hierarchy) was ratified by thinx at 17:53Z; Topic 3 (cloning plan) was ratified at 18:20Z; the empty `ologos-repos/aide-canon` repo was created by thinx at 18:19Z under JD's authorization. The non-waivable-clause rule from CONTRIBUTING.md is preserved as the default; the maintainer's prerogative to override is exercised here because the cross-ai #40 deliberation served the cooling-off function the comment-out period exists to provide.

## Context

The corpus has lived at `osa-ai-org/enterprise-ai` since its initial publication, alongside its sibling construct repository `osa-ai-org/ordsa-ai`. Through the course of 2026-05-22, three converging developments made the existing layout structurally inadequate:

1. **The corpus's argument now spans multiple altitudes.** [ADR-EA-0003](ADR-EA-0003-expand-corpus-to-include-dea.md) added DEA as a general-EA foundation upstream of the AI-EA constructs. [ADR-EA-0004](../constructs/mxm/decisions/ADR-EA-0004-add-mx-modes-as-spine-construct.md) added Mx-Modes as a spine construct, and [ADR-EA-0005](../constructs/mxm/decisions/ADR-EA-0005-clarify-mxm-archetype.md) clarified MxM as the harness archetype across all altitudes (peer methodological construct to DEA, OrdSA, OAgents). The corpus's stated scope is no longer "AI EA" — it is **enterprise architecture for the agentic era spanning foundational basis, methodological patterns, enterprise-altitude instantiations, and related work**.

2. **Foundational artifacts pre-exist the AI-EA constructs.** [HCAE](../foundation/hcae/) (`10.5281/zenodo.18368697`) and [AIDK](../foundation/aidk/) (`10.5281/zenodo.18316059`) sit upstream of AIDEX in the argument lineage (`AIDK → HCAE → AIDEX → AEON`), with their own published Zenodo DOIs that the existing repo layout could not represent without inverting dependencies. RLEG sits adjacent to HCAE at the training-methodology level, in draft.

3. **OAgents is methodologically peer to OrdSA, MxM, and DEA.** [`ologos-corp/OAgents-standard`](https://github.com/ologos-corp/OAgents-standard) had been published as a separate repository; the four-construct methodological tier (DEA/OrdSA/MxM/OAgents) only became coherent when these were recognized as peer patterns.

The `osa-ai-org/enterprise-ai` repository's `docs/`-flat layout — appropriate when the corpus was four AI-EA constructs and one allied thesis — cannot represent the multi-altitude, multi-construct, foundational + methodological + enterprise + related-work shape the corpus actually has now.

Cross-ai issue [#40](https://github.com/ologos-corp/cross-ai/issues/40) developed the canonical-home proposal collaboratively between OlogosAI (3 topic comments covering factual update, hierarchy plan, cloning plan) and thinx-Claude / JD (4 ratifying comments with 5 structural changes from OlogosAI's proposal). Topic 2 (hierarchy) was ratified at 17:53Z with the following structural changes from the original proposal:

- New `foundation/` tier for upstream cognitive-theory + training-methodology basis (HCAE, AIDK, RLEG)
- HCAE placed under `foundation/`, not `enterprise-platforms/` (preserves the upstream-of-AIDE argument lineage)
- AIDK + RLEG added to canon scope under `foundation/`
- `BUILD.md` + `MANIFEST.yaml` reserved at canon root for autonomous-build-agent navigation (deferred to follow-on PR per Refinement A)
- `enterprise-platforms/strategy/` flagged `buildable: false` in MANIFEST.yaml (deferred to follow-on PR per Refinement B)
- `tests/` siblings to each `spec/` reserved (v0.2 marker)

Topic 3 (cloning plan) was ratified at 18:20Z with the empty `ologos-repos/aide-canon` repo created as the canonical home. Two open questions in Topic 3 were resolved:

- **OAgents canonical source** — OlogosAI's judgment, with the constraint that `constructs/oagents/README.md` cites both Zenodo deposits (`19425021` + `19427785`) as bibliographic anchors. OlogosAI's follow-up at 18:51Z identified `ologos-corp/OAgents-standard` as the canonical home and flagged the migration-method change from snapshot to `git filter-repo` (parity with OrdSA's history-preserving merge).
- **ADR prefix** — (α) keep `ADR-EA-NNNN`. URL continuity wins; the cost of renaming to `ADR-AIDE-NNNN` is broken cross-references at cross-ai #40, in the merged PRs, and in external citations.

The migration is the structural move that operationalizes those decisions.

This ADR's adoption touches multiple non-waivable triggers from CONTRIBUTING.md:

- **New canonical home** (repository identity change)
- **Multi-construct corpus expansion** (4 peer methodological constructs + 3 foundational artifacts in scope; previously one repo's worth)
- **Audience and positioning shift** (corpus identity becomes "AI-enabled Digital Ecosystem" — AIDE — with the AI-EA portion as one altitude rather than the corpus's full scope)
- **Governance carry-forward** (OrdSA process per ADR-EA-0001 carries to the new canon)

## Decision

**Migrate the corpus from `osa-ai-org/enterprise-ai` to `ologos-repos/aide-canon` as the canonical home.** The new canon name encodes the corpus identity: **AI-enabled Digital Ecosystem (AIDE)** — the architectural surface a digitally-realized enterprise composes to operate trustworthy AI at scale. Concretely:

1. **Four-tier content structure under `aide-canon/`:**
   - `foundation/` — upstream cognitive-theory + training-methodology basis (`hcae/`, `aidk/`, `rleg/`)
   - `constructs/` — peer methodological patterns (`dea/`, `ordsa/`, `mxm/`, `oagents/`), each Pattern α self-contained (README + docs + infographics + decisions + spec)
   - `enterprise-platforms/` — enterprise-altitude instantiations (`strategy/` flagged `buildable: false`; `aeon/`, `aidex/`, `oaad/`)
   - `related-work/` — allied research (`theseus/`)
   - Cross-cutting: `decisions/` (canon-level ADRs) + `infographics/` (cross-construct/platform visuals)
   - Reserved: `thesis/` (master thesis forthcoming once constituent DOIs mint)

2. **Cloning approach (mixed):**
   - **`git filter-repo`** for `osa-ai-org/ordsa-ai` → `constructs/ordsa/` and `ologos-corp/OAgents-standard` → `constructs/oagents/`. Preserves schema + ADR evolution history for both standards.
   - **Snapshot copy** for `osa-ai-org/enterprise-ai/docs/` and `jdlongmire/AI-Research/1.0-Foundation/`. Content is mostly binary papers; per-file history offers low value vs. effort.

3. **ADR continuity:** `ADR-EA-NNNN` numbering carries forward per the (α) decision. ADR-EA-0001 (governance) and ADR-EA-0002 (OrdSA exemplar) live at canon-level `decisions/`. ADR-EA-0003 (DEA) lives at `constructs/dea/decisions/`. ADR-EA-0004 / 0005 (MxM) live at `constructs/mxm/decisions/`. This ADR (ADR-EA-0006) lives at canon-level `decisions/`. Construct-internal ADRs (OrdSA's `ADR-ORDSA-*`, etc.) live in their construct's `decisions/`.

4. **Relative-path adjustment in migrated ADRs:** ADRs 0003, 0004, 0005 had relative-path cross-references that no longer resolve under the canon's Pattern α layout. The decision text in each ADR is byte-preserved; only `[link](path)` targets were updated to point at the canon paths. The immutability rule's intent (preserve decision text) is honored; the transcription rule (paths reflect current repository state) is applied as ordinary text maintenance, equivalent to renaming a file referenced by a hyperlink.

5. **Governance carry-forward:** The OrdSA development process ratified for the source corpus in [ADR-EA-0001](ADR-EA-0001-adopt-ordsa-development-process.md) carries to the canon unchanged. Direct commits to `main` are not permitted. ADRs flow as PRs. `CONTRIBUTING.md` lands in a follow-on PR (deferred from this migration's scope to keep the migration PR focused on content relocation).

6. **Source repository disposition:**
   - **`osa-ai-org/enterprise-ai`** — archive with a retirement note at the top of its README pointing at `ologos-repos/aide-canon`. No new ADR at the source side (per the cross-ai #40 Topic 3 (iii) call). Per the (α) URL continuity decision, archived repos remain publicly readable; existing Zenodo deposits and external citations continue to resolve.
   - **`osa-ai-org/ordsa-ai`** — same treatment in a separate PR.
   - **`ologos-corp/OAgents-standard`** — same treatment in a separate PR.
   - **`jdlongmire/AI-Research`** — **no archive.** Theseus-pattern: the source repo stays as JD's active research portfolio. The canon hosts derivatives of the 1.0-Foundation subtree with provenance pointers; foundation artifacts cite their upstream Zenodo DOIs as canonical citation target, not the canon paths.

### Scope: this ADR + the migration PR

This ADR + the migration PR carry:

- The four-tier content scaffold + per-tier READMEs
- Canon-level README + LICENSE (CC BY 4.0, mirroring the source corpus)
- Content migration from all four source locations per the cloning plan
- ADR-EA-0006 itself + `decisions/README.md` index update
- Path-syntax updates in migrated ADRs (text preserved)

It does **not**:

- Author the source repos' retirement notes — those land in separate follow-on PRs at each source repo
- Author `CONTRIBUTING.md` for the canon — deferred follow-on PR
- Author `BUILD.md` + `MANIFEST.yaml` — deferred follow-on PR per cross-ai #40 Refinement A
- Populate per-construct `spec/` or `tests/` contents — populated per-construct as the build-target work begins
- Update existing Zenodo deposits' related-identifier URLs — they continue to point at the original `osa-ai-org/enterprise-ai` paths via GitHub's auto-redirects after archive
- Address cross-ai #41 (cross-AI-collab home in canon) — JD's (γ) decision at 18:22Z deferred to post-stand-up
- Address the OrdSA org rename (`osa-ai-org` → `ordsa-org`) — separate concern

## Consequences

- **Canonical home consolidates.** A single navigable structure replaces the previously-scattered `osa-ai-org/enterprise-ai` + `osa-ai-org/ordsa-ai` + `ologos-corp/OAgents-standard` + `jdlongmire/AI-Research/1.0-Foundation/` layout. Readers walk one tree to find the corpus.

- **Argument lineage now navigable top-down.** `AIDK → HCAE → AIDEX → AEON` is visible in the directory structure (`foundation/aidk/` → `foundation/hcae/` → `enterprise-platforms/aidex/` → `enterprise-platforms/aeon/`), not implicit in prose alone.

- **Construct/platform discipline operationalized.** Pattern α self-containment per construct (README + docs + infographics + decisions + spec) lets each construct lift cleanly if it ever leaves the canon, mirrors OrdSA's existing schema-first canonical pattern, and matches what an autonomous build agent expects to see.

- **Schema-first constructs surface their canonical artifacts.** OrdSA (`schema/ordsa-0.2.yaml`) and OAgents (`spec/oagents-nist-standard-v16.0.md`) make their machine-readable spec the canonical source; prose papers become companions. DEA and MxM remain prose-canonical for now; `spec/` placeholders reserve the schema-first slot for when they get there.

- **History preserved for schema-first constructs.** OrdSA and OAgents arrive via `git filter-repo` with full commit history under their subdirectory. Schema evolution and ADR history is locally readable, not just a snapshot.

- **URL continuity preserved via GitHub auto-redirects.** Archived `osa-ai-org/*` repos continue to serve content at original paths via GitHub redirects; existing external citations (Zenodo `related_identifier`, blog posts, slide decks) keep working until they are updated.

- **The waiver-exclusion clause set is now tested.** ADR-EA-0006 exercises new-canonical-home + multi-construct-expansion + audience-positioning-shift + governance-carry-forward triggers simultaneously. With cross-ai #40's day-long deliberation serving as the cooling-off function, the maintainer override is recorded explicitly so future readers see the rule operated as written.

- **CONTRIBUTING.md sole-author waiver clause needs revisiting.** [ADR-EA-0004](../constructs/mxm/decisions/ADR-EA-0004-add-mx-modes-as-spine-construct.md) Consequences flagged this; the canon's multi-construct shape (with one co-authored construct) makes the original sole-author framing narrower than the corpus is. Resolution deferred to a future targeted ADR; not blocking the migration.

- **Cross-ai #41 (cross-AI-collab representation) lands as ADR-EA-0007** (or whichever number it takes) after the canon stands up populated. JD's (γ) decision (both construct + platform) is recorded on #41; the ADR materializes the relocations.

## Alternatives considered

1. **Stay at `osa-ai-org/enterprise-ai`; restructure in place.** Reorganize the existing repo's `docs/` into the four-tier shape; ordsa-ai and OAgents-standard remain separate. Rejected because the corpus identity has shifted from "AI EA" to "AIDE" (AI-enabled Digital Ecosystem) — keeping the `enterprise-ai` repository name preserves a label that no longer matches scope. The `aide-canon` naming reflects what the corpus actually is now. Also: restructure-in-place would not solve the OrdSA + OAgents history-preservation problem — they would either need to stay as external links (defeating the canonical-home goal) or be force-merged with rewrites the existing repo can't cleanly absorb.

2. **Split into multiple canonical homes** (one per tier: `ai-foundation-canon`, `ai-constructs-canon`, `ai-platforms-canon`). Rejected because the cross-tier argument (`AIDK → HCAE → AIDEX → AEON`) becomes harder to traverse when separated by repo boundaries. The canon's primary affordance is reading the architecture top-down; multi-repo split would force readers to traverse out and back in.

3. **Defer migration until `BUILD.md` + `MANIFEST.yaml` are written.** Land the build-agent navigation as part of the canonical-home stand-up so adopters get a complete experience. Rejected because per cross-ai #40 Refinement A clarification at 17:54Z, build-agent navigation is *not* stand-up-blocking — content placement settles at stand-up time; everything else is post-stand-up evolution. Coupling the two would unnecessarily delay the corpus's relocation.

4. **Keep all sources live (no archive of `osa-ai-org/*`).** Treat the canon as a derivative aggregation and let the sources continue receiving PRs in parallel. Rejected because divergent edits at two locations create authority ambiguity. The canon needs to be authoritative; the sources need to either retire to read-only archive (this ADR's choice) or get reconfigured as read-only mirrors (heavier, less standard).

5. **Land migration with stricter immutability — no link-syntax updates in migrated ADRs.** Preserve each ADR's exact byte contents including broken relative links. Rejected because the immutability rule's *intent* is to preserve decision text, not transcribed file paths. A migrated ADR with broken navigation is a worse adopter experience than a migrated ADR with text-preserved decisions and updated navigation. The path updates are recorded in this ADR's section 4 above for audit visibility.

## References

- [ADR-EA-0001](ADR-EA-0001-adopt-ordsa-development-process.md) — the governance process that carries to the canon
- [ADR-EA-0002](ADR-EA-0002-reframe-as-ordsa-exemplar.md) — the OrdSA-exemplar framing that motivated the schema-first canonical pattern
- [ADR-EA-0003](../constructs/dea/decisions/ADR-EA-0003-expand-corpus-to-include-dea.md) — DEA expansion (one of the developments that exceeded the source repo's scope)
- [ADR-EA-0004](../constructs/mxm/decisions/ADR-EA-0004-add-mx-modes-as-spine-construct.md) — Mx-Modes spine construct
- [ADR-EA-0005](../constructs/mxm/decisions/ADR-EA-0005-clarify-mxm-archetype.md) — MxM as harness archetype across altitudes
- Cross-ai [#40](https://github.com/ologos-corp/cross-ai/issues/40) — the canonical-home discussion (3 topic comments from OlogosAI, 4 ratifying comments from JD/thinx, OlogosAI follow-up flagging OAgents migration-method change)
- Cross-ai [#41](https://github.com/ologos-corp/cross-ai/issues/41) — cross-AI-collab representation in canon (JD's γ decision; deferred to post-stand-up)
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — the waiver-exclusion clauses; ADR-EA-0006 triggers multiple non-waivable categories (lands in a follow-on PR)
