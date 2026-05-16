# ADR-OSA-0006 — Rename construct abbreviation from OSA to OrdSA

- **Status:** Accepted
- **Date:** 2026-05-16
- **Author:** JD Longmire
- **Bridge ADR:** This is the last ADR authored under the `ADR-OSA-NNNN` naming convention. It is renamed to `ADR-ORDSA-0006` as part of its own implementation. Future ADRs use `ADR-ORDSA-NNNN`.

## Context

The construct was introduced in v0.1 as **"Ordinal Systems Architecture (OSA)"**. The abbreviation **OSA** is heavily occupied in adjacent domains, particularly defense, aerospace, and systems-engineering — the same audiences the construct most directly serves.

Specific naming-conflict sources:

- **MOSA (Modular Open Systems Approach)** — formal DoD acquisition guidance with extensive supporting MIL-HDBK / MIL-STD references. "OSA" in defense-acquisition contexts almost always refers to the "Open Systems" lineage MOSA is built on.
- **"Open Systems Architecture"** — established phrase since the early 1990s in systems-engineering and platform-architecture literature.
- **ITRA / JCIDS / MIL-STD-810** — every defense-acquisition pipeline references OSA as an open-systems concept.

An adopter from these audiences encountering "Ordinal Systems Architecture (OSA)" plausibly assumes the construct is a continuation or specialization of Open Systems Architecture lineage. It is not. The collision compromises adoption from precisely the audience most likely to value an authority-control construct for Enterprise AI.

The full name **"Ordinal Systems Architecture"** is not the source of the collision and is retained. Only the abbreviation changes.

## Decision

**Rename the construct abbreviation from `OSA` to `OrdSA`.**

- Full name: **Ordinal Systems Architecture** (unchanged)
- Abbreviation: **OrdSA** (was: OSA)
- Pronunciation guidance: "ord-suh" or "ord-S-A" — left to community preference

The rename is executed at **Scope A — full** per the discussion that produced this ADR. All references to the abbreviation in the repository, the GitHub org/repo slugs, file names, ADR identifiers, schema dialect strings, citation URLs, and external announcements update to OrdSA.

## Scope A — what renames

| Surface | From | To |
|---|---|---|
| GitHub org | `osa-ai-org` | `ordsa-org` |
| GitHub repo | `osa-ai-org/osa-ai` | `ordsa-org/ordsa-ai` |
| Schema files | `schema/osa-N.M.yaml` | `schema/ordsa-N.M.yaml` |
| Schema dialect strings | `osa-construct-schema/N.M`, `osa-deployment-schema/N.M` | `ordsa-construct-schema/N.M`, `ordsa-deployment-schema/N.M` |
| Construct citation field | `osa_construct: "0.2"` | `ordsa_construct: "0.2"` |
| ADR file names | `decisions/ADR-OSA-NNNN-*.md` | `decisions/ADR-ORDSA-NNNN-*.md` |
| ADR identifiers in body text | `ADR-OSA-NNNN` | `ADR-ORDSA-NNNN` |
| Future ADR naming convention | `ADR-OSA-NNNN` | `ADR-ORDSA-NNNN` (numbering continues from 0007) |
| All prose in repo files | `OSA` → `OrdSA` | (verbatim global substitution, case-sensitive) |
| README, CONTRIBUTING, all docs | references updated | |

GitHub auto-redirects preserve old citation URLs for both org renames and repo renames; pinned links and adopter citations to the prior slugs continue to resolve. The redirect is best-effort and may degrade over time, so external publications should update where practical.

## Consequences

- **Single short-term churn, indefinite long-term clarity.** The internal references to update are bounded by the v0.1 codebase (six ADRs after this one is merged, ~10 docs, ~3 schema files, the main README). Adopting community has not yet formed; the rename cost is now contained.
- **GitHub redirects soften the URL migration.** Old `osa-ai-org/osa-ai` links keep working via GitHub's automatic redirect for renamed repos and orgs. Citation degradation is gradual, not abrupt.
- **The cross-fleet decision register at `ologos-corp/cross-ai`** does not yet reference OSA, so no register update is required by this ADR. When a future cross-fleet ADR ratifies OrdSA, that ADR cites the new abbreviation and the existence of this ADR as the rename precedent.
- **Telegram and external announcements made under the OSA name** remain in history; they are not retroactively edited. A follow-up Telegram post announces the rename with the rationale and the new canonical URL.
- **The ADR numbering convention shifts mid-stream.** `ADR-OSA-0001` through `ADR-OSA-0005` (the founding bundle) plus this `ADR-OSA-0006` rename to `ADR-ORDSA-NNNN` files in the migration PR. Future ADRs are authored as `ADR-ORDSA-0007`, `ADR-ORDSA-0008`, etc. — sequential numbering continues; only the prefix changes.
- **decisions/README.md** is updated to reflect the new naming and to document the bridge: ADR 0006 is identified as the rename ADR. The "Founding bundle" callout for ADRs 0001–0005 stays as historical fact.
- **No semantic change to the construct itself.** Layers, governance principle, execution rights, conformance assertions — all unchanged. This is purely a naming decision.

## Alternatives considered

1. **Keep "OSA" and rely on context to disambiguate.** Rejected — the defense / aerospace / systems-engineering audiences read OSA as Open Systems Architecture by default, not by exception. Context cannot reliably override an established acronym in audiences where that acronym is operational vocabulary.

