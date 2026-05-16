# ADR-OSA-0004 — Reference tooling: Python + pydantic for v0.2

- **Status:** Accepted
- **Date:** 2026-05-16
- **Author:** JD Longmire
- **Bundle:** Founding ADR (0004 of 0005)

## Context

[ADR-OSA-0001](ADR-OSA-0001-schema-first-canonical-form.md) through [ADR-OSA-0003](ADR-OSA-0003-construct-vs-deployment-schemas.md) define **what** the canonical OSA artifact is (schema-first, YAML source + JSON Schema, construct schema vs deployment schema). This ADR picks the language and library stack for the **reference tooling** that operates on those artifacts.

The reference tooling has four responsibilities:

1. **Validate** a deployment YAML against a construct YAML — schema validation plus the construct-defined conformance rules.
2. **Emit** JSON Schema from the YAML construct source (per ADR-OSA-0002).
3. **Generate** renderings from the canonical schema — first target is ArchiMate (the specific rendering mechanism is [ADR-OSA-0005](ADR-OSA-0005-archi-as-canonical-modeling-tool.md)'s concern), with SysML v2 and other renderings as v0.3+ work.
4. **Provide a CLI** adopters can run locally or in CI to check conformance and produce renderings.

Language candidates evaluated: **Python**, **Go**, **Rust** (with bindings), **TypeScript**.

## Decision

**Python + pydantic for v0.2 reference tooling.**

- **pydantic** models define the schema in typed Python; emit JSON Schema via `Model.model_json_schema()`; validate YAML/JSON against the models.
- **pyyaml** (or `ruamel.yaml` if round-trip preservation matters) for YAML loading.
- **lxml** for any XML manipulation (ArchiMate Open Exchange XML emission/parsing).
- **click** or **typer** for the CLI surface.
- Code lives under `tools/osa-validator/` (path subject to refinement). Licensed **Apache-2.0** when the first code lands; the repository's `LICENSE` will be updated at that point to call out the dual-license posture (CC-BY-4.0 for docs + Apache-2.0 for code).

The reference tooling is **a reference**, not a monopoly. Other-language implementations (Go, Rust, TypeScript) are welcome and explicitly anticipated — the canonical artifact is the schema, not the validator.

## Consequences

- **Adopter accessibility.** Python is widely read by EA and research audiences; many adopters will modify the tooling rather than treat it as a black box.
- **Ecosystem fit for downstream targets.** SysML v2 Pilot Implementation has Python bindings/Jupyter examples; ArchiMate XML manipulation has `lxml` and `pyArchimate`; UAF tooling reachable via Cameo's Python API. Python sits at the intersection of the three downstream worlds.
- **Distribution via pip.** Not as clean as a single static binary, but standard for the audience. CI integration via `pipx install osa-validator` is straightforward.
- **The schema is language-neutral; this ADR is replaceable.** A future ADR may add Go or Rust implementations alongside Python without invalidating the schema. The CLI contract becomes the cross-implementation specification.
- **License split is documented at first-code time.** The README and LICENSE updates ship with the first reference-tooling PR, not now.
- **Type-safety via pydantic.** pydantic v2's strict mode plus mypy gives strong correctness guarantees. The schema models become the executable specification of the construct.
- **JSON Schema emission is "free" via pydantic.** `Model.model_json_schema()` produces a draft-2020-12 JSON Schema; no separate transformation tooling needed.
- **Rendering integrations are subprocess-only.** External rendering libraries with restrictive licenses (notably pyArchimate, GPL-3.0, per [ADR-OSA-0005](ADR-OSA-0005-archi-as-canonical-modeling-tool.md)) are invoked as build-time CLI subprocesses, never imported. This preserves the Apache-2.0 license boundary for distributed code. Reviewers and contributors must enforce this boundary.

## Alternatives considered

1. **Go.** Single static binary is genuinely attractive for CI/admission-controller use cases. Rejected for v0.2 because (a) ArchiMate XML manipulation is more verbose than `lxml`; (b) SysML v2 Python tooling has no Go equivalent; (c) audience reads less Go than Python. A future ADR could add a Go binary as a *distribution mechanism* for the same schema, validated against the Python reference.

2. **Rust core + Python/Go bindings (`pyo3`, `cgo`).** Pattern proven by `ruff`, `polars`, `pydantic-core`. Premature for v0.2 — performance is not load-bearing at construct-schema scale, and the operational complexity of maintaining bindings exceeds the benefit until the validator is in production CI for large orgs.

3. **TypeScript / Node.** Reasonable cross-platform story; weaker ecosystem fit for ArchiMate/SysML v2 downstream targets. Rejected for ecosystem-fit reasons, not language-quality reasons.

4. **No reference tooling (schemas only).** Leaves adopters to write their own validators. Predictable result: per-org reinvention, inconsistent conformance interpretation, no shared CLI. Rejected.

5. **Pure JSON Schema + off-the-shelf validators (no custom code).** Works for schema-shape validation but cannot express construct-defined conformance rules (e.g., "no Assignment relationship from a higher OSA layer ID to a lower one"). Custom logic is required; might as well wrap it in a reference CLI.

## References

- [ADR-OSA-0001](ADR-OSA-0001-schema-first-canonical-form.md) — schema-first canonical form
- [ADR-OSA-0002](ADR-OSA-0002-schema-language-yaml-json-schema.md) — YAML + JSON Schema
- [ADR-OSA-0003](ADR-OSA-0003-construct-vs-deployment-schemas.md) — construct vs deployment schema shapes
- [ADR-OSA-0005](ADR-OSA-0005-archi-as-canonical-modeling-tool.md) — ArchiMate rendering pipeline (defines how this tooling generates ArchiMate)
- [pydantic v2 documentation](https://docs.pydantic.dev/latest/)
- [JSON Schema 2020-12 (the dialect pydantic emits)](https://json-schema.org/specification.html)
