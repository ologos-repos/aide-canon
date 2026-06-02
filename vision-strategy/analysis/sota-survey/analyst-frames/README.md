# analyst-frames/

Survey of tier-1 industry-analyst categorizations and assessments of the enterprise-AI / agentic ecosystem.

## In scope

**Tier-1 analyst houses:**

- **Gartner** — Hype Cycles (Agentic AI, Generative AI, Enterprise AI), Magic Quadrants, Predicts notes, CIO-altitude framings
- **Forrester** — Wave reports for AI platforms, agentic AI maturity models, Total Economic Impact studies
- **IDC** — MarketScapes, AI / agent market forecasts
- **CB Insights** — startup market maps, agentic AI category definitions

**Adjacent firms (selective inclusion):**

- **HFS Research** — agentic / AI services category
- **Constellation Research** — agentic AI category coverage
- **Omdia** — AI infrastructure + platform tracking
- **GigaOm** — AI Radar reports

## Out of scope

- Vendor-commissioned analyst content unless the assessment is independent
- Pure financial-market analyst notes (Goldman, Morgan Stanley etc.) without agentic-architecture content
- Marketing-tier "industry surveys" without analytical rigor

## Access challenge

Most tier-1 analyst content is paywalled. The survey approach:

1. **Public summaries** — analyst firms often publish category overviews + Hype Cycle entries publicly even when full reports are gated
2. **Vendor-redistributed reports** — vendors often license reports to redistribute; check vendor sites for verbatim Gartner / Forrester content
3. **Quote-level capture** — surveyed material is summarized with explicit attribution; verbatim quotes only with clear citation
4. **Independent verification** — analyst category claims (e.g., "Agentic AI is at Peak of Inflated Expectations") are noted with the analyst's framing but evaluated against AIDE's view of the same ground

## Per-entry shape

```
{firm-slug}/
├── README.md  (firm overview + tracking)
└── {report-slug}-{YYYY-Q}.md  (per-report entry)
```

Or for single-report tracking:

```
{firm-slug}-{report-slug}-{YYYY-Q}.md
```

## Sources to canvass per entry

- **Original analyst publication** — primary
- **Vendor redistributions** — secondary; flag the redistributor
- **Analyst commentary on social channels** — direction-of-travel between formal publications
- **Conference presentations** — Gartner Symposium, Forrester events
- **Press coverage / interviews** with analyst authors

## AIDE-mapping anchor

Analyst frames map differently than vendor stacks or OSS frameworks. The relevant questions:

| Frame element | AIDE relationship |
|---|---|
| Category definitions (e.g., what is "agentic AI") | Does AIDE's vocabulary match, supplement, or diverge? |
| Hype Cycle / maturity placement | Where does AIDE's *exemplar status* land vs. the analyst's "production readiness" view? |
| Maturity-model dimensions | Do the analyst's evaluation dimensions overlap with AIDE's six AEON planes? |
| Named-vendor coverage | Which AIDE-mapped vendor stacks does the analyst cover and how? |

Analyst frames are particularly useful for the **"AIDE is named in industry conversations"** Vision success signal — analyst-frame entries should track whether AIDE / OrdSA / OAgents / MxM appear in analyst vocabulary over time.

## Cadence sensitivity

Analyst content is medium-cadence: annual flagship reports (Hype Cycles, Magic Quadrants) + quarterly research notes + ad-hoc analyst commentary. Survey passes align: annual deep read of flagship publications, quarterly check on notable notes.

## Landed entries

Analyst frames are **market lenses, not architecture** — and AIDE correctly **does not appear** in any Hype Cycle / Wave / MarketScape (it's a research/exemplar-stage governance corpus, not a vendor). The value is **market-timing + category-formation** signal, and the recurring finding that the *governance category is forming as a market* validates the canon's trust-gap thesis.

| Entry | Firm | Signal for the canon |
|---|---|---|
| [`gartner.md`](gartner.md) | Gartner | Hype Cycle (agentic AI at Peak of Inflated Expectations) + **>40% of agentic projects cancelled by 2027** (cost/value/risk, *not* capability) — validates the OAgents trust-gap thesis; "agent-washing" ↔ the canon's vocab-precision argument |
| [`forrester.md`](forrester.md) | Forrester | 2026 governance turn ("hype to hard hat", GRC Wave, **AEGIS** six agentic-security dimensions — the best market mirror of the AEON planes); "agentic" enters as a scoring criterion, no standalone agent Wave |
| [`idc.md`](idc.md) | IDC | Unified AI-**governance** MarketScape (Microsoft Leader) = the governance category formed *as a market*; spending forecast = the adoption-phase clock; canon's per-action altitude is finer than the org-level governance rewarded |
| [`cb-insights.md`](cb-insights.md) | CB Insights | Funding/market-map lens; independently surfaced **"Oversight"** as an investable layer but collapses Identity/Authority/Evidence into one bucket where AIDE's vocab is precise |
| [`adjacent-firms.md`](adjacent-firms.md) | HFS · Constellation · Omdia · GigaOm | Roundup (selective-inclusion); "agentic" category forming with **no governance-altitude dimension** across all four |

**The Vision-signal baseline (load-bearing for this slice):** as of 2026-06-01, **zero** penetration of AIDE / OrdSA / OAgents / MxM in any tier-1 or adjacent analyst vocabulary. This is the honest nil baseline for the "AIDE is named in industry conversations" success signal — track it rising over time. The convergent market signal across all five firms — *the governance/oversight/trust category is forming, and capability is not the bottleneck* — is exactly the ground the canon's thesis claims; the canon is early to a category the analysts are now naming.

## Status

Scaffolding established 2026-05-22. **Five analyst-frame entries landed 2026-06-01** (Gartner, Forrester, IDC, CB Insights, adjacent-firms roundup). Slice is built out — right-sized to firm-level overviews (thinner + paywalled vs the other slices); deepen to per-report entries only when a flagship report materially shifts. With this, **all five SOTA-survey slices are built out.**
