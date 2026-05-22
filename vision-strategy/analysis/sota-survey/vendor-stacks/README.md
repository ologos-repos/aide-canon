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

## Status

Scaffolding established 2026-05-22. First vendor entries land in subsequent PRs.