2. **Pick a different abbreviation entirely** (e.g., `ORDSYS`, `OrdEA`, `OAA` for "Ordinal Authority Architecture", etc.). Rejected — `OrdSA` preserves the "Ordinal Systems Architecture" name's recognizable initials, only adding two letters from the middle word to disambiguate. Other abbreviations either drift further from the full name or introduce new collisions.

3. **Append a clarifying suffix** ("Ordinal Systems Architecture — OSA-O" or "OSA-Ord"). Rejected — half-measure that solves nothing; audiences still see `OSA` first and form the wrong association.

4. **Scope B (hybrid) rename** — keep GitHub org/repo slugs as `osa-ai-org/osa-ai`, rename everything else. Rejected — "OSA inside, OrdSA outside" creates persistent low-grade confusion ("why does the repo URL say one thing and the content say another?") and isn't materially cheaper than Scope A given current scale.

5. **Scope C (content-only) rename** — keep all file names, ADR IDs, and schema strings as `osa-*`; only change prose. Rejected — locks in "OSA" in every machine-readable surface of the construct, which is precisely the surface adopters will encounter when validating their deployments against the schema. The schema dialect string would still say `osa-construct-schema/N.M`, defeating the disambiguation goal.

6. **Defer the rename to v1.0.** Rejected — the longer the construct exists under OSA, the more external references accumulate, the higher the migration cost. The v0.1.x stage is the cheapest moment to rebrand.

## Migration plan

Implementation flows as **two PRs** for cleanness:

### PR 1 — This ADR (review and ratification)

- Adds `decisions/ADR-OSA-0006-rename-construct-to-ordsa.md` (this file)
- Adds index entry in `decisions/README.md` so the ADR is discoverable before the bulk migration
- Does **not** rename existing files yet — that's PR 2
- Label: `adr`
- Founding-bundle carve-out does not apply to this ADR; the 7-day comment-out is collapsed to a "maintainer-confirmed at draft" exception per JD authorship + sign-off

### PR 2 — Implementation (full rename)

- Rename all `decisions/ADR-OSA-NNNN-*.md` to `decisions/ADR-ORDSA-NNNN-*.md` (including this ADR — becomes `decisions/ADR-ORDSA-0006-rename-construct-to-ordsa.md`)
- Rename `schema/osa-0.2.yaml` to `schema/ordsa-0.2.yaml`; update `schema_dialect` and `osa_construct` fields throughout
- Rename `schema/example-deployment.yaml`'s `osa_construct` field to `ordsa_construct`; update schema_dialect
- Global content substitution: every prose reference to the abbreviation "OSA" updates to "OrdSA" (case-preserving)
- Update `decisions/README.md` to reflect new file names + numbering convention note
- Update main `README.md` references throughout (Status section, Governance section, link targets)
- Update `CONTRIBUTING.md` to reference the new ADR prefix
- Update `schema/README.md` similarly

### Out-of-band steps (execution order actually used)

The migration plan above describes the intended *PR sequence* (ADR first, then implementation). The out-of-band rename steps were performed in the order JD authorized at execution time, which deviated from the "after PR 2" framing originally drafted:

| Step | Status | Who | Mechanism |
|---|---|---|---|
| Rename GitHub repo `osa-ai` → `ordsa-ai` | **Done 2026-05-16, prior to this ADR's PR-open** | Operator (via JD authorization) | `gh api -X PATCH repos/osa-ai-org/osa-ai -f name=ordsa-ai` |
| Update local working tree `origin` URL | **Done 2026-05-16, same moment** | Operator | `git remote set-url origin https://github.com/osa-ai-org/ordsa-ai.git` |
| Rename GitHub org `osa-ai-org` → `ordsa-org` | Pending JD action | JD (web UI) | Org settings → top of People page → "Rename organization". GitHub API does not expose this. After this completes, the repo URL becomes `ordsa-org/ordsa-ai`. |
| Telegram heads-up | Scheduled (with PR 2 merge) | Operator | Standard `sendMessage` to `TELEGRAM_GROUP_CHAT_ID` |
| Comment on `ologos-corp/ologos-ai#162` | Scheduled (with PR 2 merge) | Operator | `gh issue comment` with new canonical URL |

The early repo rename is a defensible deviation from the original sequencing: GitHub's automatic redirect preserves existing URLs to `osa-ai-org/osa-ai`, so PR 1 (this ADR's ratification PR) opens cleanly on the renamed repo without breaking any in-flight references. The semantic gate is the ADR's ratification, not the order of mechanical steps.

## References

- [ADR-OSA-0001](ADR-OSA-0001-schema-first-canonical-form.md) through [ADR-OSA-0005](ADR-OSA-0005-archi-as-canonical-modeling-tool.md) — the founding bundle whose cross-references this rename touches
- [`../docs/concept.md`](../docs/concept.md) — full-name retention; abbreviation change reflected
- [`../docs/relationship-to-frameworks.md`](../docs/relationship-to-frameworks.md) — the framework-positioning doc that names OSA's relationship to TOGAF, UAF, ArchiMate, NIST AI RMF; the abbreviation rename touches this doc
- DoD MOSA documentation — the primary naming-conflict source. Open Systems Architecture in defense acquisition is well-documented and operationally vocabularized; OrdSA must not be conflated with it.
