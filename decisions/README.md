# decisions/

Canon-level Architecture Decision Records (ADRs) for the AIDE corpus. Append-only and immutable per ADR-EA-0001.

## Index

| ID | Title | Status |
|---|---|---|
| [ADR-EA-0001](ADR-EA-0001-adopt-ordsa-development-process.md) | Adopt OrdSA-style development process for the corpus | Accepted |
| [ADR-EA-0002](ADR-EA-0002-reframe-as-ordsa-exemplar.md) | Reframe enterprise-ai as the canonical enterprise-scale OrdSA exemplar | Accepted |
| [ADR-EA-0006](ADR-EA-0006-migrate-corpus-to-aide-canon.md) | Migrate corpus to `ologos-repos/aide-canon` as the canonical home | Accepted |
| [ADR-EA-0007](ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) | Introduce Vision-Strategy at Tier 0 (VSOK as artifact) and rename Tier 1 to Mode Alpha | Accepted |
| [ADR-EA-0008](ADR-EA-0008-reframe-corpus-authorship.md) | Reframe corpus authorship as JD Longmire and Micah Longmire (co-authored) | Accepted |
| [ADR-EA-0009](ADR-EA-0009-introduce-digital-thread-pattern.md) | Introduce digital-thread pattern at canon level with new `patterns/` tier | Proposed |
| [ADR-EA-0010](ADR-EA-0010-adopt-doerr-okr-methodology.md) | Adopt John Doerr OKR methodology for VSOK Objectives + Key Results | Accepted |

## Per-construct ADRs

Per Pattern α, construct-internal ADRs live with their construct:

- [ADR-EA-0003](../constructs/dea/decisions/ADR-EA-0003-expand-corpus-to-include-dea.md) — Expand corpus to include DEA (now at [`constructs/dea/decisions/`](../constructs/dea/decisions/))
- [ADR-EA-0004](../constructs/mxm/decisions/ADR-EA-0004-add-mx-modes-as-spine-construct.md) — Add Mx-Modes as a spine construct (now at [`constructs/mxm/decisions/`](../constructs/mxm/decisions/))
- [ADR-EA-0005](../constructs/mxm/decisions/ADR-EA-0005-clarify-mxm-archetype.md) — Clarify MxM as the harness archetype across all levels (now at [`constructs/mxm/decisions/`](../constructs/mxm/decisions/))

## Numbering

`ADR-EA-NNNN` numbering carries forward from the source corpus per the (α) prefix decision in cross-ai #40. Future canon-level ADRs continue the EA sequence. The numbering reflects the *historical* corpus name (Enterprise-AI); it is preserved for URL continuity.

## Template

See [TEMPLATE.md](TEMPLATE.md) for the ADR format.
