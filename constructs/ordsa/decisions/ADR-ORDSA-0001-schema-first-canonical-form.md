# ADR-ORDSA-0001 — Schema-first canonical form

- **Status:** Accepted
- **Date:** 2026-05-16
- **Author:** JD Longmire
- **Bundle:** Founding ADR (0001 of 0005)

## Context

OrdSA's construct could be authored canonically in any of several formats: an ArchiMate model, SysML v2 textual source, UAF viewpoints, a custom textual DSL, or a tool-neutral structured schema. The choice is load-bearing because it determines (a) what artifact adopters cite, (b) what artifact gates conformance, and (c) which tool ecosystem OrdSA implicitly endorses.

v0.1 shipped the construct as Markdown prose only. That works for human reading but offers no mechanical conformance check, no machine-readable layer definitions, and no portable artifact that downstream tools can consume.

OrdSA's stated posture is **vendor-neutral**: complementary to TOGAF, UAF, ArchiMate, and NIST AI RMF rather than bound to any of them. Authoring the canonical form in any single tool's native notation would silently violate that posture.

## Decision

**The canonical OrdSA source is a versioned, tool-neutral structured schema.** All other representations — ArchiMate templates, SysML v2 source, UAF viewpoint mappings, ASCII layer diagrams, narrative prose — are **renderings** derived from or consistent with the canonical schema, never the source.

The schema is the artifact adopters cite, validate against, and pin to a release version. Renderings may diverge from the canonical without compromising it; the canonical is what conformance is measured against.

Specific schema format and shape are decided in [ADR-ORDSA-0002](ADR-ORDSA-0002-schema-language-yaml-json-schema.md) and [ADR-ORDSA-0003](ADR-ORDSA-0003-construct-vs-deployment-schemas.md).

## Consequences

- **Schema expressiveness becomes load-bearing.** The schema must encode all OrdSA semantics: the seven layers, authority direction, evidence direction, the five execution rights, the conformance assertion structure, allowed cross-layer relationships. A semantic that cannot be expressed in the schema cannot be enforced in conformance checking.
- **Renderings are downstream artifacts**, not sources. ArchiMate templates, SysML v2 source, UAF mappings — all generated from or audited against the canonical schema.
- **URL stability matters more than it did in v0.1.** Adopters will cite specific schema versions; releases must pin canonical URLs.
- **The schema becomes the surface ADRs operate on.** Future construct ADRs change schema fields, allowed values, or relationship rules — not prose paragraphs.
- **Prose docs (`docs/concept.md`, `docs/layers/O*.md`) become explanatory companion artifacts**, not the source of truth. When prose and schema disagree, schema wins; prose is updated to match.
- **Validation tooling becomes a v0.2 deliverable**, since conformance against the schema requires it. See [ADR-ORDSA-0004](ADR-ORDSA-0004-reference-tooling-python-pydantic.md).

## Alternatives considered

1. **ArchiMate model as canonical.** Tool-bound; locks adopters into the Open Group / Archi ecosystem. ArchiMate has no MOF representation, so converting to UAF/SysML v2 is hand-built per case. Rejected — violates vendor-neutrality.

2. **SysML v2 textual as canonical.** OMG-bound; locks adopters into MBSE tooling. Strong typing and good ecosystem fit for engineering audiences, but excludes the EA/TOGAF audience and the policy-governance audience (NIST AI RMF). Rejected for the same vendor-neutrality reason.

3. **Multiple equivalent canonical formats with bidirectional sync.** Each adopter community gets its preferred format; tooling keeps them in sync. Rejected — drift is inevitable, and there is no source of truth when two formats disagree.

4. **No canonical artifact (prose only).** What v0.1 shipped. Doesn't scale to adopters who need machine-readable conformance checking. Rejected.

5. **JSON Schema as the canonical authoring format directly.** Bypasses the YAML+JSON-Schema split decided in ADR-ORDSA-0002. Rejected because JSON Schema is verbose for humans to author and loses comments — a worse source-of-truth UX than YAML.

## References

- [ADR-ORDSA-0002](ADR-ORDSA-0002-schema-language-yaml-json-schema.md) — concrete schema language choice
- [ADR-ORDSA-0003](ADR-ORDSA-0003-construct-vs-deployment-schemas.md) — construct vs deployment schema shapes
- [ADR-ORDSA-0004](ADR-ORDSA-0004-reference-tooling-python-pydantic.md) — reference validator/generator tooling
- [`../docs/relationship-to-frameworks.md`](../docs/relationship-to-frameworks.md) — OrdSA's positioning relative to TOGAF, UAF, ArchiMate, NIST AI RMF
- [`../docs/reference-implementations.md`](../docs/reference-implementations.md) — conformance bar that the schema mechanizes
