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
| [ADR-EA-0009](ADR-EA-0009-introduce-digital-thread-pattern.md) | Introduce digital-thread pattern at canon level with new `patterns/` tier | Accepted |
| [ADR-EA-0010](ADR-EA-0010-adopt-doerr-okr-methodology.md) | Adopt John Doerr OKR methodology for VSOK Objectives + Key Results | Accepted |
| [ADR-EA-0012](ADR-EA-0012-introduce-prep-pursue-pivot-pattern.md) | Introduce prep-pursue-pivot pattern (three-faculty governed agent-cognition loop) | Accepted |
| [ADR-EA-0014](ADR-EA-0014-introduce-epistemic-integrity-floor-pattern.md) | Introduce Epistemic Integrity Floor (EIF) pattern | Accepted |
| [ADR-EA-0015](ADR-EA-0015-introduce-inference-plane.md) | Introduce Inference plane as AEON's 7th service plane | Accepted |
| [ADR-EA-0016](ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md) | Adopt AI-aide / MyAide as canon vocabulary | Accepted |
| [ADR-EA-0017](ADR-EA-0017-ai-aide-principal-altitudes.md) | AI-aide principal altitudes (operator/corpus distinction) | Accepted |
| [ADR-EA-0019](ADR-EA-0019-introduce-governed-context-management-pattern.md) | Introduce Governed Context Management pattern | Accepted |
| [ADR-EA-0020](ADR-EA-0020-amend-inference-plane-catalog-contract.md) | Inference plane catalog contract amendment: mandatory `context_window` + `tokenizer` (refines ADR-EA-0015) | Accepted |
| [ADR-EA-0021](ADR-EA-0021-mxm-ordsa-boundary-citation.md) | MxM↔OrdSA boundary: discipline surfaces cite peer constructs by reference (refines ADR-EA-0013) | Accepted |
| [ADR-EA-0022](ADR-EA-0022-pattern-bplus-and-canonical-aeon-refimpls.md) | Pattern B+ adoption discipline; Hermetic and NG-AIDE-01 as canonical AEON reference implementations | Accepted |
| [ADR-EA-0023](ADR-EA-0023-thinx-discipline-refinements.md) | Reference-impl-derived discipline refinements + canonical-ref-impl pin (founder-override pattern + GCM §8 + EIF §6 operationalization + thinx canonical MxM/EIF pin) | Proposed |
| [ADR-EA-0024](ADR-EA-0024-governed-context-management-hook-mediated-tier.md) | Governed Context Management §8 hook-mediated tier: mechanized re-grounding where the host harness exposes compaction-lifecycle hooks (refines §8) | Proposed |

## Per-construct ADRs

Per Pattern α, construct-internal ADRs live with their construct:

- [ADR-EA-0003](../constructs/dea/decisions/ADR-EA-0003-expand-corpus-to-include-dea.md) — Expand corpus to include DEA (Accepted; at [`constructs/dea/decisions/`](../constructs/dea/decisions/))
- [ADR-EA-0004](../constructs/mxm/decisions/ADR-EA-0004-add-mx-modes-as-spine-construct.md) — Add Mx-Modes as a spine construct (Accepted; at [`constructs/mxm/decisions/`](../constructs/mxm/decisions/))
- [ADR-EA-0005](../constructs/mxm/decisions/ADR-EA-0005-clarify-mxm-archetype.md) — Clarify MxM as the harness archetype across all levels (Accepted; at [`constructs/mxm/decisions/`](../constructs/mxm/decisions/))
- [ADR-EA-0013](../constructs/mxm/decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md) — Define the MxM root file (the "mode" element) as harness-attach + operating-mode activator + routing, not a governing altitude (Accepted; at [`constructs/mxm/decisions/`](../constructs/mxm/decisions/))
- [ADR-EA-0018](../constructs/aicp/decisions/ADR-EA-0018-introduce-aicp-construct.md) — Introduce AICP as a Tier-3 construct (Accepted; at [`constructs/aicp/decisions/`](../constructs/aicp/decisions/))

## Numbering

`ADR-EA-NNNN` numbering carries forward from the source corpus per the (α) prefix decision in cross-ai #40. Future canon-level ADRs continue the EA sequence. The numbering reflects the *historical* corpus name (Enterprise-AI); it is preserved for URL continuity.

## Template

See [TEMPLATE.md](TEMPLATE.md) for the ADR format.
