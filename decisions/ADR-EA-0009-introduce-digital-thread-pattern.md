# ADR-EA-0009 — Introduce digital-thread pattern at canon level with new `patterns/` tier

- **Status:** Proposed (open for OlogosAI ratification per [cross-ai #20](https://github.com/ologos-corp/cross-ai/issues/20) governance)
- **Date:** 2026-05-22
- **Author:** JD Longmire (drafted by thinx-Claude)
- **Reviewers:** @ologos001 (canon prime per cross-ai #20)
- **Related issue:** [`ologos-repos/aide-canon#7`](https://github.com/ologos-repos/aide-canon/issues/7)
- **Ratification note:** This ADR is filed in `Proposed` status pending OlogosAI's review on placement and conformance specificity (the most reasonable points of disagreement). The pattern documentation lands alongside the ADR; both are open to refinement based on canon#7 discussion before status moves to `Accepted`.

## Context

The canon today names two horizontal decompositions of the AIDE architecture:

- **AEON's six service planes** (identity, authority, evidence, integration, capability composition, orchestration runtime) — at `enterprise-platforms/aeon/`
- **OrdSA's ordinal layers** O0–O6 (enterprise intent → outcome audit) with authority-down and evidence-up flows — at `constructs/ordsa/schema/ordsa-0.2.yaml`

What the canon does not name: the **vertical** through-thread that follows a single piece of work from stated intent → orchestration → execution → evidence → durable audit. This is the digital thread in enterprise-architecture practice.

An audit of [`ologos-repos/Hermetic`](https://github.com/ologos-repos/Hermetic) ([Hermetic Discussion #38](https://github.com/ologos-repos/Hermetic/discussions/38)) surfaced that Hermetic's `Eidolon` PLM layer + its `requirements/tasks/phases/artifacts/reviews/audit-log` schema operationally implements the digital-thread pattern — without using the term anywhere. The pattern is enacted, not named. Naming it at canon level gives the AIDE corpus a vocabulary for cross-tier, cross-construct traceability that is currently implicit.

The two natural questions:

1. Where in the canon does the pattern documentation live? Four options surfaced in canon#7 (top-level `patterns/`, under AEON's evidence plane, under OrdSA's construct, or as a peer methodological construct).
2. What level of conformance does the canon specify? Behavioral (properties must hold), schema (this table shape), or interface (these endpoints)?

This ADR ratifies the placement decision (Option A — new top-level `patterns/` tier) and names the pattern; the conformance specificity question is open for tuning per canon#7.

## Decision

### 1. Introduce a new top-level tier: `patterns/`

Add a top-level `patterns/` directory to the canon root, peer to `foundation/`, `constructs/`, `enterprise-platforms/`, and `related-work/`. The `patterns/` tier holds **cross-cutting architectural patterns** — recurring shapes that traverse multiple tiers, constructs, or service planes, and that benefit from being named separately from the tiers and constructs they cut across.

The `patterns/` tier is distinct in role from the existing tiers:

| Tier | Role | Examples |
|---|---|---|
| `foundation/` | Upstream cognitive-theory + training-methodology basis | HCAE, AIDK, RLEG |
| `constructs/` | Peer methodological patterns at the spine | DEA, OrdSA, MxM, OAgents |
| `enterprise-platforms/` | Enterprise-altitude instantiations | AEON, AIDEX, OAAD |
| `related-work/` | Allied research, isolated | Theseus |
| **`patterns/`** | **Cross-cutting architectural patterns that traverse multiple tiers/constructs** | **digital-thread (this ADR), federation (future candidate), …** |

Patterns are *not* constructs (they don't define a methodological surface of their own) and *not* enterprise-platforms (they don't have a buildable software target by themselves). They are recurring shapes that emerge when constructs and platforms are deployed together.

### 2. Name the digital-thread pattern

The first pattern landed under the new tier: **digital-thread**.

**Definition.** A six-layer FK-linked traceability chain that follows a single piece of work from stated intent through orchestration, execution, evidence, gate decisions, and durable audit. The chain provides bidirectional traversal: forward (intent → audit) and backward (audit → intent).

**Six-layer chain (the pattern's normative shape):**

| Layer | What it traces |
|---|---|
| **Requirements** | Stated intent — the demand for work |
| **Tasks** | Work claims that implement requirements |
| **Phases** | Lifecycle states of work-in-progress |
| **Artifacts** | Schema-validated deliverables with integrity proofs |
| **Reviews** | Gate decisions on artifacts |
| **Audit log** | Durable record of all state changes |

**Canon-vocabulary mapping (how the pattern connects to existing canon concepts):**

| Layer | Canon mapping |
|---|---|
| Requirements | Tier 0 *Vision-Strategy* concrete down-flow (intent at the operational altitude) |
| Tasks | MxM *MISSION* surface enactment (scoped task definitions) |
| Phases | OrdSA O0–O6 authority-layer progression |
| Artifacts | OAgents evidence-emission (audited, schema-validated deliverables) |
| Reviews | MxM *MORALS* surface enforcement (authority gates) |
| Audit log | OAgents evidence-trail + OrdSA O6 outcome-audit |

**Conformance criteria (Behavioral level — required; Schema level — recommended):**

*Behavioral (required for an implementation to be digital-thread-conforming):*
- The chain is FK-linked end-to-end. Every audit-log entry traces uniquely to its review (if applicable), phase, task, and requirement of origin.
- Artifacts carry integrity proofs (cryptographic hashes; SHA-256 is the recommended default).
- The audit log is append-only and tamper-evident at the entity-action level.
- Reviews record decisions explicitly (approve/reject/defer or equivalent), with attribution to a reviewer (operator or designated agent).
- Phase progression is monotonic with respect to its defined state machine; rejections route back to a prior phase, they do not erase phase history.

*Schema level (recommended; conformant impls SHOULD match this shape):*
- Table names: `requirements`, `tasks`, `phases`, `artifacts`, `reviews`, `audit_log` (or equivalent in non-relational stores)
- FK pattern: `tasks.project_id → requirements.id` (or equivalent), `phases.task_id → tasks.id`, `artifacts.phase_id → phases.id`, `reviews.phase_id → phases.id`, `audit_log.{entity_type, entity_id}`
- Artifact integrity field: `checksum` (string, SHA-256 hex recommended)
- Audit-log shape: `(entity_type, entity_id, action, actor, details JSON, created_at)` at minimum

The schema-level recommendation is provided to ease interop between conformant implementations; behavioral conformance is what determines correctness.

### 3. Cite Hermetic as the reference implementation

[`ologos-repos/Hermetic`](https://github.com/ologos-repos/Hermetic) implements the digital-thread pattern operationally. Specifically:

- Schema: `internal/store/store.go` defines all six tables with the FK chain documented above
- API: Eidolon Runtime (`internal/eidolon/`) — `OpenPhase`, `ClosePhase`, `SubmitArtifact`, `RecordReview` transact through the audit log automatically
- Tooling: `requirement_coverage_report` MCP tool, `GET /api/projects/{id}/requirements/matrix` HTTP endpoint, Eidolon TUI traceability mode (press `t`)
- Integrity: SHA-256 checksum on every artifact, recorded in the `artifacts` table

The canon cites Hermetic as the reference; Hermetic-side companion documentation declaring the canon-mapping is tracked at [`ologos-repos/Hermetic#37`](https://github.com/ologos-repos/Hermetic/issues/37).

### 4. Repository surface

```
aide-canon/
├── patterns/                       # NEW — cross-cutting architectural patterns tier
│   ├── README.md                   # tier overview + index + convention for adding patterns
│   └── digital-thread.md           # the pattern doc (this ADR's normative content lives here)
├── vision-strategy/                # unchanged
├── mode-alpha/                     # unchanged
├── foundation/                     # unchanged
├── constructs/                     # unchanged
├── enterprise-platforms/           # unchanged (AEON README updated to cross-reference patterns/digital-thread)
├── related-work/                   # unchanged
├── infographics/                   # unchanged
└── decisions/                      # this ADR + (existing 0001..0008)
```

### 5. Cross-tier updates landed alongside this ADR

- `README.md` (canon root) — surfaces the new `patterns/` tier in the structure table
- `enterprise-platforms/aeon/README.md` — cross-references the digital-thread pattern as the operational shape produced by AEON's evidence service plane

## Consequences

**Positive:**
- Names a pattern that the corpus's reference impl (Hermetic) already enacts but that the canon previously had no vocabulary for. Vocabulary closes the gap between *what we have* and *what we say we have*.
- Provides a build-pointability anchor: a Claude Code or Codex prompted with *"build a system that produces auditable AI work"* now has a documented pattern + a working reference impl to clone. Closes one specific concrete instance of the tactical-surface gap surfaced in earlier audits.
- Creates a place for future cross-cutting patterns. Federation (per [Hermetic Discussion #39](https://github.com/ologos-repos/Hermetic/discussions/39)) is a natural next candidate.
- Makes AEON's evidence service plane operationally legible — *what does the evidence plane produce?* now has a concrete answer.

**Negative:**
- Adds a new top-level tier (sixth tier; tiers 0–4 plus `related-work/` previously, now patterns/ too). Canon's tier surface grows; readers have one more category to internalize.
- Conformance level is split (behavioral required, schema recommended) — implementers must read the pattern doc carefully to know which fields they can rename without breaking conformance. Mitigated by the explicit conformance section in the pattern doc.
- Couples canon-level pattern documentation to Hermetic as the cited reference impl. If Hermetic's schema evolves, the pattern doc's schema-level recommendations may drift. Mitigated because conformance is behavioral; schema is recommendation, not requirement.

**Neutral:**
- ADR-EA-NNNN prefix continuity holds. This is ADR-EA-0009 following ADR-EA-0008 (corpus authorship reframe).
- No existing tier is renamed or restructured. Additive only.
- Hermetic's identity, governance, and license remain independent — citation pattern (Option B from canon#5, the OAgents `oagent-core` precedent) carries forward.

## Alternatives considered

1. **Option B — Place the pattern under AEON's evidence service plane** (`enterprise-platforms/aeon/evidence/digital-thread.md`). Rejected. Treats the pattern as evidence-plane sub-specification. The pattern cuts across multiple service planes (touches identity, authority, evidence, and orchestration runtime simultaneously), so subordinating it to one plane undersells it. Risks signaling that digital-thread work only matters at the evidence plane.

2. **Option C — Place the pattern under OrdSA construct** (`constructs/ordsa/patterns/digital-thread.md`). Rejected for the same cross-cutting reason as Option B. OrdSA is the closest single-construct fit (authority/evidence layering is OrdSA-native), but the pattern also touches OAgents (evidence emission), MxM (MORALS gates, MISSION enactment), and AEON (evidence plane). Burying it under one construct obscures the cross-construct nature.

3. **Option D — Promote digital-thread to a standalone construct at Tier 3** (peer to DEA, OrdSA, MxM, OAgents). Rejected. Constructs are *methodological patterns* — they define how the corpus approaches a problem space. Digital-thread is a *cross-cutting pattern* — a recurring shape that emerges when constructs are deployed together. Promoting it to peer construct would be a category error and would invite future cross-cutting patterns (federation, etc.) to seek the same elevation. The new `patterns/` tier is the right category.

4. **Defer naming until OAgents v2 absorbs the pattern.** Rejected. The pattern is operational today in Hermetic; naming it lets the canon catch up to its own reference impl. Waiting for OAgents v2 to absorb it couples a one-line pattern definition to a longer standards-revision cycle, and the canon-side benefit (build-pointability, evidence-plane operational shape) is available sooner.

5. **Conformance at schema level (required, not recommended).** Rejected. Schema-level requirements would force every implementation to use the exact table names and FK shapes Hermetic uses. That's brittle — implementations in other languages, with NoSQL stores, or with different orchestration models (e.g., event-sourced vs. table-based) would fail conformance for cosmetic reasons. Behavioral conformance + schema recommendation lets the pattern outlive Hermetic's specific shape while still giving conformant impls a near-zero-friction starting point.

## Open for tuning (per canon#7 discussion)

The following are explicitly held open for refinement based on OlogosAI/Micah/JD input on issue #7:

1. **Placement.** This ADR ratifies Option A. If discussion surfaces a strong case for B/C/D, the ADR moves to `Superseded by ADR-EA-NNNN` and a follow-up ADR captures the alternative.
2. **OAgents implications.** Whether OAgents v2 should absorb the pattern internally, or whether OAgents references the pattern externally. Either outcome is compatible with this ADR; the relationship will be documented in the OAgents construct README and the pattern doc.
3. **Federation extension.** Hermetic's intra-Prime thread is complete; cross-Prime federation traces aren't unified with the local traceability matrix. The pattern doc currently includes federation as a *variations* section but does not specify the cross-Prime case as conformant-required. Tuning input welcome.
4. **Conformance specificity.** The current behavioral/schema split is the proposed default. If discussion lands on a different conformance shape (e.g., behavioral-only, or three-tier with interface-level requirements), the pattern doc updates and this ADR is amended in-session (same-day refinement note, per ADR-EA-0007 precedent).

## Related

- [`ologos-repos/aide-canon#7`](https://github.com/ologos-repos/aide-canon/issues/7) — the open-discussion surface for tuning this pattern
- [Hermetic Discussion #38](https://github.com/ologos-repos/Hermetic/discussions/38) — canon-mapping audit (surfaced the AEON six-plane mapping)
- [Hermetic Discussion #39](https://github.com/ologos-repos/Hermetic/discussions/39) — means inventory + canon opportunities
- [aide-canon#5](https://github.com/ologos-repos/aide-canon/issues/5) — Adopt Hermetic as the canonical AEON reference implementation
- [Hermetic#37](https://github.com/ologos-repos/Hermetic/issues/37) — Hermetic-side canon-mapping doc (companion)
- [ADR-EA-0006](ADR-EA-0006-migrate-corpus-to-aide-canon.md) — migration umbrella
- [ADR-EA-0007](ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) — Tier 0 + Mode Alpha (canonical tier-shape ADR; this ADR adds `patterns/` as a sixth tier alongside it)
- AEON white paper: `enterprise-platforms/aeon/docs/AEON-White-Paper.pdf` (evidence service plane named here)
- OrdSA schema: `constructs/ordsa/schema/ordsa-0.2.yaml` (O0–O6 ordinal layers)
- OAgents NIST standard: `constructs/oagents/spec/oagents-nist-standard-v16.0.md`
