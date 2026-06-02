# Analyst frames — adjacent firms (roundup): HFS · Constellation · Omdia · GigaOm

> SOTA-survey finding. Shape per [`./README.md`](./README.md) → [`sota-survey/README.md`](../README.md). **Roundup** entry — four firms in the *selective-inclusion* tier ([`./README.md`](./README.md), "Adjacent firms"), lighter than the tier-1 houses (Gartner / Forrester / IDC / CB Insights). Cadence: **medium** (annual Radars/Horizons + quarterly ShortList/note refresh) — treat placements as a dated snapshot.

## 1. What it is — the four firms + why grouped

Four industry-analyst firms that publish agentic-AI / AI-platform coverage but sit *adjacent* to the four tier-1 houses, each with a narrower or more specialized lens. They are grouped because none of them is a tier-1 flagship-categorizer of the AIDE problem space, and each contributes one distinct angle rather than a full market-defining frame:

- **HFS Research** — a **services / sourcing** analyst house. Its agentic coverage is framed through *Services-as-Software™* — the thesis that professional/BPO services migrate from human effort to software-delivered, outcome-priced execution. 2026 flagships: *HFS Horizons: Agentic Services* (service-provider value chain) and *HFS Horizons: Agentic Technology* (the tech firms enabling it). The lens is **services-first**, not architecture-first.
- **Constellation Research** — a futurist/practitioner analyst firm whose **ShortList™** format is the most *direct* agentic-AI category coverage of the four: a standing "Cross-Platform Agentic AI" ShortList plus adjacent "AI Application Development Platforms" and role-specific agent ShortLists, refreshed on a quarterly cycle.
- **Omdia** (Informa Tech) — an **infrastructure + platform tracking** firm. Its agentic work surfaces as *Market Radar* reports scoped to platforms/regions (e.g., Agentic AI Development Platform; Agentic AI Cloud Titans), evaluated on infrastructure-grade dimensions (model support, multi-agent framework, lifecycle management).
- **GigaOm** — a **practitioner Radar** firm. Its agentic content is largely *embedded inside domain Radars* (security, AIOps, observability, AI Infrastructure) where "agentic" describes an autonomous-triage/automation capability of a domain tool, rather than a standalone agentic-governance category.

The grouping is honest about depth: only Constellation treats cross-platform agentic AI as a first-class standing category; HFS reads it through a services P&L; Omdia through infrastructure/region; GigaOm through per-domain practitioner buying decisions. None operates at the **governance/authority** altitude aide-canon occupies.

## 2. Source links (per firm — flag access)

All four firms gate full reports; the entries below are built from **public summaries, firm category pages, and vendor/press redistributions** (per [`./README.md`](./README.md) "Access challenge"). No figures or quotes are invented; redistributor-sourced numbers are attributed and flagged as such.

- **HFS Research** — `hfsresearch.com/research/hfs-horizons-agentic-services-2026/` and `…/hfs-horizons-agentic-technology-2026/` *(full reports paywalled; vendor-licensed excerpts circulate publicly, e.g. EY / KPMG redistributions of the Agentic Services Horizons — flag: redistributor PDFs)*. Press: provider award releases (Akkodis, Genpact) — flag: vendor PR.
- **Constellation Research** — `constellationr.com/research/constellation-shortlist-cross-platform-agentic-ai` and the Q1-2026 ShortList cycle blog posts; "AI Application Development Platforms" ShortList *(ShortList summaries public; full methodology/inquiry detail gated)*.
- **Omdia** — `omdia.tech.informa.com` Market Radar pages (Agentic AI Development Platform / Cloud Titans, Asia & Oceania, 2026); AI Platforms Intelligence Service *(reports paywalled; leader claims surface via vendor PR — Tencent Cloud, Alibaba Cloud — flag: vendor PR redistribution)*.
- **GigaOm** — `portal.gigaom.com`; agentic capability appears inside domain Radars (SIEM, AIOps, AI Infrastructure, ITDR) *(reports gated; leader/fast-mover claims surface via vendor PR — flag: vendor PR)*.

*(All product/category names are snapshot 2026-06-01; analyst category labels churn — verify at read time.)*

## 3. Map against AIDE

