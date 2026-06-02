# Academic paper — ReAct (Yao et al., 2022 / ICLR 2023)

> SOTA-survey finding (academic slice). Shape per [`./README.md`](README.md) → [`sota-survey/README.md`](../README.md). Cadence: **medium** (conference-cycle; foundational paper — treat as a stable lineage anchor, not a moving target). Slug retains the **2022** arXiv-first-appearance year per the slice convention (`{first-author-lastname}-{short-title}-{YYYY}`); the paper was published at **ICLR 2023**.

## 1. What it is

**ReAct ("Reason + Act")** is the foundational prompting paradigm that interleaves *reasoning traces* and *task-specific actions* in a single language-model loop, rather than treating reasoning (e.g. chain-of-thought) and acting (e.g. action-plan generation) as separate capabilities. The model emits a **thought → action → observation** cycle: a reasoning step induces/tracks/updates a plan and handles exceptions; an action step interfaces with an external source (a knowledge base, tool, or environment); the resulting observation feeds the next thought. The synergy is the contribution — reasoning makes acting more deliberate and grounded; acting makes reasoning verifiable against the world (reducing hallucination/error propagation versus reasoning-only chain-of-thought). The paper reports gains on knowledge-intensive QA/fact-verification (HotpotQA, FEVER) and on interactive decision-making benchmarks (ALFWorld +34% absolute success vs. imitation/RL baselines, WebShop +10%), with only one or two in-context exemplars.

**Citation (verified 2026-06-01):** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao. *ReAct: Synergizing Reasoning and Acting in Language Models.* arXiv:2210.03629 (6 Oct 2022; v3 10 Mar 2023). Published at **ICLR 2023** (OpenReview `WE_vluYUL-X`).

## 2. Source links

- Paper (arXiv abs): `https://arxiv.org/abs/2210.03629` · PDF: `https://arxiv.org/pdf/2210.03629`
- ICLR 2023 (OpenReview): `https://openreview.net/forum?id=WE_vluYUL-X`
- Code (author release): `https://github.com/ysymyth/ReAct`
- Author/lab explainer: Google Research blog — `https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/`
- In-canon prior research: the **prep-pursue-pivot** pattern names its own reproduced-mechanism provenance (Claude Code plan mode / `/goal`, Managed-Agents Outcomes) — see [`../../../../patterns/prep-pursue-pivot.md`](../../../../patterns/prep-pursue-pivot.md) §"Reproducibility and source concepts"; ReAct is the upstream academic ancestor of the during-action loop that pattern governs.

## 3. Map against AIDE

ReAct is a **reasoning-and-tool-use loop** — a Mind-tier mechanism, not a governance construct. It maps to the foundation tier (the reasoning/reliability question) and to the MxM **Mind** + **Methods** surfaces, and most precisely to the **prep-pursue-pivot** pattern's *pursue* faculty.

| ReAct contribution | AIDE construct / pattern | Position |
|---|---|---|
| Interleaved thought→action→observation loop (the core paradigm) | [`prep-pursue-pivot`](../../../../patterns/prep-pursue-pivot.md) — the *pursue* faculty (drive-while-acting) | **AIDE builds-on, then extends** — canon adopts the loop and wraps it in a governance gradient (below) |
| Reasoning traces that "induce, track, update plans + handle exceptions" | MxM **Mind** (how the system reasons) — see [`../../../../constructs/mxm/`](../../../../constructs/mxm/) | *Builds-on* — Mind is the canon surface this faculty lives on |
| Acting via external sources (knowledge bases / tools / environments) | MxM **Methods** (tradecraft / how acting is done) + the *prep* decomposition | *Builds-on* — ReAct is the reasoning+acting mechanism Methods codifies as disciplined practice |
| Grounding reasoning against observations to reduce hallucination | Foundation: [`AIDK`](../../../../foundation/aidk/) (AI is structurally unreliable) → loop-grounding as one mitigation | *Builds-on / complicates* — ReAct **partially** addresses AIDK's premise (grounding reduces error) but does **not** govern the loop; the residual reliability gap is exactly what HCAE/the governance gradient closes |
| Plan-then-act legibility of the trace (auditable thoughts/actions) | Foundation: [`HCAE`](../../../../foundation/hcae/) human-curation; [`../../../../patterns/digital-thread.md`](../../../../patterns/digital-thread.md) (trace as audit record) | **AIDE ahead** — ReAct's trace is *interpretable* but ungated; canon turns the trace into a *curation + audit surface* |

