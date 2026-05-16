# ADR-ORDSA-0002 — Schema language: YAML source + auto-emitted JSON Schema

- **Status:** Accepted
- **Date:** 2026-05-16
- **Author:** JD Longmire
- **Bundle:** Founding ADR (0002 of 0005)

## Context

[ADR-ORDSA-0001](ADR-ORDSA-0001-schema-first-canonical-form.md) establishes that the canonical OrdSA source is a versioned, tool-neutral schema. This ADR picks the concrete language.

Candidates evaluated: **YAML**, **JSON Schema**, **TOML**, **Protobuf**, **XML Schema (XSD)**, **custom DSL**. Constraints: human-readable for authoring, machine-validatable across language ecosystems, broad familiarity in EA and research communities, no proprietary tooling required.

A secondary constraint: adopters need a machine-validatable artifact (something a deployment can be checked against), not just a human-readable one. The two needs are in tension — human-friendly formats like YAML lack the strict typing of JSON Schema, while strict-typed formats like Protobuf are harder for humans to author and read.

## Decision

**The canonical OrdSA schema is authored in YAML.** A JSON Schema representation is **auto-emitted** from the YAML source for tooling consumption (validators, IDE integrations, code generators).

- **YAML** (`ordsa-N.M.yaml`) is the source of truth. Edited by hand, reviewed in PRs, the artifact ADRs touch.
- **JSON Schema** (`ordsa-N.M.schema.json`) is a derived artifact, generated from the YAML by reference tooling at release time. Adopters and downstream tools consume the JSON Schema.

Both ship with every OrdSA release. The release process verifies the JSON Schema is in sync with the YAML before publishing.

## Consequences

- **YAML for humans, JSON Schema for machines.** Each format serves its strongest use case; neither has to compromise.
- **Tooling owns the YAML-to-JSON-Schema transformation.** Reference tooling ([ADR-ORDSA-0004](ADR-ORDSA-0004-reference-tooling-python-pydantic.md)) is responsible for this emission and for verifying sync. A drift between the two is a release-blocking bug.
- **Comments survive in YAML.** Inline rationale and field-level explanations live in the source, where they're preserved and reviewed. JSON Schema's lack of comments doesn't matter — the source carries the commentary.
- **Language bindings derive from JSON Schema.** Future TypeScript types, Python pydantic models, Go structs, etc. are generated from the JSON Schema, not the YAML, so they pick up the strict typing.
- **One canonical version pair per release.** `ordsa-1.0.yaml` + `ordsa-1.0.schema.json` ship together; downstream tools can pin to either or both.
- **YAML quirks become content concerns.** Numeric strings, indentation sensitivity, anchor reuse — the schema must be authored defensively to avoid YAML footguns (e.g., quote layer IDs like `"O1"` to prevent boolean coercion).

## Alternatives considered

1. **JSON Schema as the source format.** Verbose for humans, no comments, awkward to author by hand. Rejected — strict typing without authoring ergonomics is the wrong trade for a source-of-truth artifact.

2. **TOML as source.** Cleaner than YAML for flat structures, but OrdSA's nested layer/relationship structure pulls toward YAML's idioms. TOML's lack of native list-of-objects support adds friction. Rejected for ergonomics.

3. **Protobuf as source.** Strong typing, code generation, mature tooling. Rejected — high barrier for EA/research audience that doesn't already work in Protobuf; less common than YAML; build-tool dependency for editing.

4. **XML Schema (XSD).** Most rigorous, native to the ArchiMate Exchange format. Rejected — XSD authoring is hostile to humans, and the construct schema operates above the ArchiMate level (which is one of several renderings, per ADR-ORDSA-0001).

5. **Custom DSL.** Premature. YAML already does what's needed; a custom DSL adds a parser, a grammar, and a learning curve for zero immediate gain.

6. **YAML only, no JSON Schema emission.** Loses machine validation in non-YAML-aware tooling. Rejected — half-measure.

## References

- [ADR-ORDSA-0001](ADR-ORDSA-0001-schema-first-canonical-form.md) — schema-first canonical form (the precondition for this choice)
- [ADR-ORDSA-0003](ADR-ORDSA-0003-construct-vs-deployment-schemas.md) — schema shape (defines what the YAML contains)
- [ADR-ORDSA-0004](ADR-ORDSA-0004-reference-tooling-python-pydantic.md) — tooling that emits JSON Schema from YAML
- [JSON Schema specification](https://json-schema.org/)
- [YAML 1.2.2 specification](https://yaml.org/spec/1.2.2/)
