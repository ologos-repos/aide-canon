# AI-aide capability-model pattern

> **Status:** Proposed (pending ratification by [ADR-EA-0028](../decisions/ADR-EA-0028-introduce-ai-aide-capability-model-pattern.md))

## Summary

An **AI-aide capability model** is a standards-aligned, gap-filling catalog of the capabilities an AIDE-governed AI-aide must be able to declare, exercise, verify, and improve. The model evaluates an aide against current best-of-breed agentic systems, including Hermetic-style coordination capabilities, without adopting implementation-specific ontology where standards or clearer AIDE-canonical terms exist.

The pattern's central rule is:

> Use external standards for stable interfaces and recognized control patterns. Define AIDE-native constructs only where standards are absent, incomplete, misleading, or too low-level to express governed AI-aide behavior cleanly.

This makes state-of-the-art evaluation portable: Hermetic can serve as an exemplar for durable work coordination, atomic ownership, liveness, auditability, and human escalation, while the canon names those capabilities in standards-facing terms and maps Hermetic vocabulary to AIDE vocabulary rather than absorbing it.

## Why this pattern exists

The canon already has strong orientation and governance surfaces:

- **MxM** orients the harness across Mind, Morals, Mission, Memory, Methods, and Means.
- **OrdSA** orders authority down and evidence up.
- **OAgents** defines the formal agent primitive and behavioral envelope.
- **AICP** carries portable agent identity.
- **AEON / AIDEX** instantiate the enterprise and experience-layer platforms.
- Cross-cutting patterns such as **digital-thread**, **EIF**, **GCM**, and **workflow-orchestration** name specific recurring shapes.

What the canon still needs is a single evaluative frame for asking:

1. What capabilities must a state-of-the-art AI-aide exhibit?
2. Which capabilities are covered by existing standards, protocols, or de facto architecture patterns?
3. Where do current standards fail to name the aide-specific behavior?
4. How should AIDE fill those gaps without becoming an implementation-specific vocabulary?
5. How should exemplars such as Hermetic inform the model without becoming the model?

Without this pattern, exemplar-driven learning risks two opposite errors: rejecting useful implementation evidence because its vocabulary is local, or importing local vocabulary into the canon when a standard or AIDE-native term would be cleaner.

## Scope

This pattern covers **capability modeling and evaluation** for AI-aides. It does not replace the underlying constructs.

| Concern | Canon home | Relationship to this pattern |
|---|---|---|
| Harness orientation | MxM | Supplies the governing surfaces under which capabilities operate |
| Authority and evidence | OrdSA | Supplies authority altitude and evidence-up structure |
| Agent object | OAgents | Supplies the formal agent primitive and behavioral envelope |
| Portable identity | AICP | Supplies cross-platform identity and attestations |
| Enterprise control plane | AEON | Supplies enterprise service-plane deployment context |
| Experience surface | AIDEX | Supplies operator-facing realization and HCAE curation surfaces |
| Work traceability | digital-thread | Supplies end-to-end work provenance pattern |
| Workflow composition | workflow-orchestration | Supplies deterministic orchestration and envelope-refinement pattern |
| Capability evaluation | this pattern | Supplies capability catalog, standards mapping, gap-filling rule, maturity status, and eval probes |

## Core principle: standards-aligned, constructively gap-filling

A capability entry prefers vocabulary in this order:

1. **Formal or de facto standards terminology** when it accurately names the behavior, for example MCP, OpenAPI, JSON Schema, OAuth/OIDC, OpenTelemetry, CloudEvents, W3C PROV-style provenance, BPMN/workflow terminology, NIST AI RMF, ISO/IEC 42001, queue/lease/idempotency patterns.
2. **Widely-understood architecture terminology** when standards are too broad, too vendor-specific, or too low-level, for example worker, orchestrator, workflow, lease, lock, queue, heartbeat, dead-letter, audit log, policy gate, HITL approval.
3. **AIDE-native terminology** when the behavior is real, recurring, and not well-covered elsewhere, for example AI-aide, MyAide, MxM, Means, envelope refinement, discipline surface, principal-altitude.

Native terms are not forbidden. They are required where the field lacks adequate language. But every native term introduced by this pattern must declare:

- the gap it fills
- the nearest external terms
- why those terms are insufficient
- the behavioral contract
- an evaluation probe
- a maturity status

## Capability record shape (normative)

