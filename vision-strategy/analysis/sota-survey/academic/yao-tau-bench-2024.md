# Academic paper — τ-bench (Yao et al., 2024): Tool-Agent-User interaction + domain-policy adherence

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Cadence: **medium** (conference-cycle; benchmark itself is versioned — treat leaderboard numbers as a dated snapshot, the *shape* of the eval as the durable finding). **Governance-adjacent special case:** τ-bench is an *evaluation benchmark*, not an agent-build framework — it does not build AI-aides, it **measures** whether an AI-aide follows a domain's policy under live user interaction, reliably. It is therefore mapped primarily against **OAgents conformance** + **MxM Morals**, and the central finding is that its two signature dimensions — **policy adherence** and **pass^k reliability** — are the academic eval-shape *closest* to testing an OAgents behavioral envelope.

## 1. What it is

**τ-bench** ("tau-bench") is a benchmark for **tool-agent-user interaction in real-world domains**, introduced by Sierra researchers. Where most agent benchmarks score a single-shot task against a ground-truth answer, τ-bench evaluates an AI-aide across a **dynamic, multi-turn conversation** with a *user simulated by a language model*, while the AI-aide uses domain-specific API tools (read + write) and must obey **domain policy guidelines** (the rules a human agent in that domain would be bound by). Two domains ship: **retail** and **airline**. Scoring is **state-based** — at conversation end, the benchmark compares the resulting database state against an annotated goal state, so the AI-aide is graded on *outcome correctness under the policy*, not on transcript similarity.

Two contributions make it load-bearing for the canon:

- **Domain-policy adherence as a first-class scored dimension.** Tasks are constructed so that the only way to reach the correct end-state is to follow the domain's rules during the interaction (e.g. verify identity before mutating an order, apply the cancellation/refund policy correctly). The benchmark therefore measures *rule-following under interaction*, not raw capability.
- **The `pass^k` reliability metric.** Beyond `pass@1`, τ-bench reports `pass^k` — the probability that an AI-aide succeeds on **all k** independent trials of the same task. This exposes *consistency/determinism* as a distinct axis from average success: even strong models (GPT-4o at the 2024 snapshot) score below 50% `pass@1` and degrade sharply under `pass^k` (retail `pass^8` below 25%). High average capability with low `pass^k` means the behavior is not reproducible — exactly the failure mode an enterprise trust argument cares about.

**Exact citation (verified 2026-06-01):** Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan. *"τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains."* 2024. arXiv:2406.12045.

**Follow-up (verified):** Victor Barres, Honghua Dong, Soham Ray, Xujie Si, Karthik Narasimhan. *"τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment."* 2025. arXiv:2506.07982. τ²-bench extends τ-bench from a *single-control* setting (only the AI-aide acts on the world) to a **dual-control** setting where the *user also wields tools* in a shared, dynamic environment (modeled as a Dec-POMDP), adding a **telecom troubleshooting** domain and a compositional task generator; it inherits and extends the policy-adherence + reliability framing. Authorship overlaps τ-bench only at Narasimhan — do not attribute τ²-bench to the τ-bench author list.

## 2. Source links

