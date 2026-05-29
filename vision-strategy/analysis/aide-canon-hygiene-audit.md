# Vocabulary + entity-distinction hygiene audit — aide-canon

**Status:** PREP-phase audit (2026-05-29). Lands together with PURSUE-1 edits in the same PR.
**Scope:** Audit aide-canon's markdown corpus for conflations against the 2026-05-29 entity-distinction clarifications (Ologos ecosystem ≠ NG-AIDE-01 ≠ thinx; NG-AIDE-01 has its own AEON; cross-entity federation, not within-fleet altitude composition). Vocabulary corrections (Skill/Tool/Workflow/Capability/Envelope per [ng-aide-01 PR #59](https://github.com/ologos-repos/ng-aide-01/pull/59) §5.1) are **deferred** to a post-ratification PURSUE-2 pass.
**Files audited:** 126 markdown files under `aide-canon:main`.
**Companion to:** [ng-aide-01#60](https://github.com/ologos-repos/ng-aide-01/pull/60) — same audit pattern applied instance-side first.

---

## Headline finding

**aide-canon is structurally cleaner than ng-aide-01 was on this axis.** The heavy lifting was already done by [ADR-EA-0016](../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md) (AI-aide / MyAide vocabulary, 2026-05-24) and [ADR-EA-0017](../../decisions/ADR-EA-0017-ai-aide-principal-altitudes.md) (principal-altitudes, 2026-05-24). The vocabulary map already names principal-altitudes; ADRs already use *AI-aide* in their recent ratifications; constructs already use *NG-AIDE-01* as a reference-implementation pointer rather than as a synonym for the Ologos ecosystem.

Two small refinements close out the cycle:
1. The vocabulary map needs an explicit **entity-boundary** clarification — ADR-EA-0017's complementarity is *cross-entity*, not *within-fleet*. Today's clarification refines (not amends) the ADR's framing.
2. A typo in `patterns/README.md` — *"Ologos/Hermit ecosystem"* → *"Ologos/Hermetic ecosystem"*.

## What the audit confirms

| Correction | aide-canon status | Edits needed |
|---|---|---|
| **1. Entity distinction (Ologos ecosystem ≠ NG-AIDE-01 ≠ thinx)** | Mostly clean. `ng-aide-01` consistently referenced as instance / reference impl, not as Ologos operational fleet. OlogosAI consistently used as canon-prime authorship attribution. Zero files conflate Ologos with ng-aide-01 directly (`grep` finds no cases where the same file claims ng-aide-01 is part of the Ologos ecosystem). | **None on the conflation axis.** One clarifying addition to the vocabulary map. |
| **2. NG-AIDE-01 has its own AEON** | Clean. `enterprise-platforms/aeon/README.md` correctly treats AEON as the canon construct and NG-AIDE-01 as a reference impl that "builds to the 7-plane shape." No conflation. | **None.** |
| **3. AI-aide / MyAide vocabulary (ADR-EA-0016)** | Ratified May 24; new content uses it. Existing canon artifacts retain prior vocabulary until next revision per ADR-EA-0016 §Consequences ("Existing artifacts retain their current prose until their next revision"). | **None this cycle.** Opportunistic update as artifacts are touched. |
| **4. Principal-altitude framing (ADR-EA-0017)** | Vocabulary map has it; one clarification on cross-entity vs within-fleet character of the complementarity (today's refinement) | **One vocabulary-map addition.** |
| **5. Skill / Tool / Workflow / Capability / Envelope vocab (PR #59 §5.1)** | Pending JD ratification of the §5.1 anchors. | **Deferred to PURSUE-2.** When ratified, vocabulary-map external columns get populated for LangChain / Anthropic / OpenAI / ADK / MS Copilot / Manus / MCP / A2A / OTel per PR #59 §5.3(2). |

## Per-file findings (PURSUE-1 scope)

### 1. `vision-strategy/analysis/aide-vocabulary-map.md` — clarifying addition

Add a new sub-section **"Entity boundaries (per 2026-05-29 clarification)"** after the "Future principal-altitudes" sub-section (line ≈ 182), capturing:

- The four entities now operating in the AIDE space (canon, Ologos ecosystem, NG-AIDE-01 deployment, thinx-as-personal-AIDE) and their currently-instantiated AI-aides
- That ADR-EA-0017's complementarity is **cross-entity**, not **within-fleet**
- That OlogosAI plays two composed entity-roles: canon-prime (corpus-altitude) and AEON for the Ologos ecosystem
- The cross-entity federation contract (`entity_id × principal_chain × verb_class`) — observe + recommend cross freely; direct requires receiving-entity-principal attestation
- Reference forward to ng-aide-01 PR #59 §6.3 #9 for the contract's working specification

This is a **clarifying refinement** of ADR-EA-0017's framing, not an amendment of it. No new ADR needed; ADR-EA-0017 already admits future principal-altitudes and the entity-boundary discipline is downstream of it.

### 2. `patterns/README.md` — typo fix

Line 32: *"in the broader Ologos/Hermit ecosystem"* → *"in the broader Ologos/Hermetic ecosystem"*

One-character correction (Hermit → Hermetic). The referent is `ologos-repos/Hermetic` (Micah's orchestrator).

## Out of PURSUE-1 scope (audited and left untouched)

- **All ADRs** (~28 in canon decisions/ + per-construct decisions/) — historical record; refinements happen via new ADRs, not in-place edits. The 2026-05-29 entity-boundary refinement is captured in the vocabulary map (per ADR-EA-0017's own future-admit clause) without requiring a new ADR.
- **All construct READMEs** (DEA, OrdSA, MxM, OAgents, AICP, foundation/AIDK/HCAE/RLEG, enterprise-platforms/AEON/AIDEX/OAAD) — audited; all use NG-AIDE-01 as instance / reference impl correctly; OlogosAI references are attribution-only where present.
- **OAgents reference-implementation files** (`constructs/oagents/reference/*`) — these are example QA-agent implementations FOR the Ologos ecosystem; "Ologos ecosystem" usage is correct in this context.
- **Published white papers** (AEON, AIDEX, DEA, HCAE, MxM) — paper revisions are Micah-gated per [ADR-EA-0008](../../decisions/ADR-EA-0008-reframe-corpus-authorship.md); excluded from this hygiene pass. Vocabulary refresh queued for the next paper-revision cycle.
- **`hermetic-engagement/` discussion threads** — historical cross-fleet dialogue; ratification record, not canon prose.

## Out-of-scope-but-queued for future cycles

- **PURSUE-2 (post-PR #59 §5.1 ratify):** vocabulary-map external columns (LangChain / Anthropic / OpenAI / ADK / MS / Manus / MCP / A2A / OTel) populated using PR #59's industry survey as source material; sota-survey/vendor-stacks + oss-frameworks + standards-bodies entries land in parallel.
- **Canon-side ADR candidate** — formalize the `<deployment-prefix>-<subdomain>` naming convention (e.g., NG-AEON for NG-AIDE-01; OL-AEON for Ologos ecosystem). Cheap to write; not blocking; could fold into a single small ADR. Optional follow-up.
- **AIDE-AF (DEA's AI-specific extension)** — referenced in `constructs/dea/README.md` as "forthcoming." Authoring is a separate cycle.

## What this PR will do

1. Land this audit doc + the two edits as a single PR.
2. Per canon discipline (CONTRIBUTING + ADR-EA process): cross-ai #59 notice posted after merge so thinx + other contributors see the refinement.

## Provenance

v0.1 — 2026-05-29, PREP phase of repo-hygiene cycle. Triggered by JD's 2026-05-29 clarifications (thinx as non-fleet collaborator; NG-AIDE-01 as separate full AIDE deployment with own AEON; OlogosAI as AEON for Ologos ecosystem only + canon-prime). Companion to [`ng-aide-01#60`](https://github.com/ologos-repos/ng-aide-01/pull/60) (instance-side hygiene PR).
