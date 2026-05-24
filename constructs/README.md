# constructs/ — Tier 3

Peer methodological patterns, transverse to altitude. Five constructs sit at this tier; each patterns a different concern. None subsumes another; they compose.

## Members

| Subdir | Patterns | Canonical artifact |
|---|---|---|
| [`dea/`](dea/) | EA coherence (three-baseline framework) | `docs/Digital-Ecosystems-Architecture-Base.pdf` |
| [`ordsa/`](ordsa/) | Authority and evidence (seven-ordinal layering) | `schema/ordsa-0.2.yaml` (schema-first; prose companion) |
| [`mxm/`](mxm/) | Harness composition (five-surface archetype) | `docs/Mx-Modes-Technical-Reference.pdf` |
| [`oagents/`](oagents/) | Agent domain model (behavioral envelope standard) | `spec/oagents-nist-standard-v16.0.md` (schema-first; paper companion) |
| [`aicp/`](aicp/) | Portable agent identity (Card + phase-gated tool injection + attestations) | `spec/AICP-v0.1.md` (spec-first, MIT; vendored snapshot — living source [`ologos-repos/AICP`](https://github.com/ologos-repos/AICP)) |

## Composition

The enterprise-platforms at [`../enterprise-platforms/`](../enterprise-platforms/) are **enterprise-altitude instantiations** of these constructs — what you get when you compose MxM (harness) ordered by OrdSA (authority/evidence) within DEA (EA coherence) at enterprise scale, with OAgents as the domain object and AICP as its portable, cross-platform identity. OAgents bounds *what an agent does*; AICP carries *who the agent is* — complementary halves of a governable agent.

## Pattern α

Each construct's subdirectory is self-contained: `README.md`, `docs/` (papers), optional `infographics/` (construct-specific visuals), `decisions/` (construct-internal ADRs), `spec/` (machine-readable spec; reserved if not yet populated). Construct-internal ADRs stay with the construct; canon-level ADRs live at [`../decisions/`](../decisions/).