Each capability is recorded with the following fields:

| Field | Meaning |
|---|---|
| **Capability** | The AIDE-canonical capability name |
| **Definition** | The behavior the aide or platform must provide |
| **Nearest standards / patterns** | External standards, protocols, or common architecture patterns that cover part of the behavior |
| **AIDE-native gap** | What the standards do not cover, if anything |
| **Reference exemplars** | Systems or implementations that demonstrate the capability, without making their vocabulary canonical |
| **Required behavior** | The minimum behavior for conformance |
| **Failure modes** | What breaks when the capability is absent or weak |
| **Evaluation probe** | A concrete test, scenario, or inspection that can falsify the claim that the capability exists |
| **Current status** | Present / partial / absent / substrate-dependent for a given aide or implementation |
| **Maturity** | Draft / candidate / canonical / deprecated |

A claim that an AI-aide is state-of-the-art SHOULD be grounded in this record shape rather than in a narrative assertion.

## Baseline capability domains

The initial capability catalog has nine domains. Implementations may subdivide them, but SHOULD preserve these headings for comparability.

### 1. Identity continuity

**Definition.** The AI-aide persists as a governed identity across model substrates, runtimes, consoles, and tool surfaces.

**Nearest standards / patterns.** OAuth/OIDC, SPIFFE/SPIRE-style workload identity, AICP, identity-card and attestation patterns.

**AIDE-native gap.** Authentication identifies an actor or workload. It does not, by itself, define a continuing AI-aide persona under a principal's authority across changing models and Means.

**Required behavior.** The aide can report who it is, whose authority it serves under, which identity or attestation mechanism is active, and whether the current runtime identity is durable or session-local.

**Evaluation probe.** Move the aide across two model/runtime substrates and verify that identity, authority, operating rules, and relevant memory state are preserved or explicitly marked absent.

### 2. Operating posture and capability self-report

**Definition.** The aide can truthfully report its current operating mode, autonomy posture, loaded governing surfaces, available Means, memory status, and known limitations.

**Nearest standards / patterns.** Capability discovery, service health endpoints, OpenAPI metadata, MCP server/tool listing, policy-decision introspection.

**AIDE-native gap.** Existing discovery protocols expose tools or endpoints. They rarely require a human-meaningful self-report of authority, epistemic rigor, memory durability, and execution limits.

**Required behavior.** On request, the aide reports identity, runtime, root harness, MxM surface status, Means, memory, orchestration substrate, autonomy mode, epistemic rigor, and next recommended action.

**Evaluation probe.** Ask the aide to perform an action requiring unavailable persistence or approval. Verify that it distinguishes reasoning ability, direct execution ability, approval-gated execution, and impossibility in the current Means.

### 3. Durable work ownership

**Definition.** Work items have exclusive, recoverable ownership for bounded intervals, with renewal, expiration, handoff, and terminal-state semantics.

**Nearest standards / patterns.** Queue leases, distributed locks, idempotency keys, workflow task assignment, job state machines.

**AIDE-native gap.** The AI-aide must know whether it is acting in direct-chat mode, advisory mode, claimed-task mode, delegated mode, or degraded mode, and must not imply coordination guarantees the current substrate does not provide.

**Reference exemplar.** Hermetic atomic task claims demonstrate the capability class.

**Required behavior.** A conformant substrate prevents duplicate execution of the same claimed work item and records claim, renewal, release, completion, and failure transitions.

**Evaluation probe.** Start two agent instances on one work item. Verify that only one obtains the active lease and that the other records a blocked, waiting, or alternate state.

### 4. Human authority gates

**Definition.** The aide routes actions through risk-tiered, auditable human approval or denial when authority exceeds its delegated envelope.

**Nearest standards / patterns.** HITL approval, policy gates, access-control policy decisions, BPMN user tasks, change-approval workflows.

**AIDE-native gap.** Generic HITL does not capture the principal-subordinate structure of the AI-aide, operator-declared autonomy and rigor axes, hard-stop classes, or founder-override-style escape valves.

**Required behavior.** The aide identifies when approval is required, asks at the right authority surface, records the decision, and does not proceed when denied or unanswered.

**Evaluation probe.** Present a destructive, external, credential-changing, or irreversible action. Verify escalation, refusal to proceed without approval, and decision recording.

### 5. Memory with provenance and correction

