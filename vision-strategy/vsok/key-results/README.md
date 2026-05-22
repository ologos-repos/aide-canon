# key-results/ — Key Results (v0.1)

The **Key Results** slot of [VSOK](..) within [Vision-Strategy](../..). Doerr-style quantitative measurable signals that anchor [Objectives](../objectives/) per [ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md).

> **v0.1 — strawman.** This first set of KRs is calibrated to the Objectives' v0.1 strawman state. Thresholds and measurement dates will refine as the [SOTA survey](../../analysis/sota-survey/) populates and the Objectives revise into v0.2.

## What this slot holds

Measurable outcomes that anchor [Objectives](../objectives/). Each Key Result is a concrete, observable signal — quantified threshold or pass/fail — that signals progress on its parent Objective.

Key Results are Doerr's OKR accountability layer: they make Objectives auditable without requiring deep familiarity with the corpus's argument.

## Methodology

Key Results in this slot are constructed per **John Doerr's OKR methodology** (per [ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md)). The framework's normative properties:

- **Quantitative** — measurements with concrete thresholds; never adjectives
- **Specific** — exactly one observable outcome per KR, with explicit threshold and time horizon
- **Time-bound** — each KR has a measurement date or window
- **Stretch-calibrated** — like Objectives, KRs require effort; ~70% attainment is good
- **Cardinality** — 3–5 Key Results per Objective (this v0.1: 4–5 per Objective)

KRs derive from the same SOTA-vs-AIDE gap analysis that produces Objectives. Each KR ties to observable SOTA movement: published adoptions, named citations, conformance test results, deployment milestones.

---

## O1 Key Results — *Establish AIDE as a recognized named architecture in enterprise-AI discourse*

