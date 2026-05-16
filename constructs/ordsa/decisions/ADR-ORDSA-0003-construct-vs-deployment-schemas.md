# ADR-ORDSA-0003 — Construct schema vs deployment schema (two shapes)

- **Status:** Accepted
- **Date:** 2026-05-16
- **Author:** JD Longmire
- **Bundle:** Founding ADR (0003 of 0005)

## Context

The canonical schema (per [ADR-ORDSA-0001](ADR-ORDSA-0001-schema-first-canonical-form.md), in YAML per [ADR-ORDSA-0002](ADR-ORDSA-0002-schema-language-yaml-json-schema.md)) must serve two distinct purposes:

- **Define the OrdSA construct itself** — the seven layers, the governance principle, allowed authority relationships, the five execution rights, the conformance assertion structure.
- **Describe a specific deployment claiming conformance** — what tools, agents, and orchestrators populate which layers in a given organization's AI architecture.

These are fundamentally different shapes:

| | Construct | Deployment |
|---|---|---|
| Mutability | Immutable within a version | Mutable per org |
| Authority | Maintainers (via ADR) | Deployment owner |
| Versioning | OrdSA release cadence | Local lifecycle |
| Validation role | The thing validated *against* | The thing *being* validated |

Conflating them — using one schema file for both — makes versioning ambiguous and obscures which fields are construct-level invariants versus per-deployment specifics.

## Decision

**Two distinct schema files per OrdSA version, with different shapes and lifecycles:**

1. **Construct schema** — `ordsa-N.M.yaml`
   - **What it is:** The OrdSA construct definition itself. Authoritative source for the seven layers, the governance principle, allowed cross-layer relationships, the five execution rights, the conformance assertion vocabulary.
   - **Mutability:** **Immutable within a version.** Changes flow through ADRs; new constructs ship as new versions (`ordsa-1.1.yaml`, `ordsa-2.0.yaml`).
   - **Authorship:** OrdSA maintainers, via the ADR + PR process.
   - **Lifecycle:** Tagged to OrdSA releases.

2. **Deployment schema** — `<deployment>.yaml` (filename is per-org)
   - **What it is:** A specific organization's claim of OrdSA conformance. Lists the deployment's concrete artifacts per layer, makes the conformance assertions defined by the construct, points at evidence.
   - **Mutability:** Mutable as the deployment evolves. Per-org governance.
   - **Authorship:** The deployment owner (whatever person, team, or automated process the org delegates to).
   - **Lifecycle:** Tied to the deployment's life, not OrdSA's release cadence.
   - **Validation:** Validated *against* a specific construct version it claims (`ordsa_construct: "1.0"` in the deployment file points at `ordsa-1.0.yaml`).

The construct schema is what adopters cite. The deployment schema is what they publish to claim conformance.

## Consequences

- **Versioning is unambiguous.** "What version of OrdSA does deployment X claim?" has a single answer in the deployment file. "Is this deployment conformant?" reduces to "does deployment X validate against construct version Y?"
- **Construct-level evolution is governed; deployment-level evolution is not.** Per-org changes don't need ADRs. Construct changes do.
- **Conformance checking is mechanical.** A validator (per [ADR-ORDSA-0004](ADR-ORDSA-0004-reference-tooling-python-pydantic.md)) takes a deployment file and a construct file, runs schema validation plus the construct-defined conformance rules, and emits pass/fail with reasons.
- **Multi-version coexistence works.** An org can have multiple deployments at different OrdSA construct versions; an OrdSA release can support older deployment files until explicitly deprecated.
- **The deployment schema's *fields* are defined by the construct schema.** A deployment can't invent new layer IDs or new execution rights — those come from the construct it claims. This is the schema-level enforcement of "no lower layer expands its own authority" (transposed: no deployment expands OrdSA's own vocabulary).
- **Per-version migration may become a thing.** Going from a deployment-at-1.0 to deployment-at-1.1 may require field-level updates. Migration helpers are a v0.3+ concern.

## Alternatives considered

1. **Single schema for both.** Conflates immutable construct definition with mutable deployment instance. Versioning becomes ambiguous ("what does it mean for `ordsa-1.0.yaml` to have my company's specific tools listed?"). Rejected.

2. **Construct as schema, deployment as freeform prose.** Loses mechanical conformance checking — the whole point of having a schema. Rejected.

3. **Deployment as schema, construct as prose.** What v0.1 effectively was. Adopters had nothing to validate against. Rejected.

4. **Three schemas — construct, profile, deployment.** A "profile" intermediate layer for industry- or sector-specific specializations (e.g., "OrdSA for defense," "OrdSA for fintech"). Considered but deferred — profiles can be added later as a v0.2+ ADR without breaking the two-schema model. Premature.

5. **Embed deployment as a section inside the construct YAML.** Same conflation problem as alternative 1. Rejected.

## References

- [ADR-ORDSA-0001](ADR-ORDSA-0001-schema-first-canonical-form.md) — schema-first canonical form
- [ADR-ORDSA-0002](ADR-ORDSA-0002-schema-language-yaml-json-schema.md) — YAML + JSON Schema
- [ADR-ORDSA-0004](ADR-ORDSA-0004-reference-tooling-python-pydantic.md) — reference validator/generator tooling
- [`../docs/reference-implementations.md`](../docs/reference-implementations.md) — conformance bar this schema mechanizes
