# Academic paper — AgentBench: Evaluating LLMs as Agents (Liu et al., ICLR 2024)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Cadence: **medium** (conference-cycle; the paper is a fixed published artifact, but the benchmark's *standing* shifts as newer multi-environment eval suites land — treat leaderboard/result specifics as a dated snapshot). **Eval-tooling special case:** AgentBench is a *benchmark*, not an agent-build framework — it does not build AI-aides, it **measures** what an LLM can do when driven as an agent across distinct environments. It is therefore mapped primarily against **OAgents conformance** and the **Evidence plane**, and it sits in the canon's eval-tooling cluster alongside [Inspect AI](../oss-frameworks/inspect-ai.md) (the harness) and SWE-bench-class task benchmarks.

## 1. What it is

**AgentBench** is the first multi-environment benchmark for quantitatively evaluating large language models *as agents* — i.e. as decision-makers driven through multi-turn, interactive tasks rather than as single-shot text predictors. It comprises **8 distinct environments**: five newly constructed by the authors — Operating System (OS), Database (DB), Knowledge Graph (KG), Digital Card Game (DCG), and Lateral Thinking Puzzles (LTP) — and three compiled from prior published datasets — House-Holding (HH, from ALFWorld), Web Shopping (WS, from WebShop), and Web Browsing (WB, from Mind2Web). The central empirical finding is a sharp capability gap: top commercial LLMs act competently as agents in complex environments, while open-source models up to 70B parameters lag substantially, with the bottlenecks attributed to **poor long-term reasoning, decision-making, and instruction-following**. The paper is the canonical reference point for the proposition that *agentic capability is a measurable, multi-dimensional property of a model* — distinct from, and not reducible to, benchmark scores on static QA.

**Exact citation (verified 2026-06-01):** Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, Jie Tang. *AgentBench: Evaluating LLMs as Agents.* International Conference on Learning Representations (**ICLR**) **2024**. arXiv:**2308.03688** (v1 2023-08-07; v2 2023-10-25). Affiliations: Tsinghua University, The Ohio State University, UC Berkeley.

## 2. Source links

