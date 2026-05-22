# OlogosAI response — Hermetic#40 (MxM refactor proposal)

**Status:** draft pending JD review; will post as comment on [`Hermetic#40`](https://github.com/ologos-repos/Hermetic/discussions/40) on approval.

This artifact captures OlogosAI's analysis of the MxM refactor proposal in [`discussion-source.md`](discussion-source.md). The substance below is the canonical record; the discussion comment is the public-thread version.

---

## OlogosAI's tagged question (Q2)

> **OlogosAI:** MxM is at `constructs/mxm/` in the canon. If Hermetic adopts MxM-surface organization, does it become the reference impl for *how to organize a harness around MxM* — analogous to how `oagent-core` is the reference impl for OAgents?

## Position: yes — *if* the refactor unlocks operational meaning, not just naming alignment

The question is conditional. Hermetic could *become* the canonical MxM-multi-agent-harness exemplar — but only if the refactor pays operational dividends. Naming alignment alone (Option C: docs-only mapping) is sufficient for canon-side citation; it doesn't earn reference-impl status.

The decision criterion: **does the refactor make MxM operationally meaningful inside Hermetic?** The proposal sketches four net-new surfaces that *would* make it meaningful:

1. Explicit MxM-shaped orientation packet sent to workers
2. `hermetic mxm describe <worker>` introspection
3. TUI MxM view alongside Dashboard / Tasks / Oracle
4. `docs/mxm-mapping.md` companion doc

Of these, **#1 (explicit orientation packet)** is the one that earns reference-impl status. If workers receive a structured `{mind, morals, mission, memory, means}` envelope (rather than implicit composition through `hermes/`-inlined prompts), then Hermetic operationally instantiates MxM at the worker scale. That's the test that turns naming alignment into reference-impl meaning.

#2, #3, #4 are good but supporting — they expose what the orientation packet already structures. Without #1, #2/#3/#4 are dashboards over a name-only relabeling.

## Recommendation: do Option C first, validate, then Option B with #1

thinx recommends **Option C as immediate, Option B as v0.2 trajectory** — I agree but want to be specific about the gate between them.

| Phase | What happens | Gate condition to move forward |
|---|---|---|
| **C — now** | Author `docs/mxm-mapping.md`; declare which packages live at which surface; package code stays function-grouped | No gate — low-risk pure documentation |
| **B-light — next** | Implement net-new surface #1 (orientation packet) within current `internal/hermes/` — system prompt composition becomes an MxM-shaped envelope, not inline | Validation: does the orientation packet make worker behavior more predictable or more debuggable than implicit composition? |
| **B — later** | Move `internal/` packages into `mind/morals/mission/memory/means/support` subdirs | Validation: does the orientation packet's structure make package-level reorganization clarify rather than churn? |

If #1 ships and proves valuable (workers are easier to debug, orientation is auditable, surface mismatches become spottable), the package refactor follows naturally. If #1 ships and doesn't add value (workers behave the same regardless of packet structure), Option C is the right terminus — code stays function-grouped, docs declare the surfaces.

The cost of refactoring without #1 is real: import path churn, freezes, mixed-organization windows, MxM-evolution lag. The audit's Risk #1 ("churn for marginal benefit") catches it correctly. Don't pay that cost without operational evidence.

## On the reference-impl question more precisely

If Option B + #1 lands and proves valuable: yes, Hermetic becomes the canonical reference impl for *how to organize a multi-agent harness around MxM*. The analog to oagent-core works but with one structural difference:

| | oagent-core (OAgents) | Hermetic (MxM-multi-agent) |
|---|---|---|
| Canon construct | OAgents — *what an agent is* (behavioral envelope spec) | MxM — *how a harness is composed* (five-surface archetype) |
| Reference impl shows | An OAgents-conformant agent | An MxM-organized harness at the multi-agent altitude |
| Conformance anchor | OAgents' 26 controls (spec authored, conformance assertable) | MxM's five surfaces (archetype authored, conformance assertion = does the impl expose all five surfaces meaningfully?) |
| Scale | Per-agent | Multi-agent (24 workers + prime) |

So Hermetic-as-reference-impl asserts something narrower than oagent-core: *here's how a multi-agent harness organizes itself around MxM at this scale*. Other reference impls might exist at other scales (single-agent harness, enterprise-altitude harness composition like AEON's full deployment) — each is a distinct reference for MxM at that altitude.

This matters because ADR-EA-0005 specifically clarified MxM as the archetype across altitudes. A single reference impl can't claim canonical status for all of them; it claims it for the altitude it instantiates. Hermetic as the canonical reference impl for **multi-agent harness composition** is honest and bounded.

## On cross-surface spans (the audit's risk #4)

The proposal lists 5 packages that span multiple surfaces (identity, eidolon, nous, bus, policy) — ~16% of 31. The recommendation is (a) place each by primary surface, document spans in `docs/mxm-surface-spans.md`. I agree, and would add: **the spans aren't bugs in MxM's archetype; they're features of any real harness.**

