# Contributing to OSA

Thanks for reading the construct closely enough to want to contribute. A few notes on how contributions flow.

## Two kinds of change

OSA distinguishes between **construct changes** and **content changes**, because they have different reversibility profiles.

**Construct changes** modify the framework itself — adding a layer, removing a layer, redefining a layer's authority boundary, changing the governance principle, altering the relationship between OSA and an external framework. These changes are hard to retract once cited. They flow through ADRs as **PRs**:

1. *(Optional)* If the change is contentious or you want community signal first, open a **Construct Q&A** discussion describing the question before authoring the ADR.
2. Draft an ADR in `decisions/ADR-OSA-NNNN-<slug>.md` (numbering is sequential, append-only) using [`decisions/TEMPLATE.md`](decisions/TEMPLATE.md) as a starting point.
3. Open a PR with the ADR. Apply the **`adr`** label. Discussion happens on the PR — the PR is the deliberation record, the merge is ratification.
4. Ratification requires explicit sign-off from the maintainer (currently @jdlongmire) and a comment-out period of at least one calendar week, unless the ADR is purely editorial or part of a maintainer-batched founding set.
5. Merged ADRs are immutable. A later ADR may supersede an earlier one; the earlier one stays in the tree marked `Superseded by ADR-OSA-NNNN`.

See [`decisions/README.md`](decisions/README.md) for the navigable index of ratified ADRs.

### Why PRs (not Issues) for ADRs

The PR *is* the ADR's lifecycle. Discussion on the PR is the deliberation, reviews are the consensus signal, the merge commit is the ratification timestamp, and the file at `decisions/ADR-OSA-NNNN-<slug>.md` is the durable record. Issues are reserved for **construct gaps**, **implementation work**, and **umbrella tracking of multi-ADR programs** — not for the decisions themselves.

**Content changes** — clarifying wording in layer files, adding examples, fixing typos, expanding the framework-positioning doc, improving diagrams — flow as ordinary PRs. No ADR needed.

## What goes where

| Change | Path | Mechanism |
|---|---|---|
| Construct definition (layers, principle) | `docs/concept.md`, `docs/layers/O*.md` | ADR + PR |
| Layer examples / anti-patterns / clarifications | `docs/layers/O*.md` | PR |
| Worked scenarios | `docs/examples/` (not yet present in v0.1) | PR |
| External-framework mapping | `docs/relationship-to-frameworks.md` | PR (or ADR if redefining the relationship) |
| Reference implementations | `docs/reference-implementations.md` | Issue to propose, PR to add |
| Reference impls / schemas | (future) `reference/` | PR (under Apache-2.0 — see LICENSE notes) |

## Style

- Prose, not jargon. If a sentence requires a glossary to parse, rewrite it.
- Examples beat exhaustive enumeration. One concrete walkthrough explains the layer better than a feature list.
- Cite frameworks by name, not by acronym alone, on first mention.
- Diagrams are welcome but should be authored as committed source (SVG / Mermaid / PlantUML) — no opaque PNG-only artifacts.

## What this repo is not

- It is **not** a product spec. OSA defines authority structure, not implementation.
- It is **not** a model-evaluation framework. OSA assumes models are capable; it governs whether they're authorized.
- It is **not** a wrapper around any single vendor's stack. The construct is vendor-neutral by design.

If you have a question about whether your idea fits, open a **Construct Q&A** discussion before writing the PR. Cheaper than a rewrite.

## Artifact roles at a glance

| Artifact | Use for |
|---|---|
| **PR** | Concrete changes (content edits, ADRs, schema updates, examples). The PR is the change's lifecycle and record. |
| **Issue** | Construct gaps, implementation work, umbrella tracking of multi-PR programs. Not the place where decisions get made. |
| **Discussion** | Pre-PR brainstorming, Construct Q&A, Adoption Stories, Reference Implementation proposals. Output may inform a PR but isn't itself a durable record. |
