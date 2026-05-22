# ADR-EA-0002 — Re-frame AI EA as the canonical enterprise-scale OrdSA exemplar

- **Status:** Accepted
- **Date:** 2026-05-21
- **Author:** JD Longmire
- **Reviewers:** @jdlongmire

## Context

This corpus and OrdSA have been published as nominally peer artifacts. The README's *Relation to OrdSA* section describes the corpus as **"methodologically allied with OrdSA"** — peer language.

Two events earlier today (2026-05-21) made the practical relationship asymmetric in a way the prose no longer matches:

1. **The OrdSA construct infographic merged into both repos** ([`OrdSA-Construct.png`](../constructs/ordsa/docs/marketing/OrdSA-Construct.png)). Its title block subtitles OrdSA as *"A Control-Oriented Architecture Construct for Enterprise AI"*. The framing positions OrdSA as the construct that orders Enterprise AI work — i.e., orders the territory this corpus occupies. It now sits alongside the four AI-EA infographics on this repo's infographic shelf.

2. **[ADR-EA-0001](ADR-EA-0001-adopt-ordsa-development-process.md) ratified** the adoption of OrdSA's PR-first + ADR-as-PR governance for enterprise-ai. The asymmetry is operationally observable: this corpus inherits OrdSA's process; OrdSA inherits nothing from this corpus.

A reader who looks at the infographics, the governance, and the README's prose simultaneously sees an inconsistency: the visual and the process say AI EA sits inside OrdSA's frame; the prose says they are peers. The peer rhetoric no longer matches the structural shape of the work.

## Decision

**Reframe AI EA in the README as the canonical enterprise-scale deployment of OrdSA, not as a methodological peer.**

The new positioning, in summary:

> *enterprise-ai is the canonical enterprise-scale deployment of [OrdSA](https://github.com/osa-ai-org/ordsa-ai). Where OrdSA specifies the layered authority, evidence, and execution-rights construct for agentic systems, this corpus develops the concrete enterprise-architectural shape — control plane (AEON), runtime, experience subdomain (AIDEX), capability platform (OAAD) — that an enterprise builds when it operationalizes OrdSA at platform scale.*

Concrete README changes (light scope — this ADR's PR carries only these prose edits):

1. **Intro paragraph (top of README):** mention that the corpus develops the canonical enterprise-scale deployment of OrdSA, rather than introducing the corpus as a standalone "coordinated architecture."
2. ***Relation to OrdSA* section:** replace "methodologically allied with OrdSA" framing with "canonical enterprise-scale deployment of OrdSA"; spell out the structural / visual / operational alignment.
3. ***Audience* section:** add one parenthetical pointer telling framework-builders to read OrdSA first, since this corpus is the deployment view, not the construct itself.

### Scope: light

This ADR modifies the README's framing prose only. It does not:

- Modify any of the eight published papers
- Re-voice paper abstracts
- Rename or reorganize files
- Change file structure
- Alter authorship
- Revise the "independent research" disclaimer

The papers continue to carry their original disclaimer unchanged. Re-voicing the corpus papers' positioning paragraphs is **not** in scope for this ADR; it would flow as either ordinary content PRs per paper or as a separate ADR if a coordinated re-voicing is later judged warranted.

### Companion paper queued

A companion paper, *How to read AI EA as an OrdSA deployment* (working title), is **queued for later authoring** as an ordinary content PR — likely landing in `osa-ai-org/ordsa-ai/docs/examples/` rather than in this repo, since the OrdSA repo is the natural home for worked-example methodological appendices. Not in scope for this ADR.

## Consequences

- **Coherence between visual / process / prose.** The README catches up to what the OrdSA construct infographic and ADR-EA-0001 already established structurally.
- **Future papers in the corpus gain a stable framing anchor.** Successor papers introduce themselves as developments within the OrdSA enterprise-scale deployment, not as freestanding architecture pieces. This shape flows through ordinary content PRs going forward; no per-paper ADR required.
- **Cross-repo navigability improves.** A reader arriving at enterprise-ai finds an unambiguous path back to OrdSA's construct repo; a reader arriving at OrdSA gains a clear pointer to the canonical enterprise-scale exemplar.
- **The companion paper is now meaningfully positioned.** Without ratifying this framing change, the companion paper "How to read AI EA as an OrdSA deployment" would have no stable anchor — "as a deployment of" presupposes a deployment-of relationship that the README didn't admit to. This ADR creates the anchor; the paper itself follows.
- **Existing citations are not invalidated.** Readers who cited the prior "methodologically allied" framing in their own work are not contradicted — the previous framing was a weaker form of the same claim, and the ADR's narrative explains the strengthening as the corpus matured.
- **Disclaimer unchanged.** The "independent research / does not represent any employer or program" framing remains. OrdSA carries the same disclaimer; the alignment is between two pieces of the same author's independent research, not between sponsored programs.

## Alternatives considered

1. **Stay at "methodologically allied" (position 1).** Status quo. Rejected because today's actions (OrdSA infographic + ADR-EA-0001) created an inconsistency between prose and practice. The peer rhetoric no longer holds without ignoring structural facts that are already published.

2. **Re-anchor at the corpus level (heavy scope).** Rename the corpus, restructure the repo, re-voice the eight papers' positioning paragraphs to make OrdSA subordination explicit throughout each paper, possibly republish the papers as v2 with OrdSA-anchored abstracts. Rejected as overcorrection — the existing papers stand on their own intellectual content. Re-voicing would be expensive bookkeeping for a marginal clarity gain at this stage. Per-paper anchoring can happen organically as each paper revises in the natural course of the corpus's evolution.

3. **Republish the corpus under OrdSA's repo entirely (collapse into one project).** Rejected because the two repos serve different audiences (CIO / CTO / Chief Architect / CISO for AI EA; framework adopters and evaluators for OrdSA) and citation surfaces. Keeping them as separate published artifacts preserves audience-targeting while making the structural relationship explicit through framing prose. This is the cheapest way to honor both purposes.

4. **Author the companion paper *How to read AI EA as an OrdSA deployment* in this same ADR PR.** Rejected as heavier than warranted for the framing-only decision being made here. The companion paper is itself a substantive piece of writing — likely 6–10 pages, requires considered argumentation about the layer-to-construct mapping — and should land as an ordinary content PR once this framing is ratified. Queued for later.

## References

- [ADR-EA-0001](ADR-EA-0001-adopt-ordsa-development-process.md) — adopts OrdSA's governance for this corpus; the operational counterpart that today's prose update aligns with
- [`OrdSA-Construct.png`](../constructs/ordsa/docs/marketing/OrdSA-Construct.png) — the visual that subtitles OrdSA *for Enterprise AI* and motivated this ADR
- [`osa-ai-org/ordsa-ai`](https://github.com/osa-ai-org/ordsa-ai) — the OrdSA construct repo this corpus is a deployment of
