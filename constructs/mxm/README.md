# MxM — Mx-Modes (Multi-mode Meta-harness)

The **harness archetype** — five governing surfaces that compose an AI operating envelope at any altitude (per-agent, multi-agent, enterprise-scale). MxM is co-authored with **Micah Longmire** ([ORCID 0009-0006-7608-9322](https://orcid.org/0009-0006-7608-9322), Sr. AI Architect); the corpus's first joint construct in the spine.

## The five surfaces

| Surface | Concern |
|---|---|
| **MIND** | Reasoning discipline — inference modes, belief revision, metacognitive calibration |
| **MORALS** | Permission boundaries — permissions, prohibitions, obligations, process gates |
| **MISSION** | Purpose and scope — telos, team, infrastructure, session protocols |
| **MEMORY** | Continuity and reference — what persists across sessions, how priors form |
| **MEANS** | Execution surface — tools, skills, workflows. Implements; does not grant permission |

A root file activates the operating posture; the model executes within the envelope the four discipline-bearing surfaces establish. Means implements; it does not grant permission.

## The architectural claim

> **AI behavior should be oriented before it is executed.**

Most AI implementations begin with capability — models, tools, APIs, plugins, automations — and try to constrain that capability afterward. MxM inverts the order: **orientation first**, then capability is loaded against an established posture. The result is categorical clarity over model behavior, not a claim about model capability or assurance.

## Scale-invariance

Per [ADR-EA-0005](decisions/ADR-EA-0005-clarify-mxm-archetype.md), MxM is **the harness archetype across altitudes** — not a single-altitude artifact:

- **Per-agent orientation** is one application
- **Multi-agent harness composition** is another
- **Enterprise-altitude harness shape** is another

The five surfaces are scale-invariant; the canon's `enterprise-platforms/` are enterprise-altitude instantiations of MxM, ordered by OrdSA within DEA.

## Canonical artifact

[`docs/Mx-Modes-Technical-Reference.pdf`](docs/Mx-Modes-Technical-Reference.pdf) — the Technical Architecture Reference. Describes the archetype.

## Layout

```
constructs/mxm/
├── README.md (this file)
├── docs/
│   └── Mx-Modes-Technical-Reference.{docx,pdf}
├── infographics/
│   └── Mx-Modes-Construct-Infographic.jpg
├── decisions/                     # construct-internal ADRs
│   ├── ADR-EA-0004-add-mx-modes-as-spine-construct.md
│   └── ADR-EA-0005-clarify-mxm-archetype.md
└── spec/                          # reserved (buildable spec)
```

## Provenance

Sourced from `osa-ai-org/enterprise-ai/docs/` (snapshot copy). ADR-EA-0004 records the spine bundling decision; ADR-EA-0005 refines the altitude characterization to harness archetype.
