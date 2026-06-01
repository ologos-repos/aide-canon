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
| [epistemic-integrity-floor.md](epistemic-integrity-floor.md) | Proposed (see [ADR-EA-0014](../decisions/ADR-EA-0014-introduce-epistemic-integrity-floor-pattern.md)) | Eight-section agent-side behavioral floor — calibrated confidence labels, three-tier defeater rules, introspection-as-hypothesis, cross-turn drift handling, bounded operator-declared exit clauses — imported by reference into MxM Mind/Morals/Memory + realized at HCAE/AIDEX |
| [governed-context-management.md](governed-context-management.md) | Proposed (see [ADR-EA-0019](../decisions/ADR-EA-0019-introduce-governed-context-management-pattern.md); §8 added per [ADR-EA-0023](../decisions/ADR-EA-0023-thinx-discipline-refinements.md)) | Eight-section context-management discipline — §1-§7 specify harness-owned mechanisms (governance pin, per-model budgeting, deterministic compaction, audited events, re-hydration, inchstone decomposition, integrity-degraded autonomy); §8 names the behavioral-discipline complement for deployments where compaction is *not* harness-owned — distributed across MxM Morals/Memory + Inference/Runtime/Evidence planes |
| [founder-override.md](founder-override.md) | Proposed (see [ADR-EA-0023](../decisions/ADR-EA-0023-thinx-discipline-refinements.md)) | Structural escape valve at the harness floor — `# FOUNDER-OVERRIDE: <reason>` per-command marker authorizes a single hard-stop-blocked command, emits the original safety warning to a visible surface, audit-logs the use. Operator-altitude principal authority gets a structural surface; default-deny posture preserved. Composes with EIF §7 as independent operator-declared deontic axis. |
| [workflow-orchestration.md](workflow-orchestration.md) | Proposed (see [ADR-EA-0027](../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)) | Deterministic control program composing multiple agent invocations into one governed unit — a deterministic, replayable orchestration substrate wrapping probabilistic agent execution. Two contributions: (1) a workflow is an OAgents `Agent` that orchestrates `Agent`s under **envelope refinement** `envelope(child) ⊑ envelope(parent)` (closes the OAgents §10 trust-boundary gap); (2) the **determinism boundary is the gate-attachment surface** — gates live in the deterministic control layer, judgment in the gated steps. Reference impl: Claude Code Workflow. |

## Adding a new pattern

A new pattern enters this directory when:

1. **It cuts across multiple tiers, constructs, or service planes** — not contained within one. If a candidate pattern fits entirely inside a single construct (e.g., OrdSA), document it inside that construct's directory instead.
2. **It has at least one reference implementation** in the broader Ologos/Hermetic ecosystem or in an open-source impl that can be cited. Patterns documented in the abstract without a working impl belong in `docs/`, not here.
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