- Paper: [arXiv:2308.03688](https://arxiv.org/abs/2308.03688) ([PDF](https://arxiv.org/pdf/2308.03688)); [ICLR 2024 proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9df36b21ff4ee211a8b71ee8b7e9f57-Abstract-Conference.html); [OpenReview](https://openreview.net/forum?id=zAdUB0aCTQ).
- Code: [`github.com/THUDM/AgentBench`](https://github.com/THUDM/AgentBench) (the 8-environment harness + tasks).
- In-canon adjacency: the OAgents conformance/evidence model in [`OAgents-v1.0 §6`](../../../../constructs/oagents/spec/versions/OAgents-v1.0.md) (Conformance, Evidence, and Certification Path — three levels + the Appendix C checklist), and the eval-tooling cluster sibling [`../oss-frameworks/inspect-ai.md`](../oss-frameworks/inspect-ai.md) (the harness that could *run* AgentBench-class environments as conformance Tasks).

## 3. Map against AIDE

Per the academic-slice [mapping anchor](README.md#aide-mapping-anchor): academic findings map most often via **foundation** (HCAE / AIDK / RLEG) and via **constructs / patterns**. AgentBench is an **evaluation benchmark**, so the anchor's first row applies — *behind if AIDE has no equivalent surface*.

### Against the four AIDE constructs (DEA / OrdSA / MxM / OAgents)

| AIDE construct | AgentBench equivalent | AIDE position |
|---|---|---|
| **DEA** (deployable enterprise architecture) | (none — AgentBench scores a model's behavior, it does not architect a deployment) | *AIDE ahead* — AgentBench is construct-unaware |
| **OrdSA** (O0–O6 authority altitudes) | (none — an environment score confers no authority; it measures task success) | **AIDE ahead** — authority altitude is wholly outside AgentBench's scope |
| **MxM** (5-surface harness) | the 8-environment task harness is a *measurement* harness, not an *operating* harness | *In flight elsewhere* — comparable rigor of decomposition, orthogonal purpose |
| **OAgents** (typed envelope + conformance) | AgentBench is a **capability benchmark**; OAgents conformance is a **behavioral-envelope** check. AgentBench answers *can the model do the task?*; OAgents answers *was the behavior governed?* | **AIDE behind on eval breadth** — the canon has conformance *criteria* ([`OAgents-v1.0 §6`](../../../../constructs/oagents/spec/versions/OAgents-v1.0.md)) but **no multi-environment harness** to exercise them — see §4 |

### Against the foundation tier + the Evidence plane

| Surface | AgentBench equivalent | AIDE position |
|---|---|---|
| **HCAE** (foundation) | (none — AgentBench measures *model* agentic capability, not human-AI collaboration quality) | *AIDE ahead* — HCAE's argument is outside the benchmark's frame |
| **RLEG** (foundation, "expert grounding") | AgentBench's failure analysis (long-horizon reasoning / instruction-following gaps) is *evidence for* the problem RLEG addresses, not a competing method | *Supports* — cite as corroborating the capability gap RLEG targets |
| **Evidence plane** (AEON) | the per-environment success-rate scoring and trajectories | **AIDE behind** — AgentBench *generates and grades* agentic-capability evidence across 8 environments; AIDE's evidence trail is emit-only spec with no multi-env harness to produce it |

### Terminology / vocabulary collision note

AgentBench's **"agent"** = *an LLM driven through a multi-turn interactive environment to a scorable outcome* — a **capability test scaffold**. This is **neither** the canon's **AI-aide** (an AI acting under a principal, per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) **nor** the OAgents **`Agent`** primitive (a typed object inside a behavioral envelope). Collapsing "AgentBench agent" into either is the casual-"agent" error the canon prohibits — name it an *AgentBench task-agent / capability scaffold*. The most load-bearing collision is on **capability** itself: AgentBench measures **capability-as-measured** — *what the model demonstrably accomplishes across environments* — which is a distinct sense from the canon's **capability-as-feature** (the Capability plane / OAAD sense of a *governed affordance an AI-aide is granted*). Same word, two altitudes: AgentBench observes capability empirically; the canon *confers and bounds* it architecturally. Flag this on read — an AgentBench score says nothing about whether a capability was authorized, enveloped, or evidenced under a principal.

## 4. Position / relationship

**Classification: AIDE behind — on eval breadth, specifically.** AgentBench is a published academic benchmark and aide-canon is a governance corpus on the foundation tier — *different categories at different altitudes* — so, as with the other eval-tooling findings, the classification is per-axis:

- **AIDE ahead** — Authority (OrdSA O0–O6), the behavioral envelope / trust layer (OAgents — AgentBench measures *whether the model succeeds*, it does not *constrain* behavior at runtime or assign an authority altitude), deontic constraints (MxM Morals), HCAE, and the principal/Identity model. AgentBench is, by construction, governance-blind: it scores task completion, not whether the behavior was permitted.
- **AIDE behind** — **eval breadth**. This is the honest, decisive gap and the headline of this entry: AgentBench is a real, rigorous, broadly-cited multi-environment capability benchmark (8 environments spanning OS, DB, KG, games, puzzles, household, web shopping, web browsing). The canon, by contrast, holds **conformance *criteria*** ([`OAgents-v1.0 §6`](../../../../constructs/oagents/spec/versions/OAgents-v1.0.md) — three levels + the Appendix C checklist) but possesses **no multi-environment harness** to exercise an AI-aide across diverse interactive settings and grade the result. The canon can *specify* what conformance evidence must look like; it cannot yet *produce* breadth-of-environment evidence.
- **In flight elsewhere** — the *measurement of agentic capability* as a research program (AgentBench, SWE-bench, TAU-bench, OSWorld and successors) is actively evolving; the canon can consume its environments and scoring rather than rebuild them.

**Synthesis — consume, don't compete; and the eval-tooling cluster is the route.** AgentBench supplies *environments and capability scoring*; [Inspect AI](../oss-frameworks/inspect-ai.md) supplies the *harness* (Tasks / Solvers / Scorers, Agent Bridge, sandboxed execution) that can run such environments reproducibly; OAgents §6 supplies the *conformance semantics* (evidence by observable artifact, three verification levels) those measurements should feed. The three compose into AIDE's missing eval surface: AgentBench-class **environments**, run through an Inspect-class **harness**, scored against OAgents **conformance criteria** — turning the Appendix C checklist into an executable, multi-environment suite. The critical boundary to keep sharp: AgentBench measures **capability-as-measured** (did the task-agent succeed?); the canon governs **capability-as-feature** under a principal (was the affordance authorized, enveloped, evidenced?). An AgentBench score is an *input* to the OrdSA evidence-up trail, never a substitute for authority-altitude or envelope enforcement — exactly the canon-spec ↔ Means-substrate relation the canon documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/).

**Citation-discipline note (per the academic-slice README):** AgentBench does *not* cite any AIDE artifact — it predates and is orthogonal to the canon — so it is a *source* finding, not an external-citation success signal. Cite it precisely (ICLR 2024 / arXiv:2308.03688); do not overstate its scope (it is a *capability* benchmark, not a governance or safety-conformance benchmark) and do not attribute to it any envelope/authority claim it does not make.

## 5. Objective implication

Two Doerr-style Objective shapes follow — both *catch-up*, on the eval-breadth axis:

1. **Catch-up by adoption (the headline).** Close the multi-environment eval-breadth gap by *consuming* AgentBench-class environments rather than authoring our own. *Objective:* make OAgents conformance executable across diverse interactive settings, not just asserted on a checklist. KR shape: run a representative subset of AgentBench environments (e.g. OS, DB, WB) through the [Inspect AI](../oss-frameworks/inspect-ai.md) harness against a reference AI-aide, with Scorers that bind **capability-as-measured** (task success) to **OAgents §6** behavioral-envelope checks (independent-review-present, enforcement-gate-fires, evidence-emitted), and produce a graded report on an AIDE exemplar ([Hermetic](../../exemplar-tracking/hermetic/) / [thinx-aidex](../../exemplar-tracking/thinx-aidex/)).
2. **Defend-and-extend (governance altitude over the benchmark).** Articulate that an AgentBench score measures capability but confers neither authority (OrdSA) nor a runtime envelope (OAgents) — position the canon as the governance layer that *consumes* benchmark output (capability evidence feeds the evidence-up trail) rather than being ranked by it. KR shape: a documented "what a capability benchmark can and cannot certify" mapping that fixes the **capability-as-measured vs capability-as-feature** distinction in canon vocabulary, keeping authority-altitude and envelope-enforcement explicitly on the AIDE side of the line.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Citation verified against [arXiv:2308.03688](https://arxiv.org/abs/2308.03688) and the [ICLR 2024 proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9df36b21ff4ee211a8b71ee8b7e9f57-Abstract-Conference.html). Pairs with [`../oss-frameworks/inspect-ai.md`](../oss-frameworks/inspect-ai.md) as the harness half of the eval-tooling cluster; revisit when a successor multi-environment benchmark materially supersedes AgentBench's standing, or at OKR refresh.
