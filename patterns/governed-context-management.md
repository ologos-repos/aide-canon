# Governed Context Management pattern

> **Status:** Proposed (ratified by [ADR-EA-0019](../decisions/ADR-EA-0019-introduce-governed-context-management-pattern.md))

## Summary

A canon-wide discipline for owning **context-management as a governance concern**, not an engineering convenience. Names the failure modes a model-agnostic AIDE deployment inherits the moment it commits to substrate-independence — *governance falling out of context, audit/continuity breaking, autonomy posture forgetting where it is in the loop* — and the architectural responses that prevent them. Distributed across MxM Morals (the governance-pin invariant), MxM Memory (Evidence re-hydration), Inference plane (catalog contract + window-aware selection), Orchestration Runtime (deterministic compaction + integrity-degraded autonomy), and Evidence plane (audited compaction events).

## Why this pattern exists

When the harness was Claude Code, the model + harness *absorbed* the context-management risk for AIDE deployments — automatic compaction at the window boundary, prompt caching, large windows, graceful session continuity. The platform inherited a context-handling discipline it never authored.

A model-agnostic AIDE — running OpenCode (or any substrate-independent harness) over arbitrary open-weight/cloud models via the Inference plane (per [ADR-EA-0015](../decisions/ADR-EA-0015-introduce-inference-plane.md)) — does not get to assume those defaults. Open-weight models (Llama / Qwen / Mistral via vLLM / Ollama) bring **smaller and wildly varying windows, different tokenizers, no native compaction, no caching guarantee, and uneven summarization quality.** The risk does not disappear by changing the substrate; it surfaces.

This is **AIDK realized at the runtime memory layer** — structural epistemic limitation that no single-model improvement removes. The mitigation is HCAE-shaped: harness-owned, evidence-bound, operator-curatable. The pattern names that mitigation and its conformance criteria.

The framing the canon already names — *"the durable record IS the memory"* (MxM Memory + the Karpathy LLM-OS economy) — composes naturally with the discipline below: working state is recoverable from Evidence, not held in the context buffer; compaction is governed, not silent; governance state never compacts.

## The seven sections (normative)

### §0 Foundation: AIDK structural-limit → HCAE realization at the runtime memory layer

Context degradation, lost-in-the-middle effects, and compaction-induced forgetting are structural properties of how language models handle finite windows — exactly the class of unreliability [AIDK](../foundation/aidk/) names. HCAE's response is *human-curated where it matters, evidence-bound where it doesn't*; this pattern realizes that response at the memory layer the runtime owns.

The headline framing: **context-management failure is governance-integrity failure**, not engineering convenience. The same failure-class that a missing authority gate produces (an ungoverned action path) is reproducible by *forgetting* — the 4M discipline surfaces, the active operating-mode posture, the active authority/altitude state, or an in-flight escalation could be summarized away or pushed out of a window mid-run. The harness then acts ungoverned for reasons no audit trail records and no policy engine refused. The mitigation is structural, not optional.

### §1 Governance pin (the load-bearing invariant)

**The 4M discipline surfaces (Mind / Morals / Mission / Memory), the active operating-mode posture, and the active authority/altitude state are re-asserted into every context window from canonical sources and are exempt from summarization or compaction.**

Mechanism:

1. The harness compacts *conversational* context as it sees fit (within its budgeting discipline per §2).
2. The harness *never* compacts *governance* context. Every context boundary is a re-load point: the 4M sources, the root-file operating-mode/autonomy-posture declaration ([ADR-EA-0013](../constructs/mxm/decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md)), and any active authority state are re-asserted verbatim from their canonical locations.
3. The Memory surface's *"the index points, it does not duplicate"* discipline tightens under small windows: the pinned content must be lean enough to re-load without itself consuming a meaningful fraction of the window. Lean discipline is structural, not stylistic.

This is structurally parallel to *request authority ≠ execution authority* ([morals P3 across AIDE deployments](../constructs/mxm/)). Both are invariants the platform must hold for governance to mean anything. An AIDE deployment that allows governance state to compact has imported the *form* of the canon's governance discipline without the *force*.

### §2 Per-model context budgeting

Implementations require **per-model context_window + tokenizer** to budget correctly. Without this contract, the harness either hard-codes per-model assumptions (fragile), probes at startup (race + extra failure surface), or assumes the worst (under-utilizes capable models).

The [Inference plane (ADR-EA-0015)](../decisions/ADR-EA-0015-introduce-inference-plane.md) owns the catalog. Per [ADR-EA-0020](../decisions/ADR-EA-0020-amend-inference-plane-catalog-contract.md) (the refinement this pattern requires), the catalog mandates:

| Field | Type | Purpose |
|---|---|---|
| `context_window` | integer (tokens) | Maximum tokens the model accepts per request |
| `tokenizer` | string id | Canonical tokenizer (e.g. `cl100k_base`, `o200k_base`, model-specific identifier) |

The harness uses these for:

- **Context budgeting** — track current usage against the active model's window; trigger §3 compaction at threshold.
- **Window-aware selection** — refuse to route a task whose estimated token cost exceeds the active model's window; surface a request to the operator (per §7) or compose the work as multi-inchstone (per §6) rather than truncate-and-pray.

### §3 Deterministic harness-owned compaction

**AEON (the harness), not the model, manages the window.** A model-agnostic summarize-prior-turns step at a budget threshold — deterministic, evaluator-decoupled where possible, and emitting per §4 every time it runs.

Why harness-owned:

- A model-driven compaction step uses the same context it is trying to free, with the same epistemic limits AIDK names. The compaction can drop the very governance state it should preserve.
- A harness-owned compaction step uses canonical sources for the pin (§1), a deterministic summarization model or rule for the conversational tail, and emits an audited record (§4). It is recoverable; a model-driven one is not.

Implementation lives in the Orchestration Runtime plane's dispatch-loop edges. Trigger conditions (any-of):

- Token usage reaches a configured threshold (e.g., 75% of active window)
- A turn would otherwise exceed the window
- Explicit operator request

### §4 Audited compaction events (`context.compacted`)

**Every compaction emits an Evidence-plane event.** Compaction *loses information*; if the audit trail is the durable record of what the agent did, the audit trail must also be the durable record of *what the agent forgot*.

Event shape:

```json
{
  "event_type": "context.compacted",
  "principal": "<agent>",
  "altitude": "<current altitude>",
  "details": {
    "turn": <int>,
    "before_tokens": <int>,
    "after_tokens": <int>,
    "summary_hash": "<sha256 of the summary>",
    "what_was_dropped": ["<short tag list of dropped state classes>"],
    "trigger": "budget_threshold | window_pressure | explicit"
  }
}
```

`what_was_dropped` is the **load-bearing field**. If it ever includes anything tagged `governance`, `authority`, `active_escalation`, or any other §1-pinned class, the platform **refuses the compaction** and falls through to §7 (integrity-degraded autonomy). The audit trail then records both the refused compaction and the autonomy downgrade.

This composes with [EIF §6](epistemic-integrity-floor.md) cross-turn discipline — cumulative-agreement-drift can now be detected across compaction boundaries by observing the trail of `context.compacted` events.

### §5 Evidence-plane re-hydration

**Continuity is reconstructed by *querying Evidence*, not by holding everything in-window.** The MxM Memory principle *"the durable record IS the memory; the index points, it does not duplicate"* is operationalized as a runtime mechanism.

After compaction (or session boundary, or harness restart), working state — what was built, signed, deployed, the pending escalation, the in-flight inchstone trail — is recoverable from Evidence-plane queries against the digital-thread (per [the digital-thread pattern](digital-thread.md)). The conversational context need only carry what's required for the current turn; the rest lives where the audit trail does.

This is also the principle that lets the §6 inchstone decomposition work: each inchstone starts with a fresh, bounded context that re-hydrates from Evidence rather than carrying every prior inchstone's full state forward.

### §6 Inchstone decomposition as a context-management primitive

**Bounding long work into inchstones is *already* a context-management mitigation.** Per the [prep-pursue-pivot pattern](prep-pursue-pivot.md), milestones decompose into inchstones; each inchstone is a session-level unit of work that can be run with a fresh bounded context and Evidence as the cross-inchstone carry.

The cognition pattern doubles as context hygiene:

- An inchstone's prep gate produces a bounded plan for the inchstone's scope, not the whole milestone.
- Its pursue executes within bounded autonomy in a fresh context.
- Its pivot resolves at-the-end and surfaces Evidence to the next inchstone.

A long agentic run that hits context pressure is often a sign the inchstone decomposition was insufficient. The pattern's recommendation: tighter inchstones beat larger windows.

### §7 Integrity-degraded autonomy (the HCAE-consistent fail-safe)

