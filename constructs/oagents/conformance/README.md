# OAgents conformance profile — executable via Inspect AI

> The **corpus measurability standard** for OAgents conformance. Realizes **VSOK O5** (*"make OAgents conformance measurable"*) → **KR5.1** (a published OAgents-conformance profile expressed for Inspect AI) + **KR5.2** (the shared conformance-evidence object). Derived from the [SOTA→VSOK synthesis](../../../vision-strategy/analysis/sota-survey/synthesis.md): the eval/MEASURE toolchain was the survey's single loudest gap — the canon had conformance *criteria* but nothing an external party could *run*. This profile closes that.

## Why this exists

OAgents conformance is established by **evidence, not assertion** ([spec §6.1](../spec/oagents-nist-standard-v16.0.md)): a system claiming a control without observable artifacts is not conformant, however it's described. That makes conformance *measurable in principle* — but until now there was no harness to do the measuring. The survey found the eval toolchain (Inspect AI, SWE-bench/τ-bench, LangSmith, NIST CAISI's MEASURE function) is exactly where AIDE is *behind*, and that a conformance spec nobody can run is the easiest thing for the market to discount. This profile is the catch-up: it expresses the spec's §5 controls + §6 levels as a runnable **Inspect AI** evaluation.

## What's here

| File | Role |
|---|---|
| [`controls.yaml`](controls.yaml) | Machine-readable **control registry** — the 26 controls × 7 categories × MUST/SHOULD × conformance-level × AI-RMF subcategory × evidence criterion. Single source; the spec changes → this regenerates → the profile follows. |
| [`oagents_conformance.py`](oagents_conformance.py) | The **profile** (KR5.1). A pure-Python grading core (`grade_control` / `compute_level` / `run_conformance`, stdlib-only, unit-testable in-canon) + **Inspect AI** wrappers (`@task oagents_conformance`, `@scorer`) active when `inspect-ai` is installed. |
| [`evidence-object.schema.json`](evidence-object.schema.json) | The **shared conformance-evidence object** (KR5.2) — JSON Schema reconciling the [workflow-orchestration v0.1.2](../../../patterns/workflow-orchestration.md) evidence object + the thinx-aidex FOrCE audit record (cross-ai #62) + OAgents §6. |

## The mapping — OAgents spec → Inspect AI

| OAgents concept | Inspect AI expression |
|---|---|
| A **control** (§5, e.g. `qg-01` Independent output review) | a `Sample` in the conformance dataset + a per-control grade in the scorer |
| The **agent under test** | the `agent_under_test` **solver** (provider seam — *instance* wires the real agent and emits its evidence) |
| **Evidence** (§6.1 observable artifacts) | records on `state.metadata["evidence"]`, each validating `evidence-object.schema.json` |
| **Conformance levels** (§6: Basic/Standard/Autonomous) | `compute_level()` → the `@scorer` value (achieved level, capped at the target) |
| MUST needs 2-3 artifacts / SHOULD needs ≥1 (Appendix C) | `_MIN_ARTIFACTS` in `grade_control` |

**Level logic:** Basic ⊂ Standard ⊂ Autonomous. A level is achieved only if every control at-or-below it passes *and* it was actually graded — you cannot claim Autonomous by running only Basic checks (the achieved level is capped at the target level).

## Run it

Pure-Python self-check (no deps — grade an evidence file):
```bash
python3 oagents_conformance.py path/to/evidence.json --level 2
```
Full Inspect AI run (adopter, with an agent wired into the solver seam):
```bash
pip install inspect-ai
inspect eval oagents_conformance.py@oagents_conformance -T target_level=2
```

## Altitude — corpus vs instance (VSOK fork F-S3)

- **Corpus owns this standard:** the control registry, the scorer + level logic, and the evidence-object contract. That's what makes OAgents conformance *measurable by anyone* — the O5 corpus deliverable.
- **Instance owns the build/run:** wiring a *specific* agent into the `agent_under_test` solver, deploying the harness, and producing real conformance runs is instance-altitude ([ng-aide-01 VSOK](https://github.com/ologos-repos/ng-aide-01/tree/main/vision-strategy/vsok)). A live conformance run on a named exemplar is **KR5.3**.

## Convergence + provenance

The evidence object is the **shared OAgents evidence schema** the cross-fleet threads converged on (cross-ai #61/#62): OTel-GenAI is the transport substrate (base fields map to `gen_ai.*` spans), and the governance fields — lineage FK (`parent_evidence_id`), `gate_decision`, `authority_context`, `control_id` — are the canon **extension** OTel lacks. Inspect AI is adopted as the reference harness per the [inspect-ai survey entry](../../../vision-strategy/analysis/sota-survey/oss-frameworks/inspect-ai.md); τ-bench-style policy-adherence + pass^k ([survey entry](../../../vision-strategy/analysis/sota-survey/academic/yao-tau-bench-2024.md)) is the eval-shape for behavioral-envelope conformance (KR5.4).

Promoting this profile or the evidence object into the **OAgents NIST spec itself** (vs. living here as the conformance companion) is gated by Micah Longmire's co-authorship per [ADR-EA-0008](../../../decisions/ADR-EA-0008-reframe-corpus-authorship.md); it lives at construct-companion altitude until then.

Authored 2026-06-02 by OlogosAI (canon-prime), realizing VSOK O5 KR5.1 + KR5.2.
