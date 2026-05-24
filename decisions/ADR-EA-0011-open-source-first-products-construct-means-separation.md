# ADR-EA-0011 — Open-source-first products: instantiate constructs on open-standard Means, never on contributor-owned components

- **Status:** Proposed
- **Date:** 2026-05-23
- **Author:** JD Longmire (drafted by OlogosAI)
- **Reviewers:** Micah Longmire (co-author of the constructs this ADR builds on + owner of the components it protects), @ologos001 (canon prime), Tracy Norrell (NG-AIDE-01 lead operator)
- **Related:** [`aide-canon` Discussion #25](https://github.com/ologos-repos/aide-canon/discussions/25) (MCP integration synthesis) · [`vision-strategy/analysis/mcp-integration/synthesis-paper-v0.2.md`](../vision-strategy/analysis/mcp-integration/synthesis-paper-v0.2.md) · [ng-aide-01#1](https://github.com/ologos-corp/ng-aide-01/issues/1)
- **Ratification trail:**
  - 2026-05-23 (filed): Filed as `Proposed`. The IP-boundary question surfaced during the NG-AIDE-01 build when an MCP-integration synthesis recommended referencing a contributor-owned component (Hermetic's galley) as a canon-level dependency. Micah, the component owner, flagged the boundary directly (NG-AIDE thread, 2026-05-23): *"please don't bring hermetic to NG until I have open sourced it properly. The NG prefix here scares me a bit."* This ADR generalizes the resolution.

## Context

Ologos builds two distinct kinds of artifact:

1. **Constructs** — the durable architectural + methodological IP of the AIDE corpus: AEON (six service planes), OrdSA (ordinal authority layering), MxM, OAgents, the digital-thread pattern (ADR-EA-0009). These are **co-authored** — AEON and OrdSA are both JD + Micah co-authored, published in the AIDE corpus with attribution, and (per the corpus's open posture) intended to be openly available.

2. **Components** — concrete software that *implements* construct patterns: Hermetic (Micah's Go multi-agent platform — galley/gateway/eidolon/oracle-bus/nous), Legate.Studio (Micah's commercial MCP-first PKM), Oracle-MCP, the domain MCPs. These are **contributor-sole-IP** — individual contributors' copyright in specific expression, on the contributors' own open-sourcing and licensing timelines, and in at least one case (Legate) already a commercial product.

The NG-AIDE-01 program is building **product instantiations** (NG-AEON and the subdomain orchestrators) under an Ologos-owned `NG-` namespace. The 2026-05-23 MCP-integration synthesis correctly identified that Micah's MCP corpus contains more mature tool-transport patterns than the bespoke dispatch NG-AIDE-01 had shipped — but its draft recommendation went one step too far: it proposed making Hermetic's galley a *canon-referenced dependency* for AEON's Integration plane.

Two problems with that:

- **It crosses an IP boundary the owner had not opened.** Hermetic is not "open sourced properly" yet (the owner's words); building a product dependency on it presumes a grant the owner is signalling he wants to control.
- **It conflated the construct with the Means.** The valuable, co-owned thing is the *AEON construct* (the plane architecture, the authority model). Hermetic is *one Means* of implementing it. In the 4M + Means governance model the corpus already uses (`mode > meta-harness > means`), Means is explicitly subordinate and swappable. A product needs the construct; it does not need any particular contributor's Means.

The corpus today has no ADR stating how product instantiations relate to (a) the co-owned constructs and (b) contributor-owned components. This ADR establishes that boundary as a framework-level principle, not a one-off resolution.

## Decision

### 1. Open-source-first product methodology

All Ologos product is built **open-source-first, then tuned to individual products.** The open-source artifact — the construct, plus a reference Means built entirely from open standards and the contributor's own open-licensed work — is the primary deliverable. Product-specific tuning (branding, proprietary integrations, commercial packaging, customer-specific configuration) is a layer applied *on top of* the open-source base, not baked into it.

This means the open-source base never carries a dependency that cannot itself be open-sourced. A product can add proprietary tuning; it cannot subtract an IP grant from its open foundation.

### 2. Construct / Means separation

Product instantiations build on the **co-owned AIDE constructs** (the durable value) over a **Means built from open standards** (the swappable substrate). Concretely:

- **Construct layer** — AEON, OrdSA, MxM, OAgents, digital-thread. Co-authored, attributed, openly published. Products instantiate these. Because they are co-authored (AEON: JD + Micah; OrdSA: JD + Micah), building a product on them *includes* the co-authors by construction rather than appropriating from any one of them.
- **Means layer** — the execution substrate (transport, identity, evidence store, orchestration runtime). Built from open standards upstream of any contributor's component. Swappable per the harness-agnostic principle.

A product owes its IP debt to the open constructs and the open standards — never to a single contributor's component.

### 3. Build from the upstream standard, not by reimplementing a contributor's design

There is a meaningful difference between two ways to "build from open-source patterns":

- ✅ **Implement from the upstream standard** — e.g., build an MCP gateway from the [MCP specification](https://modelcontextprotocol.io) + standard libraries; build OAuth 2.1 + DCR from the RFCs; build a message bus from a generic queue.
- ⚠️ **Clean-room a contributor's specific design** — study a contributor's component, then reimplement its specific synthesis (its particular catalog/executor split, its state-root convention, its provenance-field design) in product code.

The first derives from the same public sources the contributor's component *also* derived from. The second reimplements the contributor's intellectual contribution and, even where legally defensible, violates the spirit of contributor ownership. **Products build from the upstream standard.** A contributor's component may be studied as an exemplar to understand the standard better, but the product's Means is authored from the standard, not from the component.

### 4. Contributor-owned components are exemplars, not dependencies — and only on the owner's timeline

A contributor-owned component (Hermetic, Legate, etc.) may be referenced as a **read-only exemplar** in canon analysis — *and only after the owner has open-sourced it on the owner's own terms and license.* Until then it is not referenced as a dependency, not vendored, not forked, and not reimplemented into a product namespace.

If a product genuinely needs a contributor's component as a dependency (not just as a pattern source), that requires an **explicit licensing or contribution arrangement** between the contributor and Ologos Corp, documented, with counsel where commercialization is involved — never an assumed grant.

### 5. Namespace discipline — instantiation connotes "instance of," not "ownership of"

A product namespace prefix (e.g., `NG-`) on an instantiation of a co-owned construct connotes *"this is an instance of the co-owned construct"* — **not** *"the prefixing entity owns the construct."* `NG-AEON` is an instantiation of the co-owned AEON construct; it does not assert Ologos-Corp ownership over AEON, which JD and Micah co-author. Product documentation states this relationship explicitly where a prefix could imply otherwise.

## Consequences

**Effect on the MCP integration synthesis paper (v0.2).** The paper's §10 Recommendation 2 ("Hermetic galley becomes the canon-referenced MCP gateway impl") is retracted to: *"Build AEON's Integration plane from the MCP standard directly; Hermetic galley is an optional exemplar to study only after Micah open-sources it on his terms — not a canon-referenced dependency."* The §7 plane-mapping table rows that point at Hermetic (Integration, Capability) reframe to point at the MCP standard with Hermetic as exemplar-pending. §9 risk R9 (Ollama dependency inherited from galley) is reframed as a Means-implementation choice, not an inherited dependency. The paper's analytical value is unchanged — the plane mapping, the four-way authority model, and the OAuth-inbound pattern all stand on open standards + the co-owned construct.

**Effect on NG-AIDE-01.** NG-AEON's Means (Integration plane MCP gateway, Identity plane OAuth AS, Runtime plane bus) is built from open standards — MCP spec, OAuth/DCR/PKCE RFCs, a generic message bus, Go stdlib — not from Hermetic. The existing bespoke-dispatch v0.1 PRs are unaffected (they were already open-standard HTTP). Hermetic stays out of NG until Micah open-sources it, per his boundary, now codified.

**Effect on construct attribution.** OrdSA is attributed as **JD + Micah co-authored** (correcting an earlier draft that attributed it to JD alone). AEON likewise. Product instantiations carry this co-authorship attribution.

**Effect on contributor relationships.** Micah's stated boundary is honored by construction, not by ad-hoc restraint. The principle protects every contributor's components equally — including future contributors and including OlogosAI-authored components.

**Migration burden.** Low. No product has shipped a contributor-component dependency; the synthesis paper is a draft (one recommendation revises). The principle is forward-looking.

## Alternatives considered

**A. Clean-room reimplement Hermetic's specific design into NG-AEON.** Legally defensible (architecture/ideas aren't copyright-protected; only expression is). Rejected: it reimplements the owner's intellectual contribution against his stated wish, and a NG-AEON that mirrors Hermetic's specific synthesis under an Ologos prefix reinforces exactly the namespace concern the owner raised. Building from the upstream standard achieves the same capability without the appropriation.

**B. Vendor Hermetic with MIT attribution.** Rejected on two grounds: (1) the owner has signalled Hermetic is not "open sourced properly" yet, so the permissive-license assumption may not hold; (2) Legate.Studio is a commercial product built on overlapping patterns, so a vendored-Hermetic NG-AEON could read as competing with a co-founder's commercial work.

**C. Block all NG-AEON Means work until Hermetic is open-sourced.** Rejected as unnecessary. The open standards (MCP, OAuth) are upstream of Hermetic and available now; NG-AEON's Means can be built from them immediately. Waiting on Hermetic would gate product work on a contributor's release timeline for no benefit, since the product shouldn't depend on Hermetic regardless.

**D. Keep the construct/Means coupling implicit (no ADR).** Rejected: the coupling is exactly what caused the synthesis paper to over-reach. Naming the separation as a framework principle prevents the next instantiation from making the same error.

## References

- [`aide-canon` Discussion #25](https://github.com/ologos-repos/aide-canon/discussions/25) — MCP integration synthesis authorial-alignment thread
- [`vision-strategy/analysis/mcp-integration/synthesis-paper-v0.2.md`](../vision-strategy/analysis/mcp-integration/synthesis-paper-v0.2.md) — the synthesis paper this ADR revises (§7, §9, §10)
- [ADR-EA-0008 — reframe corpus authorship](ADR-EA-0008-reframe-corpus-authorship.md) — establishes co-authorship attribution discipline this ADR extends to product instantiations
- [ADR-EA-0009 — digital-thread pattern](ADR-EA-0009-introduce-digital-thread-pattern.md) — names the pattern Hermetic's Eidolon enacts; this ADR clarifies that naming the pattern ≠ depending on the component
- [ng-aide-01#1](https://github.com/ologos-corp/ng-aide-01/issues/1) — NG-AIDE-01 program umbrella
- Micah's MCP corpus (contributor-owned components): [`ologos-repos/Hermetic`](https://github.com/ologos-repos/Hermetic), [`ologos-repos/Legate.Studio`](https://github.com/ologos-repos/Legate.Studio), [`bobbyhiddn/Oracle-MCP`](https://github.com/bobbyhiddn/Oracle-MCP)
- Constructs (co-owned): AEON (`enterprise-platforms/aeon/`), OrdSA (`constructs/ordsa/`)
- The 4M + Means harness-agnostic principle (`mode > meta-harness > means`) — agent-harness-engineering reference architecture
