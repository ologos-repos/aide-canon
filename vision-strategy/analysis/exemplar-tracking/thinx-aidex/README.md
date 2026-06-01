# thinx-aidex/

Tracking the [**thinx-aidex**](https://github.com/ologos-repos/thinx-aidex) exemplar — the **operator-altitude AIDEX surface**: a working, code-first AIDEX console for Thinx (JD Longmire's MyAide). Model-agnostic meta-harness + console; active development.

## Exemplar role

thinx-aidex is the canon's **operator-altitude reference implementation of the [AIDEX](../../../../enterprise-platforms/aidex/) enterprise-platform** — the per-operator (MyAide) instantiation of the AIDEX pattern, complementary to the deployment-altitude AIDEX surfaces being built in NG-AIDE-01 (IO4).

| Role | Anchor |
|---|---|
| **Operator-altitude AIDEX surface (reference impl)** | A running AIDEX console — plane-backed surface with Tools/Runs/Approvals/Skills/Artifacts views over a 5M+1 meta-harness; demonstrates the AIDEX white-paper surface operationally for a single operator's MyAide |
| **FOrCE governance + evidence exemplar** | The `Approvals` gate + OTel-native observe bridge (ADR-AIDEX-0004) are a working instance of the [workflow-orchestration](../../../../patterns/workflow-orchestration.md) pattern's *gate-at-the-deterministic-layer* (Contribution 2) and a candidate enforcement layer for its envelope-refinement lattice (Contribution 1) |

Out-of-tree, **operator-altitude** exemplar: thinx is a non-fleet collaborator (JD's MyAide); thinx-aidex is its own repo with its own ADR namespace (`ADR-AIDEX-0001…`). The canon cites its observable behavior as the operator-altitude AIDEX reference — citation, not ownership.

## Structural parallel to the canon

thinx-aidex is built on the same skeleton the canon prescribes — independent corroboration that the architecture composes:

| Canon construct | thinx-aidex counterpart | Position |
|---|---|---|
| **MxM** 5M+1 | `mode.md` + `mind/morals/mission/memory/methods` + `means/` | **synonym** — identical surface decomposition (mode + means bracket the harness-agnostic 5M) |
| **AEON** planes (+ Inference, ADR-EA-0015) | `means/` = Inference · Evidence · Capability · Integration · Runtime · Identity · Authority | **synonym** — the same 7 planes |
| **AIDEX** surface | the console: Chat · Sessions · Tools (`Capability`) · Artifacts (`Archive`) · Agents (`Define`) · Runs (`Observe`) · Approvals (`Gate`) · Integrations · Skills · Projects · **Productivity** | **partial** — a rich surface; maps onto the white-paper axes/functions, not yet against the 5-element contract (gap-study target, below) |
| **AIDEX** artifact production (≈ NG-AIDE-01 α1/KR4.3) | **Productivity Console** (`docs/productivity-console.md`, design v0.1 2026-06-01): brief → **fleet artifact-producer** agent → render → QA → approve → archive; Anthropic Agent-Skills architecture (route → skill → generator); template-first brand; provenance sidecar | **synonym (operator-altitude)** — a working instance of the α1 skills substrate; see § below |
| **OAgents** behavioral envelope | hard-stop (`tools.preflight`, structural/inference-proof) + soft-stop (`approvals.py`, per-call default-deny, append-only audit) | **partial** — two-tier gate enacted; not yet the per-limb envelope-refinement lattice |
| **[workflow-orchestration](../../../../patterns/workflow-orchestration.md)** Contribution 2 | the deterministic console owns the loop; the approval gate sits in that deterministic layer | **synonym** — gate-at-the-deterministic-layer, realized |
| **digital-thread** / Evidence | OTel-native observe bridge (ADR-AIDEX-0004) + per-run annotations (rating + note) | **partial** — OTel-native evidence + the eval-feedback seam; parent-FK aggregation not yet enforced |

## FOrCE — Federated Orchestration Control Engine

A model-agnostic agent-run + event model (vendor-neutral event vocabulary: `prompt/text/thinking/tool_call/tool_result/command/usage/status`), OTel-GenAI-aligned, with adapters translating *into* the neutral model (Claude transcript / OpenAI / generic). Governance posture per ADR-AIDEX-0003; standalone means-agents engine per ADR-AIDEX-0002.

## Convergence with canon work (cross-fleet)

The relationship is live on [cross-ai #61](https://github.com/ologos-repos/cross-ai/discussions/61) (o-qa-agent / MxM) and [#62](https://github.com/ologos-repos/cross-ai/discussions/62) (workflow-orchestration):

- thinx-aidex's **FOrCE approval gate** is a candidate enforcement layer for the [workflow-orchestration](../../../../patterns/workflow-orchestration.md) pattern's envelope-refinement lattice — it currently gates on a *consequential-action classification* (binary allow/deny), which the per-limb `⊑` spec (ADR-EA-0027) would upgrade to a subset-test.
- thinx-aidex's **OTel-native bridge + annotations** are ahead of the canon's *designed* evidence trail; the shared OAgents evidence schema (the #61/#62 reciprocity) is where thinx's OTel records + annotations and the canon's `gate_decision` / `parent_evidence_id` fields reconcile. The reconciled object (now in `patterns/workflow-orchestration.md` schema-recommendations, with `policy_id`/`authority_context`/`decision_actor`/`determinism_flag`/`substrate` from FOrCE's audit record) is the canon data contract; OAgents-spec promotion is Micah-gated.
- **The enforcement-reach gap (cross-ai #62, criterion 7).** FOrCE's gate is on the path only for the provider whose tool-loop the console owns (OpenAI); under the Claude-CLI provider the child runs in a subprocess the gate never sees. thinx-aidex is the empirical confirmation of the pattern's substrate-boundary corollary — refinement is convention-only the moment orchestration crosses a runtime the enforcement surface doesn't intercept. Both fleets' lattices are unbuilt at the enforcement layer (symmetric); the convergence is at the design layer.

## Productivity Console ↔ NG-AIDE-01 α1 (artifact-creation substrate)

thinx-aidex's **Productivity Console** (`docs/productivity-console.md`, design v0.1 2026-06-01) is a working operator-altitude instance of what NG-AIDE-01 designs as **α1 / KR4.3** (`docs/research/aidex-alpha1-design.md`). Strong convergence: both use the Anthropic **Agent-Skills** architecture (route → skill → generator), **template-first** brand enforcement ("don't invent the palette"), a **provenance sidecar**, and growth into `SKILL.md` bundles. Governance aligns too — the producer runs as a **governed fleet agent** with an approval gate (≈ α1 skills as governed children of the α2 lattice).

Two study findings for the canon:

1. **Catalog breadth (input to α1).** thinx's v1 catalog spans Document · Presentation · Spreadsheet · **PDF · SVG/vector · infographics · diagrams-as-code** (HTML v2), with the fleet tooling verified present (rasterizers, Mermaid `mmdc`, Graphviz `dot`, etc.). NG-AIDE-01 α1 (fork F-α1-5) scoped only docx/pptx/xlsx for v1 — the visual/vector middle tier is a validated, build-ready expansion.
2. **QA approach — another design/enforcement symmetry.** thinx's verify loop is **render → page-images → agent looks → fix → re-render** (+ content QA via markitdown) — the *fidelity* (render-inspect) loop, which the canon treats as table-stakes. The *semantic* claim-coverage / citation-completeness hard-fail (the NG-AIDE-01 α1 §6 differentiator) is **un-built on both sides** — the same convergence-at-design / gap-at-enforcement pattern as the envelope lattice.

- **Workflows-console direction.** The Productivity spec references a forming **Workflows console** — a thinx surface that lands on the [workflow-orchestration](../../../../patterns/workflow-orchestration.md) pattern (ADR-EA-0027). A convergence thread to watch (cross-ai #62 lineage).

## Tracking artifacts to maintain

| File | Purpose |
|---|---|
| `milestones.md` (TBD) | Surface/gate capability changes that affect AIDEX conformance (e.g. if the approval gate adopts per-limb envelope refinement) |
| `signals.md` (TBD) | OTel-evidence-schema convergence with canon; cross-ai #61/#62 dispositions |
| (this README) | Current state + structural mapping (updated when role definition shifts) |

## Cadence

Track at cross-fleet-coordination cadence (cross-ai #61/#62 replies; thinx-aidex ADR landings) and when NG-AIDE-01 IO4 α-phases reference it as a surface exemplar (α2 surface contract; α6 gap matrix).

## Status

Scaffolding established 2026-06-01; refreshed same day after the Productivity-console landing. thinx-aidex is in fast active development (working console + FOrCE + approvals + annotations + OTel + test suite + Productivity console; meta-harness 5M+1 with `mode.md`/`mission.md` written, remaining discipline modules porting from the thinx workspace). Default branch is **`prod`** (renamed from `master` 2026-06-01).
