# vendor-stacks/

Survey of major enterprise AI vendor offerings — what they ship, what they call it, how it relates to AIDE's four-plane architecture.

## In scope

Tier-1 enterprise AI vendor stacks with substantive agentic / orchestration / governance offerings:

- **Microsoft** — Foundry (formerly Azure AI Studio), Copilot Studio, Semantic Kernel
- **AWS** — Bedrock + AgentCore, SageMaker, Q Developer
- **Google Cloud** — Vertex AI, Agent Builder, ADK (overlap with OSS slice)
- **Salesforce** — Agentforce, Einstein Platform
- **Databricks / Mosaic** — Agent Framework, Mosaic AI Gateway
- **IBM** — watsonx.ai, watsonx.governance, watsonx Orchestrate
- **Anthropic** — Claude enterprise / API + Agent SDK / Managed Agents
- **OpenAI** — Enterprise + Agents SDK + Operator
- **NVIDIA** — NIM / NeMo / Blueprints (selective; primarily infrastructure but agent platforms emerging)

Smaller-tier vendors enter scope when their position is materially differentiated (e.g., a niche vendor with the only credible offering on a specific AIDE plane).

## Out of scope

- Inference-only services without agentic / orchestration surface
- Pure infrastructure (cloud GPU, vector DBs) — surveyed in academic / standards slices when relevant to architecture
- AI features embedded in existing SaaS without standalone platform identity

## Per-vendor entry shape

```
vendor-{vendor-slug}/
├── README.md  (the survey entry per the shape in sota-survey/README.md)
└── (optional) screenshots/, transcripts/, vendor-comparison-tables.md
```

Or for vendors covered in a single file rather than a subdirectory:

```
{vendor-slug}.md
```

Convention: when a vendor has multiple distinct product surfaces (Microsoft Foundry vs Copilot Studio), each gets its own entry; cross-references between them surface the relationship.

## Sources to canvass per entry

- **Official product documentation** — primary
- **Recent product announcements** — last 90 days at minimum at survey time
- **Pricing + availability disclosure** — for build-or-buy classification
- **Reference customer case studies** — for "is this actually deployed?" signal
- **Independent analyst notes** — Gartner / Forrester (cross-reference to `../analyst-frames/`)
- **Engineering team writeups / external talks** — what the vendor *says* vs what its engineers reveal

## AIDE-mapping anchor

Each entry maps the vendor stack against AIDE's four planes (control / runtime / experience / capability) and the canon's six AEON service planes. The mapping makes "AIDE ahead" / "AIDE behind" / "in flight elsewhere" claims concrete rather than vibey.

Example mapping shape (for a hypothetical vendor X):

| AEON plane | Vendor X equivalent | AIDE position |
|---|---|---|
| Identity | Vendor's identity-as-a-service offering | *In flight elsewhere* — similar primitives, different governance model |
| Authority | (vendor lacks this concept) | *AIDE ahead* — OrdSA's authority-altitude vocabulary is missing |
| Evidence | Vendor's audit / observability tier | *Behind* — vendor's per-call trace is richer than AIDE's current emit-only spec |
| ... | | |

This forces every entry to engage AIDE specifically, not produce vendor summaries that float without AIDE context.

## Landed entries

All entries reach the same structural verdict — **different altitude** (build-and-run platform vs governance corpus): they *compose*, they don't compete. The per-axis deltas are what differ.

| Entry | Vendor stack | Per-axis highlights |
|---|---|---|
| [`langchain.md`](langchain.md) | LangChain Enterprise (LangChain / LangGraph / LangGraph Platform / LangSmith / Fleet) | AIDE ahead on authority/envelope/governance; behind on runtime/eval-tooling (LangSmith)/adoption |
| [`microsoft.md`](microsoft.md) | Microsoft Foundry · Copilot Studio · Agent Framework · Agent 365 | AIDE-distinctive = governance-of-behavior+authority vs MS's shipped governance-of-access (Agent 365 / Foundry Control Plane GA) |
| [`aws.md`](aws.md) | Bedrock · **AgentCore** (Runtime/Policy/Identity/Memory/Observability) · Q · Nova | **AgentCore Policy (Cedar)** = strongest *shipped* deterministic enforcement of any vendor — narrows the Morals-enforcement gap |
| [`google-cloud.md`](google-cloud.md) | Gemini Enterprise Agent Platform (ex Vertex) · ADK · Agent Runtime | Real governance *surface* (cryptographic agent identity); ADK Skill = most rigorous Skill protocol in the field |
| [`salesforce.md`](salesforce.md) | Agentforce · Atlas Reasoning Engine · Einstein Trust Layer | Trust Layer = real *content-safety* guardrails (in-flight), but no deontic/authority/envelope layer |
| [`databricks.md`](databricks.md) | Mosaic AI Agent Framework · Agent Bricks · Unity (AI) Gateway · MLflow 3 · Unity Catalog | Unity Catalog best-in-class on **data** governance; AIDE leads on **ordinal authority + envelope** (distinct axes) |
| [`ibm.md`](ibm.md) | watsonx.ai · **watsonx.governance** · watsonx Orchestrate | **The nuanced one** — genuine AI-governance product → AIDE *not cleanly ahead*; in-flight/partial-parity, AIDE-ahead narrowed to per-action envelope + ordinal authority |
| [`anthropic.md`](anthropic.md) | Claude (Enterprise) · Agent SDK · Skills · Claude Code · MCP | Most **convergent** — canon adopts SKILL.md verbatim; the substrate the canon's *own* exemplars (Claude Code Workflow, thinx-aidex) run on |
| [`openai.md`](openai.md) | ChatGPT Enterprise · Agents SDK · AgentKit · Responses/Apps SDK | **No Skill primitive** (behavior on `instructions`); single-vendor-locked → AIDE ahead on Inference-plane portability |
| [`nvidia.md`](nvidia.md) | NIM · NeMo (+ Guardrails, Agent Toolkit) · Blueprints | INFRASTRUCTURE altitude — **NIM ↦ AEON Inference plane** is the decisive map; NeMo Guardrails = partial envelope component |

## Status

Scaffolding established 2026-05-22. **All ten in-scope vendor entries landed 2026-06-01** (LangChain, Microsoft, AWS, Google Cloud, Salesforce, Databricks, IBM, Anthropic, OpenAI, NVIDIA). Slice is built out; refresh per-entry on vendor product shifts (fast cadence — most carry rebrand-proneness notes).
