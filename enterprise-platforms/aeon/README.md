# AEON — AI Enterprise Orchestration Nexus

The enterprise control plane for the agentic era — six service planes (identity, authority, evidence, integration, capability composition, orchestration runtime). Enterprise IT-developed and sustained, not a vendor product.

## Authors

Co-authored by **JD Longmire** (ORCID [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)) and **Micah Longmire** (ORCID [0009-0006-7608-9322](https://orcid.org/0009-0006-7608-9322)) per [ADR-EA-0008](../../decisions/ADR-EA-0008-reframe-corpus-authorship.md). The published white paper records the pre-reframe sole authorship.

## Canonical artifact

[`docs/AEON-White-Paper.pdf`](docs/AEON-White-Paper.pdf) — six service planes specified; Enterprise IT operating model; multi-classification deployment; phased path; minimal coherent subset.

## Layout

```
enterprise-platforms/aeon/
├── README.md (this file)
├── docs/
│   └── AEON-White-Paper.{docx,pdf}
└── spec/                           # reserved (buildable spec)
```

## Position in the canon

AEON is the **control plane** in the AIDE argument lineage:

> AIDK → HCAE → AIDEX → **AEON** (control plane the deployment lives in)

Six service planes order the canon's three lower constructs:
- DEA frames the EA coherence the control plane must achieve
- OrdSA orders the authority and evidence planes within AEON
- MxM is the harness archetype each AEON-bound agent instantiates

## Reference implementation and operational patterns

- **Reference impl** (proposed): [`ologos-repos/Hermetic`](https://github.com/ologos-repos/Hermetic) — see [`aide-canon#5`](https://github.com/ologos-repos/aide-canon/issues/5). Hermetic's three architectural layers (Task Queue + Oracle Bus + Signal/Gate Dispatch) plus its Worker Roster, Eidolon PLM, Sub-Prime Federation, and Nous memory map to AEON's six service planes; see the issue for the per-plane mapping.
- **Operational pattern produced by the evidence service plane:** the **[digital-thread pattern](../../patterns/digital-thread.md)** (per [ADR-EA-0009](../../decisions/ADR-EA-0009-introduce-digital-thread-pattern.md)) — a six-layer FK-linked traceability chain (requirements → tasks → phases → artifacts → reviews → audit-log) that names what AEON's evidence plane operationally produces. The pattern is cross-cutting; AEON's evidence plane is its primary canon-side surface.

## Citation

[`10.5281/zenodo.20349596`](https://doi.org/10.5281/zenodo.20349596) — Longmire, J. D., & Longmire, M. (2026). *AEON: An Enterprise Control Plane Architecture for the Agentic Era*. Zenodo.

Deposited 2026-05-22 to the [AI Research & Philosophy community](https://zenodo.org/communities/ai-research-philosophy/). Cites HCAE (`10.5281/zenodo.18368697`) and AIDK (`10.5281/zenodo.18316059`) as upstream foundation. License: CC BY 4.0.

## Provenance

Sourced from `osa-ai-org/enterprise-ai/docs/` (snapshot copy).
