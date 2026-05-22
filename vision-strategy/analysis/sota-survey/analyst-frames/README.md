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

## Status

Scaffolding established 2026-05-22. First analyst entries land in subsequent PRs.