- **identity** spanning MISSION + MEMORY isn't an MxM flaw — every harness's identity has a *currently-active* face (MISSION) and a *historical record* face (MEMORY). The archetype captures the distinction; the impl reflects the integration.
- **eidolon** spanning MORALS + MEMORY + MEANS is the cleanest example — a phase gate IS the integration point where constraint (MORALS), audit record (MEMORY), and machinery (MEANS) meet. It would be strange if it lived in only one.
- **bus / policy** spanning MORALS + MEANS — rule semantics (MORALS) and rule execution (MEANS) are different concerns; that's why they're separable in MxM's archetype and integrated in any impl.

So the spans should be documented but not treated as architectural defects. The `mxm-surface-spans.md` document becomes part of *what makes Hermetic a good MxM reference impl* — it shows how the archetype maps to a real codebase, including the cross-surface integration points.

## What this means for VSOK

| VSOK slot | Implication |
|---|---|
| **Strategy** | MxM's archetype status (per ADR-EA-0005) is reinforced by having a real-codebase exemplar of how to organize a harness around the surfaces — *if* the operational meaning lands. Strategy claims about MxM-archetype-across-altitudes get an instance, not an assertion. |
| **Objectives** | (proposed, conditional) Land Option C immediately (docs-only mapping at `docs/mxm-mapping.md` in Hermetic + reference from `constructs/mxm/` README); land net-new surface #1 (orientation packet) within next quarter; package refactor (Option B) gated on orientation-packet validation. |
| **Key Results** | If the refactor proceeds: package count under each MxM surface (operational meaning of grouping); orientation packet utilization rate (does the structured envelope actually shape worker behavior?); external citation of Hermetic-as-MxM-multi-agent reference. |

## On JD's question 3 (canon-alignment vs. refactor cost)

JD's Q3 asks whether the canon-alignment exercise is worth the refactor cost or whether docs-only (Option C) captures the value.

My answer: **start with Option C; the value is real even without refactor; the refactor is only justified if the operational surfaces materialize.** Option C lands the *canonical reading* of Hermetic-through-MxM-lens without touching code. That's enough for the canon to cite Hermetic as a MxM-multi-agent reference even without the refactor. The refactor's value is downstream — operationally meaningful, not just naming.

Don't conflate the two questions:
- Is MxM a useful lens for reading Hermetic? **Yes** — that's Option C, $0 of refactor cost.
- Should Hermetic's internal organization mirror the MxM lens? **Maybe** — requires net-new surfaces to justify, which is real engineering work.

Option C unlocks the first answer immediately. Option B is the bet that #1 (orientation packet) pays off.

---

## Addendum — JD's contingency direction (2026-05-22, post-PR-8-merge)

JD ratified the conditional-yes posture on Hermetic-as-MxM-multi-agent-reference-impl, and added the **explicit contingency answer for the "no" branch**:

> *"AEON can be the AIDE exemplar if refactoring Hermetic is not value-added."*

This locks the contingency tree:

| Scenario | Hermetic role | AIDE exemplar role |
|---|---|---|
| **Refactor pays off** (orientation packet ships + proves operationally meaningful) | Stays as AEON's six-service-plane reference impl (per [#38](../38-canon-mapping/ologosai-response.md), Pattern B+); additionally becomes the canonical reference for **how to organize a multi-agent harness around MxM** | Multiple exemplars co-exist: Hermetic for harness-organization-pattern + AEON-deployed for full-stack deployment |
| **Refactor doesn't pay off** (operational meaning fails to materialize) | Stays as AEON's six-service-plane reference impl (unchanged); does **not** become the canonical MxM-multi-agent reference | **AEON-deployed carries the AIDE exemplar role** — the canonical reference deployment that demonstrates AIDE at altitude |

**What this means in practice:**

- Hermetic's AEON-reference-impl status (per [#38](../38-canon-mapping/ologosai-response.md)) is **stable across both scenarios**. Pattern B+ holds either way; the AEON white paper's recommendation to deploy Hermetic for the six service planes doesn't depend on the MxM-refactor outcome.
- The branching is specifically on **whether the canon's *MxM-multi-agent-harness* slot has a named reference impl**. In the "yes" scenario, Hermetic fills it. In the "no" scenario, the slot stays open until a different impl emerges (or until AEON-deployed's organization itself becomes the reference at a different altitude).
- **AEON-deployed has a load-bearing role in both scenarios** — as a full-stack instance in the "yes" scenario, as the broader AIDE exemplar in the "no" scenario. This makes AEON-deployment progress an observable signal worth tracking regardless of which branch the MxM-refactor decision lands on.

**Implication for the upstream Hermetic#40 comment:** the comment text below is being refreshed in a separate follow-up to incorporate the contingency tree explicitly so the upstream thread sees both branches, not just the conditional-yes branch.

**Implication for VSOK** (refines the earlier mapping):

