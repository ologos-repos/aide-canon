# Academic paper — Reflexion: Language Agents with Verbal Reinforcement Learning (Shinn et al., 2023)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Academic-slice mapping anchor: [`academic/README.md`](README.md). Cadence: **medium** (conference-cycle; this is a settled, heavily-cited NeurIPS 2023 result — treat as a fixed landmark, not a moving snapshot).

## 1. What it is

**Reflexion** is a framework that improves a language agent's task performance through *verbal* (linguistic) self-correction rather than weight updates. After a trial fails, the AI-aide generates a natural-language self-reflection on *why* it failed, stores that reflection in an **episodic memory buffer**, and conditions subsequent attempts on the accumulated reflections — learning from trial-and-error in language rather than by gradient descent. The paper frames this as "verbal reinforcement learning": the reflective text plays the role weights play in conventional RL, and the episodic buffer is the policy store. It reports headline results including 91% pass@1 on HumanEval (vs. the then-SOTA GPT-4 baseline of 80%), with gains across sequential decision-making (ALFWorld), reasoning (HotpotQA), and code generation.

The mechanism has three couplings that matter to the canon: (a) **self-reflection** — the AI-aide introspects on its own failure and produces an account of it; (b) **episodic memory** — that account persists across trials/sessions; (c) **after-action retry** — the next attempt is steered by the stored reflection. It is an *agent-side runtime/between-trial learning loop*, not a training-time method.

