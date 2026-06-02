# Analyst frame — CB Insights (agentic-AI market maps)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Frame type: **analyst** — mapped via the AIDE-mapping anchor in [`README.md`](README.md). Cadence: **medium** (market maps refresh every few months; treat company counts as a dated snapshot). Lens caveat: CB Insights is a **market-intelligence / funding** house, not a maturity-model analyst — its categories are an *investment* lens, lighter analytical depth than Gartner/Forrester. Calibrate accordingly.

## 1. What it is

**CB Insights** is a market-intelligence platform that tracks private-company funding, M&A, and competitive landscapes, and publishes **market maps** — visual taxonomies that sort startups into categories. Its agentic-AI coverage is a family of such maps: the **AI agent market map** (400+ companies across ~16 categories, drawn from a tracked universe of 1,700+), the **AI agent tech stack** (135+ companies across seven infrastructure layers), the **enterprise AI agents & copilots** map, the **agentic commerce** map, and the annual **AI agent predictions** note. The organizing logic throughout is **where capital and revenue are concentrating** — companies are admitted by a proprietary "Mosaic" health/growth score, infrastructure-only players are filtered out, and the categories are named after *go-to-market segments* (coding, customer service, security operations, sales, healthcare & life sciences, etc.), not after architectural primitives.

Crucially, this is a **funding lens, not an architecture**. The categories are fuzzy and investment-driven: they describe *what the market is buying and funding right now* (horizontal vs. verticalized agents, who is exiting via M&A, which segments are minting unicorns), and they re-draw themselves as money moves. The value to the survey is therefore **adoption-phase and investment-timing signal** — a read on where the market is in its formation cycle — not a maturity model or a conformance vocabulary. aide-canon, by contrast, is a governance **corpus** at research/exemplar stage, not a venture-backed product, so it does not appear on (and is not the kind of thing that *would* appear on) a CB Insights map at all.

**Paywall note:** market-map images and headline findings (counts, top-segment names, a handful of revenue/M&A signals) are public; full company rosters, Mosaic scores, and the bulk of the predictions notes are gated behind a CB Insights subscription. All figures below are from the public summaries — none are invented, and the gated detail is not reconstructed here.

## 2. Source links

- **AI agent market map** — `cbinsights.com/research/ai-agent-market-map-2025/` *(headline findings public; full roster paywalled)*
- **AI agent tech stack** — `cbinsights.com/research/ai-agent-tech-stack/` *(seven-layer frame public; company detail paywalled)*
- **5 AI agent predictions for 2026** — `cbinsights.com/research/ai-agent-predictions-2026/` *(prediction 1 public; predictions 2–5 paywalled)*
- **Agentic commerce market map** — `cbinsights.com/research/report/agentic-commerce-market-map/` *(paywalled)*
- **AI / market-map research indexes** — `cbinsights.com/research/artificial-intelligence/`, `cbinsights.com/research/market-map/`
- (Counts and segment names are snapshot-dated to mid-2026 public summaries; verify at read time — CB Insights re-publishes these maps every few months and the taxonomy shifts with funding flows.)

## 3. Map against AIDE

### Category definition — match / supplement / diverge

CB Insights defines an "AI agent" operationally as **a fundable company whose primary product is an autonomous-or-assistive software agent for a market segment**. Against the canon-mapping anchor this is **diverge**: it is a *market-segment* definition (who you sell to), where the canon's vocabulary is *architectural* (what governs the entity). The collision is the field-standard one — CB Insights' bare **"agent"** spans both senses the canon separates: the persistent organizational entity (canon **AI-aide**, per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) **and** the typed primitive inside a behavioral envelope (OAgents `Agent`). This entry holds the canon discipline: per ADR-EA-0016 the casual **"agent"** is read as **AI-aide** wherever it denotes the deployed organizational entity, and the collision is flagged rather than inherited. The AIDE vocabulary is **strictly more precise** than the funding-lens category — but precision is not what a market map is for, so this is a difference of *purpose*, not a defect to close.

### Market-map placement vs. AIDE exemplar status

