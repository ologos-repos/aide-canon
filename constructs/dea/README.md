# DEA — Digital Ecosystems Architecture

A three-baseline framework for coherent digital realization, organized around three architecture disciplines and a single governing question per discipline.

| Baseline | Owned by | Governing question |
|---|---|---|
| **Digital Capability Baseline** | Enterprise Architecture | What must the enterprise be able to do to achieve its intended outcomes? |
| **Digital Technical Baseline** | Systems Architecture | How are those capabilities technically realized? |
| **Digital Operational Baseline** | Solutions Architecture | How is the resulting solution delivered, operated, governed, and sustained? |

Traceability binds the three: from business outcome to capability, capability to system, system to solution, solution to operation, and operation back to measured performance that revises the baselines above it. The framework holds that **enterprise architecture fails not by lacking design but by losing coherence across the disciplines that produce it**.

DEA is scoped to digitally-realized capabilities — those whose means of realization is substantially technical — and is intentionally **general, not AI-specific**. A forthcoming AI-specific extension, **AIDE-AF**, will bridge DEA's three baselines to the AI-focused constructs in the canon's [`enterprise-platforms/`](../../enterprise-platforms/) tier.

## Canonical artifact

[`docs/Digital-Ecosystems-Architecture-Base.pdf`](docs/Digital-Ecosystems-Architecture-Base.pdf) — the foundational paper. Sole-authored by JD Longmire (ORCID [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)).

## Layout

```
constructs/dea/
├── README.md (this file)
├── docs/                          # foundational + positioning papers
│   ├── Digital-Ecosystems-Architecture-Base.{docx,pdf}
│   ├── DEA-UAF-Positioning.{docx,pdf}
│   └── DEA-DIB-Compliance-Positioning.{docx,pdf}
├── infographics/                  # construct-specific visuals
│   ├── DEA-Construct-Infographic.jpg
│   ├── DEA-UAF-Positioning-Infographic.jpg
│   └── DEA-DIB-Compliance-Positioning-Infographic.jpg
├── decisions/                     # construct-internal ADRs
│   └── ADR-EA-0003-expand-corpus-to-include-dea.md
└── spec/                          # reserved (buildable spec)
```

## Suggested reading

1. [`docs/Digital-Ecosystems-Architecture-Base.pdf`](docs/Digital-Ecosystems-Architecture-Base.pdf) — read first. The foundational paper: three baselines, three architecture disciplines, three governing questions, bidirectional traceability.
2. [`docs/DEA-UAF-Positioning.pdf`](docs/DEA-UAF-Positioning.pdf) — positions DEA above UAF on the governance axis, below UAF on the description axis. Read after the base paper if your organization has invested in UAF.
3. [`docs/DEA-DIB-Compliance-Positioning.pdf`](docs/DEA-DIB-Compliance-Positioning.pdf) — positions DEA beneath the DoD / CMMC / NIST compliance regime as a service layer. Read if you operate in defense or other regulated contexts.

## Provenance

Sourced from `osa-ai-org/enterprise-ai/docs/` (snapshot copy). ADR-EA-0003 records the construct's addition to the corpus.
