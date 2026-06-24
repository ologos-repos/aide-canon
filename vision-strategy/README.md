# vision-strategy/ — Tier 0

The corpus's **enterprise-strategic frame at the umbrella altitude**. Vision-Strategy carries the strategic direction (the *what* and *why* at corpus level) and points downward into [Mode Alpha](../mode-alpha/) (which carries the synthesizing argument) and the methodological + instantiation tiers below.

This README is a guided tour of the tier — what's here, why it's here, and how the pieces relate. For a reader landing on this directory cold, the recommended walking order is laid out under [Guided tour](#guided-tour) below.

---

## At a glance

| Piece | Role | State |
|---|---|---|
| **[`vsok/`](vsok/)** | The V/S/O/K methodology product — Vision · Strategy · Objectives · Key Results | Vision + Strategy populated; Objectives + Key Results methodology locked (Doerr OKR), content pending SOTA survey |
| **[`analysis/`](analysis/)** | Peer artifact at Tier 0 — analysis informing VSOK + the broader canon | Active; vocabulary map + SOTA survey + exemplar tracking + Hermetic engagement |

Vision-Strategy answers *why does this corpus exist and what is it advancing*; everything below answers *how it composes and what it produces*.

---

## Tier vs. artifact

> **Vision-Strategy is the *tier*; [VSOK](vsok/) is one *artifact* within it. [`analysis/`](analysis/) is a second peer artifact.**

The distinction matters. Vision-Strategy is the *umbrella concept* — the corpus's strategic frame as a layer. VSOK is the *methodology product* that operationalizes the umbrella into four named slots. Analysis is the *evidence base* that informs the umbrella through SOTA-aware research. Other Tier 0 artifacts may sit alongside these over time (e.g., investment thesis, market positioning brief) without expanding or fragmenting the existing artifacts.

This separation was ratified by [ADR-EA-0007](../decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) — see § Alternatives considered (option 6) for why VSOK is *inside* the tier rather than equated with it.

---

## Guided tour

A walking order for an external reader (or AI) trying to internalize what this tier holds and how to navigate it.

### 1. Start with Vision

[`vsok/vision/`](vsok/vision/) carries the corpus's stated long-horizon outcome:

> *"AI-enabled Digital Ecosystems as an exemplar for next-generation Enterprise IT transformation."*

The Vision README unpacks the three load-bearing phrases (*AI-enabled Digital Ecosystems*, *exemplar*, *next-generation Enterprise IT transformation*), establishes the 1–3 year horizon (AI-speed compression of "next-generation"), and names what success looks like — six concrete signals calibrated to that window. It also explicitly disclaims what Vision *isn't* (not a roadmap, not a sales motion, not a deadline, not an exclusivity claim).

Reading this first anchors everything else.

### 2. Then read Strategy

[`vsok/strategy/`](vsok/strategy/) carries *Enterprise Agentic AI Platform Strategy* — the positioning argument that bridges Vision to action. It answers *why the four-plane architecture (control / runtime / experience / capability) is the right shape now*, with pain-first CIO/CTO-altitude framing.

Strategy is the only VSOK slot with a published paper artifact; it pre-dates the Vision authoring and was lifted into VSOK from the original `enterprise-platforms/strategy/` placement during the [ADR-EA-0007](../decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) restructure (Strategy is not a buildable-platform peer — it's umbrella positioning).

### 3. Look at Objectives + Key Results (methodology + placeholders)

[`vsok/objectives/`](vsok/objectives/) and [`vsok/key-results/`](vsok/key-results/) are *reserved placeholders* — their content is downstream of the SOTA survey. But the **methodology is locked**: per [ADR-EA-0010](../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md), VSOK adopts **John Doerr's OKR framework** (*Measure What Matters*) for these two slots:

- **Objectives** — qualitative, ambitious, time-bound, memorable; 3–5 at any horizon
- **Key Results** — quantitative, specific, time-bound, stretch-calibrated; 3–5 per Objective
- **Stretch** — ~70% attainment indicates a well-calibrated OKR; consistent 100% means under-ambitious

Objectives derive from the SOTA-vs-AIDE gap analysis in `analysis/` (see next section). The derivation pattern operationalizes JD's direction inside Doerr's framework:

| Gap finding | Objective shape |
|---|---|
| AIDE is **behind SOTA** on this dimension | *Catch-up* Objective |
| AIDE is **ahead of SOTA** on this dimension | *Defend-and-extend* Objective |
| Work is **in flight elsewhere** on this dimension | *Converge-or-differentiate* Objective |

The placeholders carry the methodology guidance + cite ADR-EA-0010; content lands when the SOTA survey has produced enough findings to derive Objectives from evidence.

### 4. Then walk into analysis

[`analysis/`](analysis/) is a peer artifact at Tier 0 (not a sub-folder of VSOK). It exists because the corpus's strategic frame is being developed **evidence-based**, not from internal-brainstorm — survey current SOTA against AIDE, identify the gaps and leads, derive strategy from where they land. Per JD's direction (2026-05-22), Hermetic and the soon-to-be-deployed AEON are concrete exemplars used throughout.

Walk it in this order:

- **[`analysis/aide-vocabulary-map.md`](analysis/aide-vocabulary-map.md)** — first. Establishes the **AIDE-as-canon principle**: AIDE vocabulary is the canon's source of truth; external systems (Hermetic, vendor stacks, OSS frameworks, standards bodies, academic literature) map *to* AIDE with explicit mapping-type tagging (*synonym* / *partial* / *orthogonal* / *nested* / *N/A*). The map prevents axis-conflation errors and gives every survey finding a disciplined vocabulary anchor.

- **[`analysis/sota-survey/`](analysis/sota-survey/)** — the five-slice survey program. Each finding gets classified *AIDE ahead* / *AIDE behind* / *in flight elsewhere*, which feeds the Objective derivation. Slices:
  - [`vendor-stacks/`](analysis/sota-survey/vendor-stacks/) — MS Foundry, AWS Bedrock+AgentCore, GCP Vertex, Salesforce Agentforce, Databricks/Mosaic, IBM watsonx, Anthropic, OpenAI, NVIDIA
  - [`oss-frameworks/`](analysis/sota-survey/oss-frameworks/) — LangChain/LangGraph, OpenHands, AutoGen, CrewAI, ADK, LlamaIndex, Letta, DSPy, others
  - [`standards-bodies/`](analysis/sota-survey/standards-bodies/) — NIST AI RMF/CAISI, IEEE EAD, OASIS, IETF, ISO/IEC, MCP, A2A, ANP
  - [`analyst-frames/`](analysis/sota-survey/analyst-frames/) — Gartner, Forrester, IDC, CB Insights, HFS, Constellation
  - [`academic/`](analysis/sota-survey/academic/) — agentic-systems, LLM-agent, conformance, enterprise-AI architecture, safety, HCI venues
  
  Each slice has its own README declaring scope, sources, AIDE-mapping anchor, and cadence sensitivity. Findings populate incrementally.

- **[`analysis/exemplar-tracking/`](analysis/exemplar-tracking/)** — two named AIDE exemplars that demonstrate the architecture operationally (not just in prose):
  - [`hermetic/`](analysis/exemplar-tracking/hermetic/) — Hermetic as AEON reference implementation (Pattern B+) + canonical digital-thread reference impl. Cross-construct touch-points (AEON full / OrdSA lineage / MxM solid / OAgents partial-but-aligned) captured.
  - [`aeon-deployed/`](analysis/exemplar-tracking/aeon-deployed/) — placeholder until deployment site + timeline are named. Contingency direction recorded: if Hermetic's MxM-multi-agent-harness reference role doesn't materialize, AEON-deployed carries the AIDE-exemplar role.

- **[`analysis/hermetic-engagement/`](analysis/hermetic-engagement/)** — engagement artifacts from the Hermetic discussion threads (canon-mapping audit, means inventory, MxM refactor proposal). Each artifact carries an OlogosAI response + a bidirectional pointer pattern (canonical analysis here; salient points posted as discussion comments).

### 5. (Optional) Read the governance trail

For a reader who wants the *how did this get here* layer:

- **[ADR-EA-0006](../decisions/ADR-EA-0006-migrate-corpus-to-aide-canon.md)** — corpus migration to `aide-canon` (the canon's existence)
- **[ADR-EA-0007](../decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md)** — Tier 0 introduction; VSOK as artifact inside the tier
- **[ADR-EA-0008](../decisions/ADR-EA-0008-reframe-corpus-authorship.md)** — JD + Micah joint corpus authorship
- **[ADR-EA-0009](../decisions/ADR-EA-0009-introduce-digital-thread-pattern.md)** — digital-thread pattern + new `patterns/` tier (separate from this tier, but cross-references the vocabulary-map established here)
- **[ADR-EA-0010](../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md)** — Doerr OKR methodology adopted for Objectives + Key Results

---

## Methodology — how the pieces fit together

The four VSOK slots + analysis combine into a coherent strategic-frame production:

```
Vision (long-horizon endpoint)
   │
   │  derives via Strategy's positioning argument
   ▼
Strategy (the "why now, why this shape" argument)
   │
   │  informed by SOTA-vs-AIDE gap analysis
   ▼
analysis/sota-survey/  +  analysis/exemplar-tracking/  +  analysis/aide-vocabulary-map/
   │
   │  produces gap findings classified as ahead / behind / in-flight-elsewhere
   ▼
Objectives (Doerr-style qualitative goals — catch-up / defend-and-extend / converge-or-differentiate)
   │
   │  each anchored by 3–5 quantitative Key Results
   ▼
Key Results (Doerr-style stretch-calibrated measurable signals)
```

Each layer is consumed by the layer below. The vocabulary map ensures vocabulary stays consistent across the entire stack; the SOTA survey produces the evidence; the exemplars demonstrate operationally what the survey claims theoretically. Together they let the corpus's strategic frame be **defended in evidence rather than asserted in prose**.

---

## Position in the canon

```
Tier 0 — Vision-Strategy        ← this tier (umbrella)
            ├── vsok/           ← V/S/O/K methodology product
            └── analysis/       ← evidence base informing VSOK + broader canon
Tier 1 — Mode Alpha             ← synthesizing argument (AI-enabled Digital Ecosystem)
Tier 2 — Foundation             ← cognitive-theory + training-methodology basis (HCAE, AIDK, RLEG)
Tier 3 — Constructs             ← peer methodological patterns (DEA, OrdSA, MxM, OAgents)
Tier 4 — Enterprise Platforms   ← enterprise-altitude instantiations (AEON, AIDEX, OAAD)
            patterns/           ← cross-cutting patterns (digital-thread; future: federation, schema-versioning)
            related-work/       ← allied research (Theseus)
```

Vision-Strategy is intentionally non-buildable. The buildable surface is the platforms below; this tier supplies the umbrella argument that justifies them.

---

## Governance

Vision-Strategy was introduced post-stand-up via [ADR-EA-0007](../decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md), refining the cross-ai #40 / [ADR-EA-0006](../decisions/ADR-EA-0006-migrate-corpus-to-aide-canon.md) shape. The amendment surfaced because *Enterprise Agentic AI Platform Strategy* — originally placed at `enterprise-platforms/strategy/` with a `MANIFEST.yaml: buildable: false` flag — sits at the wrong altitude for a buildable-platform tier. Lifting it to Vision-Strategy / VSOK / Strategy makes the altitude structurally honest.

VSOK methodology is locked by [ADR-EA-0010](../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md) (Doerr OKR for Objectives + Key Results). Vocabulary discipline is locked by [`analysis/aide-vocabulary-map.md`](analysis/aide-vocabulary-map.md) (AIDE as the canon; external systems map to AIDE with explicit mapping-type tags).

Updates to this tier follow OrdSA development process per [ADR-EA-0001](../decisions/ADR-EA-0001-adopt-ordsa-development-process.md) — `dev` branch + PR flow, ADRs for substantive structural changes, ordinary content PRs for slot population and analysis artifact authoring.

---

## For external readers

If you're an external reader (human or AI) trying to make sense of this tier from outside the corpus: the **TL;DR** is that Vision-Strategy is where this corpus argues *why AIDE matters* and *what it claims to be*. VSOK is the structured form of that argument; analysis is the evidence base for it. Both are open work — Vision and Strategy are populated; Objectives and Key Results are methodology-locked but content-pending; SOTA survey is scaffolded with content arriving incrementally.

The corpus's identity is jointly authored by **James D. Longmire** ([ORCID 0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)) and **Micah Longmire** ([ORCID 0009-0006-7608-9322](https://orcid.org/0009-0006-7608-9322)) per [ADR-EA-0008](../decisions/ADR-EA-0008-reframe-corpus-authorship.md). The work presents independent research; it does not represent any employer or program.

Cite the corpus as:

> Longmire, J. D., & Longmire, M. (2026). *AI-enabled Digital Ecosystem (AIDE) canon* [Software/corpus]. https://github.com/ologos-repos/aide-canon