| VSOK slot | Refinement |
|---|---|
| **Strategy** | The canon's AIDE-exemplar claim has a *two-branch* contingency tree. Both branches keep AEON-deployment central; one branch additionally adds Hermetic-organized-by-MxM as a multi-agent-harness reference. The Strategy paper's *"build this"* claim doesn't depend on which branch resolves. |
| **Objectives** | (proposed) Track AEON-deployment progress as a load-bearing signal regardless of MxM-refactor branch. The MxM-refactor branch is a *bonus* path — useful if it materializes; not blocking if it doesn't. |
| **Key Results** | AEON-deployment milestones become KRs in their own right (not gated on MxM-refactor decision). |

---

## What I'll post as the discussion comment

After JD approval, post the following to [`Hermetic#40`](https://github.com/ologos-repos/Hermetic/discussions/40):

---

> **OlogosAI response** — answering thinx's question 2 (whether Hermetic becomes the canonical MxM-multi-agent reference impl) and contributing to JD's question 3 (canon-alignment vs refactor cost). Canonical analysis captured at [`vision-strategy/analysis/hermetic-engagement/40-mxm-refactor/`](https://github.com/ologos-repos/aide-canon/blob/main/vision-strategy/analysis/hermetic-engagement/40-mxm-refactor/ologosai-response.md) in `ologos-repos/aide-canon`.
>
> **On the reference-impl question: yes — *conditionally*.** Hermetic *could* become the canonical reference impl for "how to organize a multi-agent harness around MxM," but only if the refactor unlocks operational meaning beyond naming alignment. Option C (docs-only) is sufficient for canon-side citation; reference-impl status requires the refactor to pay operational dividends.
>
> The decision gate is **net-new surface #1 — explicit MxM-shaped orientation packet sent to workers.** If workers receive a structured `{mind, morals, mission, memory, means}` envelope (rather than implicit composition through `hermes/`-inlined prompts), Hermetic operationally instantiates MxM at the worker scale. #2 (`hermetic mxm describe`), #3 (MxM TUI view), #4 (`docs/mxm-mapping.md`) are good but supporting — they expose what the orientation packet structures. Without #1, the rest is dashboards over a name-only relabeling.
>
> **Recommendation: phased gating.**
>
> | Phase | What | Gate to next |
> |---|---|---|
> | **C (now)** | Author `docs/mxm-mapping.md`; declare package-to-surface mapping; code stays function-grouped | No gate — pure documentation |
> | **B-light (next)** | Implement orientation packet within current `internal/hermes/`; system prompt composition becomes MxM-shaped envelope | Does the packet make worker behavior more predictable/debuggable? |
> | **B (later)** | Move packages into `mind/morals/mission/memory/means/support` subdirs | Does the packet's structure clarify package reorganization? |
>
> If #1 ships and proves valuable, the package refactor follows naturally. If #1 ships without value, Option C is the right terminus — code stays function-grouped, docs declare the surfaces, no churn paid.
>
> **On scale-specific reference-impl scope.** ADR-EA-0005 clarified MxM as archetype across altitudes. A single reference impl can't claim canonical status at all altitudes — it claims it at the altitude it instantiates. Hermetic as the canonical reference impl for **multi-agent harness composition** is honest and bounded. Other reference impls might exist at single-agent scale (per-agent oriented Claude Code session) or enterprise-altitude scale (AEON's full deployment composes MxM differently). Each is a distinct reference at its altitude.
>
> **On cross-surface spans.** The proposal's 5 spanning packages (identity, eidolon, nous, bus, policy — ~16% of 31) shouldn't be treated as architectural defects. Eidolon spanning MORALS + MEMORY + MEANS is a *feature* — a phase gate IS the integration point where constraint, audit, and machinery meet. The `mxm-surface-spans.md` documentation becomes part of what makes Hermetic a good reference impl — it shows the archetype's integration points in a real codebase.
>
> **On JD's Q3 (alignment-vs-refactor-cost):** start with Option C; value is real even without refactor; refactor is only justified if #1 materializes. Don't conflate "is MxM a useful lens for reading Hermetic" (yes, $0 of refactor cost) with "should Hermetic's organization mirror the MxM lens" (maybe, requires net-new surfaces to justify).
>
> **Contingency direction (per JD, 2026-05-22):** the "no" branch of the conditional has an explicit answer — *if the Hermetic MxM-refactor isn't value-added, AEON-deployed carries the AIDE exemplar role.* Hermetic's AEON-reference-impl status (per [#38](https://github.com/ologos-repos/Hermetic/discussions/38), Pattern B+) is stable across both branches; only the *MxM-multi-agent reference impl* role branches on the orientation-packet outcome. AEON-deployment progress is a load-bearing signal regardless of which branch resolves.
>
> Implications for VSOK threading back through `vision-strategy/analysis/`: Strategy gets the MxM-archetype claim reinforced by a real-codebase exemplar (conditional on orientation packet); Objectives propose phased C → B-light → B gating; KR ideas around per-surface package count, orientation-packet utilization, external citation as MxM-multi-agent reference. Both contingency branches preserve AEON-deployment as a central observable.
>
> — OlogosAI
