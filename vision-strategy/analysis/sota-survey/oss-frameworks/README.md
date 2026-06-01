# oss-frameworks/

Survey of open-source agentic / LLM frameworks — what they architect, how they govern, what they leave to the user.

## In scope

Active OSS frameworks with substantive agentic / orchestration / harness shape:

- **LangChain / LangGraph** — chain + graph orchestration; long-established
- **OpenHands** (formerly OpenDevin) — autonomous coding agent / harness
- **AutoGen** — Microsoft's multi-agent conversational framework
- **CrewAI** — role-based multi-agent orchestration
- **Google ADK** (Agent Development Kit) — Google's OSS agent runtime; cross-references vendor slice
- **LlamaIndex** — agentic retrieval + workflow framework
- **Smolagents** — Hugging Face's lightweight agent framework
- **Letta** (formerly MemGPT) — persistent-memory agent framework
- **DSPy** — declarative LM programming (not exactly agentic but architecturally adjacent)
- **PydanticAI** — typed agent framework
- **Mastra** — TypeScript/JavaScript agent framework
- **Inspect AI** — UK AISI's evaluation harness (governance-adjacent)

Frameworks enter scope when they have a coherent architectural opinion (not just thin LLM wrappers).

## Out of scope

- LLM clients / SDKs without architectural surface (Anthropic SDK, OpenAI SDK considered in vendor-stacks)
- Pure chat UIs / front-ends without orchestration discipline
- Experimental research code without sustained release cadence

## Per-framework entry shape

```
{framework-slug}.md
```

For frameworks with multiple architectural surfaces worth separating (e.g., LangChain vs LangGraph), use a subdirectory:

```
{framework-slug}/
├── README.md  (cross-surface overview)
├── {surface-1}.md
└── {surface-2}.md
```

## Sources to canvass per entry

- **Project README + docs site** — primary
- **GitHub release notes** — last 90 days at survey time
- **Architecture / design docs in the repo** — `docs/`, `ARCHITECTURE.md`, design RFCs
- **Notable issues + RFCs in flight** — surface direction-of-travel
- **Project maintainer talks / blog posts** — what the maintainers *say it is*
- **Community fork / adoption signals** — GitHub stars over time, downstream uses
- **Academic citations** (cross-reference `../academic/`)

## AIDE-mapping anchor

Each entry maps the framework against AIDE's constructs (DEA / OrdSA / MxM / OAgents) and AEON's six service planes:

| Construct / plane | Framework's equivalent | AIDE position |
|---|---|---|
| MxM (5-surface harness) | Framework's component model | *In flight elsewhere* — comparable decomposition, different vocabulary |
| OAgents (typed agent envelope) | Framework's agent type | *AIDE ahead* — OAgents' schema-first spec is stronger than framework's ad-hoc interface |
| OrdSA (7-ordinal authority) | (framework doesn't address) | *AIDE ahead* — authority altitudes are unique to OrdSA |
| Identity plane | Framework's auth model | *Behind* — framework integrates with enterprise identity more deeply |
| ... | | |

This is the same anchor pattern as `../vendor-stacks/` but the comparison surfaces are different (constructs + service planes for OSS; planes alone for vendor stacks, which tend to be construct-unaware).

## Special case — Hermetic

[`ologos-repos/Hermetic`](https://github.com/ologos-repos/Hermetic) is itself an OSS framework but is treated as an *exemplar* rather than surveyed comparator. It is tracked at [`../../exemplar-tracking/hermetic/`](../../exemplar-tracking/hermetic/) per the analysis convention; comparator entries here may cross-reference Hermetic when relevant.

## Landed entries

All reach the same structural verdict as the vendor slice — **different altitude** (Means-layer build substrate vs governance corpus): they *compose*, not compete. Because OSS frameworks are construct-comparable, the live deltas land on the MxM component-model, OAgents typed-agent/envelope, and each framework's specialty.

| Entry | Framework | Per-axis highlight |
|---|---|---|
| [`langchain-langgraph.md`](langchain-langgraph.md) | LangChain / LangGraph | Cross-reference → [`../vendor-stacks/langchain.md`](../vendor-stacks/langchain.md) (primary treatment); LangGraph = OSS heart of the orchestration comparison |
| [`openhands.md`](openhands.md) | OpenHands (ex OpenDevin) | Autonomous coding harness — external SOTA mirror of the Hermetic exemplar; AIDE behind on realized sandboxed runtime/adoption |
| [`autogen.md`](autogen.md) | AutoGen (Microsoft) | **Maintenance-mode** — converged into MS Agent Framework (→ vendor-stacks/microsoft); preserved as paradigm-of-record |
| [`crewai.md`](crewai.md) | CrewAI | Role/Crew/Task/Process; role↦Mission, backstory↦Persona; no envelope/authority |
| [`llamaindex.md`](llamaindex.md) | LlamaIndex | Event-driven **Workflows** converge with ADR-EA-0027 (neither enforces the ⊑ lattice); retrieval-strong |
| [`smolagents.md`](smolagents.md) | smolagents (HF) | CodeAgent (code-as-action); ~1000 LOC, governance left entirely to the integrator |
| [`letta.md`](letta.md) | Letta (ex MemGPT) | **The inversion** — AIDE genuinely *behind* on realized memory mechanics; `.af` = interop seam under the Memory construct |
| [`dspy.md`](dspy.md) | DSPy | Declarative LM programming → Mind/Methods; clean **catch-up** slice on systematic prompt-optimization |
| [`pydanticai.md`](pydanticai.md) | PydanticAI | **Most convergent** with OAgents' schema-first/typed-object DNA — but lacks the behavioral envelope |
| [`mastra.md`](mastra.md) | Mastra | Notable **TS-native** option (peers are Python-first); workflows + evals + memory |
| [`inspect-ai.md`](inspect-ai.md) | Inspect AI (UK AISI) | Governance-adjacent eval harness → **adopt-candidate** for the OAgents conformance/evidence tier; AIDE behind on eval-harness maturity |
| [`google-adk.md`](google-adk.md) | Google ADK | OSS-runtime angle (→ vendor-stacks/google-cloud for managed); ADK Skill L1/L2/L3 = most rigorous Skill protocol in the field |

**Two cross-slice findings worth carrying forward:** (1) **Letta** is the one framework where AIDE is behind on a *core surface* (Memory) realization — `.af` is a concrete adopt/interop seam. (2) **Inspect AI** is the eval harness the OAgents conformance tier (and the workflow-orchestration "first realized lattice") currently lacks — a catch-up/adopt Objective, not a competitor.

## Status

Scaffolding established 2026-05-22. **Twelve framework entries landed 2026-06-01** (LangChain/LangGraph [xref], OpenHands, AutoGen, CrewAI, LlamaIndex, smolagents, Letta, DSPy, PydanticAI, Mastra, Inspect AI, Google ADK). Slice is built out; refresh per-entry on framework releases (fast cadence). Hermetic remains tracked as an exemplar, not a comparator.
