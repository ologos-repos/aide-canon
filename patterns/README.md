# patterns/ — Cross-cutting architectural patterns

This tier holds **cross-cutting architectural patterns** — recurring shapes that traverse multiple tiers, constructs, or service planes in the AIDE corpus, and that benefit from being named separately from the tiers and constructs they cut across.

## What lives here vs. elsewhere

| Tier | Holds |
|---|---|
| [`foundation/`](../foundation/) | Upstream cognitive-theory + training-methodology basis (HCAE, AIDK, RLEG) |
| [`constructs/`](../constructs/) | Peer methodological patterns at the spine (DEA, OrdSA, MxM, OAgents) |
| [`enterprise-platforms/`](../enterprise-platforms/) | Enterprise-altitude instantiations (AEON, AIDEX, OAAD) |
| [`related-work/`](../related-work/) | Allied research, isolated (Theseus) |
| **`patterns/` (this tier)** | **Cross-cutting patterns that traverse the above tiers — recurring shapes that emerge when constructs and platforms are deployed together** |

A pattern in this directory is **not** a construct (it does not define a methodological surface of its own) and **not** an enterprise-platform (it has no buildable software target by itself). It is a recurring shape that emerges when the canon's constructs and platforms are deployed together, that benefits from being documented once and cited across.

## Index

| Pattern | Status | What it names |
|---|---|---|
| [digital-thread.md](digital-thread.md) | Proposed (see [ADR-EA-0009](../decisions/ADR-EA-0009-introduce-digital-thread-pattern.md)) | Six-layer FK-linked traceability chain (requirements → tasks → phases → artifacts → reviews → audit-log) for end-to-end AI task work |
| [prep-pursue-pivot.md](prep-pursue-pivot.md) | Proposed (see [ADR-EA-0012](../decisions/ADR-EA-0012-introduce-prep-pursue-pivot-pattern.md)) | Three-faculty governed agent-cognition loop (prep / pursue / pivot = before / during / after) with a governance gradient (approve / bounded-autonomy / governed-decision) and a milestone→inchstone work hierarchy |

## Adding a new pattern

A new pattern enters this directory when:

1. **It cuts across multiple tiers, constructs, or service planes** — not contained within one. If a candidate pattern fits entirely inside a single construct (e.g., OrdSA), document it inside that construct's directory instead.
2. **It has at least one reference implementation** in the broader Ologos/Hermit ecosystem or in an open-source impl that can be cited. Patterns documented in the abstract without a working impl belong in `docs/`, not here.
3. **It has been ratified via an ADR** in the canon's [`decisions/`](../decisions/) directory. The ADR records placement reasoning + conformance criteria.

The pattern document itself follows a recommended shape — see `digital-thread.md` as the in-tree exemplar — but variation is permitted when the pattern's structure warrants it.

## Conformance levels

Each pattern document specifies one or more conformance levels:

- **Behavioral** (typically required) — properties an implementation must satisfy to be pattern-conformant. Behavioral conformance is what determines correctness.
- **Schema** (typically recommended) — specific shapes (table names, field types, FK chains) that ease interop between conformant impls without being correctness-determining.
- **Interface** (occasionally required) — endpoint shapes, API contracts, message formats. Used when interop between conformant impls is part of the pattern's value.

A pattern that specifies only behavioral conformance allows wide latitude in implementation. A pattern that specifies behavioral + schema + interface conformance produces tighter interop but constrains implementation choices.

## Relationship to other tiers

Patterns reference but do not replace:

- **Constructs** declare *how the corpus approaches a problem space*. A pattern declares *a recurring shape that emerges when those approaches are deployed together.*
- **Enterprise-platforms** declare *enterprise-altitude instantiations of constructs*. A pattern declares *operational shapes that platforms must produce or consume.*
- **Foundation** declares *upstream cognitive-theory and training-methodology grounding*. A pattern is downstream of foundation and orthogonal to it.

A pattern's `Related` section in its document explicitly names which tiers, constructs, and platforms the pattern touches, with reciprocal cross-references in those tiers' READMEs.