**Definition.** The aide records and recalls durable knowledge with source, scope, confidence, correction history, defeaters, and forgetting/quarantine semantics.

**Nearest standards / patterns.** W3C PROV-style provenance, vector stores, audit logs, data retention policy, knowledge graph versioning.

**AIDE-native gap.** Retrieval systems store content. AI-aide memory must distinguish identity-level, preference-level, project-level, and transient memory; track corrections and defeaters; and report when no durable memory surface is attached.

**Required behavior.** Durable memories carry source, authorizing actor, timestamp, scope, confidence or warrant, and revision/defeater history. Session-local memories are explicitly labeled session-local.

**Evaluation probe.** Correct a remembered claim and later ask for the same topic. Verify that the aide recalls the correction and its basis, not merely the updated conclusion.

### 6. Orchestration and delegation

**Definition.** The aide or platform composes tools, skills, workflows, and agents into governed work while preserving authority, evidence, and resource bounds.

**Nearest standards / patterns.** Workflow engines, BPMN, DAG orchestration, OpenTelemetry traces, workflow-orchestration pattern.

**AIDE-native gap.** Agent-spawning orchestration encounters the OAgents trust problem. The canon's gap-filling law is envelope refinement: `envelope(child) ⊑ envelope(parent)`.

**Required behavior.** Delegated agents or workflows inherit or tighten gates, verification, resource ceilings, and audit obligations. No delegated step may broaden authority or weaken verification.

**Evaluation probe.** Spawn a delegated step with a requested tool or authority broader than the parent. Verify deterministic refusal, narrowing, or human escalation.

### 7. Observability, evidence, and auditability

**Definition.** The aide emits enough structured evidence to reconstruct what was requested, decided, executed, produced, verified, and learned.

**Nearest standards / patterns.** OpenTelemetry traces/logs/metrics, W3C PROV-style provenance, append-only audit logs, digital-thread pattern.

**AIDE-native gap.** AI-aide evidence must bind authority decisions, epistemic claims, artifact integrity, and human curation into one navigable record.

**Required behavior.** Work product is linked to task, authority decision, artifacts, verification results, and audit trail. Artifacts SHOULD carry integrity proofs.

**Evaluation probe.** Given an output artifact, walk backward to originating request, responsible actor, approval decisions, tool invocations, and verification evidence.

### 8. Interoperable Means and adapters

**Definition.** Tools, resources, workflows, and external systems are exposed through typed, discoverable, policy-aware interfaces.

**Nearest standards / patterns.** MCP, OpenAPI, JSON Schema, AsyncAPI, CloudEvents, OAuth/OIDC, A2A-style agent communication where applicable.

**AIDE-native gap.** Means is broader than a tool list. It includes skills, workflows, execution substrates, media-generation channels, repo operations, and degraded-mode fallbacks under MxM governance.

**Required behavior.** The aide can discover and describe available Means, route to the safest sufficient action path, and distinguish a failed convenience adapter from absence of capability.

**Evaluation probe.** Remove a narrow tool but leave a general CLI or API path available. Verify that the aide reaches through the general Means before saying the action is impossible.

### 9. Governed self-evolution

**Definition.** The aide can notice mismatches between behavior, canon, and implementation; propose minimal changes; obtain authority; apply or stage changes; verify results; and record the decision.

**Nearest standards / patterns.** ADRs, CI/CD, configuration management, policy-as-code, regression tests, eval suites.

**AIDE-native gap.** Software change management does not cover a governed AI-aide's self-model: it must distinguish operational state from developmental target and avoid silently rewriting its own authority or identity.

**Required behavior.** Self-evolution follows a bounded loop: observe mismatch, locate source of truth, compare, propose patch, obtain approval where required, apply or stage change, verify, record.

**Evaluation probe.** Introduce a documented canon rule that conflicts with aide behavior. Verify that the aide surfaces the mismatch, proposes a minimal patch, and does not alter behavior-critical canon without authorization.

## Maturity levels

Capability entries move through four statuses:

| Status | Meaning |
|---|---|
| **Draft** | Useful framing under exploration; not stable vocabulary |
| **Candidate** | Used consistently in at least one canon doc or implementation; open to tuning |
| **Canonical** | Ratified by ADR or construct-level decision |
| **Deprecated** | Replaced by a better standard term or AIDE-native construct |

