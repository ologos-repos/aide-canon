# ADR-EA-0015 — Introduce the Inference plane as AEON's 7th service plane

- **Status:** Accepted (ratified 2026-05-24 by JD Longmire as CIO + AEON paper author + canon founder per [cross-ai #20](https://github.com/ologos-corp/cross-ai/issues/20) governance; **AEON white paper v0.2 revision queued behind Micah Longmire's read per [ADR-EA-0008](ADR-EA-0008-reframe-corpus-authorship.md)** corpus-authorship discipline; Tracy Norrell's operational-reviewer input taken under founder authority per umbrella [`ng-aide-01#1`](https://github.com/ologos-repos/ng-aide-01/issues/1) Q7 lane assignment)
- **Date:** 2026-05-24
- **Author:** JD Longmire (architectural decision; ADR drafted by thinx-Claude)
- **Reviewers:** @ologos001 (canon prime); Micah Longmire (AEON paper co-author — paper-revision gate per ADR-EA-0008); Tracy Norrell (Sr. Systems Architect; operational reviewer)
- **Related:** [`aide-canon#23`](https://github.com/ologos-repos/aide-canon/issues/23) (proposal discussion) · [`enterprise-platforms/aeon/`](../enterprise-platforms/aeon/) (the construct this ADR extends) · [ADR-EA-0008](ADR-EA-0008-reframe-corpus-authorship.md) (paper-revision authorship gate) · [ADR-EA-0011](ADR-EA-0011-open-source-first-products-construct-means-separation.md) (Means-separation; inference routing is plane, model serving is Means) · [`ologos-repos/ng-aide-01`](https://github.com/ologos-repos/ng-aide-01) (NG-AIDE-01 reference implementation; Objective O8 model-agnostic + selection routine)
- **Ratification trail:**
  - 2026-05-23 (filed): aide-canon#23 opened as discussion proposal; three options surfaced (a/b/c). Asked for direction from JD (CIO + paper author), Micah (paper co-author), Tracy (operational lead).
  - 2026-05-24 (ratified): JD Longmire ratifies **option (a)** — promote inference routing to a 7th service plane — at the architectural-decision level. Tracy's operational-reviewer voice taken under founder authority per the umbrella lane-assignment pattern; Micah's voice on paper revision queued (see Consequences). NG-AIDE-01 local implementation (`planes/inference/`, in flight per umbrella Objective O8) is canon-aligned by this ratification; no relabel cost.

## Context

The AEON white paper ([`10.5281/zenodo.20349194`](https://doi.org/10.5281/zenodo.20349194)) specifies six service planes (§5–§12): identity, authority, evidence, integration, capability composition, orchestration runtime. NG-AIDE-01's Objective O8 ("AEON and all substrates must be model-agnostic with a model-connection-selection startup routine") raises an architectural question: does **inference routing** — the selection of which LLM provider and model is active across the enterprise's agentic capability set — sit at plane altitude, or below?

Inference routing has three properties that make the question non-trivial:

1. **It is enterprise-wide.** Every agentic capability invokes inference. *Which provider+model serves the call* is a single decision surface, not a per-capability concern.
2. **It has architectural responsibilities** — provider registry, model catalog, selection routine, runtime switching, per-principal binding, classification-environment filtering, audit-via-Evidence. Substantial subsystem.
3. **None of the existing 6 planes naturally absorbs it.** Identity resolves principals (not models); Authority evaluates policy (consumes inference decisions, does not make them); Evidence captures decisions (does not make them); Integration composes capabilities (could host inference as one capability but loses cross-cutting visibility); Capability Composition registers capabilities (could register inference per provider/model, but the *routing decision* is enterprise-wide, not per-capability); Orchestration Runtime hosts services (could host the gateway but does not make it architecturally first-class).

[NVIDIA's NemoClaw architecture](https://github.com/NVIDIA/NemoClaw/blob/main/docs/reference/architecture.md) is the operational precedent: OpenShell gateway is a top-level architectural component, not subordinated to a higher abstraction. Agent code calls inference; the gateway intercepts and routes to the configured provider+model; runtime switching requires no agent restart. Agents do not know which model is active.

Per AEON §1: *"a control plane is the architectural layer that orchestrates composition without executing the composed capabilities. The data plane runs the actual workloads; the control plane decides what is composed, by whom, under what authority, with what evidence, against what policy."* Adding "**with what model**" to that list is the architectural claim of this ADR.

## Decision

**Promote inference routing to a 7th service plane of AEON: the Inference plane.**

The plane's responsibilities, mirroring AEON's existing plane structure:

### Architectural responsibilities

- **Provider registry** — per-endpoint adapters (cloud / on-prem / local). OpenAI-compatible HTTP API as the lingua franca interface; explicit adapters for non-conformant providers (Anthropic Claude, Google Gemini).
- **Model catalog** — which models are reachable, per-classification-environment. Cloud-provider entries filtered out when air-gap discipline is active per ADR-EA-0011.
- **Selection routine** — operator + agent picks which provider+model to bind. Tiered: env-config-default → per-AIDEX first-run wizard → per-principal preference override (the multi-model adapter pattern formalized).
- **Routing** — agent inference call → gateway → provider → response. Agents are model-agnostic by construction.
- **Switching** — runtime change of active provider+model without agent restart. Switch propagation: <60s for explicit reconfiguration.
- **Per-principal binding** — service-default + per-principal override surface, gating on the Identity plane's authoritative principal resolution.
- **Egress posture filter** — cloud providers filtered when air-gap discipline active, gating on the Authority plane's policy evaluation of egress permissions.
- **Status** — current provider+model visible to operators and to audit via the AIDEX surface.
- **Audit** — every inference call emits an Evidence-plane event (`inference.invoked` with provider + model + tokens + duration). Cross-plane edge.

### Federation interface

OpenAI-compatible HTTP API as the federation interface — the lingua franca every modern inference endpoint speaks. Anthropic Claude and Google Gemini receive explicit adapters.

### Performance targets (per AEON §12.3 conventions)

- Routing decision: single-digit milliseconds (in-memory lookup)
- Provider failover: <500ms detection + cutover for transient failures
- Switch propagation: <60s for explicit reconfiguration

### Cross-plane edges

- **Inference → Identity** — per-principal binding resolved via Identity `/resolve`.
- **Inference → Authority** — egress-posture and provider-eligibility policy evaluation.
- **Inference → Evidence** — every routing decision + invocation emits `inference.invoked`.
- **Capability Composition → Inference** — agentic capabilities that invoke inference declare their provider/model preference (per-capability override) at registration.
- **Orchestration Runtime → Inference** — Runtime calls Inference at dispatch time to resolve which provider+model serves the agent's invocation.

### Means separation (ADR-EA-0011)

Per ADR-EA-0011, the **plane** specifies the contract; the **Means** specify the implementation. The Inference plane contract is the responsibilities + cross-plane edges + federation interface above; the Means implementation is the inference gateway component picked per `means/components.md` (LiteLLM + vLLM/Ollama at this time, per the NG-AIDE-01 components survey). Swappable per ADR-EA-0011 substrate discipline.

## Consequences

### Immediate (this ADR)

- **AEON construct README** updated to declare the 7th plane and note the AEON white paper revision queued.
- **NG-AIDE-01 local build** (`planes/inference/`, per Objective O8) is canon-aligned. No relabel or restructure cost; the local Inference plane work proceeds against this canon decision.
- **`aide-canon#23` discussion** closes with this disposition.

### Queued (separate, gated on Micah's read)

- **AEON white paper v0.2 revision** — adds §13 (or appropriate placement) specifying the Inference plane as above. Per ADR-EA-0008 corpus-authorship discipline, paper revisions gate on co-author read. Micah's review queued; no specific timeline imposed by this ADR.
- **New Zenodo deposit** for AEON paper v0.2 once Micah ratifies the revision. Existing DOI `10.5281/zenodo.20349194` remains the v1 record; v0.2 receives a new-version DOI.

### Downstream

- **Other enterprise-platforms** (AIDEX, OAAD) inherit the 7-plane control-plane reference. AIDEX surfaces gain operator-visibility for current inference binding (provider + model). OAAD positioning unchanged (Inference is plane-altitude work, not OAAD's strategic-thesis content).
- **Other constructs** unchanged. MxM, OrdSA, OAgents, DEA do not absorb inference routing (per the "none of the existing planes naturally absorbs it" diagnostic in Context; the same diagnostic applies to constructs).
- **`patterns/`** unchanged. Inference routing is a plane responsibility, not a cross-cutting pattern.
- **Reference implementations** — `ng-aide-01` is the first; future canon AEON deployments inherit the 7-plane shape.

## Alternatives considered

1. **Option (b) — Inference as a capability under §11 (Capability Composition).** Rejected. Treats a cross-cutting enterprise-wide routing decision as one capability among many. Loses architectural visibility: an operator cannot answer *"which model is active in production right now"* by querying the Capability Composition plane (which would have N inference-route capabilities, one per provider+model combination). The routing decision is not per-capability; it is enterprise-wide. Capability Composition registers *what the ecosystem can do*; it should not be repurposed to register *how the ecosystem reaches its inference substrate*.
2. **Option (c) — Inference gateway as a service within §12 (Orchestration Runtime).** Rejected. Operationally clean — the gateway runs in Runtime — but framing inference routing as a Runtime implementation detail mischaracterizes it. Runtime is the dispatch loop (Identity → Capability → Authority → adapter → Evidence per ADR-EA-0014 EIF realization at runtime). *Which provider+model serves the call* is a different concern from *how the call is dispatched* — both are plane-altitude responsibilities, neither subsumes the other. Hiding Inference inside Runtime would also obscure the per-principal binding, classification-environment filter, and switch-propagation responsibilities that Runtime has no business owning.
3. **Defer the decision pending more reference-impl experience.** Rejected. NG-AIDE-01 is building inference routing right now per Objective O8; without canon ratification, that work risks restructure cost if a future ratification picks (b) or (c). Ratifying now lets the reference impl align canon-side without rework. The pattern is well-precedented (NemoClaw) and the architectural diagnostic (none of the existing planes naturally absorbs it) is structurally clear.
4. **Promote to a peer construct at Tier 3.** Rejected. Constructs are *methodological patterns* (DEA, OrdSA, MxM, OAgents). Inference routing is an *enterprise-platform-altitude service plane*, not a methodological pattern. Promoting it to construct altitude would mis-categorize it.

## References

- [`aide-canon#23`](https://github.com/ologos-repos/aide-canon/issues/23) — the proposal discussion this ADR ratifies
- [`enterprise-platforms/aeon/README.md`](../enterprise-platforms/aeon/README.md) — AEON construct overview (updated by this PR to declare the 7th plane)
- [AEON white paper](https://doi.org/10.5281/zenodo.20349194) v1 — the published 6-plane specification (v0.2 revision queued behind Micah's read per ADR-EA-0008)
- [ADR-EA-0008](ADR-EA-0008-reframe-corpus-authorship.md) — corpus-authorship discipline (gates the AEON paper v0.2 revision)
- [ADR-EA-0011](ADR-EA-0011-open-source-first-products-construct-means-separation.md) — Means-separation (plane specifies contract; Means specifies implementation)
- [ADR-EA-0013](../constructs/mxm/decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md) — root file is the operating-mode/autonomy-posture activator; *not* the inference-binding activator (that lives in the Inference plane's per-principal binding surface, gated on the Authority plane's policy)
- [ADR-EA-0014](ADR-EA-0014-introduce-epistemic-integrity-floor-pattern.md) — EIF; the inference plane provides the model-binding context EIF §6 cross-turn discipline observes
- [`ologos-repos/ng-aide-01`](https://github.com/ologos-repos/ng-aide-01) — NG-AIDE-01 reference implementation; Inference plane build in `ng-aeon/planes/inference/` (in flight)
- [NVIDIA NemoClaw architecture](https://github.com/NVIDIA/NemoClaw/blob/main/docs/reference/architecture.md) — the operational pattern source
- [`means/components.md`](https://github.com/ologos-repos/ng-aide-01/blob/main/means/components.md) — LiteLLM + vLLM/Ollama as the inference-substrate Means picks
