# ADR-EA-0003 — Expand corpus to include Digital Ecosystems Architecture (DEA)

- **Status:** Accepted
- **Date:** 2026-05-22
- **Author:** JD Longmire
- **Reviewers:** @jdlongmire
- **Ratification note:** Comment-out period waived by explicit maintainer ratification (JD Longmire, 2026-05-22). The non-waivable-clause rule from CONTRIBUTING.md is preserved as the default; the maintainer's prerogative to override the default by ratification was exercised here alongside the parallel ratification of ADR-EA-0004. The override is recorded so future readers of the ADR see that the period was deliberately collapsed, not silently skipped.

## Context

The enterprise-ai corpus to date has positioned itself as the **canonical enterprise-scale deployment of OrdSA** ([ADR-EA-0002](../../../decisions/ADR-EA-0002-reframe-as-ordsa-exemplar.md)), developed through four AI-focused constructs: **AEON, AIDEX, HCAE, OAAD**. The corpus's stated scope has been AI enterprise architecture specifically.

On 2026-05-22 a new architectural construct was authored by the same author at a more general altitude: **Digital Ecosystems Architecture (DEA)** — a three-baseline framework for coherent digital realization, not specific to AI. DEA arrived as three working papers:

1. **Digital Ecosystems Architecture: A Three-Baseline Framework for Coherent Digital Realization** (foundational base layer)
2. **Digital Ecosystems Architecture and the Unified Architecture Framework** (positioning vs UAF)
3. **Digital Ecosystems Architecture and the DIB Compliance Stack** (positioning vs the DoD/CMMC/NIST compliance regime)

DEA's base paper explicitly names a forthcoming AI-specific extension, **AIDE-AF**, that would sit on top of DEA and bridge the general framework to AI-specific architecture work. The implied lineage:

```
DEA (general EA frame)
  └── AIDE-AF (AI extension — forthcoming)
        └── AEON / AIDEX / HCAE / OAAD (specific AI-EA constructs)
```

The existing four constructs become *instances of how AIDE-AF specializes DEA into AI-specific architecture*, with OrdSA providing the layered authority/evidence ordering that AIDE-AF deployments operationalize.

Adding DEA to this corpus touches three of the rules CONTRIBUTING.md flags as ADR-worthy and as **excluded from the maintainer-prerogative waiver**:

- Adds a new major construct (currently: AEON, AIDEX, HCAE, OAAD)
- Changes audience and positioning (corpus scope broadens from "AI enterprise architecture" to "enterprise architecture, with AI specialization")
- Changes the corpus's framing prose materially

So this requires a regular ADR with the standard one-week comment-out period.

## Decision

**Expand the enterprise-ai corpus to include Digital Ecosystems Architecture as a foundational general-EA construct upstream of the existing AI-focused constructs.** The corpus now spans general enterprise architecture **and** its AI specialization, with the relationship made explicit:

1. **DEA is the general-EA foundation.** It defines a three-baseline framework (Digital Capability Baseline, Digital Technical Baseline, Digital Operational Baseline) owned by three architecture disciplines (Enterprise, Systems, Solutions). Its scope is digitally-realized capabilities at the enterprise level, not specific to AI.

2. **AIDE-AF (forthcoming) is the AI extension.** It will specialize DEA's three baselines into AI-specific architecture. Not yet authored; placeholder named in the base paper.

3. **AEON / AIDEX / HCAE / OAAD are the AI-specific constructs.** They sit within AIDE-AF's territory and implement OrdSA's authority/evidence ordering at enterprise scale. Their relationship to DEA, once AIDE-AF lands, will be that AIDE-AF bridges DEA's general framework to these specific AI architecture patterns.

4. **OrdSA remains the authority/evidence construct.** Its relationship to DEA is orthogonal — OrdSA orders agentic systems regardless of whether they sit in DEA's three-baseline framing or not. The AI EA portion of this corpus continues to be the canonical enterprise-scale OrdSA deployment ([ADR-EA-0002](../../../decisions/ADR-EA-0002-reframe-as-ordsa-exemplar.md) still holds).

### Concrete README changes (this PR carries them)

1. **Intro paragraph:** updated to describe the corpus as developing both DEA (general EA) and the AI EA constructs (its AI specialization).
2. **New section: *Architecture frame (DEA)*** — describes the three-baseline framework as the corpus's general-EA foundation, with pointer to the base paper.
3. **The AI EA constructs (AEON/AIDEX/HCAE/OAAD)** — the existing *Four constructs* section is retained and lightly reframed to clarify it's the AI specialization, not the corpus's full scope.
4. **Suggested reading order:** revised to start with DEA's base paper, then its positioning papers, then the AI EA papers (Enterprise Agentic AI Platform Strategy, AEON white paper, etc.).
5. **Document index:** expanded with the three DEA papers, grouped under a DEA subsection above the AI EA papers.
6. **Relation to OrdSA:** updated to clarify DEA and OrdSA address different axes (DEA = EA coherence + accountability; OrdSA = layered authority/evidence). The AI EA portion remains the canonical enterprise-scale OrdSA deployment.

### Scope: README revision + three new docs