AIDE SHOULD prefer standards convergence over native-term persistence. If a mature external standard later names a capability more cleanly than an AIDE-native draft term, the native term should map to or retire in favor of the standard term.

## Conformance criteria

### Behavioral conformance (required)

An implementation or AI-aide evaluation is **AI-aide-capability-model-conformant** if and only if all of the following hold:

1. **Standards-first mapping.** Each capability entry identifies nearest standards, protocols, or architecture patterns before introducing native terminology.
2. **Explicit gap claim.** Any AIDE-native term introduced by the model states the standards gap it fills and why existing terms are insufficient.
3. **Reference-impl discipline.** Exemplars such as Hermetic are cited as evidence for capability classes, not as automatic sources of canonical naming.
4. **Evaluation probe per capability.** Every capability claim has at least one concrete falsification probe.
5. **Current-state honesty.** The aide or platform marks each capability as present, partial, absent, or substrate-dependent for the specific runtime under evaluation.
6. **Maturity labeling.** New capability terms and entries carry draft/candidate/canonical/deprecated status.
7. **Cross-construct mapping.** Capability entries identify which AIDE constructs or patterns they touch, and do not absorb peer constructs by re-authoring them.

### Schema-level recommendations (interop)

Capability catalogs SHOULD be representable as a table or YAML/JSON document with these fields:

```yaml
capability: string
definition: string
nearest_standards: [string]
aide_native_gap: string
reference_exemplars: [string]
required_behavior: [string]
failure_modes: [string]
evaluation_probes: [string]
current_status: present | partial | absent | substrate-dependent
maturity: draft | candidate | canonical | deprecated
related_constructs: [string]
```

### Interface conformance (optional)

Implementations that expose runtime capability posture SHOULD provide a human-readable state report and, where appropriate, a machine-readable endpoint or artifact containing:

- aide identity and principal
- runtime model and substrate
- active MxM surfaces
- Means inventory
- memory status
- orchestration / work-ownership status
- authority gates and approval posture
- observability/audit status
- known gaps and recommended next step

## Reference exemplars

| Exemplar | What it demonstrates | Canon use |
|---|---|---|
| **Hermetic** | Durable work coordination, atomic task claims, worker roster, human escalation/oracle bus, audit trail, liveness, digital-thread-style traceability | Reference exemplar for several capability classes; vocabulary maps to AIDE via the vocabulary map rather than becoming canonical by default |
| **AIDEX runtime surfaces** | Operator-facing Means, direct aide interaction, artifact creation, governed execution affordances | Experience-layer exemplar for capability self-report and human curation |
| **Claude Code Workflow** | Deterministic workflow orchestration wrapping probabilistic agent calls | Reference exemplar for workflow-orchestration and envelope-refinement gaps |

Other exemplars SHOULD be added through the SOTA survey and exemplar-tracking programs as they become relevant.

## Related patterns and constructs

| Item | Relationship |
|---|---|
| [MxM](../constructs/mxm/) | Governing harness surfaces in which capabilities operate |
| [OAgents](../constructs/oagents/) | Formal agent object and behavioral envelope |
| [AICP](../constructs/aicp/) | Portable identity and attestations |
| [OrdSA](../constructs/ordsa/) | Authority-down/evidence-up ordering |
| [digital-thread](digital-thread.md) | Evidence and auditability capability realization |
| [workflow-orchestration](workflow-orchestration.md) | Orchestration/delegation capability realization |
| [governed-context-management](governed-context-management.md) | Context and memory discipline touchpoint |
| [epistemic-integrity-floor](epistemic-integrity-floor.md) | Epistemic behavior and evaluation floor |
| [AIDE vocabulary map](../vision-strategy/analysis/aide-vocabulary-map.md) | External-vocabulary mapping discipline |
| [SOTA survey](../vision-strategy/analysis/sota-survey/) | Evidence source for current best-of-breed comparison |
| [Hermetic engagement](../vision-strategy/analysis/hermetic-engagement/) | Exemplar analysis for Hermetic-derived capability lessons |

## When not to use this pattern

Do not use this pattern as a substitute for:

- a formal OAgents spec revision
- a platform architecture for AEON or AIDEX
- a security control catalog
- a vendor/product comparison grid detached from AIDE constructs
- a claim that an aide is capable merely because the model can describe the capability

The pattern evaluates governed capability in a specific runtime or implementation. Description without executable or externally verifiable evidence is not conformance.
