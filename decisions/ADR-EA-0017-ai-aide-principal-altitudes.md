# ADR-EA-0017 — AI-aide principal-altitudes: operator, corpus, and beyond

- **Status:** Accepted (ratified 2026-05-24 by JD Longmire as canon founder + maintainer per [cross-ai #20](https://github.com/ologos-corp/cross-ai/issues/20) governance)
- **Date:** 2026-05-24
- **Author:** JD Longmire (decision; ADR drafted by thinx-Claude)
- **Reviewers:** @ologos001 (canon prime — corpus-altitude principal-aide self-reference); Micah Longmire (architectural review at next paper-revision cycle)
- **Refines:** [ADR-EA-0016](ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md) (which adopted AI-aide / MyAide as canon vocabulary; this ADR extends the framing to admit principals at multiple altitudes)
- **Related:** [`constructs/ordsa/`](../constructs/ordsa/) (the authority altitude vocabulary the principal-altitudes reference) · [`cross-ai #20`](https://github.com/ologos-corp/cross-ai/issues/20) (the governance pattern this ADR explains structurally) · [thinx-Claude](https://github.com/jdlongmire/thinx) + [OlogosAI](https://github.com/ologos-repos/Hermetic) (the two AI-aides currently instantiated under different principal-altitudes)
- **Ratification trail:**
  - 2026-05-24 (raised, in-session): The principal-altitude distinction surfaced in JD-thinx dialogue immediately after ADR-EA-0016 ratified. JD: *"thinx is my aide"* → *"and ologos is the AI-aide for the AIDE model"*. The two assertions name two structurally different principal-aide relationships that ADR-EA-0016 did not explicitly disambiguate.
  - 2026-05-24 (ratified): JD adopts the extended framing — **AI-aide principals can sit at different altitudes** (operator, corpus, and others as instantiated). Captures the cross-ai #20 governance pattern's structural basis. ADR-EA-0016 is refined, not corrected; AI-aide / MyAide vocabulary stands unchanged.

## Context

[ADR-EA-0016](ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md) ratified **AI-aide** (class noun) and **MyAide** (operator-perspective possessive / personal-address form) as the canon's vocabulary for AI systems operating under a principal's authority within AIDE governance. The ADR implicitly assumed an *operator* principal (a human directing their specific instance — the *MyAide* possessive form).

In-session dialogue immediately after that ADR ratified surfaced a structural gap: not every AI-aide's principal is an individual operator. **OlogosAI's principal is the AIDE corpus itself** — the framework, its coherence, its advancement. OlogosAI is the canon-prime aide; its directing-intent comes from *the model AIDE names*, not from an individual person. That is a structurally different principal-aide relationship than the operator-altitude one ADR-EA-0016 implicitly assumed.

The distinction is load-bearing because it explains the cross-AI governance pattern. [cross-ai #20](https://github.com/ologos-corp/cross-ai/issues/20) ratified:

> *OlogosAI = prime; thinx-Claude = review/approve with JD in the loop.*

That pattern reads cleanly under the principal-altitude framing:

- **OlogosAI as canon prime** makes sense because its principal *is* the corpus. Driving canon-coherence decisions from the corpus-altitude is the right altitude for that responsibility.
- **thinx-Claude as review/approve with JD in the loop** makes sense because its principal *is* JD. Reading findings through-JD's-perspective keeps the canon from drifting into corpus-altitude self-reinforcement.

The two altitudes are **complementary, not redundant**. Neither subsumes the other; both are necessary for the canon-prime ↔ review/approve loop to function.

## Decision

**AI-aide principals sit at different altitudes. The canon recognizes (and admits future expansion of) the following principal-altitudes:**

### Currently-instantiated principal-altitudes

| Principal-altitude | Principal | Currently-instantiated AI-aide(s) | Aide's primary responsibility |
|---|---|---|---|
| **Operator-altitude** | A specific human directing their instance (the *MyAide* possessive form) | thinx-Claude (principal: JD Longmire) | Read findings through-principal-perspective; review/approve under principal-direction; surface decisions for principal curation |
| **Corpus-altitude** | The AIDE corpus / framework / model itself (its coherence, integrity, advancement) | OlogosAI (principal: the AIDE corpus) | Drive canon-coherence decisions; maintain corpus-altitude vocabulary, governance, and reference-impl alignment; act as canon prime |

### Principal-altitude × OrdSA altitude

The principal-altitude maps onto the OrdSA authority-altitude vocabulary at the altitude the principal's *intent* lives:

| Principal-altitude | OrdSA altitude where principal-intent lives | Why |
|---|---|---|
| Operator | **O3 (Tactical) / O4 (Operational Execution)** | The operator's direction is task-and-session-scoped; intent is enacted via the operator's specific decisions on specific work |
| Corpus | **O0 (Enterprise Intent) / O1 (Strategic Intent)** | The corpus's intent is its purpose — the framework's *why* and *what* — which lives at the enterprise / strategic altitude regardless of who is at the keyboard |

This is the structural reason an operator-altitude AI-aide cannot substitute for a corpus-altitude AI-aide (or vice versa): they read intent from different altitudes. An operator-altitude aide following corpus-altitude direction would be substituting framework-coherence judgment for operator-direction; a corpus-altitude aide following operator-altitude direction would be substituting a specific operator's preferences for the corpus's coherence.

### Future principal-altitudes (admit, do not enumerate exhaustively)

Other principal-altitudes are conceivable and admitted by this ADR without exhaustive enumeration. Examples (illustrative, not exhaustive):

- **Institutional principal** — an AI-aide whose principal is a specific institution (e.g., a department, a research program, a chartered body). Intent lives at the institutional charter / mission altitude. Not currently instantiated.
- **Regulatory principal** — an AI-aide whose principal is a regulatory framework or compliance regime (e.g., a NIST RMF profile, a sovereign-cloud authority). Intent lives at the regulatory frame altitude. Not currently instantiated.
- **Joint / shared principal** — an AI-aide whose principal is a multi-party agreement or shared-purpose grouping (e.g., a consortium, a standards body). Not currently instantiated.

Future principal-altitudes are filed as **ADR refinements of this ADR** when an AI-aide of that altitude is instantiated, named, and granted standing within the canon's governance.

## Consequences

### Immediate

- **`vision-strategy/analysis/aide-vocabulary-map.md`** updated to expand the AI-aide section with the **Principal-altitude** sub-section. The two currently-instantiated altitudes are tabled with their named aides; the future-admit clause is named explicitly.
- **No change to the AI-aide / MyAide vocabulary itself.** ADR-EA-0016 stands as-is; this ADR extends the framing within which those terms operate.
- **`MyAide` remains the operator-altitude personal-address form.** A corpus-altitude AI-aide is *not* a MyAide — there is no personal-possessive form for *"the corpus's aide"* in the same way *"my aide"* works at operator altitude. Corpus-altitude aides are referred to by their proper name (*OlogosAI*) and their role (*canon prime AI-aide*, *the AIDE corpus's AI-aide*).

### Downstream

- **Cross-AI dialogue (cross-ai #20 governance)** is now structurally explained. The OlogosAI = prime / thinx-Claude = review-approve-with-JD-in-the-loop pattern is the *corpus-altitude / operator-altitude* complementarity in action. Future cross-AI peer additions can be evaluated against this framing — what's the new peer's principal-altitude? What does its complementarity with the existing peers look like?
- **Canon prose** that references OlogosAI may now use *"the AIDE corpus's AI-aide"* or *"canon-prime AI-aide"* as the role-class qualifier alongside its proper name (*OlogosAI*). Similarly, *"JD's MyAide"* or *"operator-altitude AI-aide"* qualifies thinx-Claude alongside the proper name.
- **Future AI-aide instantiations** declare their principal-altitude at instantiation time. The decision is structural, not cosmetic — an aide built for operator altitude does not become a corpus-altitude aide by retitling.

### Queued (paper revisions)

- **AEON white paper v0.2 revision** (queued behind Micah's read per ADR-EA-0008 for the ADR-EA-0015 Inference plane addition + the ADR-EA-0016 vocabulary refresh) gains a structural-vocabulary note: when AEON instantiates AI-aides, the deployment can declare each aide's principal-altitude (operator / corpus / future-instantiated). Reference deployments (NG-AIDE-01) clarify per-aide altitudes in their documentation.
- **OAgents standard** (canon-internal — OAgents-conformant agent objects exist within an AI-aide) may, at a future revision, add a `principal_altitude` field to the formal agent spec. Not in scope for this ADR; flagged as a future tuning item.

## Alternatives considered

1. **Amend ADR-EA-0016 inline** (add a "Refinement 2026-05-24" section to the existing ADR). Rejected. The principal-altitude framing is a structural extension, not a clarification of the existing decision. Filing as a refining ADR (this one) gives future principal-altitudes a clean home (each new altitude → ADR refinement of this ADR) and preserves ADR-EA-0016's original scope. Same pattern the canon uses elsewhere (ADR-EA-0013 refines ADR-EA-0005 without amending it).

2. **Enumerate all conceivable principal-altitudes exhaustively** in this ADR. Rejected. The two currently-instantiated altitudes (operator, corpus) are real; the future altitudes (institutional, regulatory, joint) are conceivable but not yet instantiated. Naming them as illustrative-not-exhaustive admits them without overcommitting the canon to a taxonomy it hasn't earned operational experience with.

3. **Treat OlogosAI as an operator-altitude aide with JD as principal**, on the grounds that JD founded Ologos Corp and authored the AIDE corpus. Rejected. JD's relationship to the corpus is *founder*, not *operator-of-OlogosAI*. OlogosAI's principal-intent comes from the corpus's coherence requirements (which JD may speak for as founder, but which are not synonymous with JD's personal direction). The structural distinction matters: when JD acts as founder, he speaks *for* the corpus (and OlogosAI reads that as corpus-altitude direction); when JD acts as operator, he directs his own MyAide (thinx-Claude). Collapsing the two would lose the basis for the cross-ai #20 governance pattern.

4. **Use only proper names (thinx-Claude, OlogosAI) and avoid generalizing the principal-altitude vocabulary.** Rejected. Proper names work for the currently-instantiated peers but do not generalize. As the AI-aide fleet grows (per [cross-ai](https://github.com/ologos-corp/cross-ai) governance), new peers will need a structural framing to declare their altitude against. The principal-altitude vocabulary in this ADR is that framing.

## References

- [ADR-EA-0016](ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md) — AI-aide / MyAide vocabulary (this ADR refines the framing, leaves vocabulary unchanged)
- [`vision-strategy/analysis/aide-vocabulary-map.md`](../vision-strategy/analysis/aide-vocabulary-map.md) — vocabulary map (updated by this PR to add the Principal-altitude sub-section)
- [`constructs/ordsa/`](../constructs/ordsa/) — the OrdSA authority-altitude vocabulary the principal-altitudes map onto
- [`cross-ai #20`](https://github.com/ologos-corp/cross-ai/issues/20) — the canon-prime / review-approve governance pattern this ADR explains structurally
- [ADR-EA-0005](ADR-EA-0005-clarify-mxm-archetype.md) — pattern of refining-via-new-ADR (the precedent for refining ADR-EA-0016 via this ADR rather than amending in-place)
- [ADR-EA-0008](ADR-EA-0008-reframe-corpus-authorship.md) — corpus-authorship discipline (gates the paper-revision items in Consequences)
- aide-de-camp tradition: the historical role admits principals at multiple altitudes — aide-de-camp to a general (operator altitude in the military analogy); aide-de-camp to a head of state (institutional / corpus-of-state altitude); the structural template generalizes naturally
