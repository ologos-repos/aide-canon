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
7. **Inference** — provider+model routing; per-principal binding; classification-environment filter; runtime switching. Catalog contract mandates `context_window` + `tokenizer` per model entry (per [ADR-EA-0020](../../decisions/ADR-EA-0020-amend-inference-plane-catalog-contract.md)), so the model-agnostic harness can budget context against truth-from-the-plane per the [Governed Context Management pattern](../../patterns/governed-context-management.md) §2.

## Reference implementations and operational patterns

AEON reference implementations are governed by **Pattern B+** (out-of-tree cite + conformance-anchored manifest when spec lands) per [ADR-EA-0022](../../decisions/ADR-EA-0022-pattern-bplus-and-canonical-aeon-refimpls.md). Two canonical AEON reference implementations are currently recognized, role-differentiated:

### Hermetic — production-maturity exemplar

[`ologos-repos/Hermetic`](https://github.com/ologos-repos/Hermetic). Production system (295 Go files, MIT, Ologos LLC, used in production via [Rhode](https://github.com/bobbyhiddn/Rhode), private). Implements the AEON service planes — Worker Roster (Identity), Oracle Bus + Ordinal Escalation L0–L3 (Authority), Eidolon PLM phase-gates + audit log + SHA-256 artifact tracking (Evidence), Sub-Prime Federation + Telegram bridge (Integration), worker affinity + capability tags + auto_delegate routing (Capability Composition), Prime main loop + dispatch loop + TUI (Orchestration Runtime). The 7th plane (Inference, per [ADR-EA-0015](../../decisions/ADR-EA-0015-introduce-inference-plane.md)) lands in the manifest as Hermetic's model-routing surface matures against the [Inference catalog contract](../../decisions/ADR-EA-0020-amend-inference-plane-catalog-contract.md). Conformance manifest: `docs/canon-mapping.md` (forthcoming, per [`Hermetic#37`](https://github.com/ologos-repos/Hermetic/issues/37)).

### NG-AIDE-01 — canon-fidelity exemplar

[`ologos-repos/ng-aide-01`](https://github.com/ologos-repos/ng-aide-01). Built under the latest canon batch (ADRs 0013 / 0015 / 0017 / 0019 / 0020) with explicit traceability of every plane to current ADRs. Six AEON service planes v0.1 (stdlib-Go services mirroring AEON spec idioms) + [Inference plane scope](https://github.com/ologos-repos/ng-aide-01/pull/22) (ADRs 0015 / 0019 / 0020) + three domains v0.1 (InfOps / DevSecOps / Cyber) + [AICP attestation ingress at the verify-only floor](https://github.com/ologos-repos/ng-aide-01/pull/19) (per [ADR-EA-0018](../../constructs/aicp/decisions/ADR-EA-0018-introduce-aicp-construct.md)) + OpenCode runtime harness wired to the AEON MCP gateway. Conformance manifest: `docs/canon-mapping.md` (forthcoming, same shape as Hermetic's).

The two roles are complementary, not redundant — Hermetic's production-maturity is the empirical proof that the AEON pattern works at scale; NG-AIDE-01's canon-fidelity is the formal proof that the current-vintage canon is buildable. Future canon-conformant AEON impls may be added under the same Pattern B+ discipline per [ADR-EA-0022](../../decisions/ADR-EA-0022-pattern-bplus-and-canonical-aeon-refimpls.md) §Part 4.

### Operational patterns

- **The [digital-thread pattern](../../patterns/digital-thread.md)** (per [ADR-EA-0009](../../decisions/ADR-EA-0009-introduce-digital-thread-pattern.md)) — a six-layer FK-linked traceability chain (requirements → tasks → phases → artifacts → reviews → audit-log) that names what AEON's evidence plane operationally produces. The pattern is cross-cutting; AEON's evidence plane is its primary canon-side surface.
- **The [Governed Context Management pattern](../../patterns/governed-context-management.md)** (per [ADR-EA-0019](../../decisions/ADR-EA-0019-introduce-governed-context-management-pattern.md)) — distributes context-management discipline across the Inference plane (catalog contract per [ADR-EA-0020](../../decisions/ADR-EA-0020-amend-inference-plane-catalog-contract.md)), Orchestration Runtime (compaction), and Evidence plane (`context.compacted` audit events). The model-agnostic AEON harness consumes this pattern; both canonical reference impls realize it.

## Citation

[`10.5281/zenodo.20349596`](https://doi.org/10.5281/zenodo.20349596) — Longmire, J. D., & Longmire, M. (2026). *AEON: An Enterprise Control Plane Architecture for the Agentic Era*. Zenodo.

Deposited 2026-05-22 to the [AI Research & Philosophy community](https://zenodo.org/communities/ai-research-philosophy/). Cites HCAE (`10.5281/zenodo.18368697`) and AIDK (`10.5281/zenodo.18316059`) as upstream foundation. License: CC BY 4.0.

## Provenance

Sourced from `osa-ai-org/enterprise-ai/docs/` (snapshot copy).
