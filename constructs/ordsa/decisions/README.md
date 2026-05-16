# Architectural Decision Records

This directory holds the **ratified ADRs** for OSA — append-only records of construct-level decisions and the reasoning behind them.

For the authoring process, see [`../CONTRIBUTING.md`](../CONTRIBUTING.md). For the ADR shape, see [`TEMPLATE.md`](TEMPLATE.md).

## Index

| ADR | Status | Date | Title |
|---|---|---|---|
| [0001](ADR-OSA-0001-schema-first-canonical-form.md) | Accepted | 2026-05-16 | Schema-first canonical form |
| [0002](ADR-OSA-0002-schema-language-yaml-json-schema.md) | Accepted | 2026-05-16 | Schema language: YAML source + auto-emitted JSON Schema |
| [0003](ADR-OSA-0003-construct-vs-deployment-schemas.md) | Accepted | 2026-05-16 | Construct schema vs deployment schema (two shapes) |
| [0004](ADR-OSA-0004-reference-tooling-python-pydantic.md) | Accepted | 2026-05-16 | Reference tooling: Python + pydantic for v0.2 |
| [0005](ADR-OSA-0005-archi-as-canonical-modeling-tool.md) | Accepted | 2026-05-16 | ArchiMate as canonical visual notation; pyArchimate as reference renderer |
| [0006](ADR-OSA-0006-rename-construct-to-ordsa.md) | Accepted | 2026-05-16 | Rename construct abbreviation from OSA to OrdSA (disambiguation from Open Systems Architecture / MOSA) — last ADR under `ADR-OSA-NNNN` naming; future ADRs use `ADR-ORDSA-NNNN` |

### Founding bundle

ADRs 0001–0005 ratify the v0.2 baseline as a single coherent set: schema-first source of truth (0001), YAML + JSON Schema (0002), construct vs deployment shapes (0003), Python + pydantic for reference tooling (0004), and ArchiMate via pyArchimate for visual rendering (0005). Per [`../CONTRIBUTING.md`](../CONTRIBUTING.md), founding ADRs are exempt from the one-week comment-out period; future ADRs follow the standard cadence.

### Where each ADR's artifacts live

| ADR | Concrete artifact embodying the decision |
|---|---|
| 0001 (schema-first) | [`../schema/`](../schema/) — the directory holding the canonical schema |
| 0002 (YAML + JSON Schema) | [`../schema/osa-0.2.yaml`](../schema/osa-0.2.yaml); JSON Schema emission deferred to reference-tooling PR |
| 0003 (construct vs deployment) | [`../schema/osa-0.2.yaml`](../schema/osa-0.2.yaml) (construct) + [`../schema/example-deployment.yaml`](../schema/example-deployment.yaml) (deployment shape) |
| 0004 (Python + pydantic) | `tools/osa-validator/` — not yet present; lands in a follow-up PR |
| 0005 (ArchiMate via pyArchimate) | Rendering pipeline; first diagrams emerge with reference tooling |

## Conventions

- **Numbering** is sequential and never reused: `ADR-OSA-0001`, `ADR-OSA-0002`, etc. A retracted-before-merge draft does not consume a number; ADRs are numbered at PR-open time and the number is held until merge or withdrawal.
- **Filename** is `ADR-OSA-NNNN-<slug>.md` where `<slug>` is lowercase-kebab-case (e.g., `ADR-OSA-0001-schema-first-canonical-form.md`).
- **Status** values: `Proposed` (PR open), `Accepted` (PR merged), `Superseded by ADR-OSA-NNNN` (a later ADR replaces this one). Withdrawn drafts don't enter the index.
- **Immutability**: once an ADR is merged, the file is not edited except for typo fixes and the addition of a `Superseded by` note in the header. Substantive revision happens by writing a new ADR that supersedes the old one.

## How to read this index

The entries here are durable claims. If you're integrating OSA into your enterprise architecture practice, ADRs explain the *why* behind the construct as it stands today — they tell you which design alternatives were considered and rejected, so you can judge whether your context warrants reopening a question.

If an entry says **Superseded by**, follow the chain — the latest ADR in the chain is the active position. Earlier ADRs in the chain remain in the tree as history, but should not be cited as current.
