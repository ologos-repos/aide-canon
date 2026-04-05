# OAgents: A Behavioral Envelope Standard for Trustworthy AI Agent Operations

**An Implementation Profile of the NIST AI Risk Management Framework (AI RMF 1.0)**

---

## What Is OAgents?

OAgents is an open standard for behavioral envelopes that wrap AI agents in structured pre-execution gates, post-execution verification, and operational discipline mechanisms. The standard is model-agnostic: behavioral guarantees are properties of the envelope, not properties of the underlying model.

The behavioral envelope is to AI agents what OAuth was to identity delegation — a trust layer the industry needs before enterprise adoption can scale.

## Key Documents

- **[OAgents v1.0 Specification](spec/OAgents-v1.0.md)** — Full standard with component taxonomy, compliance levels, AI RMF mapping, and conformance evidence criteria
- **[NIST AI RMF Alignment](spec/OAgents-v1.0.md#2-ai-rmf-alignment-statement)** — How OAgents maps to GOVERN, MAP, MEASURE, MANAGE
- **[Conformance Evidence (Appendix C)](spec/OAgents-v1.0.md#appendix-c-conformance-evidence)** — Observable criteria for compliance verification

## At a Glance

- **26 components** across 7 categories
- **3 compliance levels**: Basic (supervised), Standard (production), Autonomous (minimal oversight)
- **Model-agnostic by architecture** — works with any LLM provider
- **NIST AI RMF 1.0 aligned** — maps to all four functions (GOVERN, MAP, MEASURE, MANAGE)
- **Evidence-based conformance** — compliance demonstrated through observable artifacts, not assertions

## Compliance Levels

| Level | Name | Oversight | Verification |
|-------|------|-----------|-------------|
| 1 | OAgent-Basic | Human oversight standard | Self-assessment |
| 2 | OAgent-Standard | Exception-based oversight | Documented evidence review |
| 3 | OAgent-Autonomous | Minimal oversight | Third-party verification |

## Component Categories

1. **Behavioral Shaping** — Feedback memory, failure mode catalogs, degradation detection
2. **Quality Gates** — Independent review, process enforcement, security audit, schema validation
3. **Operational Discipline** — Session protocols, impact levels, incident tracking, logging
4. **Knowledge Injection** — Persistent memory, domain skills, lessons-learned pipeline
5. **Enforcement Mechanisms** — Executable gates, escalation rules, compliance verification
6. **Project Governance** — Work tracking, platform sovereignty, asset registry, vendor independence
7. **Anti-Hallucination** — State verification, memory staleness detection, hallucination tracking

## Getting Involved

- **[Discussions](https://github.com/ologos-corp/OAgents-standard/discussions)** — Questions, feedback, implementation experiences
- **[Issues](https://github.com/ologos-corp/OAgents-standard/issues)** — Bug reports, component proposals, conformance clarifications
- **Replication** — Implement the standard and share your results

## Standards Track

This specification is submitted as a community contribution to:
- **NIST AI RMF** — as an Implementation Profile for enterprise AI agent operations
- **NIST CAISI** — AI Agent Standards Initiative (February 2026)

Published via [Zenodo](https://zenodo.org) for persistent DOI and citability.

## Author

**JD Longmire**
Northrop Grumman Fellow (unaffiliated research)
ORCID: [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)

## License

This specification is published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt this material for any purpose, with attribution.