- Paper (τ-bench): [arXiv:2406.12045](https://arxiv.org/abs/2406.12045).
- Follow-up (τ²-bench): [arXiv:2506.07982](https://arxiv.org/abs/2506.07982); code at [`github.com/sierra-research/tau2-bench`](https://github.com/sierra-research/tau2-bench) (the repo now hosts both τ-bench and τ²-bench).
- Author affiliation: Sierra ([sierra.ai](https://sierra.ai)).
- In-canon adjacency — the **harness** half of this finding: the eval-engine that would *run* a τ-bench-style policy-adherence suite is surveyed in [`../oss-frameworks/inspect-ai.md`](../oss-frameworks/inspect-ai.md) (Inspect AI as the candidate OAgents conformance harness). τ-bench supplies the *eval shape*; Inspect supplies the *harness*. Adjacent benchmark scoping in [`README.md`](README.md) (Conformance + evaluation cluster).
- In-canon target — OAgents conformance/evidence model: [`OAgents-v1.0 §6`](../../../../constructs/oagents/spec/versions/OAgents-v1.0.md) (evidence-by-observable-artifact, three verification levels). Deontic-constraint construct: [MxM](../../../../constructs/mxm/) (Morals surface).

## 3. Map against AIDE

### Against the four AIDE constructs (DEA / OrdSA / MxM / OAgents)

| AIDE construct | τ-bench equivalent | AIDE position |
|---|---|---|
| **DEA** (deployable enterprise architecture) | (none — τ-bench scores an interaction, it does not architect a deployment) | *AIDE ahead* — construct-unaware |
| **OrdSA** (O0–O6 authority altitudes) | (none — τ-bench has no authority/principal-altitude model; "policy" is a flat domain rulebook, not an authority lattice) | **AIDE ahead** — authority altitude is outside τ-bench's scope |
| **MxM** (5-surface harness; **Morals** = deontic constraints) | **domain-policy adherence** — the scored dimension that asks "did the AI-aide follow the domain's rules under interaction?" | **AIDE behind** on the *executable test*; **conceptually convergent** — policy adherence is the closest academic analogue to **Morals conformance**. See §4. |
| **OAgents** (typed envelope + conformance) | **the whole benchmark** — τ-bench measures *behavioral conformance under interaction*, which is precisely what an OAgents envelope claims to constrain; `pass^k` measures the *reliability* OAgents requires | **AIDE behind** on a built, runnable conformance suite; **complementary, not competing** — τ-bench is the eval-shape closest to probing an envelope. See §4. |

### Against the six AEON service planes

| AEON plane | τ-bench equivalent | AIDE position |
|---|---|---|
| **Identity** | the simulated *user* is a counterpart, not a principal/identity model | *AIDE ahead* — out of scope for the benchmark |
| **Authority** | (none) | **AIDE ahead** — OrdSA O0–O6 authority-down/evidence-up is absent |
| **Evidence** | state-based scoring + `pass^k` reliability statistics = a *graded evidence artifact* about behavior | **AIDE behind** — τ-bench *produces and grades* behavioral evidence; AIDE's evidence trail is emit-only spec |
| **Integration** | per-domain API tool sets (read + write) the AI-aide invokes | *In flight elsewhere* — domain-tool harness, narrower than a general integration plane |
| **Capability composition** | multi-turn tool use under a user-simulator loop | *In flight elsewhere* — composes *to test*, not to enforce an **envelope-refinement** composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | the eval-run loop (agent ↔ user-simulator ↔ tools ↔ DB-state check) | *In flight elsewhere* — a test-time runtime, not an operating runtime |

*(Inference is AEON's 7th plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md): τ-bench runs over arbitrary model providers, but model-agnosticism is a convenience of the harness, not a first-class **governance** property the way the Inference plane frames it.)*

### Vocabulary / terminology note

τ-bench's **"agent"** is the AI under test acting on a user's behalf within a domain — in canon terms an **AI-aide** (an AI acting under a principal, per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)), **not** the OAgents **`Agent`** primitive (a typed object inside a behavioral envelope). Reading τ-bench's "agent" as the OAgents `Agent` is the casual-"agent" collision the canon prohibits — flag on read. τ-bench's **"policy"** = a flat per-domain rulebook the AI-aide must obey; this maps to the canon's **MxM Morals** *content* (deontic constraints) but **not** its *structure* — Morals are authority-anchored (which principal's rules, at which OrdSA altitude), whereas a τ-bench domain policy is altitude-flat. The mapping is conceptual-shape, not structural-equivalence; preserve the distinction. τ-bench's **"user"** is an LLM-simulated counterpart, **not** a principal in the OrdSA sense — no authority flows from it.

## 4. Position / relationship + synthesis

**Mixed — "AIDE behind on the executable eval; ahead on governance altitude," and the two are complementary.** τ-bench is a benchmark and aide-canon is a governance corpus — *different categories at different altitudes* — so the classification is per-axis:

- **AIDE ahead** — Authority (OrdSA O0–O6), the authority-anchored *structure* of deontic constraint (MxM Morals are tied to a principal at an altitude; a τ-bench policy is a flat rulebook), and the principal/Identity model (τ-bench's "user" is a simulated counterpart, not a principal). τ-bench is, by design, authority-unaware: it scores rule-following, not *whose* rules at *what* altitude.
- **AIDE behind** — the **executable conformance eval itself**. This is the honest, decisive gap and the headline of this finding: τ-bench is a real, peer-recognized benchmark that *runs* a policy-adherence + reliability test, while OAgents conformance is, today, an asserted checklist with no harness to run it. As with the [Inspect AI](../oss-frameworks/inspect-ai.md) and [LangSmith](../vendor-stacks/langchain.md) findings, AIDE is behind on built measurement, not on conceptual position.
- **In flight elsewhere** — multi-turn tool-use mechanics and user-simulation loops; convergent test-time machinery AIDE can consume rather than rebuild.

**The synthesis — τ-bench is the eval-shape closest to testing an OAgents behavioral envelope; adopt the shape, run it on the canon's harness.** Two of τ-bench's design choices line up almost exactly with what the canon's trust argument needs to *measure*:

1. **Policy adherence ≈ envelope/Morals conformance.** τ-bench asks the single question OAgents and MxM Morals exist to answer operationally: *does the AI-aide follow the domain's rules while interacting with a user?* That is the behavioral-envelope conformance question stated as an executable eval. No surveyed academic benchmark is closer to probing an OAgents envelope — most score capability (can it?) where τ-bench scores governed behavior (does it follow the rules while doing it?). The gap to close is structural, not conceptual: τ-bench's policy is altitude-flat; an OAgents/Morals eval would additionally need to bind each rule to a principal at an OrdSA altitude.
2. **`pass^k` reliability ≈ the determinism/repeatability the canon's evidence values.** The canon's evidence discipline prizes reproducible, repeatable behavior — a one-off pass is weak evidence of a governed envelope. `pass^k` formalizes exactly that: it rewards *consistent* rule-following across independent trials and penalizes lucky single passes. It is the quantitative shape of "the envelope holds every time," which is what conformance-by-evidence should demand.

Concretely, the canon should treat τ-bench as the **eval-shape donor** and [Inspect AI](../oss-frameworks/inspect-ai.md) as the **harness**: encode policy-adherence checks as Inspect `Task`s/`Scorer`s, score them with a `pass^k`-style reliability statistic, and bind each policy rule to an OrdSA altitude so the eval measures *Morals conformance* rather than flat rule-following. This is the [`feedback_enforcement_not_documentation`] discipline applied to behavioral conformance — a reliability-scored policy-adherence suite is enforcement; an Appendix-C checklist is documentation. τ-bench supplies the *what to measure*; Inspect supplies the *how to run it*; OAgents + OrdSA + MxM supply the *altitude and envelope* the benchmark itself does not model. Note the boundary clearly: **τ-bench measures whether behavior follows a flat domain policy; it confers neither authority altitude (OrdSA) nor a runtime envelope (OAgents)** — those remain AIDE-distinctive, sitting *above* the benchmark, the same canon-spec ↔ Means-substrate relation the canon documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/).

## 5. Objective implication

Two Doerr-style Objective shapes follow — both *catch-up/adopt*, not compete:

1. **Catch-up by adoption (the headline).** Adopt τ-bench's **policy-adherence + `pass^k`** eval-shape as the template for an executable **OAgents/MxM-Morals conformance suite**. *Objective:* make "the behavioral envelope holds, reliably" measurable rather than asserted. KR shape: encode a domain's Morals as policy-adherence `Task`s on the [Inspect AI](../oss-frameworks/inspect-ai.md) harness, score with a `pass^k`-style reliability statistic, bind each rule to an OrdSA altitude, and produce a graded conformance report on an AIDE exemplar ([Hermetic](../../exemplar-tracking/hermetic/) / [thinx-aidex](../../exemplar-tracking/thinx-aidex/)). Pairs with the Inspect finding as the *eval-shape* half of the same conformance-harness program.
2. **Defend-and-extend (governance altitude over the benchmark).** Articulate that a τ-bench score measures rule-following but confers neither authority (OrdSA) nor a runtime envelope (OAgents), and that the canon's contribution is the **altitude-anchored** upgrade: policy bound to principal-at-altitude rather than a flat rulebook. KR shape: a documented "score-an-OAgent's-Morals-conformance" mapping that extends τ-bench's flat-policy model with OrdSA authority binding, bounding what a behavioral eval can and cannot certify.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Citations verified 2026-06-01 against arXiv:2406.12045 (τ-bench) and arXiv:2506.07982 (τ²-bench follow-up). Pairs with [`../oss-frameworks/inspect-ai.md`](../oss-frameworks/inspect-ai.md): τ-bench is the *eval-shape*, Inspect the *harness*, OAgents/OrdSA/MxM the *altitude + envelope*. Revisit on a τ²-bench domain/leaderboard shift or at OKR refresh.