Per the analyst-frames AIDE-mapping anchor ([`./README.md`](./README.md) → category framing · maturity/placement · named-vendor coverage · whether AIDE/OrdSA/OAgents/MxM appear).

### Per-firm row

| Firm | Category framing | Maturity / placement frame | Vendor coverage (cross-ref `../vendor-stacks/`) | AIDE / OrdSA / OAgents / MxM named? |
|---|---|---|---|---|
| **HFS** | *Agentic Services* + *Agentic Technology*, both under **Services-as-Software™** (a services-economics frame, not an architecture frame) | **Horizons 1–3** maturity bands; Horizon 3 = "Market Leader" embedding agents into workflows/governance/systems-of-record | Names hyperscalers + SaaS at H3 — [AWS](../vendor-stacks/aws.md), [Google Cloud](../vendor-stacks/google-cloud.md), [Microsoft](../vendor-stacks/microsoft.md), [Salesforce](../vendor-stacks/salesforce.md), ServiceNow; plus agentic-native firms (Ema, Rhino.ai) | **No** |
| **Constellation** | **"Cross-Platform Agentic AI"** standing ShortList — the most direct category match of the four; defines agentic AI as systems that decide/act with reduced human guidance | **ShortList™** = a curated qualified-set (not a maturity placement); quarterly refresh cadence | 50+ solutions screened across hyperscalers + platforms ([Google Cloud](../vendor-stacks/google-cloud.md), [Microsoft](../vendor-stacks/microsoft.md), [AWS](../vendor-stacks/aws.md), [Salesforce](../vendor-stacks/salesforce.md), [Databricks](../vendor-stacks/databricks.md)); adjacent "AI App Dev Platforms" ShortList overlaps [LangChain](../vendor-stacks/langchain.md)-class runtimes | **No** |
| **Omdia** | **"Agentic AI Development Platform"** — infrastructure framing (build/deploy/manage autonomous agents); evaluated on context engineering, model support, multi-agent framework, lifecycle mgmt | **Market Radar** leader/challenger placement; current flagships are region-scoped (Asia & Oceania) | Hyperscaler-heavy: [AWS](../vendor-stacks/aws.md), [Google Cloud](../vendor-stacks/google-cloud.md), [Microsoft](../vendor-stacks/microsoft.md) + Alibaba/Tencent Cloud (regional) | **No** |
| **GigaOm** | No standalone agentic category — "agentic" is a **capability axis inside domain Radars** (SIEM/AIOps/AI Infra/ITDR); plus an AI Infrastructure Radar where agent-hosting is one use case | **Radar** rings + "Fast Mover" momentum vector; practitioner-buying lens | Mostly security/ops vendors (CrowdStrike, Dynatrace, PagerDuty) + AI-infra ([NVIDIA](../vendor-stacks/nvidia.md)-adjacent compute, Clarifai); thin on the AIDE-mapped governance-vendor set | **No** |

### Combined AIDE-named-in-vocabulary signal

Across all four firms: **AIDE, OrdSA, OAgents, and MxM are absent** from every category page, Radar, Horizon, and ShortList surveyed. This is the calibrated, honest reading — these terms have **zero penetration** into adjacent-analyst vocabulary as of 2026-06-01, exactly as for the tier-1 houses. The firms' shared vocabulary is the market-category word **"agentic AI"** (a collision the canon flags below), plus firm-specific frames (Services-as-Software, ShortList, Market Radar, Horizons). Tracking this row over time is the point: it is the baseline against which the Vision success-signal *"AIDE is named in industry conversations"* ([`./README.md`](./README.md)) is measured — and the baseline is currently nil.

### Vocabulary discipline (applied)

- **"agentic" collision flag.** All four firms use **"agentic AI"** as a market-category umbrella covering everything from autonomous decisioning to a SIEM auto-triage feature. The canon does *not* adopt this as a precise term — it spans at least three distinct AIDE concepts (an **AI-aide** as a persistent principal, the **OAgents `Agent`** typed primitive inside a behavioral envelope, and mere tool-call automation). Where these firms say "agent," the canon means **AI-aide** per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md); bare "agent" is avoided.
- **No entity conflation.** These are external market frames; nothing here implies any Ologos deployment or NG-AIDE-01 placement — the firms cover commercial vendor stacks, not the canon's exemplars.

