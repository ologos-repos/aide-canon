# OSA Reference Implementations

OSA is a vendor-neutral construct. It does not prescribe a single runtime, a single agent standard, or a single tool surface — it describes the **authority grammar** that any such implementation must satisfy.

This file links to concrete implementations of OSA layers as they mature.

## Status

**v0.1** — No reference implementations linked yet. This file is a forward placeholder; entries land here once published implementations satisfy the inclusion criteria below.

## Criteria for inclusion

For an implementation to be linked here it must:

1. **Implement one or more OSA layers (O0–O6)** in a way that respects the governance principle — authority flows downward, evidence flows upward, no lower layer expands its own authority.
2. **Be published** — code or specification — under a license that permits independent review.
3. **Carry a documented OSA conformance statement** that names which layers it implements and how its authority boundaries align with this construct.

Implementations without an explicit conformance statement may still be useful examples, but they are not part of the OSA reference set listed here.

## How to propose an implementation

Open an issue describing:

- The implementation's name, repo, and license
- Which OSA layers it claims to cover (O0 through O6)
- Its conformance statement — how each claimed layer's authority boundary maps to OSA's definition
- Any known divergences and the reasoning behind them

Discussion happens on the issue. Accepted entries flow as PRs into this file with a short profile per implementation.

## Layer coverage matrix (target)

When implementations are added, they will appear here in a coverage matrix:

| Implementation | O0 | O1 | O2 | O3 | O4 | O5 | O6 |
|---|---|---|---|---|---|---|---|
| _none yet_ | — | — | — | — | — | — | — |

A given implementation rarely covers all seven layers. The matrix makes per-layer coverage explicit, so adopters can compose implementations across layers rather than assuming any single implementation is canonical.
