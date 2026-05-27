# ADR-EA-0026 — Introduce `methods` as the fifth MxM discipline surface (tradecraft)

- **Status:** Proposed (concept ratified by JD Longmire via the operator channel, 2026-05-27; **Accepted is gated on Micah Longmire's co-author review** — MxM is a joint construct, same co-author gate as [ADR-EA-0013](ADR-EA-0013-define-mxm-root-file-mode-element.md))
- **Date:** 2026-05-27
- **Author:** JD Longmire (decision / concept); OlogosAI (drafted)
- **Reviewers:** @ologos001 (canon prime); **Micah Longmire (MxM co-author — required for ratification)**; thinx-Claude
- **Refines:** [ADR-EA-0005](ADR-EA-0005-clarify-mxm-archetype.md) (the harness archetype — adds a discipline surface) · extends [ADR-EA-0013](ADR-EA-0013-define-mxm-root-file-mode-element.md) (the 4M+1 / bracket framing) · [ADR-EA-0004](ADR-EA-0004-add-mx-modes-as-spine-construct.md) (spine bundling — unchanged)

## Context

The MxM construct ([`constructs/mxm/README.md`](../README.md)) defines **five governing surfaces (the "4M+1")** — **Mind · Morals · Mission · Memory** (the four discipline-bearing surfaces: durable, harness-agnostic) plus **Means** (the execution surface) — bracketed by the root file (`mode`), the harness-attach + operating-mode activator (ADR-EA-0013).

The four disciplines cover cognition (Mind), permission boundaries (Morals), purpose (Mission), and continuity (Memory). **None covers codified procedural craft and rigor — *how to do the work well*.** That knowledge exists and accumulates, but today it scatters across three surfaces with no coherent home:

- as **Memory** entries (operator lessons stored as continuity — e.g., "render the deck to PDF and visually inspect before done," "test actual egress, not the routing table");
- as the *obligatory* subset inside **Morals** (process-gates — QA-before-done, dev-first);
- as enforcement in **Means** (the hooks that execute those gates).

The scattering is the problem. The gap surfaced repeatedly through operator practice — rigor-enforcement work (session-lifecycle board reconciliation gates), best-practice / best-of-breed research captures, and a large body of "lessons" with no construct locus. Per the corpus's standing discipline of **naming a recurring, homeless cross-cutting shape** (the basis for the `patterns/` tier in [ADR-EA-0009](../../../decisions/ADR-EA-0009-introduce-patterns-tier.md), and for ratifying [GCM, ADR-EA-0019](../../../decisions/ADR-EA-0019-introduce-governed-context-management-pattern.md)), the tradecraft warrants a first-class surface.

## Decision

**Introduce `methods` as a fifth discipline-bearing surface of MxM.** The durable, harness-agnostic core becomes **5M** — Mind · Morals · Mission · Memory · **Methods** — and the construct presents **five disciplines + Means ("5M+1", was "4M+1")**. The root file (`mode`) and **Means** continue to bracket the disciplines exactly per [ADR-EA-0013](ADR-EA-0013-define-mxm-root-file-mode-element.md) — that framing is unchanged; only the membership of the durable core grows by one.

### 1. Definition

`methods` is the **codified, evidenced, reusable procedures and rigor disciplines for doing work to a standard — the harness's tradecraft.** It answers *"how do we do this kind of work well?"* It **recommends**; it does not constrain (Morals), implement (Means), or reason (Mind).

Proposed surface-table row (added on acceptance):

| Surface | Concern |
|---|---|
| **METHODS** | Tradecraft — codified best-practice and rigor; how a kind of work is done to a standard. Recommends; does not grant permission (Morals) or implement (Means). |

### 2. The methods ↔ morals boundary is **enforcement / obligation**

- **Morals** holds the *obligatory, enforced* disciplines — violating is a compliance breach.
- **Methods** holds *recommended craft* — departing is suboptimal, not a violation.

### 3. The graduation pipeline (the surface's signature dynamic)

`practice → method (codified) → moral (obligatory, when it matters enough) → means (enforced, via a hook)`. A single discipline may project across surfaces — the *technique* of QA is a Method, the *duty* to QA is a Moral, the *hook* is Means — while the large body of non-obligatory craft stays purely in Methods. This makes "enforcement over documentation" a lifecycle rather than a slogan: a method **graduates** to an enforced Moral when it earns it.

### 4. Altitude relation to the `patterns/` tier

`methods` (MxM — **operator** altitude: how the *agent* does its work) and `patterns/` (ADR-EA-0009 — **architecture** altitude: how the *system* is shaped) are **peers at different altitudes**. Methods may *cite* patterns; neither subsumes the other.

### 5. Entry discipline (anti-junk-drawer)

"Best practice" is broad enough to absorb anything. A method qualifies for the surface only if it is **evidenced** (proven through repetition, not speculative), **named and reusable**, and carries its **rationale** (why this way).

## Consequences

- **MxM README updated on acceptance** — "five surfaces / four discipline-bearing" → "six surfaces / five discipline-bearing"; the surface table gains METHODS; the bracket framing (root file + Means bracket the disciplines) and the orientation-first claim stand unchanged. *(Deferred until ratified — not asserted by this Proposed ADR.)*
- **Each MxM instantiation gains a methods surface** (e.g., a `methods.md` alongside `mission/mind/morals/memory`; the OlogosAI operator harness adds one and updates its `CLAUDE.md` routing; NG-AIDE-01 likewise). Realization is per-deployment, not forced retroactively.
- **Scattered craft reorganizes**: the recommended-craft subset of operator lessons surfaces as Methods; the obligatory subset stays in / graduates to Morals; enforcement stays in Means. The method→moral graduation becomes an explicit, trackable lifecycle.
- **Co-authored construct + Zenodo deposit.** MxM is jointly authored with Micah Longmire and deposited ([`10.5281/zenodo.20349200`](https://doi.org/10.5281/zenodo.20349200)). Adding a discipline surface is a substantive change to a joint, published artifact: **ratification is gated on Micah's co-author review**, and any Zenodo re-deposit is **separate, out of scope here, and thinx-handled** per standing policy. This ADR is the canon-side proposal only.
- **No change** to the bracket framing (ADR-EA-0013), the spine bundling (ADR-EA-0004), the archetype / scale-invariance (ADR-EA-0005), or the orientation-first claim — strictly additive.

## Alternatives considered

1. **Keep methods scattered (Memory + Morals + Means).** Rejected: no coherent locus; the craft is real and recurring, and the scattering *is* the problem this names — the same reasoning that justified the `patterns/` tier and the GCM ratification.
2. **Treat methods as a subset of Morals.** Rejected: conflates *recommended craft* with *obligatory-enforced* constraint. The enforcement cut is exactly what separates them, and collapsing the two loses the graduation dynamic (§3).
3. **Treat methods as identical to `patterns/`.** Rejected: different altitude — patterns are architecture-level (how the system is shaped); methods are operator-level (how the agent works). Peers, not equals; methods cites patterns.
4. **A cross-cutting pattern (like digital-thread) rather than a surface.** Rejected: methods is *durable, harness-agnostic governance content* — it belongs in the discipline core with the other faculties, not as an adjacent pattern. Professional-practice analogy: **tradecraft is a peer faculty to ethics (Morals) and knowledge/judgment (Mind)** — a surgeon's technique is neither their ethics nor their raw knowledge.
5. **A bracketing layer like `mode`/Means.** Rejected: `mode` and Means bracket *because they are swappable seams* (harness-attach and substrate). Methods is durable — it survives harness and substrate swaps — so it is a core discipline, not a bracket.

## References

- [`constructs/mxm/README.md`](../README.md) — the construct definition this extends
- [ADR-EA-0013](ADR-EA-0013-define-mxm-root-file-mode-element.md) — the 4M+1 + bracket framing (structurally unchanged; core membership extended) · [ADR-EA-0005](ADR-EA-0005-clarify-mxm-archetype.md) — the harness archetype · [ADR-EA-0004](ADR-EA-0004-add-mx-modes-as-spine-construct.md) — spine bundling
- [`patterns/`](../../../patterns/) + [ADR-EA-0009](../../../decisions/ADR-EA-0009-introduce-patterns-tier.md) — the altitude peer
- [ADR-EA-0019](../../../decisions/ADR-EA-0019-introduce-governed-context-management-pattern.md) (GCM) · [ADR-EA-0025](../../../decisions/ADR-EA-0025-instance-vsok-derivation.md) (instance VSOK) — prior uses of the "name the homeless recurring shape" discipline
- Mx-Modes Zenodo deposit [`10.5281/zenodo.20349200`](https://doi.org/10.5281/zenodo.20349200) — the co-authored artifact; re-deposit gated on co-author review + thinx
