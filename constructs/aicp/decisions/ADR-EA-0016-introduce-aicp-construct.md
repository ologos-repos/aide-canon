# ADR-EA-0016 — Introduce AICP (Agent Identity Card Protocol) as a Tier-3 construct

- **Status:** Proposed
- **Date:** 2026-05-24
- **Author:** Micah Longmire (AICP construct, sole) — *ADR drafted by OlogosAI on JD Longmire's direction for maintainer ratification*
- **Reviewers:** @jdlongmire (canon maintainer — ratification) · @bobbyhiddn (Micah Longmire — AICP author)

## Context

The canon's Tier-3 `constructs/` holds four peer methodological patterns — **DEA** (EA coherence), **OrdSA** (authority/evidence), **MxM** (harness composition), **OAgents** (agent domain model) — each a standalone, model-agnostic pattern that the enterprise-platforms instantiate (top-level [README](../../../README.md), [`constructs/README.md`](../../README.md)).

A fifth pattern now qualifies. The **Agent Identity Card Protocol (AICP)** — authored by **Micah Longmire**, published by **Ologos LLC under the MIT License** at [`ologos-repos/AICP`](https://github.com/ologos-repos/AICP) (v0.1.0 Draft, spec + 5 JSON schemas) — defines **platform-mediated agent identity, phase-gated tool injection, and work-lifecycle management**. It sits above MCP (tool transport) and alongside A2A (peer discovery), filling a gap neither addresses: a *platform* issues agent identities (Cards), controls which tools are available as a function of agent state, and (in its federation profile) lets Cards carry cryptographically-verifiable, portable reputation across platforms.

To date AICP has appeared in the canon only **indirectly**, via the [Theseus Agent Thesis](../../../related-work/theseus/) (Micah Longmire, 2026-05-20) in `related-work/`. The Theseus README already names AICP as "a separate artifact published by Ologos LLC under the MIT License" and "a candidate identity-and-memory primitive that an OrdSA-conformant agent at O3 could carry" ([`related-work/theseus/README.md`](../../../related-work/theseus/README.md)). The thesis presents AICP explicitly as an *archetype* — i.e., the thesis is the theory, AICP is one protocol instantiation of it.

This positioning understates AICP. It is no longer adjacent theory: it is a **published, independently-implementable open protocol** with a normative spec, JSON schemas, conformance levels (`AICP-Core` … `AICP-Full`), and a reference implementation ([CrewPort](https://crewport.ai), Ologos LLC, private). That is the same shape as **OAgents** — a schema-first, model-agnostic *standard* with a separately-hosted reference implementation. AICP belongs at the constructs tier, peer to OAgents, where OAgents patterns the agent's *behavioral envelope* and AICP patterns the agent's *portable identity and reputation*.

Admitting a new construct is an ADR-worthy, non-waivable trigger under the canon's inherited governance (top-level [README §Governance](../../../README.md); [ADR-EA-0001](../../../decisions/ADR-EA-0001-adopt-ordsa-development-process.md)) — it adds a major construct and changes the README's construct enumeration and tier map. This ADR is the structural record; supporting analysis is in [`ologos-repos/ng-aide-01:docs/research/aicp-deep-dive.md`](https://github.com/ologos-repos/ng-aide-01/blob/main/docs/research/aicp-deep-dive.md).

## Decision

**Admit AICP to Tier 3 (`constructs/`) as a fifth peer methodological construct, alongside DEA · OrdSA · MxM · OAgents.**

1. **What AICP patterns.** *Portable agent identity and reputation* — the platform-issued **Card** as the unit of identity, phase-gated tool injection as the access model, and (federation profile) third-party-verifiable attestations as portable reputation. Where OAgents answers *what an agent is* (typed object + behavioral envelope), AICP answers *who an agent is across platforms, and what it has earned*. The two are peers; neither subsumes the other.

2. **Six protocol layers** (per the published spec): L1 Enrollment + L2 Tool Injection are CORE; L3 Discovery, L4 Engagement, L5 History, L6 Federation are optional profiles. Signing, JWKS publication, and attestations are L6 Federation (asymmetric — EC P-256/Ed25519; symmetric keys prohibited for federation).

3. **Authorship is sole Micah Longmire.** Consistent with the Theseus thesis and the `ologos-repos/AICP` repository (Ologos LLC / Micah Longmire). This differs from the corpus-level co-authorship and from MxM's and OAgents' joint authorship; per [ADR-EA-0008](../../../decisions/ADR-EA-0008-reframe-corpus-authorship.md), artifact-level authorship is recorded at the artifact and may differ from corpus authorship.

4. **Canonical artifact is a vendored snapshot with a living upstream source.** A pinned, verbatim snapshot of the AICP spec + JSON schemas is vendored at `constructs/aicp/spec/` (AICP v0.1.0 Draft, `ologos-repos/AICP@f85a76c`), carrying the upstream **MIT** `LICENSE` in the construct directory — the embedded-license convention OrdSA and OAgents already use, which isolates it from the canon's CC BY 4.0. The **living source** remains the public repo `ologos-repos/AICP`; the snapshot may lag it. Vendoring was authorized by the author (full-use approval, 2026-05-24); MIT permits redistribution with attribution. This gives full OAgents parity (canon-resident, offline/air-gap-readable spec) while pinning manages drift.

5. **Reference implementation stays decoupled.** CrewPort (the reference implementation, private, All-Rights-Reserved) is referenced as the reference implementation and **not absorbed** into the canon — the same "Theseus-pattern decoupling" OAgents uses with `oagent-core` ([`constructs/oagents/README.md`](../../oagents/README.md)).

6. **Theseus stays allied; the coupling splits.** The Theseus *thesis* remains allied related-work (Micah's master's-thesis theory paper, under his own terms). AICP *the protocol* graduates to a construct. The Theseus README gains a cross-reference to AICP's construct home. In the canon this change is **additive** (Theseus's `related-work/` placement is unchanged); the literal `Theseus (AICP)` allied-row coupling that needs reconciling lives in the downstream working map [`ologos-repos/ng-aide-01:vision-strategy/aide-model.md`](https://github.com/ologos-repos/ng-aide-01/blob/main/vision-strategy/aide-model.md), reconciled in lockstep with this ADR.

### Concrete changes this PR carries

- New `constructs/aicp/README.md` (construct entry, modeled on `constructs/oagents/README.md`) + this ADR + a `decisions/README.md` index entry.
- Vendored AICP spec snapshot at `constructs/aicp/spec/` (`AICP-v0.1.md` + 5 schemas + `spec/README.md` provenance) and the MIT `constructs/aicp/LICENSE` (§4).
- Top-level [README](../../../README.md): constructs tier-table row (`DEA · OrdSA · MxM · OAgents` → `· AICP`); the "four peer methodological patterns" detailed table gains an AICP row ("four" → "five"); reading-order "Constructs (harness + agent)" gains AICP (identity).
- [`constructs/README.md`](../../README.md): "Four constructs" → "Five"; AICP row in the Members table; composition note.
- [`related-work/theseus/README.md`](../../../related-work/theseus/README.md): cross-reference AICP's new construct home.

It does **not**: absorb CrewPort (§5); mint a Zenodo deposit (deposits are thinx-Claude's lane); change the canon's governance process; or integrate AICP into any NG-AIDE-01 build (tracked separately).

## Consequences

- **The constructs tier grows from four to five.** The "four peer methodological patterns" framing in both READMEs is updated. Adopters who cited "four constructs" are not contradicted — the four remain, AICP is added.
- **AEON's relationship to AICP becomes nameable.** AEON (Tier-4 platform) can be described as *consuming* AICP — its Identity plane verifying an AICP Card/attestation and minting an in-plane authority token off attested attributes — exactly as AEON instantiates OrdSA's authority model. This is the "informs the spine" relationship made structural. (The integration itself is downstream and out of scope here.)
- **Cross-construct boundary with OAgents is clarified, not blurred.** OAgents = behavioral envelope (what an agent does, bounded); AICP = portable identity + reputation (who an agent is, across platforms). Both compose under MxM/OrdSA at enterprise scale.
- **License surface is mixed but isolated.** The canon is CC-BY; AICP is MIT in its own repo. By referencing rather than vendoring (§4), no MIT content lands in the CC-BY tree in this PR. If a snapshot is later vendored, it carries its own LICENSE in `constructs/aicp/` (the OAgents/embedded-license pattern).
- **Migration burden is low.** No existing construct's scope shifts; no platform paper is edited; the change is additive plus two README touch-ups and one cross-reference.

## Alternatives considered

1. **Keep AICP in `related-work/` (status quo, un-split).** Rejected: contradicts the maintainer's direction to canonize, and undersells a published MIT standard with a normative spec, schemas, conformance levels, and a reference implementation. Related-work is for *adjacent* research; AICP is a buildable, independently-implementable pattern.

2. **Fold AICP under AEON's Identity plane (Tier 4, enterprise-platforms).** Rejected: AEON's Identity plane is *in-plane authority* (local, short-TTL, symmetric); AICP is *cross-platform identity/reputation* (portable, asymmetric, third-party-verifiable). Folding AICP into AEON conflates the portable passport with the local visa and strips AICP of its standing as an independent standard that non-AEON platforms can implement. AEON *consumes* AICP; it does not *contain* it.

3. **Vendor the AICP spec + schemas into `constructs/aicp/spec/` (full OAgents parity).** **Adopted** (this PR), following the author's full-use approval (2026-05-24). A pinned MIT snapshot is vendored with its own per-directory `LICENSE`, isolating it from the canon's CC BY 4.0; the living source stays upstream. Drift is managed by pinning the snapshot to a version + commit. (Initially this ADR admitted the construct by reference only; the snapshot was added once the author cleared the license-interaction question.)

4. **Admit AICP as a new pattern under `patterns/` (like digital-thread).** Rejected: `patterns/` holds cross-cutting patterns that traverse tiers/constructs (e.g., digital-thread, epistemic-integrity-floor). AICP is a self-contained methodological standard with its own spec and conformance levels — the constructs tier is the correct altitude, peer to OAgents.

## References

- [ADR-EA-0001](../../../decisions/ADR-EA-0001-adopt-ordsa-development-process.md) — the governance process this ADR follows (PR-first; append-only ADRs)
- [ADR-EA-0003](../dea/decisions/ADR-EA-0003-expand-corpus-to-include-dea.md) — the construct-introduction precedent (admitting DEA); same shape, ADR filed in the new construct's `decisions/`
- [ADR-EA-0008](../../../decisions/ADR-EA-0008-reframe-corpus-authorship.md) — artifact-level vs corpus-level authorship discipline (basis for sole-Micah attribution)
- [`related-work/theseus/`](../../../related-work/theseus/) — the Theseus Agent Thesis (Micah Longmire), which introduces AICP as an archetype; stays allied
- [`ologos-repos/AICP`](https://github.com/ologos-repos/AICP) — the authoritative AICP spec + schemas (MIT, Ologos LLC), the canonical artifact this construct references
- [CrewPort](https://crewport.ai) — the reference implementation (private), decoupled per the Theseus/OAgents pattern
- [`ologos-repos/ng-aide-01:docs/research/aicp-deep-dive.md`](https://github.com/ologos-repos/ng-aide-01/blob/main/docs/research/aicp-deep-dive.md) — the supporting deep-dive analysis (AICP↔AEON-Identity comparison; placement options)
