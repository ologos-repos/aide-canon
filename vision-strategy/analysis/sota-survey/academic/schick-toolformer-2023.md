# Academic — Toolformer (Schick et al., NeurIPS 2023)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Mapping anchor: academic findings map to AIDE via **foundation** (HCAE / AIDK / RLEG) + **constructs / patterns** (see [`README.md` § AIDE-mapping anchor](README.md)). Cadence: **slow** — a settled 2023 foundational paper, not a moving product; revisit only when a successor reframes the tool-use primitive itself.

## 1. What it is

**Toolformer** is a self-supervised method for teaching a language model to use external tools through API calls. The model learns, in a self-supervised loop, *which* APIs to call, *when* to call them, *what arguments* to pass, and *how* to fold the returned results back into next-token prediction — needing only a handful of human demonstrations per API. The training data is **model-self-annotated**: the LM samples candidate API calls inline in text, executes them, and keeps only the calls whose results measurably reduce the loss on the following tokens (a perplexity-filtered, self-generated dataset). The demonstrated toolset spans a calculator, a Q&A system, a search engine, a translation system, and a calendar. The headline result is that a 6.7B-parameter model fine-tuned this way improves zero-shot downstream performance — in places matching far larger models — **without degrading core language-modeling ability**.

Toolformer is foundational research, not a framework or product. Its lasting contribution to the field is establishing that **tool-use is a learnable capability of the base model itself**, acquired from self-supervision rather than hand-wired into an external orchestration layer. It is one of the canonical origin points for what the field now calls the **Tool** primitive: an *atomic invocation* the model emits and consumes inline.

**Exact citation.** Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom. "Toolformer: Language Models Can Teach Themselves to Use Tools." *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, oral presentation. arXiv:2302.04761 (submitted 9 Feb 2023). Meta AI Research.

## 2. Source links

- **Paper (arXiv):** `https://arxiv.org/abs/2302.04761` (PDF: `https://arxiv.org/pdf/2302.04761`)
- **NeurIPS 2023 proceedings:** `https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html`
- **OpenReview (reviews + decision):** `https://openreview.net/forum?id=Yacmpz84TH`
- **Semantic Scholar (citation graph / what-cites-it):** `https://www.semanticscholar.org/paper/53d128ea815bcc0526856eb5a9c42cc977cb36a7`
- **In-canon prior research:** the **Tool** primitive and the `Agent`/`Skill`/`Tool` vocabulary convergence in [`aide-vocabulary-map.md`](../../aide-vocabulary-map.md); the OAgents envelope / behavioral-trust framing in [`constructs/oagents/`](../../../../constructs/oagents/).

## 3. Map against AIDE

Toolformer touches a single, sharply defined point in the AIDE stack — the **Tool** primitive — and is silent above it. The mapping is therefore narrow-but-deep, not broad.

### Against the foundation + capability surface

| Toolformer contribution | AIDE construct / plane / pattern | Position |
|---|---|---|
| **Tool-use as a learned model capability** (self-supervised API invocation) | AEON **Capability** plane (OAAD) — the surface that *supplies* invocable capability ([ADR-EA-0015 frames Inference as the 7th plane](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md)) | *In flight elsewhere → AIDE builds-on* — Toolformer is the convergent field definition of the primitive AIDE governs, not duplicates |
| **The `Tool` primitive** = atomic invocation the model emits/consumes | Canon **Tool** = atomic invocation (convergent across the field; see [`aide-vocabulary-map.md`](../../aide-vocabulary-map.md)) | *Convergent* — Toolformer is foundational to this exact definition; the canon **extends** it with governance, it does not redefine it |
| **Self-supervised acquisition of the capability** (perplexity-filtered self-annotation) | RLEG foundation — "expert grounding" of capability ([`foundation/rleg/`](../../../../foundation/rleg/)) | *In flight elsewhere* — Toolformer grounds capability in self-supervision; RLEG frames grounding in expert evidence. Complementary acquisition stories, same target |
| **No authority / envelope / deontic layer** over which tools fire or whether they *should* | MxM **Means** (execution substrate) under **Morals**; OAgents behavioral **envelope**; OrdSA authority ([`constructs/mxm/`](../../../../constructs/mxm/), [`constructs/oagents/`](../../../../constructs/oagents/), [`constructs/ordsa/`](../../../../constructs/ordsa/)) | **AIDE ahead** — this is the load-bearing delta (see § 4) |
| **No human-curation / operator experience** model around tool invocation | HCAE foundation — operator-as-curator ([`foundation/hcae/`](../../../../foundation/hcae/)) | **AIDE ahead** — Toolformer is fully autonomous self-annotation; HCAE supplies the human-curation argument it has no concept of |