There is **no placement to map** — and that is the honest finding. A CB Insights map is a roster of venture-funded private companies sorted by capital signal; aide-canon is a governance corpus at **research/exemplar** stage (operationally evidenced by [Hermetic](https://github.com/ologos-repos/aide-canon) and the AEON-deployed exemplars, not by a funding round). The two are not on the same axis. What the map *does* supply is the **adoption-phase backdrop** against which AIDE's exemplar status reads: the market is in explosive category-formation (universe grew from ~300 to thousands of agent companies; "1 in 5 new unicorns" building agents; 54%+ of the customer-service segment founded since 2023). That is precisely the window in which a vendor-neutral governance vocabulary is *not yet* a named category — and the signal that one is being demanded.

### Taxonomy dimensions vs. the six AEON planes

CB Insights' **AI agent tech stack** (its most architectural frame) defines seven layers. Mapped to the AEON service planes:

| CB Insights tech-stack layer | AEON plane | Relationship |
|---|---|---|
| Foundation Models & Infrastructure | (Inference, ADR-EA-0015) | Partial — CB Insights treats models as a *supply* layer, not a governance property |
| Agent Frameworks & Dev Platforms | Capability composition | Overlap — but framework-as-vendor-segment, no envelope-refinement composition law |
| Tool Integration (incl. MCP) | Integration | Overlap — convergent on MCP |
| Context (memory, vector DBs) | (cross-cuts Identity / Evidence) | Partial — "context" is a product category, not an authority/evidence concept |
| Orchestration | Orchestration runtime | Overlap |
| **Oversight** (auth, security, monitoring, governance) | **Identity + Authority + Evidence** *collapsed into one* | **Diverge — AIDE ahead.** CB Insights folds identity, authority, monitoring and governance into a single "Oversight" bucket; the canon separates **Identity**, ordinal **Authority** (OrdSA O0–O6), and **Evidence** as distinct planes |
| Payments Infrastructure | (none) | CB Insights tracks autonomous-payments as a funded segment; no AEON analogue, and no canon claim there |

The decisive divergence is **Oversight**: the funding lens has discovered that "governance/security/monitoring" is an investable layer, but treats it as **one undifferentiated category**. The canon's contribution is exactly the *decomposition* CB Insights does not make — Identity ≠ Authority ≠ Evidence, with OrdSA supplying authority-down/evidence-up structure the market has not yet named.

### Named-vendor coverage (cross-ref `../vendor-stacks/`)

CB Insights' maps cover the funded-startup tier; the canon's [`../vendor-stacks/`](../vendor-stacks/) entries cover the major platform vendors. Overlap is partial and asymmetric:

- **[LangChain](../vendor-stacks/langchain.md)** — appears in CB Insights' *Agent Frameworks & Dev Platforms* layer; the canon's vendor-stack entry analyzes it at far greater architectural depth (per-plane, vocabulary-collision).
- **[Anthropic](../vendor-stacks/anthropic.md)**, **[OpenAI](../vendor-stacks/openai.md)** — sit in CB Insights' *Foundation Models & Infrastructure* layer (model suppliers), and as agent-platform players elsewhere.
- The hyperscaler stacks the canon tracks — **[AWS](../vendor-stacks/aws.md)**, **[Google Cloud](../vendor-stacks/google-cloud.md)**, **[Microsoft](../vendor-stacks/microsoft.md)**, **[NVIDIA](../vendor-stacks/nvidia.md)**, **[Databricks](../vendor-stacks/databricks.md)**, **[IBM](../vendor-stacks/ibm.md)**, **[Salesforce](../vendor-stacks/salesforce.md)** — are mostly *incumbents* on CB Insights' maps (the "copilots" map), against which the agent-native startups are positioned.
- **Where CB Insights adds coverage the vendor-stacks do not:** the long tail of agent-native private companies (Sierra, Cursor/Anysphere, Replit, Decagon, etc.) and the M&A/exit signal layer — useful as *adoption evidence*, not as architecture to map plane-by-plane.

### Vision-signal check — is AIDE / OrdSA / OAgents / MxM in analyst vocab?

**No — honestly, not yet.** None of **AIDE**, **OrdSA**, **OAgents**, or **MxM** appears in any CB Insights agentic-AI map, category definition, or predictions note surveyed here. This is the expected null result for a funding-lens house at this market phase: CB Insights names *companies and capital flows*, and the canon is neither a company nor a funded category. The tracked Vision success signal ("AIDE is named in industry conversations") is therefore **unmet** in this frame — recorded as a baseline, not a gap to spin. What *is* present is the adjacent demand signal: CB Insights independently surfaced "Oversight" (governance/security/monitoring) as an investable layer and named agent observability/eval and continuous red-teaming as 2026 M&A and standardization targets — the market converging on the *problem* the canon vocabulary addresses, without yet reaching for the canon's *terms*.

## 4. Relationship + synthesis

**Different instruments, complementary readings — the relationship is market-timing + category-formation signal, not competition.** CB Insights and aide-canon do not occupy the same ground: one is a *funding telescope* pointed at private companies, the other a *governance corpus* defining vocabulary and conformance. They cannot be "ahead" or "behind" each other on a shared axis, so the survey's three-way classification ([`sota-survey/README.md`](../README.md)) applies only obliquely — the load-bearing read is **signal extraction**, not head-to-head placement.

Three things the CB Insights frame tells the canon:

1. **Adoption phase.** The agentic market is in explosive, capital-driven category-formation (300 → thousands of agent companies; verticalization surging; coding and customer-service segments leading revenue). This is the **pre-standardization window** — the canon's research/exemplar timing is *early but on-trend*, not late.
2. **The market is independently discovering the governance layer — without the vocabulary.** CB Insights' "Oversight" tech-stack layer, plus its 2026 predictions naming agent **observability/eval as M&A targets** and **continuous red-teaming as standard**, are the funding-side echo of exactly what OAgents (behavioral envelope / trust), OrdSA (authority), and MxM Morals (deontic constraints) specify — but collapsed into one undifferentiated investable bucket. **The AIDE vocabulary is more precise than the funding-lens category map**: it decomposes "Oversight" into Identity / Authority / Evidence as distinct planes, which the money has not yet learned to price separately.
3. **Investment-timing, not maturity rigor.** Because CB Insights is market-intelligence (Mosaic scores, M&A probabilities) rather than a maturity-model house, its signal is *where money is flowing and what is about to exit* — high value for **timing** the canon's defend/converge moves, low value for evaluating architectural maturity. The deeper maturity-model read belongs to the Gartner/Forrester entries this slice will also carry; this entry is calibrated to its lighter analytical weight.

The synthesis: CB Insights answers *"is the market ready, and where is the capital?"* — and the answer (explosive formation, governance/oversight emerging as a fundable-but-undifferentiated layer) is the timing argument for propagating the canon's more-precise vocabulary **now**, before the funding lens hardens a fuzzy "Oversight" category into the field's default mental model.

## 5. Objective implication

Two Doerr-style Objective shapes follow ([`sota-survey/README.md`](../README.md) classifications):

1. **Defend-and-extend (vocabulary precision, market-timing-driven).** CB Insights has independently surfaced "Oversight" as an investable layer but left it undifferentiated. KR shape: publish a crisp **"Oversight is three planes, not one"** mapping (Identity / Authority-via-OrdSA / Evidence) positioned against the funding-lens collapse — propagate the more-precise canon decomposition into the window *before* the market's fuzzy category sets, citing CB Insights' own tech-stack frame as the contrast.
2. **Converge-or-differentiate (Vision-signal tracking).** The "AIDE is named in industry conversations" signal is baselined **absent** here. KR shape: track, refresh-over-refresh, whether AIDE / OrdSA / OAgents / MxM enter *any* analyst-frame vocabulary (CB Insights included) — with this entry as the t=0 null, and the adjacent "Oversight / agent-eval / red-teaming" demand signals as the leading indicators to watch.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Lens: CB Insights = market-intelligence / funding, not maturity-model — calibrated as adoption-phase + investment-timing signal. All figures from public summaries; gated detail not reconstructed. Revisit on the next CB Insights agentic-map republication (every few months) or at OKR refresh.
