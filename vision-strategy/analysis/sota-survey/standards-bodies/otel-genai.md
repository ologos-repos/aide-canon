# Standards body — OpenTelemetry GenAI semantic conventions (CNCF)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../../README.md), AIDE-mapping anchor per the [standards-bodies README](README.md#aide-mapping-anchor). Cadence: **slow** (CNCF SIG deliverable) — but the *operation taxonomy* is moving fast right now (Development status, breaking renames between point releases), so treat the version/status header as load-bearing.

## 1. What it is

> **Version/status header.**
> **Effort:** OpenTelemetry Semantic Conventions — Generative AI (`gen_ai.*`), CNCF / OpenTelemetry Semantic-Conventions SIG.
> **Version analyzed:** the `main`/published spec as of **2026-06-01** (the GenAI conventions reference baseline v1.36.0 for the stability opt-in; agent-spans operation taxonomy carries later additions, e.g. the v1.41 `invoke_agent` CLIENT-vs-INTERNAL split).
> **Status:** **Development** (every GenAI semantic-conventions document — client spans, metrics, events, and agent/framework spans — currently carries the *Development* stability badge). Client spans + metrics are the furthest along; **agent + framework spans (`create_agent` / `invoke_agent` / `invoke_workflow` / `execute_tool`) remain Development.** Not yet Stable. Migration is gated behind `OTEL_SEMCONV_STABILITY_OPT_IN` with the `gen_ai_latest_experimental` token; a stable-version transition plan is promised but not yet published.
> **Geography:** none — vendor-neutral, jurisdiction-independent CNCF spec.

**OpenTelemetry GenAI semantic conventions** are the de-facto observability standard for generative-AI and agentic systems: a controlled vocabulary of span/metric/event shapes under the `gen_ai.*` namespace, so that a trace emitted by one framework (OpenAI Agents SDK, LangChain/LangGraph, LlamaIndex, AutoGen) is read identically by any OTel-compatible backend (LangSmith, Greptime, Databricks/MLflow, Jaeger, vendor APMs). It is an **interface standard for evidence**, not an agent runtime or a governance model — it specifies *how a generative-AI operation is recorded after it happens*, not what is permitted to happen.

The taxonomy that matters for AIDE is `gen_ai.operation.name`, whose defined values are: **`chat`**, **`text_completion`**, **`generate_content`** (multimodal), **`embeddings`**, **`retrieval`**, **`create_agent`**, **`invoke_agent`** (CLIENT for remote, INTERNAL for in-process framework execution), **`invoke_workflow`** (INTERNAL), and **`execute_tool`**. The three agentic operations — `invoke_workflow` ⊃ `invoke_agent` ⊃ `execute_tool` — are exactly the orchestration→agent→tool nesting the canon's [workflow-orchestration pattern](../../../../patterns/workflow-orchestration.md) names independently.

## 2. Source links

- Spec root: `opentelemetry.io/docs/specs/semconv/gen-ai/` (overall Development status + stability opt-in).
- Agent & framework spans (the operation taxonomy): `opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/`.
- Client AI spans: `opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/`; metrics: `.../gen-ai-metrics/`; events: `.../gen-ai-events/`.
- Attribute registry (authoritative `gen_ai.*` list): `opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/`.
- Repo: `github.com/open-telemetry/semantic-conventions` (GenAI SIG work area).
- **In-canon prior adoption:** [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md) §"cross-cutting" table + §"Schema-level recommendations" (the shared evidence object) + §"Interface conformance" (the `invoke_workflow` / `invoke_agent` / `execute_tool` span mapping), ratified [ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md). This entry surveys the standard the canon **already adopted** there.

## 3. Map against AIDE

### Against OAgents + the AEON service planes (Evidence-anchored)

