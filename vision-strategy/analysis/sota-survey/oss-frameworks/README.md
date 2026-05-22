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

## Status

Scaffolding established 2026-05-22. First framework entries land in subsequent PRs.