**Terminology note.** ReAct's "agent" is the canonical bare-loop usage the canon deliberately re-vocabularies: an LM-under-no-principal running a reasoning/acting cycle. In canon vocabulary this is an **AI-aide** when placed under a principal ([ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)); the bare ReAct loop is precisely the *ungoverned* form that motivates the AI-aide framing. ReAct's **"action"** (a single tool/environment call) maps cleanly to the OAgents **`Tool`** primitive (atomic invocation) — no collision. ReAct has no construct corresponding to the OAgents **`Agent`** object (a typed entity inside a behavioral envelope); the paper's "ReAct agent" is a *prompting strategy*, not an envelope-bounded entity — flag this as a same-word/different-altitude distinction, not a true collision.

## 4. Position / relationship + synthesis

**The canon builds-on ReAct and extends it with a governance gradient — that is the AIDE-ahead delta.** ReAct is upstream lineage: it is *the* foundational reasoning-plus-tool-use pattern, and every during-action loop in the canon (most directly **prep-pursue-pivot**'s *pursue*) is a descendant of it. The honest relationship is **builds-on/extends**, not ahead/behind — the canon does not out-reason ReAct, it *governs* the loop ReAct named.

The delta is specific and load-bearing. The bare ReAct loop has **uniform, ungoverned autonomy**: thought→action→observation runs at one autonomy level with no human-curation gate, no decoupled evaluator, and no governed decision point. prep-pursue-pivot **extends** this exact loop with a three-step governance gradient the bare paradigm lacks:

- **prep — APPROVE** — before the act loop unlocks, an inspectable plan + inchstone decomposition passes a human-curation gate (HCAE front gate). ReAct has no plan-approval boundary; it acts on the first thought.
- **pursue — BOUNDED AUTONOMY** — the ReAct loop *is* pursue, but with a **decoupled evaluator** (separate context) judging "done" via evidence-up, so completion is not self-certified. Bare ReAct self-terminates from inside its own trace.
- **pivot — GOVERNED DECISION** — at a course-change inflection, the system surfaces a stay-or-change decision (human-choose or policy-authorized, dialable), recording resolver + reason. Bare ReAct silently continues or stops with no governed inflection.

So the synthesis is the same canon-spec ↔ mechanism relationship the survey records elsewhere: **ReAct supplies the during-action mechanism; AIDE supplies the governance the mechanism structurally lacks.** ReAct made acting *interpretable*; the canon makes the interleaved loop *governed* — auditable via the [digital-thread](../../../../patterns/digital-thread.md), gated via [HCAE](../../../../foundation/hcae/), authority-bounded via the pivot modes ([OrdSA](../../../../constructs/ordsa/) authority-down/evidence-up). Per the [academic slice anchor](README.md#aide-mapping-anchor), this is the "new orchestration pattern → **AIDE ahead** where AIDE has the canonical vocabulary" case: the loop is shared lineage, the **governance gradient is the canon's own contribution**.

*Citation discipline:* ReAct does not cite any AIDE artifact (it predates the canon by years); the lineage runs the other way — the canon's during-action faculty *descends from* ReAct and should cite it as ancestor. No reverse-citation signal to track here.

## 5. Objective implication

Two Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance gradient over the reason-act loop).** ReAct is the universally-adopted during-action mechanism; the AIDE position is the *governed* loop on top of it. KR shape: ship the prep-pursue-pivot **behavioral-conformance** check (prep approval gate + decoupled pursue evaluator + governed pivot, all emitting to the digital-thread) on an AIDE exemplar, demonstrated against a plain ReAct-style loop as the ungoverned baseline — making the "governance gradient is the delta" claim cite-able rather than asserted.
2. **Builds-on lineage hygiene (Methods/Mind provenance).** ReAct is the honest academic ancestor of the *pursue* faculty; the [prep-pursue-pivot reproducibility table](../../../../patterns/prep-pursue-pivot.md) currently sources *pursue* from product mechanisms (`/goal`, Managed-Agents Outcomes) without naming their academic root. KR shape: add ReAct (Yao et al., ICLR 2023) as the cited academic ancestor of *pursue* in the pattern's provenance table — closing a citation-discipline gap surfaced by this survey.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Citation independently verified against arXiv:2210.03629 and ICLR 2023 / OpenReview `WE_vluYUL-X` on this date. Revisit on a major ReAct follow-up (e.g. a successor paradigm from the same authors) or at OKR refresh.