| `gen_ai.*` element | AIDE construct / AEON plane | Alignment status |
|---|---|---|
| `invoke_workflow` span (INTERNAL) | OAgents `Agent` at orchestration altitude · AEON **Meta-Orchestration plane** · OrdSA **O3** workflow | **ALIGN/ADOPTED** — the canon's orchestration span *is* this span |
| `invoke_agent` span (CLIENT/INTERNAL) | OAgents **`Agent`** primitive (typed object in a behavioral envelope) · OrdSA **O3** agent | **ALIGN/ADOPTED** — child-spawn span |
| `execute_tool` span | OAgents tool invocation · OrdSA **O4** Tool · MxM **MEANS** | **ALIGN/ADOPTED** — atomic-invocation span |
| `gen_ai.usage.*`, `gen_ai.request.model`, `gen_ai.provider.name` | AEON **Evidence plane** machine record · AEON **Inference plane** (provider-agnosticism, ADR-EA-0015) | **CONSUME** — AIDE ingests these as-is |
| span/trace tree (parent/child) | canon **[digital-thread](../../../../patterns/digital-thread.md)** (task→phase→artifact) · evidence aggregation | **ALIGN** — OTel parentage is the thread's transport |
| `gen_ai.operation.name` controlled vocab | AEON **Evidence plane** operation taxonomy | **ALIGN/ADOPTED** — adopted verbatim |
| **— no equivalent —** `parent_evidence_id` / `orchestration_run_id` lineage FK | OAgents evidence-emission lineage (workflow-orchestration criterion 5, MUST) | **EXTEND** — OTel has span parentage but no *enforced* evidence-lineage FK as a first-class governance field |
| **— no equivalent —** `gate_decision` (authorized/refused/escalated + envelope_delta) | MxM **MORALS** gate · AEON **Authority plane** · OrdSA authority-down | **EXTEND** — OTel records what ran, not what a *gate decided* |
| **— no equivalent —** `authority_context` / `decision_actor` / `determinism_flag` / `substrate` | AEON **Authority** + **Identity** planes · OrdSA principal-altitude authority | **EXTEND** — the governance-grade fields the canon adds in the shared evidence object |

### Vocabulary-collision note (per [aide-vocabulary-map](../../aide-vocabulary-map.md))

- **`gen_ai.agent`** — OTel's "agent" is *whatever the framework calls an agent* (a free-form `gen_ai.agent.name` / `gen_ai.agent.id` / `gen_ai.agent.description`, no typing). The canon does **not** read this as the casual "agent": at AIDE altitude the operating entity is the **AI-aide** ([ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)), and the OAgents **`Agent`** is a *typed object inside a behavioral envelope* — a far stronger claim than OTel's untyped label. Same string, three different referents; flagged.
- **`execute_tool` / `gen_ai.tool.*`** (`tool.name`, `tool.call.id`, `tool.type` ∈ {function, extension, datastore}) — convergent with the canon's **Tool** (atomic invocation, O4 / MEANS). No collision.
- **`invoke_workflow` / `gen_ai.workflow.name`** — convergent with the canon **Workflow** (O3 orchestration object); OTel has the *observation* of a workflow but not the **envelope-refinement composition law** that makes it governed.
- **Absent from `gen_ai.*` entirely:** no attribute for **skill, capability, persona, role, authority, permission, governance, gate, or decision-actor** (confirmed against the attribute registry, 2026-06-01). This is the vocab gap the canon vocabulary map already records, and it is *precisely* the surface the canon EXTENDS. OTel-GenAI is an after-the-fact telemetry vocabulary; it has no notion of what was *permitted*, only what *occurred*.

## 4. Alignment classification

**This is the canon's already-adopted evidence schema — classify it ADOPTED + EXTENDED, not as a competitor.** OTel-GenAI is not "in flight elsewhere" to be converged-with; the canon already rode it in [workflow-orchestration v0.1.2](../../../../patterns/workflow-orchestration.md) (ADR-EA-0027) and in AIDEX α2 evidence. Per-axis:

