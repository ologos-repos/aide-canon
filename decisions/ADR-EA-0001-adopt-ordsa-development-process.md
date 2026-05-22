# ADR-EA-0001 — Adopt OrdSA-style development process for enterprise-ai

- **Status:** Accepted
- **Date:** 2026-05-21
- **Author:** JD Longmire
- **Reviewers:** @jdlongmire
- **Bundle:** Founding ADR

## Context

enterprise-ai launched as a public corpus on 2026-05-20 with a freeform direct-to-`main` commit cadence. Over the first 24 hours the corpus accumulated framework-level commitments that are not self-evident from `git log` and not durably recorded:

- The four-construct enumeration (AEON, AIDEX, HCAE, OAAD)
- Positioning as independent research under a "does not represent any employer or program" disclaimer
- Audience scoping to CIO / CTO / Chief Architect / CISO in sovereignty-constrained enterprises
- CC BY 4.0 licensing
- A "methodologically allied with OrdSA" framework-alignment claim in the README
- Publication under the `osa-ai-org` namespace rather than an author-affiliated org

These are reversible only at high cost once the corpus is cited. The next several months will introduce more such commitments — additional papers, an OrdSA-anchored re-framing, possibly cross-references to other frameworks. Continuing to make those commitments freeform on `main` would leave their *why* unrecorded.

OrdSA — the methodologically-allied construct this corpus already cites — operates under a PR-first + ADR-as-PR governance pattern documented in [`osa-ai-org/ordsa-ai/CONTRIBUTING.md`](https://github.com/osa-ai-org/ordsa-ai/blob/main/CONTRIBUTING.md). That pattern distinguishes construct-level decisions from content edits, preserves the *why* behind framework choices, and gives adopters a stable reference surface for citation and extension.

The recent arrival of the OrdSA construct infographic in this corpus — which positions OrdSA as "*A Control-Oriented Architecture Construct for Enterprise AI*" — makes the methodological subordination explicit. Adopting the corresponding development discipline is the operational counterpart of that subordination.

## Decision

**enterprise-ai adopts OrdSA-style development governance, scoped to the corpus.**

Specifically:

1. **Branch flow.** `dev` is the working branch; `main` is the released, citable surface. All changes land on `main` via PR. No direct commits to `main`.
2. **ADRs as PRs.** Framework-level changes (see "ADR-worthy bar" below) flow as ADRs in `decisions/ADR-EA-NNNN-<slug>.md`, ratified by PR merge.
3. **Content changes as ordinary PRs.** Prose refinements, new papers within an existing construct's scope, infographic additions, README cleanup, and errata flow as ordinary PRs without ADR.
4. **Append-only ADRs.** Merged ADRs are immutable; substantive revision happens via a superseding ADR.
5. **GitHub Discussions for pre-PR framing.** Brainstorming on framework-level questions uses Discussions; the PR is the durable record.

### ADR-worthy bar for enterprise-ai

A change is ADR-worthy if it does any of the following:

- Adds, removes, or redefines a major construct (currently: AEON, AIDEX, HCAE, OAAD)
- Changes the audience or positioning (e.g., who the corpus addresses, the "independent research" framing)
- Adds, removes, or revises a framework alignment claim (currently: methodologically allied with OrdSA)
- Changes the license, citation pattern, or attribution model
- Adopts a new methodology that affects how the corpus itself is governed (this ADR is an example)

Refinements within an existing construct, new worked examples, additional papers in the existing scope, infographic additions, and prose clarifications do not require an ADR.

### Bundle exemption

As a self-referential founding ADR, ADR-EA-0001 is exempt from the standard one-week comment-out period defined in `CONTRIBUTING.md`. Future ADRs follow the standard cadence.

## Consequences

- **Archeological richness.** The git history of enterprise-ai gains a durable *why*-record. Future adopters can trace not just what the corpus says but why it was shaped that way.
- **Editing friction increases for framework changes.** Substantive commitments now cost a PR + ADR cycle. The corpus trades velocity for durability — the right trade now that the corpus is public and citable.
- **Existing decisions are grandfathered.** ADR-EA-0001 is the first ADR. Prior decisions (publish public, position as independent research, four-construct enumeration, OrdSA alignment, CC BY 4.0, namespace choice) are not backfilled as ADRs; they remain visible in the README and the published papers. If any of them become contentious, a superseding decision is captured as a new ADR.
- **New scaffolding.** A `decisions/` directory, `CONTRIBUTING.md`, and ADR template are introduced as part of this PR.
- **Methodological alignment becomes operationally visible.** Adopters of the corpus see the same governance discipline they see in OrdSA, reinforcing the methodological alignment in practice and not only in prose.
- **Cross-repo consistency.** Authors and reviewers move between `ordsa-ai` and `enterprise-ai` without context-switching on process. Pattern carries forward to any future `osa-ai-org` corpus.

## Alternatives considered

1. **Stay on direct-to-`main` edits.** Current state. Lowest friction, but loses the durability and *why*-recording benefits as the corpus grows. Rejected — the corpus is past the inflection where freeform editing is sustainable.

2. **PR-first but no ADRs.** Half-measure. PR review alone does not distinguish framework-level commitments from prose refinements, and PRs have no durable *what was decided and why* surface independent of their diff. Rejected because the value of ADRs comes from the deliberate framing of *which* changes get the heavyweight treatment.

3. **Full OrdSA mirror (changelog versioning, branch protection, founding-bundle of multiple ADRs).** Heavier setup; brings discipline that may not be needed at this corpus's scale yet. Deferred — adopt the development process now; revisit changelog versioning and branch protection separately if and when they become load-bearing.

4. **Backfill ADRs for existing decisions.** Retrospectively author ADRs for the major decisions already made (publish public, independent research framing, four-construct enumeration, OrdSA alignment, license, namespace). Rejected for now — the existing decisions are visible in the README and the corpus is small enough that backfill would be bookkeeping that distracts from forward work. Revisitable if specific decisions become contentious or if adopters begin citing them in ways that demand a *why*-record.

5. **A bespoke process tuned to AI EA specifically.** Could be done; would diverge from OrdSA over time. Rejected because cross-repo consistency under `osa-ai-org` is itself a value: contributors and readers move between the two corpora; same process is friction-reducing for both.

## References

- [`osa-ai-org/ordsa-ai/CONTRIBUTING.md`](https://github.com/osa-ai-org/ordsa-ai/blob/main/CONTRIBUTING.md) — the OrdSA development process this ADR mirrors
- [`osa-ai-org/ordsa-ai/decisions/README.md`](https://github.com/osa-ai-org/ordsa-ai/blob/main/decisions/README.md) — OrdSA's ADR index used as the structural template for `decisions/README.md`
- [`osa-ai-org/ordsa-ai/decisions/TEMPLATE.md`](https://github.com/osa-ai-org/ordsa-ai/blob/main/decisions/TEMPLATE.md) — ADR shape mirrored at `decisions/TEMPLATE.md`
- [`OrdSA-Construct.png`](../constructs/ordsa/docs/marketing/OrdSA-Construct.png) — the OrdSA construct visual that positions OrdSA *for Enterprise AI*; the methodological context that motivates this ADR
