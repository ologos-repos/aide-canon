# AEON — AI Enterprise Orchestration Nexus

The enterprise control plane for the agentic era — **seven service planes** (identity, authority, evidence, integration, capability composition, orchestration runtime, **inference** — per [ADR-EA-0015](../../decisions/ADR-EA-0015-introduce-inference-plane.md)). Enterprise IT-developed and sustained, not a vendor product.

> *White-paper currency:* the published [AEON white paper v1](https://doi.org/10.5281/zenodo.20349194) specifies six planes (the canonical record at deposit time, 2026-05-22). The 7th plane (Inference) was ratified at canon level on 2026-05-24 per [ADR-EA-0015](../../decisions/ADR-EA-0015-introduce-inference-plane.md); the **AEON white paper v0.2 revision adding §13 (Inference plane) is queued behind Micah Longmire's co-author read per [ADR-EA-0008](../../decisions/ADR-EA-0008-reframe-corpus-authorship.md)** corpus-authorship discipline. Reference implementations (NG-AIDE-01) build to the 7-plane shape immediately; the paper revision follows.

## Authors

Co-authored by **JD Longmire** (ORCID [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)) and **Micah Longmire** (ORCID [0009-0006-7608-9322](https://orcid.org/0009-0006-7608-9322)) per [ADR-EA-0008](../../decisions/ADR-EA-0008-reframe-corpus-authorship.md). The published white paper records the pre-reframe sole authorship.

## Canonical artifact

[`docs/AEON-White-Paper.pdf`](docs/AEON-White-Paper.pdf) — six service planes specified (v1, 2026-05-22 deposit); Enterprise IT operating model; multi-classification deployment; phased path; minimal coherent subset. The 7th plane (Inference, per [ADR-EA-0015](../../decisions/ADR-EA-0015-introduce-inference-plane.md)) is canon-ratified; the paper revision adding it as §13 is queued behind Micah's co-author read per ADR-EA-0008.

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

Seven service planes order the canon's three lower constructs:
- DEA frames the EA coherence the control plane must achieve
- OrdSA orders the authority and evidence planes within AEON
- MxM is the harness archetype each AEON-bound agent instantiates

The seven planes (per [ADR-EA-0015](../../decisions/ADR-EA-0015-introduce-inference-plane.md) as of 2026-05-24):

1. **Identity** — resolve principals; delegation chains
2. **Authority** — envelope evaluation; OrdSA authority modes
3. **Evidence** — append-only audit substrate; digital-thread orchestration layer
4. **Capability Composition** — registry; lifecycle staging (only operational dispatches)
5. **Integration** — MCP gateway; cross-domain workflow composition; the inbound external surface
6. **Orchestration Runtime** — the dispatch loop; tie-point for the other planes
7. **Inference** — provider+model routing; per-principal binding; classification-environment filter; runtime switching

## Reference implementation and operational patterns

- **Reference impl** (proposed): [`ologos-repos/Hermetic`](https://github.com/ologos-repos/Hermetic) — see [`aide-canon#5`](https://github.com/ologos-repos/aide-canon/issues/5). Hermetic's three architectural layers (Task Queue + Oracle Bus + Signal/Gate Dispatch) plus its Worker Roster, Eidolon PLM, Sub-Prime Federation, and Nous memory map to AEON's six service planes; see the issue for the per-plane mapping.
- **Operational pattern produced by the evidence service plane:** the **[digital-thread pattern](../../patterns/digital-thread.md)** (per [ADR-EA-0009](../../decisions/ADR-EA-0009-introduce-digital-thread-pattern.md)) — a six-layer FK-linked traceability chain (requirements → tasks → phases → artifacts → reviews → audit-log) that names what AEON's evidence plane operationally produces. The pattern is cross-cutting; AEON's evidence plane is its primary canon-side surface.

## Citation

[`10.5281/zenodo.20349194`](https://doi.org/10.5281/zenodo.20349194) — Longmire, J. D., & Longmire, M. (2026). *AEON: An Enterprise Control Plane Architecture for the Agentic Era*. Zenodo.

Deposited 2026-05-22 to the [AI Research & Philosophy community](https://zenodo.org/communities/ai-research-philosophy/). Cites HCAE (`10.5281/zenodo.18368697`) and AIDK (`10.5281/zenodo.18316059`) as upstream foundation. License: CC BY 4.0.

## Provenance

Sourced from `osa-ai-org/enterprise-ai/docs/` (snapshot copy).
