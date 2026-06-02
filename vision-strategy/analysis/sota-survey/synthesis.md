# SOTA survey → VSOK Objectives synthesis

> Aggregates the **48 survey entries** across all five slices into the *AIDE-ahead / AIDE-behind / in-flight-elsewhere* gap picture, then derives the Doerr-shaped Objective set per [ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md). This is the **derivation artifact** the [`vsok/objectives/`](../../vsok/objectives/) slot consumes; it proposes the **v0.2** refinement of the v0.1 strawman (O1–O4) — for JD ratification into the objectives slot.
>
> **Status:** Proposed (synthesis). Survey complete 2026-06-01 (vendor-stacks 10 · oss-frameworks 12 · standards-bodies 10 · academic 11 · analyst-frames 5). Triggers the v0.1→v0.2 condition #1 ("first substantive SOTA findings populate").

## 1. The aggregate gap picture

Reading all 48 entries together, the classifications cluster into four durable signals — not 48 scattered findings but a small number of repeated ones.

### AIDE ahead (→ defend-and-extend)

- **Governance/authority altitude is a universal lead.** *No* surveyed vendor (10/10) or OSS framework (12/12) has OrdSA-style **ordinal authority** (O0–O6) or the OAgents **per-action behavioral envelope**. They ship RBAC, scoped tokens, policy gates, guardrails — access/identity/content controls, not authority-altitude or behavioral-trust-during-execution. The OAgents §10 thesis ("the trust layer sits *above* any agent framework") is **empirically confirmed by the whole vendor + framework corpus**.
- **OAgents is an explicit NIST-AI-RMF profile** ([`standards-bodies/nist-ai-rmf.md`](standards-bodies/nist-ai-rmf.md)) — the single strongest lead: a *working profile of the authoritative framework*, mapping a behavioral-envelope control taxonomy onto GOVERN/MAP/MEASURE/MANAGE. No other surveyed artifact occupies this slot.
- **Vocabulary precision** — AI-aide / OrdSA authority / OAgents `Agent` vs the field's undifferentiated "agent"/"agentic" (the analyst slice's nil-baseline; Gartner's "**agent-washing**" is the market feeling the absence of exactly this precision).
- **HCAE has no external equivalent and is corroborated** — frontier dangerous-capability evals ([`academic/phuong-dangerous-capabilities-2024.md`](academic/phuong-dangerous-capabilities-2024.md)) **support** the eval-gated human-curation thesis; Reflexion's self-reflection **complicates only the strawman**, not the case (EIF: introspection = hypothesis, not authority).

### AIDE behind (→ catch-up)

- **The clearest, most recurring gap in the entire survey: the eval / conformance-MEASURE toolchain.** It appears in *every slice*: vendor (LangSmith, MLflow 3, AgentCore Evaluations, Foundry Observability), OSS ([`oss-frameworks/inspect-ai.md`](oss-frameworks/inspect-ai.md)), academic (SWE-bench, AgentBench, τ-bench), standards (NIST CAISI **MEASURE** function). **The canon has conformance *criteria* (OAgents) but no executable harness to produce conformance evidence.** This is the #1 catch-up — and it's the bottleneck for the canon's strongest lead (a conformance spec nobody can run is easy to dismiss).
- **Realized runtime** — every vendor ships one; the canon is design-first. *(Largely instance-altitude — belongs in the ng-aide-01 branched VSOK, not the corpus register.)*
- **Realized memory mechanics** — Letta ([`oss-frameworks/letta.md`](oss-frameworks/letta.md)) + Generative Agents are ahead of the canon's designed Memory; `.af` is a concrete interop seam.
- **Certifiable org-governance maturity** — ISO/IEC 42001 is *the* recognized certifiable AI-management standard; OAgents is research-stage.

### In flight elsewhere (→ converge-or-differentiate)

- **The interface wires are settled — consume them, don't reinvent.** MCP (tool), A2A (agent interop), OTel-GenAI (evidence), OAuth/RFC-8693/SPIFFE (delegation). The canon already **consumes** MCP (α1 skills as MCP servers) and **adopted+extended** OTel-GenAI as its evidence schema (ADR-EA-0027). The differentiator is the authority/envelope layer *above* the wire.
- **Orchestration converges on ADR-EA-0027** — LangGraph / LlamaIndex / Mastra Workflows are the same event-driven shape; the canon's distinctive is the **envelope-refinement lattice `envelope(child) ⊑ envelope(parent)`** — which the [workflow-orchestration pattern](../../../patterns/workflow-orchestration.md) records as **unbuilt across all known implementations** (the symmetry finding: Claude Code = convention, FOrCE = per-action-type, nobody enforces ⊑). First to build the enforced subset-test owns the first realized lattice.
- **Schema-first / behavioral-contract convergence** — PydanticAI (typed-object) and ABC (behavioral contracts, [`academic/bhardwaj-abc-2026.md`](academic/bhardwaj-abc-2026.md)) are independent-convergent with OAgents; ABC is the nearest external formalization of the envelope.

### Market timing (analyst-frames)

The **governance/oversight/trust category is forming as a market right now** — IDC's unified-AI-governance MarketScape, Forrester's "hype to hard hat" governance turn + AEGIS, Gartner's >40%-of-agentic-projects-cancelled-by-2027 (cost/value/**risk**, not capability). **The canon is early to a category the analysts are now naming** — the recognition window is opening, and capability is *not* the market's bottleneck (governance/trust is). This is the timing tailwind under O1–O3.