## 4. Relationship + combined synthesis

**Relationship: market-timing and category-formation signal — not competition, and not at the canon's altitude.** As with the tier-1 frames, aide-canon is a **governance corpus at research/exemplar stage**, not a vendor in any of these Radars/Horizons/ShortLists. None of the four firms evaluates *governance, authority-layering, deontic constraint, or behavioral-envelope conformance* as a primary dimension — they evaluate **platforms, services, and tool capabilities**. So the relationship is **orthogonal**: the canon would be the layer assessed *above* the agentic platforms these firms rank, not an entry within their rankings.

Per-firm read, calibrated to actual depth:

- **HFS** is the *least* architecture-adjacent: its frame is a services-economics thesis (Services-as-Software). Useful as evidence that "agents replace delivered effort" has reached sourcing analysts — but it says nothing about *how* that execution is governed, which is precisely the canon's claim.
- **Constellation** is the *closest* category match (a standing cross-platform agentic-AI ShortList), and therefore the best single firm to watch for whether a **governance/trust** sub-dimension ever emerges in an adjacent-analyst category. Its market-size projections are firm-attributed forecasts (paywalled detail) — treated as directional signal, not adopted as fact.
- **Omdia** confirms the *infrastructure* category is consolidating (development-platform Radars with explicit lifecycle/multi-agent dimensions), overlapping the same hyperscaler set the canon maps in [`../vendor-stacks/`](../vendor-stacks/). Its current agentic flagships being region-scoped is a real limitation on global-category weight.
- **GigaOm** is the most *diffuse*: agentic shows up as a capability bullet inside security/ops Radars. This is honest evidence that "agentic" has gone **practitioner-mainstream as a feature word** — which is a category-formation signal — but it is *not* evidence of an agentic-governance category forming.

**Combined synthesis.** The four adjacent firms, read together, triangulate a single fact: the market is forming an **"agentic AI" category across services (HFS), platforms (Constellation/Omdia), and domain tools (GigaOm)** — and that category is defined in **capability/economics terms with no governance-altitude dimension and no AIDE/OrdSA/OAgents/MxM vocabulary**. The canon's vocabulary is **more precise** than any of these market categories: where they have one elastic word ("agentic"), the canon distinguishes principal (AI-aide), primitive (OAgents `Agent`), authority (OrdSA), constraint (MxM Morals), and substrate (Means). This precision gap is the load-bearing finding — consistent with the tier-1 frames and with the [LangChain vendor-stack finding](../vendor-stacks/langchain.md) (different *altitude*, not a competitor).

## 5. Objective implication

Two Doerr-style Objective shapes follow (per [`sota-survey/README.md`](../README.md) classification → Objective link):

1. **Defend-and-extend (category-vocabulary lead).** *In flight elsewhere* — these firms are actively forming an "agentic AI" market category with no governance dimension. Propagate AIDE's more-precise vocabulary (AI-aide / OAgents `Agent` / OrdSA / MxM Morals) as the *governance layer naming* the category lacks. KR shape: a mapping that overlays canon vocabulary onto each firm's category labels (HFS Horizons / Constellation ShortList / Omdia Radar dimensions), demonstrating the precision delta — and a tracked count of any adjacent-analyst surface that names a governance/trust sub-dimension.
2. **Track-the-signal (Vision success metric).** The combined "AIDE-named?" row is currently **nil** across all four firms. KR shape: a quarterly re-survey of these four category pages recording any first appearance of AIDE/OrdSA/OAgents/MxM, or of a governance/authority evaluation dimension — the leading indicator for the *"AIDE is named in industry conversations"* Vision signal, with the present entry as the zero baseline.

*(Calibration note: depth is deliberately not overstated — only Constellation offers a direct standing agentic category; HFS is a services lens, Omdia is region/infra-scoped, GigaOm is per-domain practitioner Radars. The finding is a category-formation signal, not a finding of governance-aware analyst coverage.)*

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI (canon-prime)**. Built from public category pages, firm summaries, and flagged vendor/press redistributions; all full reports paywalled. Revisit at the next quarterly ShortList/Radar/Horizons refresh, or ad-hoc if any of the four publishes a governance/authority evaluation dimension or names AIDE/OrdSA/OAgents/MxM.
