# exemplar-tracking/

Tracking artifacts for the canon's named AIDE exemplars — concrete instances that demonstrate AIDE's claims operationally, not just in prose.

## Purpose

Per JD's VSOK methodology directive (2026-05-22):

> *"...leveraging Hermetic and the soon-to-be-deployed AEON as exemplars."*

Exemplars are the working evidence base. When the canon claims *AIDE composes a coherent enterprise architecture*, the exemplars are what backs that claim — not just in *aide-canon* prose but in deployed, observable systems.

This subfolder tracks each exemplar over time: what they prove, what they're missing, what changes when they evolve.

## Relation to SOTA survey

[`../sota-survey/`](../sota-survey/) identifies what *others* are doing; exemplar tracking captures what *AIDE itself demonstrates*. The two complement:

- When a survey finding classifies AIDE as *ahead* of SOTA, the corresponding exemplar should be cite-able as the proof.
- When a survey finding classifies AIDE as *behind*, the gap analysis informs what the exemplars need to extend to.
- When a survey finding classifies the topic as *in flight elsewhere*, the exemplars demonstrate AIDE's specific approach as the navigation reference.

## Named exemplars

| Exemplar | Role | Tracking subfolder |
|---|---|---|
| **[Hermetic](hermetic/)** | Reference implementation of AEON six service planes (Pattern B+ per [Hermetic Discussion #38](https://github.com/ologos-repos/Hermetic/discussions/38)) + canonical digital-thread reference impl (per [aide-canon#7](https://github.com/ologos-repos/aide-canon/issues/7) + ADR-EA-0009) | [`hermetic/`](hermetic/) |
| **[AEON-deployed](aeon-deployed/)** | Live AEON instance at an enterprise-altitude target — TBD deployment | [`aeon-deployed/`](aeon-deployed/) |
| **[Claude Code Workflow](claude-code-workflow/)** | Reference implementation of the [workflow-orchestration pattern](../../../patterns/workflow-orchestration.md) (per [ADR-EA-0027](../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)) — deterministic agent-orchestration substrate; out-of-tree (Anthropic product), cited for behavior | [`claude-code-workflow/`](claude-code-workflow/) |
| **[thinx-aidex](thinx-aidex/)** | Operator-altitude reference implementation of the [AIDEX](../../../enterprise-platforms/aidex/) surface — JD's MyAide console (5M+1 meta-harness, 7-plane `means/`, FOrCE gate + OTel-native evidence); out-of-tree, operator-altitude, cited for behavior. Complements the deployment-altitude AIDEX surfaces in NG-AIDE-01 IO4 | [`thinx-aidex/`](thinx-aidex/) |

The two-exemplar framing is intentional:

- **Hermetic** is the *technical exemplar* — it demonstrates the architectural patterns end-to-end at the implementation level
- **AEON-deployed** is the *operational exemplar* — it demonstrates the architecture surviving contact with a real enterprise

The contingency tree captured in [`../hermetic-engagement/40-mxm-refactor/ologosai-response.md`](../hermetic-engagement/40-mxm-refactor/ologosai-response.md) (addendum) covers what happens if Hermetic's MxM-multi-agent-harness role doesn't materialize: AEON-deployed carries the AIDE-exemplar role; Hermetic retains its AEON-reference-impl role.

## Per-exemplar tracking shape

Each exemplar subfolder maintains:

```
{exemplar}/
├── README.md          (current state + what the exemplar proves)
├── milestones.md      (chronological progress markers, dated)
├── signals.md         (observable progress signals — adoptions, citations, ops metrics)
└── (artifact docs, screenshots, conformance assertions)
```

The shape evolves with the exemplar's lifecycle. Hermetic has working content from day one (it exists); AEON-deployed is mostly placeholder until the deployment lands.

## Cadence

- **Hermetic** — track milestones as Hermetic releases land or major architectural decisions get committed at `ologos-repos/Hermetic`. Watch the discussion threads ([#38](https://github.com/ologos-repos/Hermetic/discussions/38), [#39](https://github.com/ologos-repos/Hermetic/discussions/39), [#40](https://github.com/ologos-repos/Hermetic/discussions/40)) for ratification signals.
- **AEON-deployed** — placeholder until deployment site + timeline are named; once live, track at deployment-relevant cadence (deployment milestones, expansion phases, observable enterprise outcomes).

## Status

Scaffolding established 2026-05-22. Hermetic tracking populated from existing engagement artifacts; AEON-deployed remains placeholder until deployment is named.
