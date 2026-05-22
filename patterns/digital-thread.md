# Digital-thread pattern

> **Status:** Proposed (ratified by [ADR-EA-0009](../decisions/ADR-EA-0009-introduce-digital-thread-pattern.md), open for tuning per [`aide-canon#7`](https://github.com/ologos-repos/aide-canon/issues/7))

## Summary

A six-layer FK-linked traceability chain that follows a single piece of AI work from stated intent through orchestration, execution, evidence, gate decisions, and durable audit. The chain supports bidirectional traversal: forward (intent → audit) for impact tracing, backward (audit → intent) for provenance lookup.

The pattern names what AEON's evidence service plane operationally produces, what OrdSA's authority-down/evidence-up flows carry, what OAgents' behavioral envelope emits, and what MxM's MORALS surface gates — unified as a single threaded record for any one piece of work.

## Why this pattern exists

The AIDE corpus has horizontal decompositions for the AI control plane: AEON's six service planes, OrdSA's seven ordinal layers, OAgents' behavioral envelope categories, MxM's five governing surfaces. Each decomposition describes a useful axis. None of them, by itself, describes the **trajectory** of a single piece of work *through* these axes.

The digital-thread pattern names that trajectory. For a given requirement (or task initiated without an explicit requirement), the thread is the durable, FK-linked record of:

- **what was asked for** (intent)
- **what work was attempted** (tasks)
- **how it progressed** (phases)
- **what was produced** (artifacts)
- **what was approved or rejected** (reviews)
- **what happened, step by step, attributably** (audit log)

The pattern is useful in any setting where AI work product must be auditable, traceable, or governable — which is most production settings.

## The six-layer chain (normative)

| Layer | Role | Cardinality |
|---|---|---|
| **Requirements** | Stated intent — formal demand for work. Optional; tasks may originate without an explicit requirement. | 0..N requirements per project |
| **Tasks** | Work claims that implement requirements. Each task may implement zero or more requirements; each requirement may be implemented by one or more tasks. | 1..N tasks per requirement (when linked) |
| **Phases** | Lifecycle states of work-in-progress (`draft → review → approved/rejected` is the canonical state machine; impl may extend). | 1..N phases per task |
| **Artifacts** | Schema-validated deliverables produced within a phase. Each artifact carries an integrity proof (cryptographic hash). | 0..N artifacts per phase |
| **Reviews** | Gate decisions on phase progression (approve/reject/defer). Each phase that progresses past `draft` must have at least one review. | 0..N reviews per phase |
| **Audit log** | Append-only durable record of every state change across the chain, with actor attribution and JSON-encoded context. | 1..N entries per state-changing operation |

**FK chain (each layer carries an explicit reference to the layer above):**

```
requirements
    │
    ├── tasks  (tasks.project_id → requirements.project_id; tasks may link many-to-many via a join table)
    │       │
    │       └── phases  (phases.task_id → tasks.id)
    │               │
    │               ├── artifacts  (artifacts.phase_id → phases.id; artifacts.task_id → tasks.id)
    │               │       │
    │               │       └── (checksum field; SHA-256 hex recommended)
    │               │
    │               └── reviews  (reviews.phase_id → phases.id)
    │
    └── audit_log  (audit_log.entity_type ∈ {'requirement','task','phase','artifact','review'},
                    audit_log.entity_id → the corresponding row's id)
```

**Bidirectional traversal:**

- *Forward (intent → audit):* given a requirement, list all tasks → their phases → their artifacts and reviews → the audit-log entries for any of the above.
- *Backward (audit → intent):* given any audit-log entry, walk the FK back through review/artifact → phase → task → requirement.

The traversal is closed — every audit-log entry traces uniquely (or to a small bounded set) of originating requirements; every requirement reaches its complete operational trace.

## Canon-vocabulary mapping

How the six-layer chain connects to existing canon concepts:

| Layer | Canon mapping |
|---|---|
| **Requirements** | Tier 0 *[Vision-Strategy](../vision-strategy/)* concrete down-flow — intent expressed at the operational altitude |
| **Tasks** | [MxM](../constructs/mxm/) *MISSION* surface enactment — scoped task definitions are what MxM-oriented agents act on |
| **Phases** | [OrdSA](../constructs/ordsa/) O0–O6 authority-layer progression — phase transitions move work between ordinal authority altitudes |
| **Artifacts** | [OAgents](../constructs/oagents/) evidence-emission — schema-validated, integrity-proofed deliverables OAgents-conformant agents produce |
| **Reviews** | [MxM](../constructs/mxm/) *MORALS* surface enforcement — gate decisions enact the constraint layer that orients agent action |
| **Audit log** | [OAgents](../constructs/oagents/) evidence-trail standard + [OrdSA](../constructs/ordsa/) O6 outcome-audit layer |

The pattern is the *vertical slice* that connects these horizontal decompositions for a single piece of work.

## Conformance criteria

### Behavioral conformance (required)

An implementation is **digital-thread-conformant** if and only if all of the following hold:

1. **FK-linked end-to-end.** Every audit-log entry traces uniquely (or to a bounded, declared set) to its review (if applicable), phase, task, and requirement of origin. The chain has no orphan layers — an artifact belongs to a phase, a phase belongs to a task, a task belongs to a requirement (or is explicitly marked as ad-hoc).
2. **Integrity proofs on artifacts.** Every artifact carries a cryptographic hash of its content (SHA-256 hex is the recommended default; stronger hashes are conformant; weaker — MD5, CRC32 — are not).
3. **Append-only, tamper-evident audit log.** The audit log accepts new entries but does not allow modification or deletion of existing entries. Implementations SHOULD use database constraints or content-addressed storage to enforce this; at minimum the impl MUST document the tamper-evidence mechanism it relies on.
4. **Explicit review decisions with attribution.** Every review records: a decision (approve/reject/defer or equivalent in the impl's state machine), the reviewer's identity (operator or designated agent), a timestamp, and optionally a comment. Reviews without explicit decisions or attribution are not conformant.
5. **Monotonic phase progression.** Phase state machines progress monotonically with respect to their defined state graph. Rejections route work back to a prior phase by creating a *new* phase entry, not by erasing or rewriting the rejected phase's record.

### Schema-level recommendations (interop)

An implementation that follows these recommendations interoperates with other recommendation-following implementations at the data-model level. Implementations that diverge from these recommendations are still conformant if they satisfy the behavioral criteria above.

**Recommended table/collection names:** `requirements`, `tasks`, `phases`, `artifacts`, `reviews`, `audit_log`. (Or equivalent named entities in non-relational stores.)

**Recommended FK pattern:**

- `tasks.project_id` references `requirements.project_id` (many-to-many via join table is conformant)
- `phases.task_id` references `tasks.id`
- `artifacts.phase_id` references `phases.id`
- `artifacts.task_id` references `tasks.id` (denormalized for query efficiency; not strictly required if `phase_id` is reliable)
- `reviews.phase_id` references `phases.id`
- `audit_log.(entity_type, entity_id)` references the corresponding row's primary key

**Recommended artifact integrity field:** `checksum` (string, lowercase hex, SHA-256). Field name variation is conformant if documented.

**Recommended audit-log shape:** `(id, entity_type, entity_id, action, actor, details JSON, created_at)` at minimum. Implementations may extend with additional fields (e.g., `correlation_id` for cross-Prime federation).

### Interface conformance (optional)

Implementations that expose a programmable interface SHOULD provide:

- A **traceability matrix endpoint** that, given a project (or scope) identifier, returns each requirement with its linked tasks and a coverage percentage
- A **coverage report endpoint** that returns per-project (or per-scope) total / covered / orphan counts and coverage percentage
- A **drill-down query** by entity ID that returns the entity's full chain (forward and/or backward traversal)

These interfaces are optional but recommended; their presence makes the thread human- and agent-navigable beyond the schema itself.

## Reference implementation: Hermetic

**Repository:** [`ologos-repos/Hermetic`](https://github.com/ologos-repos/Hermetic) — MIT-licensed, Go, Ologos LLC. Per [`aide-canon#5`](https://github.com/ologos-repos/aide-canon/issues/5), Hermetic is cited as the canonical AEON reference implementation; it is also (and separately) the canonical digital-thread reference implementation per this pattern doc.

**Implementation details:**

| Pattern element | Hermetic location |
|---|---|
| Schema | `internal/store/store.go` — defines `requirements`, `tasks`, `phases`, `artifacts`, `reviews`, `audit_log` tables with the FK chain documented above |
| Runtime API | `internal/eidolon/` — `OpenPhase`, `ClosePhase`, `SubmitArtifact`, `RecordReview`; all transact through `audit_log` automatically |
| Integrity | SHA-256 checksums on every `artifacts` row, recorded in the `checksum` column |
| Traceability matrix endpoint | `GET /api/projects/{id}/requirements/matrix` (defined in `internal/prime/dashboard_requirements.go`) |
| Coverage report tool | `requirement_coverage_report` MCP tool (`internal/eidolon/tools.go`) |
| TUI drill-down | Eidolon TUI traceability mode — press `t` at the requirements level (`internal/tui/eidolon.go`; spec in `docs/specs/ms5-tui-parity.md` §"Goal 5") |
| Audit log model | Append-only via insert-only DB convention; tamper-evidence documented in `docs/architecture/state.md` |

**Hermetic-side companion document** (declaring the canon-mapping from the impl side): tracked at [`ologos-repos/Hermetic#37`](https://github.com/ologos-repos/Hermetic/issues/37).

**Alternative implementations are explicitly welcome.** This pattern doc does not constrain implementations to Go, to SQLite, or to Hermetic's specific schema. Behavioral conformance is the bar; the schema and interface recommendations are starting points, not requirements.

## Operational mechanics

### Forward traversal (intent → audit)

Given a `requirement_id`, the forward walk is:

1. Query `tasks` where the project/requirement linkage matches.
2. For each task, query `phases` where `task_id` matches.
3. For each phase, query `artifacts` and `reviews` where `phase_id` matches.
4. For each entity along the way (requirement, task, phase, artifact, review), query `audit_log` where `entity_type` and `entity_id` match.

The result is a hierarchical record of every action taken in pursuit of the requirement, with timestamps and actor attribution at every step.

### Backward traversal (audit → intent)

Given an `audit_log` entry, the backward walk is:

1. Read `entity_type` and `entity_id`. If `entity_type = 'review'`, fetch the review's `phase_id`.
2. From the phase (or directly, if starting at phase-level), fetch the task by `task_id`.
3. From the task, fetch the requirement linkage (via `project_id` or join table).
4. The requirement is the originating intent.

Backward traversal is what makes the pattern useful for compliance, incident analysis, and operator-facing *why-did-this-happen?* queries.

### Federation (variation)

When work is delegated across multiple AEON deployments (or multiple Hermetic Primes in a federation topology — see [Hermetic's federation pattern](https://github.com/ologos-repos/Hermetic/blob/main/docs/design/topology.md)), the digital thread crosses the federation boundary. The pattern admits two extension shapes:

- **Local-only threads** (current Hermetic implementation): each Prime maintains its own complete thread; federation delegation records a parent reference but does not unify the threads at query time.
- **Unified threads via correlation IDs** (proposed future): a `correlation_id` field on the audit log allows downstream Primes' threads to be joined to the originating Prime's thread for cross-Prime traversal.

The unified-thread case is **out of scope** for this v0.1 pattern doc; documented here for v0.2 evolution. See [Hermetic Discussion #39](https://github.com/ologos-repos/Hermetic/discussions/39) for the federation pattern at large.

## When NOT to use this pattern

The digital-thread pattern is appropriate when AI work product must be auditable, traceable, or governable. It is **not** appropriate when:

- **Throughput trumps traceability** — high-volume, low-stakes work (e.g., bulk inference) where per-task audit overhead is prohibitive. Use a sampled-audit approach instead, or selectively apply the thread to high-stakes work only.
- **Work is genuinely ephemeral** — chat interactions or one-shot tool calls where there is no downstream consumer of the audit trail. Use lighter logging.
- **The implementer cannot guarantee append-only audit log integrity** — without that guarantee, behavioral conformance fails. Implementations that cannot enforce append-only should either implement the guarantee first or document the deviation explicitly (and accept that they are non-conformant).

## Variations and extensions

| Variation | Status |
|---|---|
| Local-only thread | Current Hermetic impl; behavioral-conformant |
| Federated thread with correlation IDs | Out of scope for v0.1; v0.2 candidate |
| Multi-tenant thread isolation | Not specified; tenancy is an orthogonal concern. Implementations are free to add tenant FK to each layer. |
| Cryptographic chain (each audit entry includes hash of previous entry) | Not required by behavioral conformance; conformant if added |
| Distributed audit log (append to durable storage outside the implementing DB) | Conformant if integrity properties hold; storage choice is an impl detail |

## Related patterns

| Pattern | Relationship |
|---|---|
| Federation (future, candidate `patterns/federation.md`) | The federation pattern handles cross-Prime delegation. The digital thread is the per-Prime work record; federation extends the thread across Prime boundaries. |
| Schema-versioning (future, candidate) | Threads evolve as schemas evolve. A canonical schema-versioning pattern would address how migrations affect thread integrity. |

## Related (constructs, platforms, tiers)

This pattern touches:

- **Tier 0 — [Vision-Strategy](../vision-strategy/)** — requirements originate in the strategic frame
- **Tier 3 — Constructs:** [OrdSA](../constructs/ordsa/) (authority-layer progression), [OAgents](../constructs/oagents/) (evidence emission + audit), [MxM](../constructs/mxm/) (MISSION + MORALS surfaces)
- **Tier 4 — [AEON](../enterprise-platforms/aeon/)** — the evidence service plane's operational shape

Cross-references in those tiers' READMEs declare the relationship from the other side.

## Document version

- **v0.1** — 2026-05-22 — Initial proposal alongside [ADR-EA-0009](../decisions/ADR-EA-0009-introduce-digital-thread-pattern.md). Open for tuning per [`aide-canon#7`](https://github.com/ologos-repos/aide-canon/issues/7).
