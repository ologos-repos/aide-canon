# academic/

Survey of recent academic work on agentic systems, enterprise-AI architecture, and conformance research.

## In scope

**Topical clusters:**

- **Agentic-systems architecture** — papers on multi-agent orchestration, agent identity, agent-to-agent communication, agent-tool interfaces
- **LLM-agent foundations** — papers on tool use, planning, reasoning, self-reflection
- **Conformance + evaluation** — agent benchmarks, harness evaluations, capability assessments (SWE-bench, AgentBench, TAU-bench, OSWorld, etc.)
- **Enterprise AI architecture** — papers on AI governance, AI risk frameworks, AI-native enterprise design
- **AI safety / alignment** with architectural implications — interpretability, monitoring, controllability at deployment scale
- **HCI for AI** — human-AI collaboration patterns, AI-assisted workflow design (overlap with HCAE)

**Venues to track:**

- **Conferences** — NeurIPS, ICLR, ICML, ACL, EMNLP (ML); CHI, CSCW (HCI); FAccT, AIES (governance)
- **Workshops** — agent-focused workshops at major venues
- **arXiv** — pre-prints in cs.AI / cs.MA / cs.CL / cs.HC categories
- **Industry research labs** — Anthropic, DeepMind, OpenAI, Meta AI publications

## Out of scope

- Pure ML / training methodology papers without architectural or governance implications
- Papers on specific application domains (medical AI, legal AI) unless they engage agentic architecture generally
- Theoretical papers without operational connection to deployment

## Per-entry shape

```
{topic-slug}/
├── README.md  (topic overview + tracking)
└── {paper-slug}-{YYYY}.md  (per-paper entry)
```

Or for single-paper tracking:

```
{paper-slug}-{YYYY}.md
```

Use `{first-author-lastname}-{short-title}-{YYYY}` as the slug convention (e.g., `wei-react-2022.md` style).

## Sources to canvass per entry

- **Paper PDF + arXiv link**
- **Code release** (if applicable)
- **Author thread / blog post** explaining the paper informally
- **Citation graph** — what does the paper cite, and what cites it
- **Follow-up work** by the same authors / groups
- **Implementations / replications** by third parties

## AIDE-mapping anchor

Academic findings map to AIDE most often via foundation (HCAE, AIDK, RLEG) and via cross-cutting patterns. The mapping captures:

| Paper contribution | AIDE construct / pattern | Position |
|---|---|---|
| New evaluation benchmark | OAgents conformance criteria / future patterns/ | *Behind* if AIDE has no equivalent surface; *In flight elsewhere* if benchmark targets a surface AIDE is also developing |
| New orchestration pattern | MxM / OrdSA / patterns/ tier | *AIDE ahead* if AIDE has the canonical vocabulary; *In flight elsewhere* if independently derived |
| New safety / governance argument | HCAE / foundation tier | Evaluate against HCAE's argument explicitly — does the paper support, complicate, or supersede HCAE's case? |
| New training methodology | RLEG / foundation tier | Compare to RLEG's "expert grounding" framing |

## Citation discipline

Academic-slice entries are also potential citation surfaces for the canon's own published work. Track which academic findings *cite AIDE artifacts* — citations of HCAE / AIDK / OrdSA / OAgents / MxM in external academic work is a Vision success signal.

## Cadence sensitivity

Conference-cycle: NeurIPS / ICLR papers cluster around their submission deadlines + acceptance announcements. arXiv has continuous flow. Survey passes align: monthly arXiv scan for the topical clusters above; deeper read at major conference acceptance windows (typically twice a year).

## Status

Scaffolding established 2026-05-22. First academic entries land in subsequent PRs.
