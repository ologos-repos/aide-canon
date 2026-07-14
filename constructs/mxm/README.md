# MxM — Mx-Modes (Multi-mode Meta-harness)

The **harness archetype** — six governing surfaces that compose an AI operating envelope at any altitude (per-agent, multi-agent, enterprise-scale). MxM is co-authored with **Micah Longmire** ([ORCID 0009-0006-7608-9322](https://orcid.org/0009-0006-7608-9322), Sr. AI Architect); the corpus's first joint construct in the spine.

## The six surfaces

| Surface | Concern |
|---|---|
| **MIND** | Reasoning discipline — inference modes, belief revision, metacognitive calibration |
| **MORALS** | Permission boundaries — permissions, prohibitions, obligations, process gates |
| **MISSION** | Purpose and scope — telos, team, infrastructure, session protocols |
| **MEMORY** | Continuity and reference — what persists across sessions, how priors form |
| **METHODS** | Tradecraft — codified best-practice and rigor; how a kind of work is done to a standard. Recommends; does not grant permission (Morals) or implement (Means) |
| **MEANS** | Execution surface — tools, skills, workflows. Implements; does not grant permission |

A root file activates the operating posture; the model executes within the envelope the five discipline-bearing surfaces establish. Means implements; it does not grant permission.

### The root file (the activator) — per [ADR-EA-0013](decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md)

The root file is the **harness-attach point and operating-mode activator** — the element an instantiation may name `mode.md`, and for which Claude Code's `CLAUDE.md` is the canonical example. It is **not a seventh surface and not a governing altitude.** It has three roles, none of them governance:

1. **Harness-attach / entry** — harness-specific and swappable (`CLAUDE.md` under Claude Code, another bootstrap under another harness). It isolates harness-specificity so the six surfaces stay harness-agnostic.
2. **Operating-mode / posture activation** — sets the mode the surfaces apply under (advisory / read-only / operational / degraded) and the autonomy posture (how much an agent self-directs before surfacing a decision). This is the "Mx-*Modes*" the construct's name refers to.
3. **Routing** — points the agent into the six surfaces.

**The root file and Means *bracket* the five discipline surfaces** — the root file is the swappable seam at the *attach* end, Means the swappable seam at the *execution* end, and Mind/Morals/Mission/Memory/Methods the durable, harness-agnostic core. Swap the root file to move harnesses; swap Means to move substrates; keep the governance.

### The methods surface — per [ADR-EA-0026](decisions/ADR-EA-0026-introduce-methods-surface.md)

**METHODS** is the harness's **tradecraft** — the codified, evidenced, reusable procedures and rigor disciplines for doing a kind of work *to a standard*. It answers *"how do we do this well?"* It **recommends**; it does not constrain (that's Morals), implement (that's Means), or reason (that's Mind).

- **Boundary vs. Morals = enforcement/obligation.** Morals holds the *obligatory, enforced* disciplines (violation is a breach); Methods holds *recommended craft* (departure is suboptimal). A method **graduates** when it earns enforcement: `practice → method → moral → means` — one discipline can project across surfaces (the *technique* of QA is a Method, the *duty* a Moral, the *hook* Means).
- **Relation to the [`patterns/`](../../patterns/) tier = altitude.** Patterns are *architecture*-level (how the system is shaped); Methods is *operator*-level (how the agent works). Peers; Methods may cite patterns.
- **Entry bar:** a method qualifies only if evidenced (proven through repetition), named/reusable, and carrying its rationale — not a junk drawer.

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

## Related patterns

| Pattern | How MxM participates |
|---|---|
| [MxH-P synthesis](../../patterns/mxh-p-synthesis.md) ([ADR-EA-0028](../../decisions/ADR-EA-0028-introduce-mxh-p-synthesis-pattern.md)) | MxM is the **orientation and constraint** altitude in the MxM · Hermetic · P/G/E composition. Operational form: **orientation packet** injected at every worker/role spawn (not package renames). |
| [workflow-orchestration](../../patterns/workflow-orchestration.md) | MxM Morals/Means supply envelope limbs refined under `envelope(child) ⊑ envelope(parent)`. |
| [epistemic-integrity-floor](../../patterns/epistemic-integrity-floor.md) | Imports into Mind/Morals/Memory. |
| [digital-thread](../../patterns/digital-thread.md) | Morals gates + Memory/Means evidence along a single work trajectory. |

## Citation

[`10.5281/zenodo.20349200`](https://doi.org/10.5281/zenodo.20349200) — Longmire, J. D., & Longmire, M. (2026). *Mx-Modes: A Meta-Harness Framework for Multi-Mode AI Operation*. Zenodo.

Deposited 2026-05-22 to the [AI Research & Philosophy community](https://zenodo.org/communities/ai-research-philosophy/). The corpus's first joint construct in the spine; co-authorship recorded on the artifact title page. License: CC BY 4.0.

## Provenance

Sourced from `osa-ai-org/enterprise-ai/docs/` (snapshot copy). ADR-EA-0004 records the spine bundling decision; ADR-EA-0005 refines the altitude characterization to harness archetype.
