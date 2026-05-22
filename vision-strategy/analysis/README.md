# analysis/

Canonical home for **analysis artifacts** that inform [VSOK](../vsok/). Per JD's directive (2026-05-22), all analysis informing the canon's strategic frame lives here; outputs can be leveraged elsewhere by citation.

## Position in Vision-Strategy

Per [ADR-EA-0007](../../decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md), Vision-Strategy is the *tier*; VSOK is one *artifact* within it. Analysis is a **second peer artifact** at Tier 0 — alongside VSOK, not inside it. The relationship:

```
vision-strategy/
├── README.md        — tier overview
├── vsok/            — V/S/O/K methodology product
└── analysis/        — analysis artifacts that inform VSOK's slots
```

Findings from analysis feed Strategy refinements, Objectives derivation, and Key Results anchoring. They also inform the broader canon — `enterprise-platforms/aeon/`, `constructs/*/`, and `decisions/` can cite analysis artifacts by their canonical path.

## Methodology

The canon's strategic frame is being developed via an **evidence-based** rather than internal-brainstorm approach: survey current state-of-the-art against the AIDE architecture, identify where AIDE is ahead / behind / in-flight elsewhere, and derive strategies from the gaps. Hermetic and the soon-to-be-deployed AEON instance are concrete exemplars used throughout.

Each analysis artifact follows a consistent shape:
- **Source material** — what's being analyzed (discussion body, SOTA snapshot, deployment report, etc.) cached locally so the artifact reads coherently even if the source moves
- **OlogosAI response / analysis** — substantive output of the analysis pass
- **VSOK implications** — explicit mapping back to which V/S/O/K slot(s) the finding informs

## Current contents

| Subfolder | What it holds |
|---|---|
| [`hermetic-engagement/`](hermetic-engagement/) | Analysis tied to the Hermetic discussion threads ([#38](https://github.com/ologos-repos/Hermetic/discussions/38) canon-mapping audit, [#39](https://github.com/ologos-repos/Hermetic/discussions/39) means inventory, [#40](https://github.com/ologos-repos/Hermetic/discussions/40) MxM refactor). Hermetic positioned as a concrete AEON exemplar. |

## Reserved (future analysis tracks)

These subfolders will appear as the corresponding work begins:

- `sota-survey/` — SOTA research program covering vendor stacks (MS, AWS, GCP, Salesforce, etc.), OSS frameworks (LangGraph, OpenHands, AutoGen, ADK, etc.), standards bodies (NIST AI RMF, MCP, A2A, ANP), and analyst frames (Gartner, Forrester). Gap analysis vs current AIDE architecture.
- `exemplar-tracking/` — Hermetic + AEON-deployed as concrete exemplars; observable progress signals over time; what the exemplars prove out about Vision feasibility.

## Bidirectional pointer pattern

For analysis tied to external discussion / issue threads (e.g., Hermetic discussions):

1. Analysis artifact lands in this subfolder first as the canonical record
2. Salient points get posted as a comment on the source thread, with the comment citing back to the canonical artifact's path
3. Future readers find the analysis here (in the canon, navigable top-down); the discussion thread documents the conversation that produced it

This keeps the canon's analysis discoverable inside the canon, not buried in external GitHub discussion threads.

## Provenance

Established 2026-05-22 by JD's directive following the VSOK methodology discussion. Joint-authored per the canon-level joint authorship in [ADR-EA-0008](../../decisions/ADR-EA-0008-reframe-corpus-authorship.md).