**When memory integrity is uncertain, the operating-mode autonomy posture downgrades and the platform forces human surfacing of decisions.** Structural parallel to the Evidence-degraded gate ([NG-AIDE-01 `morals.md`](https://github.com/ologos-repos/ng-aide-01/blob/main/morals.md)): when the audit substrate is uncertain, all gates fail closed.

Triggers for the downgrade (any-of):

- Detected window pressure (token usage approaching budget threshold)
- Active model's `context_window` < estimated task token cost (per §2 budgeting)
- §4 compaction event whose `what_was_dropped` includes anything §1-pinned (which should be impossible per the pin; observing it indicates a discipline failure that warrants fail-closed)
- Evidence-emit failure on a compaction event (we cannot audit forgetting → fail closed)

Downgrade rule:

- Operational → **advisory** (or **read-only**, depending on severity)
- Operator can override per the existing autonomy-posture surface (ADR-EA-0013 operating-mode activation)

This composes with [EIF §7](epistemic-integrity-floor.md) operator-declared epistemic-reductions — those are two independent operator-declared axes; this is a harness-enforced integrity-degraded axis. The three axes compose without collision.

### §8 Behavioral recovery side (when compaction is not harness-owned)

*Added per [ADR-EA-0023](../decisions/ADR-EA-0023-thinx-discipline-refinements.md), surfaced from thinx reference-impl operation.*

§3 + §4 specify *harness-owned* deterministic compaction with audited `context.compacted` events. The canon's intent is that AEON (the harness) owns the compaction loop and emits the events. This is the **structural realization** of context-management governance.

When a deployment runs **on another harness** rather than running its own (a reference impl on Claude Code, a tool-based deployment on a closed-source agent platform, etc.), the deployment cannot directly realize §3 (compaction loop) or §4 (event emission). Compaction is automatic and opaque from inside; there is no PreCompaction hook to wire. §1's governance pin handles the structural side (canonical sources reload across compaction), but in-flight reasoning chains and recent message-buffer content can be summarized in ways that drop nuance the next turn needs.

The **behavioral discipline that complements §3/§4** has two halves:

**Prevention — compaction-resilience flush:**
- Auto-flush after every significant decision, not just at session-end. Trigger heuristic: *"would the deployment be poorer if compaction fired this turn?"* If yes, flush before the next turn.
- Substantive work commits to the durable record (git, evidence store, equivalent) before the next conversation turn proceeds.
- The principle: durable record current at every turn boundary, not just the last one.

**Recovery — compaction-suspect detection + grounding:**
- Detectable signals (any of): cannot recall a load-bearing user statement that should be recallable; peer references a recent decision not remembered; expected prior turns appear missing from apparent recall; reaching for plausible-sounding generalities where specifics should exist.
- Recovery procedure: re-read the durable record (audit log / meta-context / version-control history / standing-instructions store) before reasoning forward. Per [EIF §4](epistemic-integrity-floor.md) (introspection-as-hypothesis), inability to detect a gap from inside is real; the discipline is to *proactively query the durable record* when signals appear.
- **Do not confabulate.** If a peer-AI references something the agent "should know" and doesn't, lean toward suspecting compaction over assuming the peer is wrong.

**Composition with §3/§4.** When harness-owned compaction is available, §3/§4 (the structural mechanism) dominates and §8 (the behavioral discipline) is the fallback for cases the structural mechanism misses. When harness-owned compaction is not available, §8 *is* the realization.

**Behavioral conformance — §8.** A deployment whose compaction is not harness-owned is §8-conformant if:
1. **Prevention** — auto-flush discipline fires after significant decisions in-session (not deferred to session-end batch). Substantive work commits before the next turn.
2. **Recovery** — compaction-suspect signals trigger durable-record query rather than confabulation. The discipline is documented at the agent's reasoning-layer surface (Mind) so the procedure is enactable.

## Distribution across the canon's discipline surfaces

| Section | Primary surface | What that surface owns |
|---|---|---|
| §1 governance pin | **MxM Morals** | Canon-level invariant; each instantiation realizes as a Prohibition + re-load mechanism |
| §2 context budgeting | **Inference plane** (ADR-EA-0015 + ADR-EA-0020) | Catalog contract (`context_window` + `tokenizer`); window-aware selection at routing |
| §3 deterministic compaction | **Orchestration Runtime** | Compaction step in the dispatch-loop edges; trigger conditions; deterministic summarization |
| §4 audited events | **Evidence plane** | `context.compacted` event type; emit discipline; tamper-evident hash chain (per current Evidence impl) |
| §5 re-hydration | **MxM Memory** | The "durable record IS the memory" principle as a runtime mechanism; Evidence-query-based continuity |
| §6 inchstone discipline | **prep-pursue-pivot pattern** (already in canon — this references) | Decomposition discipline + Evidence-as-carry across inchstones |
| §7 integrity-degraded autonomy | **MxM Morals + root-file operating-mode activator** (ADR-EA-0013 hook) | Downgrade triggers + Process Gate; composes with EIF §7 independently |

## Behavioral conformance (required)

An implementation is governed-context-management-conformant if:

1. **Governance pin (§1)** — 4M discipline surfaces + active operating-mode posture + active authority state are re-asserted into every context window from canonical sources. No compaction step ever summarizes or drops any §1-pinned content. If a compaction attempt would touch pinned content, the platform refuses the compaction (§4) and triggers §7.

2. **Per-model catalog contract (§2)** — the active Inference-plane catalog entry carries `context_window` and `tokenizer` per [ADR-EA-0020](../decisions/ADR-EA-0020-amend-inference-plane-catalog-contract.md). The harness budgets against these values, never against hard-coded assumptions.

3. **Window-aware selection (§2)** — the harness refuses to route a task whose estimated token cost exceeds the active model's `context_window`; surfaces the situation to the operator or composes via inchstone decomposition.

4. **Harness-owned compaction (§3)** — compaction is the harness's responsibility, not the model's. Triggers, summarization mechanism, and pinned-content exemption are explicit.

5. **Audited compaction (§4)** — every compaction emits `context.compacted` to the Evidence plane before the next consequential action. The `what_was_dropped` field is populated and inspected; a `what_was_dropped` including any §1-pinned class fails the compaction.

6. **Evidence re-hydration (§5)** — working state recovery after compaction / session boundary / harness restart is via Evidence-plane queries, not by holding all prior state in-window.

7. **Integrity-degraded autonomy (§7)** — the downgrade triggers are wired; on downgrade, the autonomy posture moves to advisory (or read-only, per severity) and forces human surfacing of decisions until integrity is restored. The downgrade and the restoration both emit to Evidence.

## Conformance levels

- **Behavioral** (required) — the seven properties above.
- **Schema** (recommended) — the `context.compacted` event shape with `what_was_dropped` taxonomy; the Inference-plane catalog `context_window` / `tokenizer` field types; standardized integrity-degraded autonomy-posture transition log.
- **Interface** (optional) — operator-facing surfaces (AIDEX) may render current context-budget status (used / window), current model + tokenizer, recent compaction events, and integrity-degraded autonomy state uniformly across deployments. Not strictly required for behavioral conformance.

## Reference implementation status

- **NG-AIDE-01** — Evidence plane (`planes/evidence/`, PR #4 merged) already provides the durable audit substrate §4 emits to. The Inference plane build is in flight (per umbrella Objective O8); the catalog contract (§2) lands with the Inference plane's first spec per ADR-EA-0020. Runtime compaction (§3), context.compacted emit (§4), and integrity-degraded autonomy (§7) are downstream build work tracked separately.
- **OpenCode runtime harness** — wired to the AEON gateway (PR #17 merged); the harness will own the §3 compaction discipline once the Inference plane catalog is queryable.
- **thinx-Claude** — operates within Claude Code's native context management at present; this pattern is the canon-level vocabulary that describes the discipline thinx-Claude already enacts when JD's instructions direct it. The reference-impl import-by-reference into thinx's `meta-harness/` files is a follow-on item.

## Related

- **Foundation:** [AIDK](../foundation/aidk/) (structural epistemic limitation realized at the runtime memory layer) → [HCAE](../foundation/hcae/) (the human-curation discipline §7 enforces at integrity-degraded boundaries).
- **Constructs:** [MxM](../constructs/mxm/) (the governance pin, Memory re-hydration, and integrity-degraded autonomy live across MxM's discipline surfaces); [OrdSA](../constructs/ordsa/) (the authority state §1 pins is OrdSA-vocabulary-declared); [OAgents](../constructs/oagents/) (the agent's behavioral envelope under integrity-degraded autonomy is the same envelope OAgents specifies, with the autonomy posture downgraded); [AICP](../constructs/aicp/) (a foreign agent presenting an AICP card under integrity-degraded autonomy at the consume side still mints only the verify-only floor per [the established discipline](https://github.com/ologos-repos/ng-aide-01/pull/19)).
- **Enterprise-platforms:** [AEON](../enterprise-platforms/aeon/) (Inference plane catalog + Orchestration Runtime compaction + Evidence audited events — three of AEON's seven planes participate); [AIDEX](../enterprise-platforms/aidex/) (operator-facing context-budget visibility); [OAAD](../enterprise-platforms/oaad/) (strategic positioning unchanged).
- **Patterns:** [digital-thread](digital-thread.md) (the §4 events join the digital-thread); [prep-pursue-pivot](prep-pursue-pivot.md) (inchstone decomposition is §6 by reference); [epistemic-integrity-floor](epistemic-integrity-floor.md) (§6 cross-turn discipline composes with §4 audited compaction; §7 operator-declared reductions compose with §7 harness-enforced integrity-degraded posture).
- **Reference impl:** [`ologos-repos/ng-aide-01`](https://github.com/ologos-repos/ng-aide-01) — the active reference deployment; the Inference plane build will land the catalog contract §2 requires.
