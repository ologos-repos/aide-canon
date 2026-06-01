# ADR-EA-0028 – Introduce AI-aide capability-model pattern for standards-aligned SOTA evaluation

- **Status:** Proposed
- **Date:** 2026-06-01
- **Author:** Thinx (operator-altitude aide, under JD direction)
- **Reviewers:** JD Longmire; OlogosAI / canon-prime review recommended; cross-vendor QA recommended before ratification

## Context

The AIDE canon has strong constructs for orientation, authority, identity, agent behavior, enterprise platforms, and cross-cutting work patterns. It also has a SOTA survey program and Hermetic engagement analysis that treats Hermetic as a concrete exemplar of many best-of-breed multi-agent capabilities.

JD's direction for Thinx and related AI-aides is that they should be state-of-the-art, including evaluation against current best-of-breed systems. Hermetic-style capabilities matter for that evaluation: durable work coordination, atomic task ownership, worker identity, human escalation, liveness, auditability, dependency-aware dispatch, and recovery. But JD also clarified that AIDE should not adopt all Hermetic-specific components or naming. The canon should take the goodness while keeping architecture and naming tied to standards where standards exist, and should fill gaps where standards do not cover the aide-specific behavior.

The current canon has pieces of this discipline:

- `vision-strategy/analysis/aide-vocabulary-map.md` maps external vocabulary to AIDE vocabulary.
- `vision-strategy/analysis/sota-survey/` provides a program for comparing AIDE against current external work.
- `vision-strategy/analysis/hermetic-engagement/` treats Hermetic as an exemplar and analyzes its cross-construct touchpoints.
- `patterns/digital-thread.md` and `patterns/workflow-orchestration.md` already demonstrate exemplar-derived pattern extraction without making the exemplar's implementation details canonical.

What is missing is a single pattern for capability evaluation itself: a standards-first, gap-filling model that says how to define an aide capability, how to map it to standards, how to identify an AIDE-native gap, how to cite exemplars such as Hermetic, and how to attach evaluation probes.

## Decision

Add [`patterns/ai-aide-capability-model.md`](../patterns/ai-aide-capability-model.md) as a proposed cross-cutting pattern.

The pattern defines an AI-aide capability model as a standards-aligned, gap-filling catalog of the capabilities an AIDE-governed AI-aide must be able to declare, exercise, verify, and improve. It evaluates AI-aides against current best-of-breed systems without importing implementation-specific ontology where standards or AIDE-canonical terms suffice.

The pattern's central rule is:

> Use external standards for stable interfaces and recognized control patterns. Define AIDE-native constructs only where standards are absent, incomplete, misleading, or too low-level to express governed AI-aide behavior cleanly.

The pattern introduces:

1. A standards-first naming policy: formal/de facto standards first, widely-understood architecture terms second, AIDE-native constructs only where the gap is real.
2. A normative capability-record shape: capability, definition, nearest standards, AIDE-native gap, reference exemplars, required behavior, failure modes, evaluation probe, current status, maturity.
3. Nine baseline capability domains: identity continuity; operating posture and capability self-report; durable work ownership; human authority gates; memory with provenance and correction; orchestration and delegation; observability/evidence/auditability; interoperable Means and adapters; governed self-evolution.
4. Conformance criteria requiring standards mapping, explicit gap claims, exemplar discipline, evaluation probes, current-state honesty, maturity labeling, and cross-construct mapping.
5. Hermetic as a reference exemplar for several capability classes, not as the canonical naming source.

Update `patterns/README.md` to index the new proposed pattern.

## Consequences

**Positive:**

- Gives Thinx and other AI-aides a consistent way to report current capability state and developmental gaps.
- Converts SOTA comparison into an evaluable capability matrix rather than a narrative impression.
- Preserves the value of Hermetic as a best-of-breed exemplar while preventing Hermetic-local naming from becoming canon by accident.
- Creates a disciplined path for filling standards gaps with AIDE-native constructs.
- Provides a bridge between MxM orientation, OAgents/AICP formalization, OrdSA authority/evidence, AEON/AIDEX deployment, SOTA survey findings, and runtime evaluation probes.

**Negative / risk:**

- The pattern may overlap with future OAgents or AICP revisions if those standards later absorb capability reporting, identity continuity, or runtime posture reporting. This is acceptable if the pattern remains a cross-cutting evaluation layer and maps to future standards as they mature.
- The initial nine domains are broad. Without follow-on machine-readable catalogs or tests, the pattern could remain aspirational. The evaluation-probe requirement is meant to counter that risk.
- Standards references evolve quickly. The pattern should avoid freezing a list of standards as exhaustive and should keep them as nearest mappings.

**Neutral:**

- Additive only. No existing construct is redefined.
- Hermetic remains a reference exemplar and does not become a required substrate.
- The pattern does not edit OAgents, AICP, MxM, OrdSA, AEON, or AIDEX directly.

## Alternatives considered

1. **Place this under MxM.** Rejected. Capability evaluation touches MxM, but also OAgents, AICP, OrdSA, AEON, AIDEX, digital-thread, workflow-orchestration, SOTA survey, and exemplar tracking. It is cross-cutting, not a harness-surface refinement.
2. **Place this under SOTA survey only.** Rejected. The SOTA survey gathers evidence. This pattern defines the capability model used to evaluate and operationalize that evidence.
3. **Adopt Hermetic's ontology directly.** Rejected. Hermetic is valuable as a reference implementation, but AIDE should prefer standards-facing vocabulary where available and AIDE-native gap-filling terms where standards are insufficient.
4. **Wait for external standards to mature.** Rejected. Some aide-specific gaps are already operationally visible: persistent aide identity across model substrates, MxM-style orientation before execution, human authority as governance rather than generic approval, memory with epistemic/moral provenance, and governed self-evolution. Waiting would leave the canon unable to evaluate current systems honestly.
5. **Make this a new construct.** Rejected for now. The model is an evaluative cross-cutting pattern, not a peer methodological surface like MxM, OrdSA, OAgents, or AICP. If it later becomes a machine-readable conformance standard with independent lifecycle, promotion can be reconsidered by ADR.

## References

- [`patterns/ai-aide-capability-model.md`](../patterns/ai-aide-capability-model.md)
- [`vision-strategy/analysis/aide-vocabulary-map.md`](../vision-strategy/analysis/aide-vocabulary-map.md)
- [`vision-strategy/analysis/sota-survey/`](../vision-strategy/analysis/sota-survey/)
- [`vision-strategy/analysis/hermetic-engagement/`](../vision-strategy/analysis/hermetic-engagement/)
- [`patterns/digital-thread.md`](../patterns/digital-thread.md)
- [`patterns/workflow-orchestration.md`](../patterns/workflow-orchestration.md)
- [`constructs/mxm/`](../constructs/mxm/)
- [`constructs/oagents/`](../constructs/oagents/)
- [`constructs/aicp/`](../constructs/aicp/)
- [`constructs/ordsa/`](../constructs/ordsa/)