### Terminology note

Per canon vocabulary discipline ([ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)):

- **Tool** — Toolformer's "tool / API call" maps cleanly to the canon **Tool** primitive (*atomic invocation*). No collision: this is the convergent field definition, and Toolformer is one of its foundational sources. The canon inherits the term as-is.
- **"agent"** — the paper does not market itself as an "agent" system, and this entry does **not** import that framing. Where the AI invoking tools acts under a principal it is an **AI-aide** (ADR-EA-0016), never a casual "agent"; the OAgents **`Agent`** is a typed object inside a behavioral envelope — a distinct construct Toolformer has no analogue for.
- **No entity conflation** — Toolformer is external Meta AI research. It is not an Ologos-ecosystem component and not an NG-AIDE-01 component; no "fleet" reading applies. It is lineage, surveyed as such.

## 4. Position / relationship + synthesis

**AIDE builds-on (and extends) — convergent at the primitive, ahead at the governance layer.**

Toolformer and aide-canon are at **different altitudes on the same column**. Toolformer establishes that a model can *learn the capability to invoke a Tool*; aide-canon governs *Tool invocation under a behavioral envelope and an authority structure*. The canon does not re-derive Toolformer's result — it **builds on** the now-convergent **Tool** primitive that Toolformer is foundational to, and **extends** it with the layer Toolformer structurally omits.

The delta is precise and decisive:

- **Toolformer learns tool-use capability but has no governance over it.** The self-supervised loop optimizes a single criterion — *does this API call lower the loss on the next tokens?* There is no notion of *whether the call is permitted*, *under whose authority it fires*, *whether it falls inside the AI-aide's behavioral envelope*, or *whether a human principal sanctioned it*. The model decides autonomously, from self-annotated data, with no deontic gate.
- **That governance layer is exactly the canon's contribution.** MxM **Means** is the substrate on which Tool calls execute — but Means is subordinate to **Morals** (the deontic constraints on what may fire) and operates inside the OAgents behavioral **envelope** (the typed-object boundary that bounds what an `Agent` may do), under **OrdSA** authority (authority-down / evidence-up over *who may authorize* the invocation). HCAE supplies the human-curation argument over the whole thing.

So the **AIDE delta = Tool calls under a behavioral envelope + authority**, not the bare ability to make Tool calls. Toolformer answers *"can the model learn to call APIs?"* (yes, self-supervised). The canon answers the orthogonal question Toolformer never poses: *"under what authority, inside what envelope, subject to what deontic constraints, with what human curation, may a tool call fire?"*

**The synthesis:** they **compose, not compete** — the same canon-spec ↔ substrate relationship the survey documents for build-and-run platforms, now at the foundational-research altitude. Toolformer (or any successor self-supervised tool-use method) supplies the *Capability* — a model that knows *when/how* to invoke a Tool. The canon wraps that capability in the envelope + authority + Morals + HCAE-curation it has no concept of. Toolformer is upstream lineage for the Tool primitive; the canon is the governance tier that sits above it.

## 5. Objective implication

Two Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance over the Tool primitive).** Toolformer is the canonical demonstration that *capability acquisition is solved-and-convergent at the model layer* while *governance over invocation is absent*. Propagate the position that the canon's value is precisely the envelope + authority + deontic gate over Tool calls — the layer self-supervised tool-use does not and cannot supply from a perplexity objective. KR shape: a documented "govern-a-Toolformer-class-capability" mapping — Tool invocation routed through OAgents envelope + OrdSA authority + MxM Morals, with the perplexity-only acquisition criterion shown as orthogonal to (and silent on) the governance criteria.
2. **Converge-or-differentiate (capability grounding).** Toolformer grounds capability in *self-supervision*; RLEG grounds it in *expert evidence*. Articulate the relationship explicitly rather than treat them as rivals. KR shape: an RLEG note positioning self-supervised tool-use acquisition as a complementary grounding source the foundation tier can sit above, differentiated by RLEG's expert-grounding argument where autonomy-only acquisition is insufficient.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime).
