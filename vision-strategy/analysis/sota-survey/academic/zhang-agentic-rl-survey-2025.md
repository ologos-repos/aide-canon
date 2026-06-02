# Academic paper — Agentic Reinforcement Learning survey (Zhang et al., 2025)

> SOTA-survey finding (academic slice). Shape per [`./README.md`](README.md) → [`sota-survey/README.md`](../README.md). Cadence: **medium** (this is a living survey — arXiv v5 as of Apr 2026; treat the *taxonomy* as the stable artifact and the cited-works enumeration as a moving target). Slug uses the **2025** arXiv-first-appearance year per the slice convention (`{first-author-lastname}-{short-title}-{YYYY}`).

## 1. What it is

**"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey"** is a large synthesis (500+ works) that formalizes the shift from *LLM-RL* (RL applied to a passive sequence generator over a degenerate single-step MDP) to *Agentic RL* (an LLM as an autonomous decision-maker in a temporally extended, partially observable environment — a POMDP). Its load-bearing contribution for this canon is the **capability taxonomy**: it organizes the field around **six core agentic capabilities — planning, tool use, memory, reasoning, self-improvement, and perception** — and treats reinforcement learning as the mechanism that turns each from a static, heuristic module into adaptive, learned behavior. (A second taxonomy axis organizes the same literature by application domain — search, code, math, GUI, multi-agent, etc. — but it is the capability axis that the canon's vocabulary work cites.) This six-axis decomposition is now the field's de-facto standard answer to "what does an LLM agent *do*," which is exactly why it warrants a canon position: it is a **capability vocabulary**, and the canon must state how it relates to its own **governance** vocabulary.

**Citation (verified 2026-06-01):** Guibin Zhang, Hejia Geng, Xiaohang Yu, Zhenfei Yin, Zaibin Zhang, Zelin Tan, Heng Zhou, Zhongzhi Li, Xiangyuan Xue, Yijiang Li, Yifan Zhou, Yang Chen, Chen Zhang, Yutao Fan, Zihu Wang, Songtao Huang, Francisco Piedrahita-Velez, Yue Liao, Hongru Wang, Mengyue Yang, Heng Ji, Jun Wang, Shuicheng Yan, Philip Torr, Lei Bai. *The Landscape of Agentic Reinforcement Learning for LLMs: A Survey.* arXiv:2509.02547 (submitted 2 Sep 2025; v5 17 Apr 2026). Categories: cs.AI, cs.CL. This is the agentic-RL survey cited as **[A2]** in the canon's [vocabulary map](../../aide-vocabulary-map.md) / §5.1 SOTA-vocabulary research.

## 2. Source links

- Paper (arXiv abs): `https://arxiv.org/abs/2509.02547` · PDF: `https://arxiv.org/pdf/2509.02547` · HTML (v5): `https://arxiv.org/html/2509.02547v5`
- Hugging Face paper page: `https://huggingface.co/papers/2509.02547`
- alphaXiv discussion: `https://www.alphaxiv.org/resources/2509.02547`
- In-canon prior research: the agentic-RL row of the [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md) (cited as **[A2]**); the SOTA-vocabulary synthesis in [ng-aide-01 PR #59 §5.1](https://github.com/ologos-repos/ng-aide-01/pull/59).
- Sibling academic entry: [`yao-react-2022.md`](yao-react-2022.md) — ReAct is the upstream mechanism for two of this survey's six axes (reasoning + tool use).

## 3. Map against AIDE

The survey's six **capability** axes map onto the canon's two **governance** vocabularies — MxM's discipline surfaces ([`../../../../constructs/mxm/`](../../../../constructs/mxm/)) and the AIDEX eight-axis modularity model ([`../../../../enterprise-platforms/aidex/`](../../../../enterprise-platforms/aidex/) — presentation · persona · role · authority · context · memory · modality · lineage). The mapping is **axis-by-axis**, and the most informative result is what *fails* to map.

### Six capability axes vs. MxM surfaces vs. AIDEX axes

| Agentic-RL capability axis | MxM surface | AIDEX axis | Position |
|---|---|---|---|
| **Planning** | Mind (reason) + Methods (tradecraft) | Context (the working frame planning operates over) | *Builds-on* — canon adopts the capability; governs *whether* a plan unlocks action via the prep gate ([`prep-pursue-pivot`](../../../../patterns/prep-pursue-pivot.md)) |
| **Tool use** | Means (execution surface) | Modality (channels/affordances the aide acts through) | *Builds-on* — `Tool` = atomic invocation, convergent across the field (cf. OAgents `Tool`) |
| **Memory** | Memory (continuity) | **Memory** (direct axis match) | *Builds-on / converges* — the one axis with a 1:1 name match across all three vocabularies |
| **Reasoning** | Mind | Context | *Builds-on* — ReAct-class loop ([`yao-react-2022.md`](yao-react-2022.md)) is the mechanism; Mind is the surface |
| **Self-improvement** | Methods (graduation: practice→method→moral→means) | Lineage (provenance of what improved, and on whose authority) | *In flight elsewhere / complicates* — canon has the **governance** form (a method only graduates to enforcement under review); the survey has the **learned** form (RL self-edits weights/behavior). Self-improvement that edits behavior *without a graduation gate* is precisely what AIDK warns of |
| **Perception** | (no MxM surface — input modality, not a discipline) | Modality + Presentation | *Builds-on* — perception is an input affordance the canon places under Modality, not a governed discipline of its own |
| — *no capability axis* — | **Mission** (telos/scope) | — | **Governance-only — survey has no equivalent** |
| — *no capability axis* — | **Morals** (permissions/prohibitions/obligations) | **Authority** | **Governance-only — survey has no equivalent** |
| — *no capability axis* — | — | **Persona** | **Governance-only — survey has no equivalent** |
| — *no capability axis* — | — | **Role** | **Governance-only — survey has no equivalent** |

**The asymmetry is the finding.** Every one of the survey's six axes is a **capability** (what the AI-aide *can do*). The canon's governance axes — **Authority, Persona, Role, Lineage** (AIDEX), and **Mission + Morals** (MxM) — have **no counterpart** in the capability taxonomy. The survey enumerates capability; it does not govern it. That gap is the AIDE-ahead delta (§4).

**Terminology note.** The survey's pervasive bare **"agent"** is the field-standard usage the canon deliberately re-vocabularies: an LLM running autonomously. In canon vocabulary an LLM-under-a-principal is an **AI-aide** ([ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)); the survey's "autonomous decision-making agent" with *no principal in the loop* is the **ungoverned** form the AI-aide framing exists to discipline — flag the collision, do not adopt the term. The survey's **"tool use"** maps cleanly onto the OAgents **`Tool`** primitive (atomic invocation) — no collision. The survey has **no** construct corresponding to the OAgents **`Agent`** object (a typed entity inside a behavioral envelope): its "agent" is a *capability-bearing policy*, not an envelope-bounded entity — same-word/different-altitude, flag but not a true collision. Note also that the survey's **"memory"** (a learned capability — retrieval/state the policy maintains) and AIDEX/MxM **Memory** (a *governance* axis — what persists under whose curation) are the same word at different altitudes: capability vs. governed continuity.

## 4. Position / relationship + synthesis

**The canon builds-on the capability vocabulary and extends it with the governance axes the taxonomy lacks — and that extension is the AIDE-ahead delta.** The honest relationship is **builds-on/extends with a governance complement**, not a flat ahead/behind: the canon does not out-enumerate the survey on capability (the survey, at 500+ works, is the authoritative capability map), and it should *adopt* the six-axis vocabulary as the shared field language for "what an AI-aide can do."

The delta is structural and specific. The agentic-RL taxonomy is **capability-centric** — planning/tool-use/memory/reasoning/self-improvement/perception all answer *what can the agent do*. The canon's vocabularies answer a different, orthogonal question — *under what authority, as whom, in what role, with what lineage, toward what mission, within what permissions*:

- **Authority** (AIDEX axis; OrdSA O0–O6, [`../../../../constructs/ordsa/`](../../../../constructs/ordsa/)) — the survey's agent acts at one undifferentiated autonomy level; the canon binds every action to an ordinal authority with authority-down/evidence-up. No capability axis carries authority.
- **Persona / Role** (AIDEX axes) — the survey's agent is a faceless policy; the canon types *who* the aide presents as and *what function* it occupies. No capability axis carries identity-of-presentation or function-assignment.
- **Lineage** (AIDEX axis) — the survey's self-improvement edits behavior with no provenance gate; the canon requires a lineage trail (and, for *methods*, a graduation gate practice→method→moral→means before any improvement earns enforcement). Capability self-improvement is exactly the case where the canon's lineage governance is load-bearing.
- **Mission + Morals** (MxM surfaces) — the survey has neither a telos/scope surface nor a deontic permission surface. Capability without Mission is undirected; capability without Morals is ungated. Both are governance-only in the canon and absent from the taxonomy.

So the synthesis is the canon-spec ↔ capability-vocabulary relationship the survey records elsewhere in this slice: **the agentic-RL survey supplies the capability vocabulary; the canon supplies the governance the vocabulary structurally lacks.** The survey enumerates *what an AI-aide can do*; the canon governs *whether, as whom, under what authority, and toward what end it does it*. Per the [academic slice anchor](README.md#aide-mapping-anchor), this is the "new safety/governance argument → evaluate against HCAE explicitly" *and* the "new orchestration vocabulary → **AIDE ahead** where AIDE has the canonical vocabulary" case at once: the capability axes are shared field language to adopt, the **governance axes are the canon's own contribution**.

*Citation discipline:* the survey does not cite any AIDE artifact (it is capability-field literature, orthogonal to the governance corpus); the canon should cite it as the **authoritative source of the six-axis capability vocabulary** — the [vocabulary map](../../aide-vocabulary-map.md) [A2] anchor — and use it as the foil that makes the governance-axes delta cite-able rather than asserted. No reverse-citation signal to track yet; a future agentic-RL survey edition citing OrdSA/AIDEX/OAgents on the *governance* gap would be a Vision success signal worth watching.

## 5. Objective implication

Two Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance axes over the capability taxonomy).** The six-axis capability taxonomy is becoming the field's standard decomposition; the AIDE position is the **governance complement** — Authority/Persona/Role/Lineage (AIDEX) + Mission/Morals (MxM) — that the taxonomy provably lacks. KR shape: publish a one-page **"six capability axes × canon governance axes" crosswalk** (the §3 table, hardened) into the [vocabulary map](../../aide-vocabulary-map.md), making the "capability ≠ governance, and the canon holds the governance" claim a cite-able artifact against a named 500-work SOTA survey — the strongest available *AIDE-ahead-on-governance* evidence in the academic slice.
2. **Builds-on lineage hygiene (adopt the capability vocabulary).** The canon should speak the field's capability language where it is purely descriptive (planning/tool-use/memory/reasoning/perception), reserving its own coinages for the governance surfaces. KR shape: align the MxM/Means and OAgents capability descriptions to the survey's six-axis vocabulary (citing [A2]) so the canon **builds-on** the shared vocabulary rather than reinventing it — closing the vocabulary-provenance gap the §3 terminology note surfaces, while preserving the AI-aide / `Agent`-object distinctions ([ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) against the survey's bare-"agent" usage.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Citation independently verified against arXiv:2509.02547 (abs page author list + v5 dates) on this date. Revisit on a major new edition of this survey, a successor agentic-capability taxonomy, or at OKR refresh.