This ADR's PR carries only:
- README revisions described above
- Three DEA documents (`.docx` source + rendered `.pdf`) under `docs/`
- ADR-EA-0003 itself + `decisions/README.md` index entry

It does **not**:
- Author AIDE-AF (forthcoming work)
- Modify any of the existing eight AI EA papers' content
- Restructure file paths under `docs/` (DEA papers sit alongside AI EA papers at `docs/` root, naming-convention-normalized)
- Change the corpus's CC BY 4.0 license, citation pattern, or "independent research" disclaimer
- Change the governance process from [ADR-EA-0001](../../../decisions/ADR-EA-0001-adopt-ordsa-development-process.md) (PR-first + ADRs as PRs)

## Consequences

- **Corpus identity broadens.** The repository's stated scope shifts from "AI EA" to "EA with AI specialization." Adopters who cited the corpus for AI EA specifically are not contradicted — AI EA is still the central focus — but the corpus now also speaks to general EA practice.
- **Forward path for AIDE-AF.** Once AIDE-AF is authored, it lands as an ordinary content PR under the expanded scope. No further ADR required for AIDE-AF unless it changes the construct enumeration or alignment claims beyond what this ADR establishes.
- **Reading order coherence improves.** DEA's three-baseline framework is genuinely foundational to the rest of the work; placing it first in the reading order matches the intellectual lineage.
- **Compliance + governance positioning gains a citable anchor.** Defense and regulated-enterprise readers can now find the corpus's stance on UAF (as architectural description) and the DIB compliance stack (as the governing layer DEA serves) explicitly.
- **Audience expands.** Beyond the existing CIO / CTO / Chief Architect / CISO audience for AI EA, the corpus now also addresses Enterprise Architects, Systems Architects, and Solutions Architects in general digital-ecosystem practice.
- **Existing eight AI EA papers stand unchanged.** Their content, their disclaimers, their attribution, their alignment with OrdSA all continue as before. The relationship to DEA is established in the README's framing, not by editing those papers.

## Alternatives considered

1. **Subdirectory bundle (`docs/dea/`) as a separate sub-program, sole-author preserved.** Equivalent in pattern to how the Theseus thesis was bundled in [PR #4](https://github.com/osa-ai-org/enterprise-ai/pull/4). Treats DEA as a sibling research line within the same author's broader program but keeps the AI EA four-construct enumeration untouched. Rejected because DEA is upstream of AIDE-AF and the AI EA constructs — putting it in a sibling subdirectory obscures the intellectual lineage. DEA is foundational; treating it as a parallel sub-program would misrepresent its role.

2. **Direct addition to `docs/` with no README restructure.** Drop the three papers into the document index and stop there. Rejected because the README's four-construct enumeration would become factually wrong (the corpus has more than four constructs now), and the corpus's stated AI-specific scope would no longer match its contents. The inconsistency would surface every time a reader read the README against the file tree.

3. **Author AIDE-AF first; land DEA + AIDE-AF together.** Defer DEA's landing until the AI extension is written, so the full DEA → AIDE-AF → AEON/AIDEX/HCAE/OAAD lineage is in place. Rejected because AIDE-AF isn't ready yet; deferring DEA's landing would delay the corpus's expansion for an unknown period and would leave the foundational base paper unpublished from the corpus's perspective. DEA stands on its own as a general-EA framework regardless of AIDE-AF's existence.

4. **Reposition the corpus as DEA-primary with AI EA as one application.** Re-voice the corpus's intro and four-construct enumeration to make DEA the headline construct with AEON/AIDEX/HCAE/OAAD reframed as one application of DEA. Rejected because it overcorrects — the existing AI EA work has its own identity (and its own OrdSA-deployment framing per ADR-EA-0002) that shouldn't be subordinated to DEA in the prose. The relationship is "DEA is foundational *and* AI EA is the corpus's central published work to date," not "AI EA is just one application of DEA."

## References

- [ADR-EA-0001](../../../decisions/ADR-EA-0001-adopt-ordsa-development-process.md) — the governance process this ADR follows
- [ADR-EA-0002](../../../decisions/ADR-EA-0002-reframe-as-ordsa-exemplar.md) — the framing of AI EA as canonical OrdSA enterprise-scale deployment (still holds; this ADR layers DEA above it as the general-EA foundation)
- [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) — the waiver-exclusion clauses that make this ADR require the standard one-week period
- [`docs/Digital-Ecosystems-Architecture-Base.docx`](../docs/Digital-Ecosystems-Architecture-Base.docx) / [`.pdf`](../docs/Digital-Ecosystems-Architecture-Base.pdf) — the DEA foundational paper introduced by this ADR
- [`docs/DEA-UAF-Positioning.docx`](../docs/DEA-UAF-Positioning.docx) / [`.pdf`](../docs/DEA-UAF-Positioning.pdf) — DEA's positioning relative to UAF
- [`docs/DEA-DIB-Compliance-Positioning.docx`](../docs/DEA-DIB-Compliance-Positioning.docx) / [`.pdf`](../docs/DEA-DIB-Compliance-Positioning.pdf) — DEA's positioning beneath DIB compliance
