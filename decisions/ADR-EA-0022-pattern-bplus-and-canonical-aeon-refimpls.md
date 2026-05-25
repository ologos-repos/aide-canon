# ADR-EA-0022 — Pattern B+ adoption discipline; Hermetic and NG-AIDE-01 as canonical AEON reference implementations

- **Status:** Accepted (ratified 2026-05-25 by JD Longmire as canon founder + maintainer per [cross-ai #20](https://github.com/ologos-corp/cross-ai/issues/20) governance, under founder authority; ratifies the (c) strategic call recorded at [`aide-canon#5 comment 4530974480`](https://github.com/ologos-repos/aide-canon/issues/5#issuecomment-4530974480) and incorporates OlogosAI's 2026-05-22 Pattern B+ refinement. OlogosAI canon-prime substantive review remains welcome post-ratification; AEON white paper v0.2 revision queued behind Micah Longmire's co-author read per ADR-EA-0008 corpus-authorship discipline)
- **Date:** 2026-05-24 (drafted)
- **Author:** thinx-Claude (operator-altitude AI-aide; principal = JD Longmire per [ADR-EA-0017](ADR-EA-0017-ai-aide-principal-altitudes.md))
- **Reviewers:** @ologos001 (canon prime — touches AEON spec surface + names canonical reference impls); JD Longmire (founder ratification); Micah Longmire (architectural review at next AEON paper-revision cycle per ADR-EA-0008)
- **Refines:** the Pattern B precedent established by [`constructs/oagents/`](../constructs/oagents/) citing `oagent-core` as out-of-tree reference impl
- **Related:** [`aide-canon#5`](https://github.com/ologos-repos/aide-canon/issues/5) (the originating proposal + OlogosAI's 2026-05-22 Pattern B+ refinement) · [`ologos-repos/Hermetic`](https://github.com/ologos-repos/Hermetic) (first canonical AEON ref impl) · [`ologos-repos/ng-aide-01`](https://github.com/ologos-repos/ng-aide-01) (second canonical AEON ref impl) · [ADR-EA-0008](ADR-EA-0008-reframe-corpus-authorship.md) (AEON paper-revision authorship gate) · [ADR-EA-0015](ADR-EA-0015-introduce-inference-plane.md) (7th plane; both impls build to seven) · [ADR-EA-0019](ADR-EA-0019-introduce-governed-context-management-pattern.md) (consumed by both impls at the Inference plane) · [ADR-EA-0021](ADR-EA-0021-mxm-ordsa-boundary-citation.md) (citation discipline applies to ref-impl cites — they cite peer constructs by reference, not absorption)
- **Ratification trail:**
  - 2026-05-22 (raised): [`aide-canon#5`](https://github.com/ologos-repos/aide-canon/issues/5) — proposed Hermetic as canonical AEON ref impl under Pattern B (out-of-tree cite). OlogosAI's substantive response refined the pattern to **Pattern B+** (out-of-tree cite + conformance-anchored manifest when AEON spec lands) and tightened the cross-construct touch-points (OAgents = partial-not-whole / OrdSA = lineage-not-deployment / MxM = solid).
  - 2026-05-24 (raised): #5 walked through as a strategic call for JD. The decision space gained a complication absent at filing time — **NG-AIDE-01** ([`ologos-repos/ng-aide-01`](https://github.com/ologos-repos/ng-aide-01)) came online as a second canon-aligned AEON impl, built under the latest canon batch (ADRs 0013–0020).
  - 2026-05-24 (ratified, this ADR): JD adopts **(c) — both canonical, role-differentiated.** Pattern B+ as canon-wide adoption discipline; Hermetic and NG-AIDE-01 as the two current canonical AEON reference implementations with complementary roles.

## Context

The AEON white paper specifies a six-plane (now seven-plane per ADR-EA-0015) enterprise control plane, but `enterprise-platforms/aeon/` carries no "build this" surface — the README + paper are present; `spec/` is reserved/empty. Pointing an agent or operator at the canon and saying *"build AEON"* produces no concrete starting point. The canon needs reference implementation citations.

[`constructs/oagents/`](../constructs/oagents/) already established a working pattern: **Pattern B** — cite an out-of-tree reference impl (OAgents cites `oagent-core` at `ologos-corp/oagent-core` as its MIT/BSL-1.1 reference). The reference impl retains independent identity, governance, and release cycle; the canon gets a concrete starting answer.

[`aide-canon#5`](https://github.com/ologos-repos/aide-canon/issues/5) proposed extending this pattern to AEON via Hermetic. OlogosAI's 2026-05-22 response refined Pattern B to **Pattern B+** by adding the conformance-manifest requirement: every reference impl carries a per-deployment manifest against the platform's spec, so the relationship graduates from citation (v0.1) to conformance assertion (v1.0, when spec lands).

Since #5 was filed, a second canon-aligned AEON impl emerged. **NG-AIDE-01** ([`ologos-repos/ng-aide-01`](https://github.com/ologos-repos/ng-aide-01)) was built under the latest canon batch with explicit per-plane traceability to current ADRs:

- Six AEON service planes v0.1 (Identity / Authority / Evidence / Capability Composition / Integration / Orchestration Runtime) — each as a stdlib-Go service mirroring AEON spec idioms
- Inference plane scope (per [ADR-EA-0022's queued sibling](https://github.com/ologos-repos/ng-aide-01/pull/22) building the 7th plane under ADRs 0015 + 0020)
- Three domains (InfOps, DevSecOps, Cyber) standing v0.1
- AICP attestation ingress at the verify-only floor (per [ADR-EA-0018](../constructs/aicp/decisions/ADR-EA-0018-introduce-aicp-construct.md))
- OpenCode runtime harness wired to the AEON MCP gateway
- Canon-aligned by construction; conformance to ADRs 0013 / 0015 / 0019 / 0020 traceable per merged PR

The canon now has two candidates for "canonical AEON reference implementation":

| Candidate | Strength | Status |
|---|---|---|
| **Hermetic** | Production-maturity (295 Go files, MIT, Ologos LLC, used in production via Rhode) + the substantial six-plane mapping + cross-construct refinement work already landed | Mapping landed; conformance manifest queued |
| **NG-AIDE-01** | Canon-fidelity-by-construction under the latest ADR batch; explicit traceability of every plane to current canon | Build-in-flight; conformance manifest queued |

Forcing a "winner" between them discards real signal. Pattern B+ as ratified admits multiple conformant impls via per-deployment conformance manifests — the canon-coherent move is to use that admission cleanly.

## Decision

### Part 1 — Pattern B+ is the canon-wide adoption discipline for reference impls

Every canon-cited reference impl is governed by:

1. **Out-of-tree.** The impl lives at its own repository, retaining independent identity, governance, and release cycle. The canon cites; it does not absorb. (This composes with [ADR-EA-0021](ADR-EA-0021-mxm-ordsa-boundary-citation.md) — discipline surfaces and platform surfaces cite peer artifacts; they do not re-author them.)
2. **Cited from the canon's platform README.** The relevant `enterprise-platforms/<platform>/README.md` carries the citation with a one-paragraph statement of the impl's role and a pointer to its conformance manifest.
3. **Conformance manifest required.** The impl maintains a `docs/canon-mapping.md` (or equivalent) at its own repo. The manifest carries tables mapping the impl's subsystems against the canon's relevant axes (see Part 3 for the AEON-specific axes).
4. **Graduation from Pattern B to Pattern B+.** When the platform's `spec/<platform>-N.M.yaml` lands, the conformance manifest gains an explicit conformance-assertion section against that spec. Pattern B is the v0.1 phase (cite + manifest tables); Pattern B+ is the v1.0 phase (cite + manifest tables + conformance-assertion against ratified spec).
5. **Multiple canonical impls admitted by construction.** A platform may have N>1 canonical reference implementations under Pattern B+. Role-differentiation in each impl's citation block (in the platform README) names what each impl exemplifies. The conformance manifests differentiate substantively.

### Part 2 — Hermetic and NG-AIDE-01 are the canonical AEON reference implementations

Two canonical impls under Pattern B+:

| Impl | Role | Repo | Conformance manifest |
|---|---|---|---|
| **Hermetic** | **Production-maturity exemplar.** Proves the AEON patterns at scale; six-plane mapping ratified collaboratively with OlogosAI 2026-05-22; production use via [Rhode](https://github.com/bobbyhiddn/Rhode); MIT-licensed; Ologos LLC-owned. Carries the prior claim + the substantial mapping work already done. | [`ologos-repos/Hermetic`](https://github.com/ologos-repos/Hermetic) | `docs/canon-mapping.md` (per [`Hermetic#37`](https://github.com/ologos-repos/Hermetic/issues/37)) — OAgents-controls × Eidolon-coverage, OrdSA-axis × Hermetic-positioning, MxM-surfaces × Hermetic-subsystems |
| **NG-AIDE-01** | **Canon-fidelity exemplar.** Built under the latest canon batch (ADRs 0013 / 0015 / 0017 / 0019 / 0020) with explicit traceability of every plane to current ADRs. Six AEON planes v0.1 + three domains + AICP ingress + OpenCode harness. Canon-aligned by construction; demonstrates the canon's "build this" answer at the current canon vintage. | [`ologos-repos/ng-aide-01`](https://github.com/ologos-repos/ng-aide-01) | `docs/canon-mapping.md` — same shape as Hermetic's, traced against the current canon batch |

Both impls cited from `enterprise-platforms/aeon/README.md` (this PR updates the README; see Consequences §Immediate).

The two roles are **complementary, not redundant**. Hermetic's production-maturity is the empirical proof that the AEON pattern works at scale; NG-AIDE-01's canon-fidelity is the formal proof that the current-vintage canon is buildable. Neither subsumes the other; both signals matter; the canon admits both.

### Part 3 — Conformance manifest axes for AEON-platform impls

Every AEON reference impl's `docs/canon-mapping.md` carries tables along the following axes (extending OlogosAI's 2026-05-22 framing):

| Axis | Table shape | Purpose |
|---|---|---|
| **AEON service planes × impl subsystems** | 7 planes (post-ADR-EA-0015) × the impl's subsystems | Names which subsystem realizes which plane; flags coverage gaps |
| **OAgents controls × impl coverage** | All 26 OAgents controls (current standard version) × {implemented, partial, not-addressed, addressed-by-other-subsystem} per impl-subsystem | Names the impl's behavioral-envelope conformance precisely |
| **OrdSA axis × impl positioning** | O0–O6 ordinal layers × the impl's positioning at each | Distinguishes *ordinal-pattern-aligned* (using OrdSA's escalation pattern at one altitude) from *full OrdSA deployment* (positioned across O0–O6) |
| **MxM surfaces × impl subsystems** | Mission / Mind / Morals / Memory / Means × the impl-subsystems that enact each surface | Names where MxM's discipline surfaces live in the impl |

(Optional, when the impl uses) AICP: ingress mechanism + verify chain + reputation-mapping disposition.

### Part 4 — Adding future reference impls

Any AEON-conformant impl can request canon citation by:
1. Authoring a Pattern B+ conformance manifest at its own repo (tables per Part 3)
2. Opening an aide-canon PR adding a citation block to `enterprise-platforms/aeon/README.md`
3. Filing an ADR refinement of this ADR naming the new impl's role and citing its manifest

The dual-canonical model in Part 2 admits N>2 by the same mechanism. There is no "exclusive" canonical claim — Pattern B+ is plural by construction.

## Consequences

### Immediate (this PR)

- **`decisions/ADR-EA-0022-pattern-bplus-and-canonical-aeon-refimpls.md`** — this ADR, lives at top-level `decisions/` (canon-wide).
- **`enterprise-platforms/aeon/README.md`** — the "Reference implementation" section is updated to cite both Hermetic and NG-AIDE-01 with role-differentiated blocks; the "(proposed)" qualifier on Hermetic is removed; the Pattern B+ adoption discipline is named with a pointer to this ADR.
- **`decisions/README.md`** index — adds ADR-EA-0022 entry.

### Downstream (OlogosAI lane — build/integration)

- **Hermetic-side:** `docs/canon-mapping.md` per [`Hermetic#37`](https://github.com/ologos-repos/Hermetic/issues/37) — table form per Part 3.
- **NG-AIDE-01-side:** `docs/canon-mapping.md` — same shape, traced against current canon batch.

### Downstream (canon side)

- **AEON spec (`enterprise-platforms/aeon/spec/aeon-0.1.yaml`)** — queued; when authored, the Pattern B+ "+" half lands for both impls (conformance-assertion sections in their manifests). AEON paper revision (queued behind Micah's read per ADR-EA-0008) covers the spec at the same time as §13 Inference + the vocabulary refresh.
- **Similar audit-and-adopt cycles for AIDEX and OAAD** — open follow-on if reference impls exist in the Ologos / JD repo space (per #5 sub-work list).

### Queued (paper revisions)

- **AEON paper v0.2 revision** (queued behind Micah's read per ADR-EA-0008) — adds a §"Reference implementations" section naming both impls under Pattern B+. Same revision cycle as the §13 Inference addition + AI-aide vocabulary refresh + governed-context-management cite from this session's batch.

## Behavioral conformance

An AEON reference impl is **Pattern B+ conformant** if:

1. **Out-of-tree.** Maintained at its own repository with independent identity, governance, and release cycle.
2. **Cited.** A citation block exists in `enterprise-platforms/aeon/README.md` naming the impl, its role, and a pointer to its conformance manifest.
3. **Manifest authored.** A `docs/canon-mapping.md` (or equivalent) at the impl's repo carries the tables in Part 3.
4. **Manifest currency.** The manifest is versioned alongside impl releases; significant impl changes that affect plane coverage update the manifest in the same PR.
5. **(Pattern B+, when spec lands)** A conformance-assertion section in the manifest cites `enterprise-platforms/aeon/spec/aeon-0.1.yaml` and names per-section conformance status.

## Alternatives considered

1. **(a) Single canonical (Hermetic OR NG-AIDE-01).** Rejected. Forces a choice that loses signal — Hermetic's production-maturity and NG-AIDE-01's canon-fidelity are complementary, not in conflict. The canon-coherent move under Pattern B+ (which OlogosAI's own refinement admits multiple manifests) is to recognize both.
2. **(b) Defer until AEON spec lands.** Rejected. Leaves the canon without a "build this" answer for months until the spec ships. The EIF reference-impl pattern (thinx as ref-impl named at pattern ratification) demonstrates the value of naming ref impls before specs ossify — the named impls then *inform* spec authoring, rather than being retrofitted after.
3. **(c) Pattern A (in-tree).** Rejected. Both Hermetic and NG-AIDE-01 are independently substantial repos with their own identity + governance + release cycle. Absorbing them into the canon collapses those properties for no gain. Pattern B+ already addresses the citation discipline.
4. **(d) Separate ADRs per impl.** Rejected. The Pattern B+ rule is the same across both; one ADR + a table of current realizations is canon-coherent. New impls in the future file refinement ADRs against this one (Part 4 mechanism).

## References

- [`aide-canon#5`](https://github.com/ologos-repos/aide-canon/issues/5) — originating proposal + OlogosAI's Pattern B+ refinement
- [`ologos-repos/Hermetic`](https://github.com/ologos-repos/Hermetic) — first canonical AEON ref impl
- [`ologos-repos/ng-aide-01`](https://github.com/ologos-repos/ng-aide-01) — second canonical AEON ref impl
- [`ologos-repos/Hermetic#37`](https://github.com/ologos-repos/Hermetic/issues/37) — Hermetic canon-mapping doc tracker
- [`constructs/oagents/`](../constructs/oagents/) — Pattern B precedent (cites `oagent-core` as out-of-tree ref impl)
- [ADR-EA-0008](ADR-EA-0008-reframe-corpus-authorship.md) — AEON paper-revision authorship gate
- [ADR-EA-0015](ADR-EA-0015-introduce-inference-plane.md) — 7th service plane; both impls build to seven
- [ADR-EA-0019](ADR-EA-0019-introduce-governed-context-management-pattern.md) — Governed Context Management pattern; both impls consume the Inference catalog contract
- [ADR-EA-0020](ADR-EA-0020-amend-inference-plane-catalog-contract.md) — catalog contract; both impls realize
- [ADR-EA-0021](ADR-EA-0021-mxm-ordsa-boundary-citation.md) — citation discipline; ref-impl cites use the same import-by-reference mechanism
- [`enterprise-platforms/aeon/`](../enterprise-platforms/aeon/) — the platform this ADR provides reference impls for
