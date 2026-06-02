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

## Landed entries

Academic work is the canon's research *lineage* — the position is usually **builds-on / extends / cites-as-lineage**, not ahead/behind. Two exceptions: the canon is honestly *behind* on the eval-benchmark surface, and *ahead* where it adds governance the paper lacks.

| Entry | Paper | Position |
|---|---|---|
| [`wang-voyager-2023.md`](wang-voyager-2023.md) | Voyager (Wang et al., TMLR 2024) | **Lineage anchor** — "skills as programs" is the academic origin of Skill↦Means; canon builds-on + adds governance |
| [`yao-react-2022.md`](yao-react-2022.md) | ReAct (Yao et al., ICLR 2023) | Builds-on/extends — prep-pursue-pivot wraps the bare reason/act loop in a governance gradient (AIDE-ahead delta) |
| [`shinn-reflexion-2023.md`](shinn-reflexion-2023.md) | Reflexion (Shinn et al., NeurIPS 2023) | HCAE call: **supports** EIF ("introspection = hypothesis, not authority") when bounded; doesn't supersede |
| [`park-generative-agents-2023.md`](park-generative-agents-2023.md) | Generative Agents (Park et al., UIST 2023) | Memory construct builds-on the memory-stream + recency/importance/relevance retrieval; rejects zero-curation |
| [`schick-toolformer-2023.md`](schick-toolformer-2023.md) | Toolformer (Schick et al., NeurIPS 2023) | Foundational to the convergent atomic-**Tool** primitive; canon adds envelope/authority |
| [`jimenez-swe-bench-2023.md`](jimenez-swe-bench-2023.md) | SWE-bench (Jimenez et al., ICLR 2024) | **AIDE behind** on eval — the measurement surface OAgents conformance lacks (catch-up) |
| [`yao-tau-bench-2024.md`](yao-tau-bench-2024.md) | τ-bench (Yao et al., 2024) | Eval-shape *closest* to envelope/Morals conformance (domain-policy adherence + pass^k) |
| [`liu-agentbench-2023.md`](liu-agentbench-2023.md) | AgentBench (Liu et al., ICLR 2024) | AIDE behind on multi-env eval breadth; capability-as-measured vs capability-as-feature |
| [`zhang-agentic-rl-survey-2025.md`](zhang-agentic-rl-survey-2025.md) | Agentic-RL survey (Zhang et al., 2025) | Six-axis capability taxonomy; canon extends with governance axes (Authority/Persona/Role/Lineage) the survey lacks |
| [`phuong-dangerous-capabilities-2024.md`](phuong-dangerous-capabilities-2024.md) | Frontier dangerous-capability evals (Phuong et al., DeepMind 2024) | HCAE call: **supports** the eval-gated human-curation thesis; surfaces the capability-vocab collision |
| [`bhardwaj-abc-2026.md`](bhardwaj-abc-2026.md) | Agent Behavioral Contracts (Bhardwaj 2026) | **Envelope lineage** — independent-convergent with OAgents (§10); ABC = within-session formal kernel, OAgents = cross-session envelope |

**Cross-slice threads worth carrying forward:** (1) the **eval cluster** — SWE-bench + AgentBench + τ-bench (measurement) ↔ Inspect AI ([oss-frameworks](../oss-frameworks/inspect-ai.md), harness) ↔ OpenHands (subject) is the OAgents-MEASURE-function toolchain the canon lacks; τ-bench's policy-adherence + pass^k is the eval-shape closest to envelope-conformance testing. (2) **ABC** is the nearest external formalization of the OAgents envelope — a peer to track for the conformance-spec lineage. (3) **Follow-up flagged:** the `aide-vocabulary-map.md` carries the skill↦Means discipline but has no Voyager-attributed lineage row, and the `[A2]`/`[A3]` register markers (agentic-RL survey, frontier-safety) aren't literal strings in the map yet — add on the next vocab-map pass.

## Status

Scaffolding established 2026-05-22. **Eleven academic-paper entries landed 2026-06-01** (Voyager, ReAct, Reflexion, Generative Agents, Toolformer, SWE-bench, τ-bench, AgentBench, agentic-RL survey, frontier dangerous-capabilities, ABC). Slice is built out; cadence is conference-cycle + continuous arXiv scan per the topical clusters above.
