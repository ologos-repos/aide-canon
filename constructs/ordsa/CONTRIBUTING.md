# Contributing to OSA

Thanks for reading the construct closely enough to want to contribute. A few notes on how contributions flow.

## Two kinds of change

OSA distinguishes between **construct changes** and **content changes**, because they have different reversibility profiles.

**Construct changes** modify the framework itself — adding a layer, removing a layer, redefining a layer's authority boundary, changing the governance principle, altering the relationship between OSA and an external framework. These changes are hard to retract once cited. They flow through ADRs:

1. Open an issue tagged `construct-change` describing the motivation and proposed change.
2. Draft an ADR in `decisions/ADR-OSA-NNNN-<slug>.md` (numbering is sequential, append-only).
3. Open a PR with the ADR. Discussion happens on the PR.
4. Ratification requires explicit sign-off from the maintainer (currently @jdlongmire) and a comment-out period of at least one calendar week unless the change is purely editorial.
5. Merged ADRs are immutable. A later ADR may supersede an earlier one; the earlier one stays in the tree marked `Superseded by ADR-OSA-NNNN`.

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

If you have a question about whether your idea fits, open an issue before writing the PR. Cheaper than a rewrite.