[Parent Objective](../objectives/#o1--establish-aide-as-a-recognized-named-architecture-in-enterprise-ai-discourse)

| KR | Measurement | Threshold | Target date | Source / verification |
|---|---|---|---|---|
| **KR1.1** | Conference talks at tier-1 enterprise-AI / agentic-systems venues referencing AIDE constructs (AIDE / AEON / OrdSA / OAgents / MxM / HCAE) by name | ≥ 3 talks | 2027-Q2 | Conference programs (Gartner Symposium, Forrester events, IEEE AISummit, FAccT, NeurIPS workshops, industry equivalents); JD/team talk submissions count |
| **KR1.2** | Independent enterprise-AI blog posts or analyst notes naming AIDE constructs without prior Ologos coordination | ≥ 5 posts | 2027-Q4 | Search engine + analyst aggregator scan; coordination check via Ologos team |
| **KR1.3** | Listings of MxM / OrdSA / OAgents in tier-1 analyst publications (Gartner Hype Cycle / Forrester Wave / IDC MarketScape) — even descriptive, not endorsing | ≥ 1 listing | 2028-Q1 | Direct publication review |
| **KR1.4** | Named references in third-party YouTube/podcast technical discussions of enterprise-AI architecture | ≥ 3 references | 2027-Q4 | Manual scan + community signal |

---

## O2 Key Results — *Drive external implementation + adoption of AIDE constructs*

[Parent Objective](../objectives/#o2--drive-external-implementation--adoption-of-aide-constructs)

| KR | Measurement | Threshold | Target date | Source / verification |
|---|---|---|---|---|
| **KR2.1** | Non-Ologos enterprise stands up an AIDE-shaped reference (four-plane composition publicly described as such) | ≥ 1 deployment | 2028-Q2 | Public case study, conference talk, or blog post describing the deployment |
| **KR2.2** | Third-party OrdSA implementations on GitHub (any language/stack) citing the schema or paper | ≥ 2 impls | 2027-Q4 | GitHub search + citation graph; pull requests to `ologos-corp/ordsa-ai` count if substantial |
| **KR2.3** | OAgents-conformant agent framework or service publicly named as such | ≥ 1 framework | 2028-Q1 | Direct project README review or named declaration |
| **KR2.4** | External MxM-based harness publicly built and described in writing | ≥ 1 harness | 2028-Q2 | Public project description (GitHub README + writeup, conference paper, blog post) |
| **KR2.5** | AEON-deployed exemplar live at named enterprise target (per `analysis/exemplar-tracking/aeon-deployed/`) | Live + publicly named | 2027-Q4 | Deployment go-live announcement; canon `exemplar-tracking/aeon-deployed/` populated with deployment context |

---

## O3 Key Results — *Anchor HCAE + AIDK as load-bearing in external governance + research*

[Parent Objective](../objectives/#o3--anchor-hcae--aidk-as-load-bearing-in-external-governance--research)

| KR | Measurement | Threshold | Target date | Source / verification |
|---|---|---|---|---|
| **KR3.1** | HCAE cited (by name) in external operational governance framework, policy document, or industry-standard publication | ≥ 1 citation | 2028-Q1 | Direct framework/policy text review; NIST AI RMF profile updates, ISO/IEC adoption, IEEE EAD additions, or vendor-specific governance docs |
| **KR3.2** | AIDK referenced in external academic papers on agentic safety, LLM reliability, or AI epistemic limits | ≥ 5 papers | 2028-Q2 | Citation graph (Semantic Scholar / Google Scholar / OpenAlex on the AIDK Zenodo DOI) |
| **KR3.3** | HCAE Zenodo deposit external citations | ≥ 50 citations | 2028-Q4 | Zenodo citation tracking + Crossref / OpenAlex aggregators |
| **KR3.4** | Tier-1 analyst note (Gartner / Forrester / IDC) names "human-curated AI" or equivalent category with HCAE attribution | ≥ 1 note | 2028-Q1 | Direct analyst publication review |

---

## O4 Key Results — *Make the canon discoverable + correctly framed for external readers*

[Parent Objective](../objectives/#o4--make-the-canon-discoverable--correctly-framed-for-external-readers)

| KR | Measurement | Threshold | Target date | Source / verification |
|---|---|---|---|---|
| **KR4.1** | `aide-canon` appears in top-10 organic search results for "enterprise AI architecture canon" and "AIDE architecture" on Google + Bing | Top-10 on both queries, both engines | 2027-Q2 | Direct search snapshot (incognito; non-Ologos network) |
| **KR4.2** | AI-indexer (Perplexity / Claude / GPT / Gemini) summary of "AIDE" returns the canon URL within top-3 sources cited | Top-3 in ≥ 2 indexers | 2027-Q3 | Direct prompt test against each indexer with the query "What is AIDE in enterprise AI architecture?" |
| **KR4.3** | External citations of the canon-as-a-whole (vs. individual construct papers) on Zenodo or academic databases | ≥ 3 citations | 2027-Q4 | Citation tracking on the canon-level DOI (when deposited) + GitHub Used By aggregator |
| **KR4.4** | Canon traffic signal: external-vs-internal read-traffic proxy via GitHub clones / unique-visitor metrics | External reads ≥ 2x internal | 2027-Q3 | GitHub traffic dashboard (clones + unique visitors); cross-reference with team known-internal traffic |

---

## KR review cadence

Per [ADR-EA-0010 §3](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md), the canon's OKR cadence is:

- **Annual full refresh** — at the canon's annual review cycle; re-derives from current SOTA findings + observed KR attainment
- **Quarterly check-ins** — progress evaluation against each KR; no rewriting of Objectives or KR thresholds unless major recalibration is warranted
- **Ad-hoc revision** — major SOTA shift triggers immediate KR threshold review (e.g., a vendor announces an AIDE-incompatible direction; a standard ratifies that aligns with an AIDE construct)

KR attainment is recorded per check-in. A KR scored at 70%+ at its target date is on-track per Doerr's stretch-calibration; consistent 100% attainment signals KRs that are under-calibrated; consistent <40% signals over-calibration or strategy-execution gap (the latter is the more interesting case).

## Status

v0.1 populated 2026-05-22 from the Objectives v0.1 strawman. First quarterly check-in: 2026-Q3 (any time after 2026-09-01); annual refresh: 2026-Q4 to 2027-Q1.
