# Analyst frame — Gartner (Agentic AI)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Cadence: **medium** (annual flagship Hype Cycles + quarterly Predicts notes — treat figures as a dated snapshot). **Paywall:** Gartner's primary documents (the Hype Cycle for Agentic AI, the Magic Quadrants, the full Predicts notes) are subscriber-gated; this entry is built from Gartner's own public press releases + article summaries and attributed vendor redistributions, never from the gated full text. No quote or number here is invented — figures that could not be reached at their primary source are flagged as redistributor-sourced.

## 1. What it is

**Gartner** is the tier-1 industry analyst house whose categorizations set enterprise procurement vocabulary and CIO-altitude market timing. For the agentic ground this entry surveys three current (2025–2026) Gartner frames:

- **Hype Cycle for Agentic AI (2026)** — the first dedicated agentic Hype Cycle. It places **agentic AI / AI agent development platforms at the *Peak of Inflated Expectations*** with a **"High" benefit rating** and a **2–5 year time-to-mainstream-adoption**, and maps 30+ innovations across development, deployment, management, and governance phases. The defining 2026 signal is the *early* emergence of oversight-flavored profiles — **agentic AI governance**, **agentic AI security**, and **FinOps for agentic AI** — distributed across the curve rather than clustered late, indicating that accountability/control/cost discipline is being recognized as a *day-one* concern, not a post-deployment retrofit. The report names **"agent-washing"** (legacy automation/RPA rebadged as agentic) as an explicit market problem.
- **Predicts — project-cancellation note (2025-06-25).** Gartner predicts **"over 40% of agentic AI projects will be canceled by the end of 2027,"** attributing the failures to **escalating costs, unclear business value, and inadequate risk controls** — *not* to a capability ceiling. Same note: ≥15% of day-to-day work decisions made autonomously by 2028 (from 0% in 2024); 33% of enterprise applications including agentic AI by 2028 (from <1%).
- **Maturity / adoption framing.** Gartner's CIO survey data (carried in the 2026 Hype Cycle) reports **only ~17% of organizations have deployed AI agents, with 60%+ intending to within two years** — described as the most aggressive adoption curve of any emerging technology measured. The maturity dimensions Gartner organizes around are the four phase-bands above (development → deployment → management → governance), plus the explicit "deployment ≠ orchestration" caution.

Gartner sits at a **different layer** than the surveyed vendor stacks and OSS frameworks: it is a **market-categorization and timing frame**, not a product or a corpus. It tells the canon *where the market believes it is* and *what vocabulary buyers will use* — it does not itself architect anything.

## 2. Source links

