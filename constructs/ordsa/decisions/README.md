# Architectural Decision Records

This directory holds the **ratified ADRs** for OSA — append-only records of construct-level decisions and the reasoning behind them.

For the authoring process, see [`../CONTRIBUTING.md`](../CONTRIBUTING.md). For the ADR shape, see [`TEMPLATE.md`](TEMPLATE.md).

## Index

| ADR | Status | Date | Title |
|---|---|---|---|
| _none yet_ | — | — | The founding ADRs (0001–0004) will land with the v0.2 schema PR. |

## Conventions

- **Numbering** is sequential and never reused: `ADR-OSA-0001`, `ADR-OSA-0002`, etc. A retracted-before-merge draft does not consume a number; ADRs are numbered at PR-open time and the number is held until merge or withdrawal.
- **Filename** is `ADR-OSA-NNNN-<slug>.md` where `<slug>` is lowercase-kebab-case (e.g., `ADR-OSA-0001-schema-first-canonical-form.md`).
- **Status** values: `Proposed` (PR open), `Accepted` (PR merged), `Superseded by ADR-OSA-NNNN` (a later ADR replaces this one). Withdrawn drafts don't enter the index.
- **Immutability**: once an ADR is merged, the file is not edited except for typo fixes and the addition of a `Superseded by` note in the header. Substantive revision happens by writing a new ADR that supersedes the old one.

## How to read this index

The entries here are durable claims. If you're integrating OSA into your enterprise architecture practice, ADRs explain the *why* behind the construct as it stands today — they tell you which design alternatives were considered and rejected, so you can judge whether your context warrants reopening a question.

If an entry says **Superseded by**, follow the chain — the latest ADR in the chain is the active position. Earlier ADRs in the chain remain in the tree as history, but should not be cited as current.
