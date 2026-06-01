# OSS framework — LangChain / LangGraph (cross-reference)

> SOTA-survey finding (OSS-frameworks slice). **Primary treatment is in the vendor-stacks slice** — see [`../vendor-stacks/langchain.md`](../vendor-stacks/langchain.md). This entry is a deliberate cross-reference so the OSS-frameworks index stays complete without duplicating the analysis.

## Why this is a cross-reference, not a full entry

LangChain spans both slices: the **OSS libraries** (LangChain + LangGraph — chain/graph orchestration, the long-established framework) belong here, but the substantive AIDE-mapping was done against the **commercial LangChain Enterprise stack** (LangChain / LangGraph / LangGraph Platform / LangSmith / Fleet) in [`../vendor-stacks/langchain.md`](../vendor-stacks/langchain.md), because the enterprise tier is where the runtime + observability + governance comparison actually bites. The OSS framework and the enterprise platform share the same architectural opinion; surveying them twice would split the finding.

## OSS-framework angle (the delta from the vendor entry)

The two pieces that are purely OSS-framework-shaped:

- **LangChain** — the framework/abstraction layer (chains, model/tool integrations). Maps to MxM **Means** (a composition library), construct-unaware.
- **LangGraph** — stateful, graph-based orchestration (durable execution, persistence, human-in-the-loop, cyclic control flow). This is the OSS heart of the [workflow-orchestration](../../../../patterns/workflow-orchestration.md) comparison: LangGraph is the closest OSS analogue to AEON's **Composition / Orchestration-runtime** planes and the workflow-orchestration pattern's deterministic control flow — **but it enforces no envelope-refinement `⊑` lattice** (the same convergence-at-design / gap-at-enforcement finding the pattern records industry-wide).

## Mapping

The full **4-AIDE-plane + 6-AEON-plane** mapping, per-axis classification, and synthesis are in [`../vendor-stacks/langchain.md`](../vendor-stacks/langchain.md) §3–§5. Construct-level summary for this slice:

| AIDE construct | LangChain/LangGraph (OSS) | AIDE position |
|---|---|---|
| **MxM** (5-surface harness) | LangChain components + LangGraph graph state | *in flight elsewhere* — a composition/runtime library, not a governing harness |
| **OAgents** (typed agent envelope) | LangGraph node/agent + (LangChain) "Agent" = persistent org entity ↦ canon **AI-aide** | *AIDE ahead* — no behavioral envelope; LangChain "Agent" collides with the AI-aide role-class |
| **OrdSA** (ordinal authority) | (absent) | *AIDE ahead* |
| **DEA** | (absent) | *AIDE ahead* |

## Classification

**Mixed — different altitude**, identical to the vendor finding: LangChain/LangGraph is a Means-layer build substrate; aide-canon is the governance layer above it. See the vendor entry for the per-axis detail and the "canon governs a LangChain deployment" synthesis.

## Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Cross-reference entry; primary treatment + revision cadence tracked in [`../vendor-stacks/langchain.md`](../vendor-stacks/langchain.md).
