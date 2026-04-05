# OAgents: A Pre-Standardization Draft Profile for Operational AI Agent Trustworthiness

*A Community-Authored Pre-Standardization Draft*

---

## What Is OAgents?

OAgents is an open profile and candidate conformance framework for operational AI agent trustworthiness. It defines a behavioral envelope: a structured set of pre-execution gates, post-execution verification controls, and operational-discipline mechanisms that bound an AI agent's behavior.

The profile specifies 26 controls across 7 categories, 3 conformance levels, and observable evidence criteria. It is model-agnostic: behavioral guarantees are properties of the envelope, not properties of the underlying model.

## Document Type

This is a **community-authored pre-standardization draft** proposing a behavioral control and evidence profile for operational AI agents. It is not a NIST-issued publication, a consensus standard, or a formally adopted federal requirement. It is intended to inform AI agent standards development, implementation profiling, and public review, and to support routing into future NIST, NCCoE, IEEE, OASIS, IETF, or other voluntary consensus processes.

## Key Documents

| Document | Format |
|----------|--------|
| [Current Specification](spec/oagents-nist-standard-v16.0.md) | Markdown |
| [Current Specification](spec/oagents-nist-standard-v16.0.pdf) | PDF |
| [Current Specification](spec/oagents-nist-standard-v16.0.docx) | Word |
| [Reference Implementation](reference/) | Sanitized source |
| [Prior Versions](spec/versions/) | Archive |

## At a Glance

| Property | Value |
|----------|-------|
| Controls | 26 across 7 categories |
| Conformance levels | 3 (Basic, Standard, Autonomous) |
| Model dependency | None (model-agnostic by architecture) |
| AI RMF alignment | All 4 functions (GOVERN, MAP, MEASURE, MANAGE) |
| Conformance basis | Observable evidence artifacts, not assertions |
| Reference implementation | Included (sanitized, 21 files) |

## Conformance Levels

| Level | Name | Oversight Model | Verification |
|-------|------|----------------|-------------|
| 1 | OAgent-Basic | Human oversight standard | Self-assessment |
| 2 | OAgent-Standard | Exception-based oversight | Documented evidence review |
| 3 | OAgent-Autonomous | Minimal oversight | Third-party verification |

## Control Categories

1. **Behavioral Shaping** -- Persistent feedback memory, named failure mode catalogs, context degradation detection
2. **Quality Gates** -- Independent output review, process enforcement gates, security audit, schema validation
3. **Operational Discipline** -- Session lifecycle protocols, impact level classification, incident tracking, structured logging
4. **Knowledge Injection** -- Persistent memory system, domain skill loading, lessons-learned pipeline
5. **Enforcement Mechanisms** -- Executable action gates, severity escalation rules, protocol compliance verification
6. **Project Governance** -- Centralized work tracking, platform sovereignty, asset registry, vendor independence
7. **Anti-Hallucination** -- State verification protocol, memory staleness detection, hallucination tracking

## Requested Reviewer Action

The author requests feedback on four questions:

1. Whether this document is appropriately structured as an AI RMF implementation profile for operational AI agents.
2. Whether the behavioral-envelope taxonomy is technically coherent and materially distinct from existing identity, authorization, and agent-interoperability efforts.
3. Which elements are best advanced through NIST or NCCoE guidance and which belong in voluntary consensus venues such as IEEE, OASIS, or IETF-adjacent workstreams.
4. Which control definitions, conformance artifacts, or mappings should be revised before broader circulation.

## Getting Involved

- **[Discussions](https://github.com/ologos-corp/OAgents-standard/discussions)** -- Questions, feedback, implementation experiences
- **[Issues](https://github.com/ologos-corp/OAgents-standard/issues)** -- Component proposals, conformance clarifications, mapping corrections
- **Replication** -- Implement the profile and share conformance evidence

## Standards Track

This draft is offered as a community contribution aligned with:
- **NIST AI Agent Standards Initiative** (CAISI, February 2026)
- **NIST AI RMF 1.0** (NIST AI 100-1) -- as an implementation profile
- **NIST AI 600-1** (Generative AI Profile) -- hallucination risk category addressed

**DOI:** [10.5281/zenodo.19425020](https://doi.org/10.5281/zenodo.19425020)

## Author

**JD Longmire**
Northrop Grumman Fellow (unaffiliated research)
ORCID: [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)
Contact: jdlongmire@outlook.com

## License

This specification is published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt this material for any purpose, with attribution.