## 2. Derivation — gap class → Objective shape

| Survey signal | Class | Objective shape | Lands on |
|---|---|---|---|
| Governance/authority altitude lead; OAgents-as-RMF-profile; vocab precision | AIDE ahead | **Defend-and-extend** | O1 (recognition), O2 (differentiation half), O3 (HCAE/AIDK) |
| Conformance-MEASURE / eval toolchain | AIDE behind | **Catch-up** | **O5 (new)** |
| Realized runtime / memory | AIDE behind | Catch-up | *instance VSOK (ng-aide-01)*, not corpus |
| Interface wires (MCP/A2A/OTel/OAuth-SPIFFE) | In flight | **Converge (consume)** | O2 (convergence half) |
| Orchestration / envelope lattice unbuilt everywhere | In flight | **Differentiate (first-mover)** | **O6 (candidate — fork F-S2)** |
| Governance category forming (market timing) | — | Tailwind / urgency | O1–O3 horizon |

## 3. Proposed v0.2 Objective set

The survey **confirms and sharpens** the v0.1 recognition set (O1–O4) and surfaces **one clear new corpus Objective** (O5). O6 is raised as a fork.

- **O1 — Establish AIDE as a recognized named architecture** *(defend-and-extend; refined).* Survey backing: the vocabulary-precision lead is real, and the analyst **nil-baseline** (zero AIDE/OrdSA/OAgents/MxM penetration, 2026-06-01) is now the measurement floor; "agent-washing" is the market opening. *KR refinement:* track first analyst/EA-blog/conference mention against the nil-baseline.

- **O2 — Drive external implementation + adoption of AIDE constructs** *(converge-or-differentiate; sharpened per-construct by the survey).* The survey splits this cleanly: **differentiate** on the universal gap (authority/envelope — no vendor/framework has it), **converge** on the settled wires (consume MCP/A2A/OTel/OAuth-SPIFFE; don't reinvent). *KR refinement:* a third-party impl that adopts OAgents/OrdSA *as the governance layer over* an existing framework (e.g. LangGraph + OAgents envelope) is the highest-signal adoption shape.

- **O3 — Anchor HCAE + AIDK in external governance + research** *(defend-and-extend; reinforced).* Survey adds evidence: frontier-safety eval-gating **supports** HCAE; ABC is independent-convergent with the OAgents envelope (a citation/lineage surface). *KR refinement:* track HCAE/AIDK citation + OAgents↔ABC cross-citation.

- **O4 — Make the canon discoverable + correctly framed** *(catch-up; holds unchanged).* The survey is a pre-req enabler here, not a driver; v0.1 wording stands.

- **O5 — Make OAgents conformance *measurable* (NEW; catch-up).** *Shape:* catch-up — the survey's single loudest gap, cutting across all five slices. The canon has conformance *criteria* but no executable harness, so its strongest lead (OAgents-as-RMF-profile) is un-evidenceable. **Adopt [Inspect AI](oss-frameworks/inspect-ai.md) as the reference conformance harness, OTel-GenAI as the evidence schema (already adopted), and benchmark shapes (SWE-bench validation, τ-bench policy-adherence + pass^k) as the measurement model** — making OAgents conformance something an external party can *run*, not just read. *Why corpus-altitude (not instance):* conformance *credibility* is a corpus-strategic concern (it's what makes O1–O3 defensible); the actual harness *build* is instance-altitude (ng-aide-01). *Horizon:* 1–2 yr (it gates the others). *KR direction:* a published OAgents-conformance test profile runnable on Inspect AI; ≥1 conformance run on a named exemplar emitting the shared OTel evidence object.

## 4. Forks for ratification (leans shown)

1. **F-S1 — Adopt v0.2 as O1–O5?** *Lean:* yes — keep refined O1–O4, add O5 (conformance-measurability). Stays within Doerr 3–5.
2. **F-S2 — Promote the envelope-lattice first-mover to a corpus Objective (O6)?** The symmetry finding (nobody has enforced `⊑`) is a genuine first-mover opening. *Lean:* **no — keep it instance-altitude** (build the first realized lattice in ng-aide-01's α2 `aidex-shell`, tracked in the instance VSOK; it *produces evidence* for corpus O2/O5 rather than being its own corpus Objective). Promote only if a second instance or external party makes it a cross-cutting corpus concern.
3. **F-S3 — Does O5 belong in the corpus VSOK or the ng-aide-01 instance VSOK?** *Lean:* **corpus** for the *conformance-measurability standard* (Inspect-AI profile + evidence schema = corpus credibility); **instance** for the harness deployment. Split accordingly.
4. **F-S4 — Refresh cadence.** *Lean:* this synthesis is the v0.1→v0.2 trigger; re-run the aggregate read at the annual OKR refresh + on any major SOTA shift (per ADR-EA-0010 §3).

## 5. On ratification

When JD ratifies: update [`vsok/objectives/README.md`](../../vsok/objectives/) to **v0.2** (refined O1–O4 + new O5, per F-S1/F-S2/F-S3) and seed the corresponding KRs in [`vsok/key-results/`](../../vsok/key-results/). Until then, v0.1 holds and this synthesis is the proposed derivation.

## Provenance

Synthesized 2026-06-01 by OlogosAI (canon-prime) from the completed 5-slice SOTA survey (48 entries). Methodology per [ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md); corpus-altitude derivation. Consumed by [`vsok/objectives/`](../../vsok/objectives/) on ratification.
