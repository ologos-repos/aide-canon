# Ordinal Systems Architecture (OSA)

**A control-oriented enterprise architecture construct for Enterprise AI that orders AI capability by ordered authority, abstraction, execution rights, and evidence flow.**

> Enterprise AI needs an ordinal architecture because agentic systems are not merely applications. They are delegated actors inside a governed enterprise.

OSA's premise is simple: enterprise AI cannot be governed only by *components*. It must be governed by *order*. A model may appear capable. That does not mean it should be authorized.

OSA makes the distinction between **intelligence and authority** explicit.

---

## The Ordinal Layers

| # | Layer | What it governs |
|---|---|---|
| **O0** | [Enterprise Intent](docs/layers/O0-enterprise-intent.md) | Mission, strategy, policy, risk appetite, standards |
| **O1** | [Enterprise AI Orchestrator](docs/layers/O1-enterprise-ai-orchestrator.md) | Governance, routing, identity, model access, policy enforcement |
| **O2** | [Domain Orchestrators](docs/layers/O2-domain-orchestrators.md) | Development, infrastructure, cyber, mission, engineering, business |
| **O3** | [Agents and Workflows](docs/layers/O3-agents-workflows.md) | Task-specific AI workers under bounded delegation |
| **O4** | [Tools and Execution Channels](docs/layers/O4-tools-execution.md) | APIs, automation, ITSM, CI/CD, cloud, repositories |
| **O5** | [Data and Knowledge Substrate](docs/layers/O5-data-knowledge.md) | Documents, logs, CMDB, code, policies, telemetry, vector stores |
| **O6** | [Outcome, Audit, Feedback](docs/layers/O6-outcome-audit.md) | Evidence, metrics, decisions, incidents, drift, value realization |

## The Governance Principle

```
No lower ordinal layer may expand its own authority.
Authority only flows downward.
Evidence must flow upward.
```

That is the architectural core. Every other rule in OSA is a consequence of it.

---

## Why "Ordinal"?

*Ordinal* means **ordered**. The order is along four dimensions simultaneously:

1. **Authority** — what each layer is allowed to decide
2. **Abstraction** — how close to strategy vs. how close to execution
3. **Risk** — how much state each layer can change
4. **Execution rights** — read-only, recommend-only, draft-only, supervised, autonomous

A higher ordinal *contains* the authority of every lower ordinal. A lower ordinal cannot reach upward and grant itself rights it was not delegated.

This is the same logical structure that governs how real enterprises work — strategy authorizes operations, operations authorize execution, execution does not authorize itself. Most "AI architectures" today collapse these levels and confuse capability with authorization.

---

## Positioning vs. Existing Frameworks

OSA is **complementary**, not a replacement.

| Framework | What it gives you | What OSA adds |
|---|---|---|
| **TOGAF** | Architecture method | Authority grammar for AI capability layering |
| **UAF** | Systems-of-systems / mission alignment | Per-layer execution-rights model |
| **ArchiMate** | Modeling language | Vocabulary for AI-specific authority relations |
| **NIST AI RMF** | Risk management vocabulary (govern, map, measure, manage) | Concrete layered control surface to apply those functions against |

See [`docs/relationship-to-frameworks.md`](docs/relationship-to-frameworks.md) for the detailed mapping.

---

## Read the Construct

- **[`docs/concept.md`](docs/concept.md)** — canonical statement of the construct
- **[`docs/layers/`](docs/layers/)** — one file per ordinal layer (O0 through O6)
- **[`docs/relationship-to-frameworks.md`](docs/relationship-to-frameworks.md)** — OSA next to TOGAF, UAF, ArchiMate, NIST AI RMF
- **[`docs/relationship-to-ologos.md`](docs/relationship-to-ologos.md)** — OSA next to Modus Primus and the OAgent framework

## Status

**v0.1** — Construct definition published. Layer files are scaffolds, intentionally brief; deep-dives, ArchiMate/UAF mappings, and worked examples will follow in v0.2.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Substantive changes to the construct (new layers, layer redefinition, governance principle revision) go through ADRs; refinements and examples flow as ordinary PRs.

## License

Documentation is licensed under [CC-BY-4.0](LICENSE). Future code contributions will be dual-licensed Apache-2.0; that addition will be called out explicitly when introduced.

## Authorship

OSA is the work of **JD Longmire**, Chief Information Officer, Ologos Corp. Maintained under the `ologos-corp` GitHub organization.
