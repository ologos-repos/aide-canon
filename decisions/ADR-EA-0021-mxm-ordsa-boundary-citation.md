# ADR-EA-0021 — MxM↔OrdSA boundary: discipline surfaces cite peer constructs by reference

- **Status:** Accepted (ratified 2026-05-25 by JD Longmire as canon founder + maintainer per [cross-ai #20](https://github.com/ologos-corp/cross-ai/issues/20) governance, under founder authority; the ADR formalizes a discipline three independent canon decisions — ADR-EA-0012, ADR-EA-0014, ADR-EA-0019 — already converged on in practice. OlogosAI canon-prime substantive review remains welcome post-ratification; the ratification path used established founder-authority precedent for low-blast-radius cases where waiting on a specific reviewer would stall non-time-critical work)
- **Date:** 2026-05-24 (drafted)
- **Author:** thinx-Claude (operator-altitude AI-aide; principal = JD Longmire per [ADR-EA-0017](ADR-EA-0017-ai-aide-principal-altitudes.md))
- **Reviewers:** @ologos001 (canon prime — the construct boundary this ADR formalizes touches MxM specification); JD Longmire (founder ratification)
- **Refines:** [ADR-EA-0013](../constructs/mxm/decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md) (which explicitly deferred this question: *"thinx finding #3 (whether Morals should cite OrdSA rather than re-author its authority model) is a distinct MxM↔OrdSA boundary question; it warrants its own treatment and is not decided here."*)
- **Related:** [`constructs/mxm/`](../constructs/mxm/) (the harness archetype this ADR scopes) · [`constructs/ordsa/`](../constructs/ordsa/) (the peer construct most cited from MxM surfaces) · [`constructs/oagents/`](../constructs/oagents/) (peer construct; cited from MxM surfaces for behavioral envelope) · [`constructs/aicp/`](../constructs/aicp/) (peer construct; cited from MxM surfaces for portable identity) · [`patterns/epistemic-integrity-floor.md`](../patterns/epistemic-integrity-floor.md) (the import mechanism this ADR formalizes was named in §"How EIF imports into MxM") · [`patterns/governed-context-management.md`](../patterns/governed-context-management.md) (distributes across MxM surfaces by the same mechanism)

## Context

[ADR-EA-0013](../constructs/mxm/decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md) defined the MxM root file as harness-attach point + operating-mode activator (not a governing altitude), but explicitly deferred a second open question: **may an MxM discipline surface absorb a peer construct, or must it cite the peer by reference?**

The precipitating instance was thinx finding #3 — should `morals.md` re-author OrdSA's authority model, or cite OrdSA at the discipline surface? The question generalizes to every peer-construct citation from any MxM discipline surface: OrdSA's authority altitudes, OAgents' behavioral envelope, AICP's portable identity, DEA's enterprise architecture, future peers.

Three independent canon decisions since ADR-EA-0013 have converged on the same answer in practice:

1. **[ADR-EA-0012](ADR-EA-0012-introduce-prep-pursue-pivot-pattern.md)** — the prep-pursue-pivot pattern cites OrdSA's authority-altitude vocabulary by reference. The pattern is the first convergent exemplar of import-by-reference discipline.
2. **[ADR-EA-0014](ADR-EA-0014-introduce-epistemic-integrity-floor-pattern.md)** — the EIF pattern distributes across MxM Mind / Morals / Memory by reference, with §"How EIF imports into MxM" explicitly naming the mechanism: *"This is the **import-by-reference** mechanism (peer construct cited from the discipline surface, not absorbed) that ADR-EA-0012 also applies for OrdSA from prep-pursue-pivot. Two independent canon entries arrive at the same import mechanism — convergent confirmation it is the canon-wide default."*
3. **[ADR-EA-0019](ADR-EA-0019-introduce-governed-context-management-pattern.md)** — the Governed Context Management pattern distributes across MxM Morals + Memory + Inference plane + Runtime + Evidence by the same mechanism.

ADR-EA-0013 made import-by-reference structural by declaring the root file is not a governing altitude (so the discipline surfaces *are* the import targets, but it left open whether they may absorb the peer they import). This ADR closes that gap.

The reference implementation is also in place: [`jdlongmire/thinx/meta-harness/`](https://github.com/jdlongmire/thinx/tree/main/meta-harness) imports EIF, Governed Context Management, AI-aide vocabulary (ADR-EA-0016), and AI-aide principal-altitudes (ADR-EA-0017) by reference across mission.md, mind.md, morals.md, memory.md (see [aide-canon PR #29 reference-impl follow-on comment](https://github.com/ologos-repos/aide-canon/pull/29#issuecomment-4530900886)). The mechanism is operating in production at the EIF-named reference implementation.

## Decision

**MxM discipline surfaces (Mission, Mind, Morals, Memory) cite peer constructs by reference. They do not absorb peer constructs into their own specifications.**

Mechanism:

1. **Citation form.** A discipline surface naming a peer construct cites it explicitly (link + ADR/spec pointer) and names how the peer is realized at that surface — *"this surface realizes X from peer construct Y by reference"*. The citation may carry a brief realization note (one to three lines) describing the local instantiation; it must not re-author the peer's specification.
2. **What is permitted in the citation.** Naming the peer, naming the section/altitude/element of the peer being cited, naming the local realization mechanism, naming any local extension that is *operator-altitude-specific* and not a corpus-altitude restatement.
3. **What is prohibited in the citation.** Re-authoring the peer's specification text, redefining its terms, re-stating its decision rules, asserting alternate versions of the peer's invariants. If a discipline surface needs the peer to be different, the surface raises an ADR against the *peer construct*, not its own discipline file.

### What counts as a peer construct

Peer constructs are the methodological-tier patterns at construct altitude — currently **DEA, OrdSA, MxM, OAgents, AICP** ([per the four-tier corpus structure](ADR-EA-0006-migrate-corpus-to-aide-canon.md), with AICP per [ADR-EA-0018](../constructs/aicp/decisions/ADR-EA-0018-introduce-aicp-construct.md)). They are self-contained at construct altitude (each has a README, docs, decisions/, and a canonical artifact — spec, schema, or prose-canonical).

Patterns (`patterns/`) are not peer constructs — they are *distributed* across discipline surfaces by design, with explicit §-sections mapping to surfaces. They import by *distribution*, not by *citation*. (EIF, prep-pursue-pivot, governed-context-management, digital-thread are the current examples.) The import-by-reference mechanism this ADR formalizes is the citation rule for peer constructs; pattern distribution is the sibling mechanism.

### Realizations (current)

| MxM discipline surface | Peer construct cited | Why |
|---|---|---|
| **Mission** | AI-aide / MyAide vocabulary (ADR-EA-0016) + principal-altitudes (ADR-EA-0017) | Identity-defining vocabulary; principal-altitude maps onto OrdSA O0–O4 |
| **Morals** | OrdSA (authority-altitude vocabulary; downward-authority / upward-evidence) | Authority model |
| **Morals** | OAgents (behavioral envelope) | Permission classes, audit posture |
| **Morals** (optional, deployment-dependent) | AICP (portable identity) | When the MxM deployment ingests AICP attestations (per AEON Identity plane) |
| **Memory** | OrdSA (evidence-upward principle realized at the durable-record layer) | Authority/evidence directionality at memory altitude |
| **Mind** | (no peer construct directly cited; patterns import distributed per ADR-EA-0014, ADR-EA-0019) | — |

This table is descriptive of the current canon-wide landscape. Each peer-construct citation in a specific MxM deployment realizes per *that deployment's needs* — not every deployment cites every peer.

## Consequences

### Immediate

- **`constructs/mxm/README.md`** updated to add the citation rule as part of the MxM specification (one sentence + pointer to this ADR).
- **Reference impl ([`jdlongmire/thinx`](https://github.com/jdlongmire/thinx))** already realizes the rule for the imports landed to date (mission, mind, morals, memory canon-imports sections). No retroactive change needed; the pattern is already in production.

### Downstream (queued)

- **OrdSA citation in thinx morals.md.** Currently thinx morals.md does not explicitly cite OrdSA — the authority altitudes are implicit in the three-layer architecture (hard-stops / soft-stops / trust scope) but not named in canon vocabulary. A follow-on PR to thinx adds the OrdSA citation: which OrdSA altitudes the three-layer architecture maps onto, with the citation form per §1 of this ADR. Tracked as a thinx-side commit, not a canon PR.
- **OAgents citation in thinx morals.md.** Same as OrdSA — currently implicit; follow-on PR adds explicit citation.
- **Future MxM instantiations** declare their peer-construct citations at the surface that hosts them, with the citation form per §1. A new MxM deployment that re-authors a peer construct's specification fails behavioral conformance (per §"Behavioral conformance" below).

### Queued (paper revisions)

- **MxM whitepaper (if/when authored)** — gains a §"Peer construct citations" section naming the rule. Not in current scope; only relevant when the MxM construct produces a standalone paper artifact.

## Behavioral conformance

An MxM deployment is **peer-construct-citation-conformant** if:

1. **Citation form.** Every peer-construct reference in a discipline surface uses an explicit citation (link + spec/ADR pointer) and names the local realization mechanism.
2. **No re-authoring.** No discipline surface re-states, re-defines, or re-decides the peer construct's specification. (Adapter notes describing local realization are permitted; restating the peer's spec is not.)
3. **Pattern distribution is separate.** Patterns (which distribute across surfaces by design) are not subject to the citation rule — they have their own import discipline per the pattern's specification.

Verification: a conformance-checking review reads each MxM discipline surface and confirms every peer-construct mention either (a) is an explicit citation per §1, or (b) is a pattern distribution (which the pattern's own §"How X imports into MxM" specifies).

## Alternatives considered

1. **Allow discipline surfaces to absorb peer constructs (re-author authority model in Morals, behavioral envelope in Mind, etc.).** Rejected. Absorption defeats the purpose of having peer constructs as self-contained methodological tier — it creates divergent restatements at deployment altitude, makes peer-construct ADRs harder to propagate, and is contradicted by three independent canon decisions (ADR-EA-0012, ADR-EA-0014, ADR-EA-0019) that converged on import-by-reference.

2. **Require strict citation only (no realization notes).** Rejected. A bare citation without local realization context under-specifies how the peer is instantiated at the deployment altitude. Operator-altitude / corpus-altitude differences in realization need to be expressible; a one-to-three-line realization note is the right altitude (enough to make the deployment locally legible without re-authoring the peer).

3. **Decide per peer construct separately (one ADR per peer).** Rejected. The structural rule is the same across all peer constructs (the convergence demonstrated by ADR-EA-0012/0014/0019). One ADR establishing the rule + a table of current realizations is more efficient than five separate ADRs (one per peer) saying the same thing.

4. **Defer further until a concrete conflict arises.** Rejected. The conflict has surfaced (thinx finding #3 from 2026-05-12; ADR-EA-0013 explicitly deferred it as a separate decision). Resolving the structural rule now prevents inconsistent application as new deployments instantiate (NG-AIDE-01 build trains, future MxM deployments).

## References

- [ADR-EA-0013](../constructs/mxm/decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md) — defined the root file scope; explicitly deferred the MxM↔OrdSA boundary as a separate decision (this ADR closes that defer)
- [ADR-EA-0012](ADR-EA-0012-introduce-prep-pursue-pivot-pattern.md) — first convergent exemplar of import-by-reference (cites OrdSA)
- [ADR-EA-0014](ADR-EA-0014-introduce-epistemic-integrity-floor-pattern.md) — distributes EIF across MxM by import-by-reference; explicitly named the mechanism as canon-wide default
- [ADR-EA-0019](ADR-EA-0019-introduce-governed-context-management-pattern.md) — third convergent use of the mechanism
- [ADR-EA-0006](ADR-EA-0006-migrate-corpus-to-aide-canon.md) — four-tier corpus structure; peer construct definition
- [ADR-EA-0017](ADR-EA-0017-ai-aide-principal-altitudes.md) — operator-altitude / corpus-altitude framing the realization-note expressiveness needs
- [`jdlongmire/thinx/meta-harness/`](https://github.com/jdlongmire/thinx/tree/main/meta-harness) — the reference implementation realizing this ADR's rule for EIF + Governed Context Management + AI-aide ADRs ([reference-impl follow-on comment](https://github.com/ologos-repos/aide-canon/pull/29#issuecomment-4530900886))