**Citation (verified):** Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). *Reflexion: Language Agents with Verbal Reinforcement Learning.* Advances in Neural Information Processing Systems 36 (**NeurIPS 2023**). arXiv:[2303.11366](https://arxiv.org/abs/2303.11366).

## 2. Source links

- **Paper (arXiv):** [arxiv.org/abs/2303.11366](https://arxiv.org/abs/2303.11366) (v1 2023-03-20; v4 2023-10-10).
- **NeurIPS 2023 proceedings:** [proceedings.neurips.cc — Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf); poster [neurips.cc/virtual/2023/poster/70114](https://neurips.cc/virtual/2023/poster/70114).
- **OpenReview:** [openreview.net/forum?id=vAElhFcKW6](https://openreview.net/forum?id=vAElhFcKW6).
- **Code release:** [github.com/noahshinn/reflexion](https://github.com/noahshinn/reflexion).
- **Citation-graph note:** Reflexion builds on the ReAct reasoning/acting lineage (Yao et al., 2023; shared author Shunyu Yao) and is among the most-cited agent self-improvement papers; it is a near-universal upstream reference for "self-reflection / self-refine" agent work surveyed in this slice.

## 3. Map against AIDE

Per the [academic mapping anchor](README.md) — academic findings map most often via **foundation (HCAE/AIDK/RLEG)** and via **cross-cutting patterns**. Reflexion is a *mechanism*, so it maps cleanly to the MxM discipline surfaces and to two patterns:

| Reflexion contribution | AIDE construct / pattern | Position |
|---|---|---|
| **Verbal self-reflection** on task failure (introspective account in language) | [MxM **Mind**](../../../../constructs/mxm/) — the reasoning surface; + [epistemic-integrity-floor §4](../../../../patterns/epistemic-integrity-floor.md) "treat introspection as hypothesis" | *In flight elsewhere* — Reflexion supplies a concrete mechanism for a loop EIF already governs as *hypothesis, not authority* |
| **Episodic memory buffer** of reflections persisting across trials | [MxM **Memory**](../../../../constructs/mxm/) — cross-turn/cross-session continuity; EIF §6 ("preserve *decisions and their defeaters*, not just conclusions") | *AIDE ahead* on the governance shape — EIF §6 already specifies *what* the buffer should retain (defeater-history), which Reflexion's buffer does not constrain |
| **After-action retry** steered by stored reflection (learn → change course → re-attempt) | [prep-pursue-pivot **"pivot"**](../../../../patterns/prep-pursue-pivot.md) — the *after/at-inflection* faculty: consolidated experience → governed stay-or-change decision | *AIDE ahead* on governance — pivot wraps the same after-action learning in a **governed decision**, which Reflexion performs *ungoverned* (the agent self-pivots silently) |
| Self-correction *raises measured performance* without fine-tuning | [RLEG](../../../../foundation/rleg/) (training-time expert grounding) — Reflexion is the **runtime** sibling | *In flight elsewhere* — runtime calibration complements RLEG's train-time calibration, exactly as EIF and pivot already frame the runtime/between-session sibling relationship |

### Terminology note (canon vocabulary discipline)

Reflexion's paper-native term is **"language agent."** Per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md) the canon does **not** use bare "agent" for an AI-under-principal; this entry reads Reflexion's "language agent" as the canon's **AI-aide** and uses that term throughout. This is a read-mapping, not a claim that the paper adopts the vocabulary. No collision with the OAgents **`Agent`** primitive (the typed object inside a behavioral envelope) arises here — Reflexion has no envelope concept; its "agent" is the whole AI-aide, not a typed envelope object. Reflexion's **"memory"** is specifically an *episodic reflection buffer*, narrower than MxM **Memory** (which is the full continuity discipline: types, retention, session-boundary contract); the entry keeps the qualifier "episodic" wherever the distinction is load-bearing. No Ologos-ecosystem / NG-AIDE-01 entities are implicated by this academic finding.

## 4. Position / relationship

**In flight elsewhere, at the mechanism altitude — and the AIDE position is *governance over the mechanism*, not the mechanism itself.** Reflexion is exactly the kind of *published, public mechanism* the canon's patterns are designed to *wrap*, not re-derive: it is a working self-reflection-plus-episodic-memory loop, while aide-canon contributes the governance gradient that loop runs under. This is the same canon-spec ↔ public-mechanism relationship [prep-pursue-pivot already documents](../../../../patterns/prep-pursue-pivot.md) for its "pivot" faculty (where the underlying consolidation mechanisms are public and the AIDE contribution is the curation gate + autonomy dial + drift/poisoning safeguards).

### The HCAE call (load-bearing): does self-reflection support, complicate, or supersede HCAE's case?

The honest reading is **it complicates the naive reading of HCAE but, correctly bounded, it *supports* HCAE — as a loop UNDER human curation, not a replacement for it.** Three steps:

1. **The surface tension is real.** [HCAE](../../../../foundation/hcae/)'s thesis is the **human as the locus of judgment and accountability** — AI work is *human-curated*. Reflexion is automated self-curation: the AI-aide judges its own prior output, writes the correction, and acts on it without a human in the loop. Taken at face value, "the AI-aide curating itself" reads as a partial *displacement* of the human curator — a complication of HCAE's case.

2. **But [AIDK](../../../../foundation/aidk/) + [EIF §0/§4](../../../../patterns/epistemic-integrity-floor.md) dissolve the tension by denying self-reflection *authority*.** Reflexion's self-reflection is precisely the kind of introspective account EIF names as **"reconstruction, not verified causal trace"** (§4) and that EIF §0 flags as a structural limit: *the model lacks reliable internal access to the distinctions its self-account claims to draw.* A verbal self-reflection is a **hypothesis about its own failure**, not a validated diagnosis. Under EIF §8 the loop is meaningful only because an *external* regime (controlled comparison, primary-source check, human review) closes it — and Reflexion's own evidence is *external*: the retry's measured pass-rate, not the eloquence of the reflection, is what validates the correction. Reflexion empirically *demonstrates* EIF's premise — that introspection is a useful trigger for an externally-validated retry, not a self-certifying judgment.

3. **So the canon-correct framing is a *bounded loop under human curation*, which is what HCAE has always allowed.** HCAE never required a human to author every keystroke; it requires the human as locus of judgment *at the load-bearing decision points*. Map Reflexion onto [prep-pursue-pivot](../../../../patterns/prep-pursue-pivot.md): the self-reflection-and-retry is *pursue → pivot*, and pivot's autonomy is **dialable** — crank it down and every course-change surfaces to the human (full HCAE); open it up and the AI-aide self-pivots within pre-declared bounds and escalates at the edges. Reflexion is the **fully-opened pivot dial with no escalation rail and no defeater-preservation** — useful, but ungoverned. The AIDE position is to *re-instrument* that loop: keep Reflexion's mechanism, add (a) EIF §4 "introspection-as-hypothesis" labeling on the reflection, (b) EIF §6 defeater-history in the episodic buffer (not just "I failed, here's the fix" but the *defeater* that made the prior approach wrong), and (c) prep-pursue-pivot's escalation rail so out-of-bounds pivots surface to the human.

**Verdict: SUPPORTS (when bounded); COMPLICATES only the strawman of HCAE that equates curation with keystroke-authorship.** Reflexion does **not** supersede HCAE — it is structurally incapable of doing so, because under AIDK self-reflection cannot self-certify, so the loop *requires* an external validator (measured retry success and/or human curation) to mean anything. Reflexion is best read as **empirical corroboration of EIF**: a public, benchmarked demonstration that automated introspection is valuable precisely as an externally-validated hypothesis-generator, exactly the role EIF assigns it.

### Synthesis

Reflexion is **a public mechanism the canon governs, not a position the canon must answer.** The three couplings (self-reflection / episodic memory / after-action retry) land on three canon surfaces that *already exist and already constrain them* — MxM Mind, MxM Memory, and prep-pursue-pivot's pivot — with EIF supplying the integrity floor that turns ungoverned self-correction into governed, hypothesis-labeled, defeater-preserving, escalation-railed self-correction under HCAE. The canon is *ahead on governance shape* and *converging on the mechanism*.

## 5. Objective implication

Two Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance-over-self-correction).** Position EIF + prep-pursue-pivot as the governing spec over Reflexion-class self-reflection loops — the canon already has the vocabulary (introspection-as-hypothesis, defeater-preservation, dialable pivot, external validation) that Reflexion's bare mechanism lacks. *KR shape:* a documented "govern-a-Reflexion-loop" mapping — reflection labeled per EIF §4, episodic buffer retaining defeaters per EIF §6, retry gated by a pivot escalation rail — demonstrated on an AIDE exemplar.
2. **Converge-or-differentiate (runtime calibration).** Reflexion is the canonical published instance of *runtime* (vs. RLEG train-time) calibration. *KR shape:* cite Reflexion as the external SOTA reference when articulating the EIF-runtime / RLEG-train-time calibration pair, and differentiate explicitly on the governance wrapper (HCAE locus-of-judgment + external validation regime) that Reflexion's open-loop self-correction omits.

## 6. Date + reviewer

Surveyed **2026-06-01 by OlogosAI (canon-prime)**. Citation verified against arXiv:2303.11366 and the NeurIPS 2023 proceedings (all six authors; venue confirmed). Revisit at OKR refresh or if a successor self-reflection paper supersedes Reflexion as the slice's reference instance.