- **ALIGN / CONSUME (the base spans) — convergent, adopted.** The `invoke_workflow` ⊃ `invoke_agent` ⊃ `execute_tool` nesting, the trace parent/child tree, `gen_ai.usage.*` / `gen_ai.request.model` / `gen_ai.provider.name` — AIDE **consumes these as-is**. The canon's shared evidence object is explicitly defined as *"the OTel record + …"* — the OTel span is the substrate, not a rival. There is no daylight here and no gap to close: this is convergence the canon banked.
- **EXTEND (the governance fields) — AIDE-ahead, by construction.** OTel-GenAI records *what ran*; it has **no** lineage FK (`parent_evidence_id` / `orchestration_run_id` as an enforced MUST), **no** `gate_decision` (authorized/refused/escalated + `envelope_delta`), and **no** `authority_context` / `decision_actor` / `determinism_flag` / `substrate`. The canon adds exactly these to turn correlated telemetry into *governance-grade, recoverable* evidence — the digital-thread lineage, the per-spawn gate decision, and the determinism/substrate fields that let a reviewer know the gate was actually on the execution path (workflow-orchestration criterion 7). This EXTENSION is the **AIDE-ahead** position in the standards-bodies slice — the same shape the [standards-bodies README](README.md#aide-mapping-anchor) anchors for OAgents-vs-NIST-AI-RMF: AIDE is a *governance profile over* the interface.
- **DIFFERENTIATE — only on framing, not mechanism.** AIDE does not fork the wire format; it differentiates on *what evidence is for* — OTel for operability/debugging, AIDE for authority-down/evidence-up governance. The mechanism stays OTel; the obligation layer is the canon's.

**The synthesis: AIDE rides OTel-GenAI and extends it.** The base spans (`invoke_workflow` / `invoke_agent` / `execute_tool`) already match the workflow-orchestration vocabulary one-for-one — the canon adopted them deliberately so its evidence interoperates with every OTel backend. On top, AIDE attaches the governance fields OTel structurally lacks (lineage FK, gate-decision, authority context, determinism/substrate), mapped to the **AEON Evidence plane** and the canon **digital-thread**. OTel makes an orchestration *observable*; the canon's extension makes it *governable*. They compose — OTel is the evidence transport AIDE governs *through*, not a standard AIDE competes with.

## 5. Objective implication

Two Doerr-style Objective shapes follow — both *defend-and-extend* on a standard the canon has already committed to, not catch-up:

1. **Defend-and-extend (evidence-governance extension).** Establish the AIDE evidence object — OTel-GenAI span **+** lineage FK + `gate_decision` + `authority_context` + `decision_actor` + `determinism_flag` + `substrate` — as the canonical governance-grade evidence shape, and propagate it as a *profile over* OTel rather than a parallel format. KR shape: an exemplar emits valid `gen_ai.*` spans **and** the governance extension on the same trace, ingestible by a stock OTel backend (proving ALIGN) while a governance reviewer can replay authority/gate decisions end-to-end (proving the EXTEND value). Closes the LangSmith-grade-evidence gap noted in [`../vendor-stacks/langchain.md`](../vendor-stacks/langchain.md) §5.
2. **Converge-the-vocabulary (taxonomy tracking).** OTel-GenAI agent-spans are *Development* and renaming between point releases (the v1.41 `invoke_agent` split is the live example). KR shape: pin the workflow-orchestration interface-conformance recommendation to a named `gen_ai.operation.name` version, and re-survey on each agent-spans release so the canon's `invoke_workflow`/`invoke_agent`/`execute_tool` mapping never silently drifts from the standard it adopted.

## 6. Date + reviewer

Surveyed **2026-06-01 by OlogosAI (canon-prime).** Analyzes the GenAI semantic conventions at *Development* status as of that date (agent-spans taxonomy incl. the v1.41 `invoke_agent` CLIENT/INTERNAL split; v1.36.0 stability-opt-in baseline). Inherits the canon's prior adoption in [workflow-orchestration](../../../../patterns/workflow-orchestration.md) (ADR-EA-0027) and AIDEX α2. **Revisit on each agent-spans release** (operation-taxonomy renames are breaking) and when the GenAI conventions transition from Development toward Stable.