- **Primary (paywalled — flagged):** Gartner, *Hype Cycle for Agentic AI* (2026), `gartner.com/en/documents/7671861` and the public summary article `gartner.com/en/articles/hype-cycle-for-agentic-ai` (both subscriber-gated for full text; HTTP 403 to anonymous fetch — summary content below is from Gartner's own public excerpts + redistributions).
- **Primary (public press release):** Gartner, *"Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027"* (2025-06-25), `gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027` — this press release is public; the 40%/2027 figure and the cost/value/risk-control attribution are verified to it.
- **Secondary (attributed redistributions — flagged):** Tray.ai, *"5 hard truths from the first-ever Agentic AI Hype Cycle"* (`tray.ai/blog/gartner-agentic-ai-hype-cycle-2026/`) — source of the development/deployment/management/governance phase mapping, the orchestration-sprawl and token-spend paraphrases (marked paraphrased by the redistributor), and the 17%/42%/22% adoption split; xpander.ai (`xpander.ai/blog/gartner-hype-cycle-for-agentic-ai-what-it-means-for-ai-agent-development-platforms`) — source of the "High benefit / 2–5 yr" rating for AI agent development platforms. Both are vendor blogs redistributing Gartner framing; treat as secondary.
- **In-canon prior research:** the SOTA-vocabulary synthesis in [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md); the trust-gap thesis in [`constructs/oagents/spec/oagents-nist-standard-v16.0.md`](../../../../constructs/oagents/spec/oagents-nist-standard-v16.0.md) §1.1.

## 3. Map against AIDE

Per the [analyst-frames AIDE-mapping anchor](README.md#aide-mapping-anchor), analyst frames map by four questions, not by the vendor-stack plane grid.

### (a) Category definitions — match / supplement / diverge?

Gartner's **"agentic AI"** is a loose market umbrella: any system that plans, uses tools, and acts with some autonomy. The canon's vocabulary is **more precise and *diverges deliberately***:

- Gartner's "AI agent" as deployed-organizational-actor ≈ the canon's **AI-aide** (the class noun for an AI assistant acting *under a principal*, [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)). The canon never uses bare "agent" for an AI-under-principal — and Gartner's undifferentiated "agentic" is exactly the collision the canon's vocabulary exists to resolve. Gartner's own **"agent-washing"** finding is the market discovering, the blunt way, that "agent" has been stretched past usefulness — which is the same diagnosis that motivated [ADR-EA-0016].
- The canon's **OAgents `Agent` primitive** (a typed object inside a behavioral envelope) is a *finer* construct than anything in Gartner's vocabulary; Gartner has no envelope concept.
- **OrdSA** authority-layering (O0–O6 authority-down / evidence-up) and **MxM** (mode/means + the 5M governance modules) have **no Gartner analogue** — Gartner's "governance" profile names the *need* without supplying the *structure*.

**Verdict: diverge (more precise).** The canon supplies terms one ordinal level below Gartner's market category.

### (b) Hype-Cycle / maturity placement vs AIDE's exemplar status

Gartner places the **market** at the Peak of Inflated Expectations (2–5 yr to mainstream). The canon **does not appear on this curve at all, and correctly so** — the Hype Cycle plots *market-traded technologies/vendors*, and **aide-canon is a governance/architecture corpus at research/exemplar stage, not a vendor or a product.** AIDE has **no market presence** to place; that is the accurate, calibrated read, not a gap to apologize for. The useful cross-read is the *content* of the curve: the early, distributed appearance of **agentic AI governance / security / FinOps** profiles is the market arriving at ground the canon already occupies by design (OAgents envelope, OrdSA authority, MxM Morals). The canon's exemplar status maps to "operationally demonstrated outside the market frame," which the Hype Cycle has no axis for.

### (c) Maturity-model dimensions vs the six AEON planes

Gartner's organizing dimensions are the four phase-bands (development → deployment → management → governance) plus orchestration and cost. Against AEON's six service planes:

| Gartner dimension | Nearest AEON plane | Note |
|---|---|---|
| Development / build | Capability composition + Integration | Gartner tracks tooling maturity; AEON tracks the **envelope-refinement composition law** Gartner has no concept of |
| Deployment / orchestration | Orchestration runtime | Gartner's "deployment ≠ orchestration; sprawl is the risk" maps directly to AEON's meta-orchestration framing |
| Management / observability | Evidence | Gartner names observability/auditability (MCP-gateway-mediated); AEON's Evidence plane is the same intent, spec-level |
| **Governance** | **Authority** + Morals (MxM) | Gartner names governance as a *profile to acquire*; AEON/OrdSA supplies it as **ordinal structure** — the sharpest divergence |
| Security | Authority + Identity | Gartner has a parallel Hype Cycle for Agentic AI **Security**; maps to AEON Identity + Authority |
| FinOps / cost | (no dedicated AEON plane) | Genuinely *AIDE behind* — cost-governance is not yet a first-class canon plane; **catch-up signal** |

Gartner's dimensions **overlap** AEON's planes on five of six, and the canon is **finer-grained** on Authority/governance while **lagging** on a dedicated cost/FinOps plane.

### (d) Named-vendor coverage (cross-ref `../vendor-stacks/`)

Gartner's agentic frames cover the same vendor population the survey tracks in [`../vendor-stacks/`](../vendor-stacks/) — Microsoft, Google Cloud, AWS, OpenAI, Anthropic, Salesforce, IBM, NVIDIA, Databricks — and the **LangChain**-class build-and-run platforms surveyed at [`../vendor-stacks/langchain.md`](../vendor-stacks/langchain.md) fall under Gartner's "AI agent development platforms" Peak-of-Inflated-Expectations entry. Gartner's lens is *market-timing per vendor*; the survey's vendor-stack entries are *architecture-altitude per vendor*. The two compose: Gartner says *when* a vendor's category matures; the vendor-stack entries say *where in the AIDE plane model* that vendor sits.

### Vision-signal check — is AIDE / OrdSA / OAgents / MxM named in analyst vocabulary?

**Honest answer: no.** As of 2026-06-01, none of **AIDE**, **OrdSA**, **OAgents**, or **MxM** appears in Gartner's published agentic vocabulary. Gartner names the *problems* the canon addresses (governance-from-day-one, agent-washing, trust/risk-control failure) but uses none of the canon's terms. This is the expected baseline for a research-stage corpus with no market presence, and it is the explicit thing the analyst-frame slice exists to **track over time** per the README's "AIDE is named in industry conversations" Vision success signal. **Baseline established: zero canon-term penetration in Gartner vocabulary, 2026-06-01.**

## 4. Relationship — agree / supplement / diverge + synthesis

- **Agree (strongly).** Gartner's headline diagnosis is the canon's founding thesis. The 40%-cancelled-by-2027 prediction attributes failure to **cost, unclear value, and inadequate risk controls — explicitly not capability.** That *is* the OAgents trust-gap thesis ([oagents §1.1](../../../../constructs/oagents/spec/oagents-nist-standard-v16.0.md): *"Model capability is improving. The barrier is trust… the central barrier to enterprise adoption"*). Gartner, independently and from market data, validates the premise the canon was built on: **agentic projects fail on governance/trust, not on model capability.** The early distributed appearance of governance/security/FinOps profiles on the Hype Cycle is the same signal a second time.
- **Supplement.** Gartner supplies what the canon lacks: **market timing** (2–5 yr to mainstream; the 17%→60% adoption curve) and **buyer vocabulary** (what CIOs will procure against). The canon should *consume* this as demand-timing evidence for VSOK objectives, and should note one genuine **lag**: Gartner's **FinOps-for-agentic** profile has no dedicated AEON plane — a real *catch-up* dimension.
- **Diverge (precision).** Where Gartner says loose **"agentic"**, the canon says **AI-aide** (under-principal, ADR-EA-0016), **OAgents `Agent`** (typed envelope object), **OrdSA** authority ordinals, **MxM** Morals. The canon's terms are one resolution level finer; Gartner's "agent-washing" finding is the market beginning to feel the absence of exactly this precision. Flag wherever Gartner's "agentic" is quoted in canon prose — it collides with the canon's precise terms and must not be adopted bare.

**Synthesis:** Gartner is a **market-timing + category-formation instrument, not a competitor and not a peer corpus.** aide-canon does not belong on a Hype Cycle (it is not a vendor); it belongs *underneath* the governance profile that Gartner says the market now urgently needs. The relationship is: **Gartner names the trust/governance gap as the #1 cause of agentic project failure; the canon is a structured answer to that exact gap** — OAgents envelope + OrdSA authority + MxM Morals as the day-one governance Gartner says cannot be deferred. The canon's job here is to (1) cite Gartner's prediction as external validation of the trust-gap thesis, (2) consume Gartner's adoption curve as demand-timing, and (3) keep its own vocabulary distinct from Gartner's loose "agentic" rather than collapse into it.

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (trust-gap validation → vision signal).** Use Gartner's 40%-cancelled-by-2027 prediction and the early governance/security profiles as the external proof point that the canon's trust-gap thesis is market-validated. **KR shape:** a cited "why-agentic-projects-fail" brief anchoring OAgents §1 to the Gartner Predicts note; and a standing **vision-signal tracker** that re-checks each annual Gartner agentic Hype Cycle for any appearance of AIDE/OrdSA/OAgents/MxM terms (baseline: zero, 2026-06-01).
2. **Catch-up (cost/FinOps plane).** Gartner's FinOps-for-agentic profile exposes a genuine canon gap — no dedicated cost-governance plane. **KR shape:** scope whether cost/FinOps becomes a first-class AEON concern or folds into the Evidence/Authority planes, and document the decision (candidate ADR).
3. **Converge-or-differentiate (vocabulary discipline).** Gartner's "agent-washing" finding is convergent evidence that bare "agent" has failed the market. **KR shape:** maintain the [vocabulary map](../../aide-vocabulary-map.md) as the canon's answer to agent-washing — precise, conformance-testable terms (AI-aide / OAgents `Agent` / OrdSA authority / MxM Means) — and flag every place canon prose risks adopting Gartner's loose "agentic."

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI (canon-prime).** Primary figures (40%/2027; Peak-of-Inflated-Expectations placement) verified to public Gartner press release / article excerpts; phase-band and adoption-split detail sourced to attributed vendor redistributions (Tray.ai, xpander.ai) and flagged as secondary. Revisit on the next annual Gartner agentic Hype Cycle (or any new Predicts note that moves the cancellation figure) and re-run the AIDE-named-in-vocabulary vision-signal check at that time.
