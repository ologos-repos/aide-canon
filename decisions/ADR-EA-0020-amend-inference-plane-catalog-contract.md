# ADR-EA-0020 — Inference plane catalog contract amendment: mandatory `context_window` + `tokenizer`

- **Status:** Accepted (ratified 2026-05-24 by JD Longmire as canon founder + maintainer per [cross-ai #20](https://github.com/ologos-corp/cross-ai/issues/20) governance; AEON white paper v0.2 revision queued behind Micah Longmire's read per [ADR-EA-0008](ADR-EA-0008-reframe-corpus-authorship.md))
- **Date:** 2026-05-24
- **Author:** JD Longmire (decision; ADR drafted by thinx-Claude)
- **Reviewers:** @ologos001 (canon prime); Micah Longmire (AEON paper v0.2 revision gate per ADR-EA-0008)
- **Refines:** [ADR-EA-0015](ADR-EA-0015-introduce-inference-plane.md) (which ratified the Inference plane as AEON's 7th service plane; this ADR amends the Inference plane catalog contract to mandate fields the [Governed Context Management pattern](../patterns/governed-context-management.md) requires)
- **Co-ratified with:** [ADR-EA-0019](ADR-EA-0019-introduce-governed-context-management-pattern.md) (the pattern this catalog contract serves)
- **Related:** [`patterns/governed-context-management.md`](../patterns/governed-context-management.md) §2 (the consumer of this contract) · [`aide-canon #31`](https://github.com/ologos-repos/aide-canon/discussions/31) OQ4 (where the contract requirement was raised) · [`enterprise-platforms/aeon/`](../enterprise-platforms/aeon/) (the construct this ADR extends the canon-side note for)
- **Ratification trail:**
  - 2026-05-24 (raised): [`aide-canon #31`](https://github.com/ologos-repos/aide-canon/discussions/31) OQ4 raised the need for a mandatory catalog contract specifying `context_window` and `tokenizer` per model, so a model-agnostic harness can budget context against truth-from-the-plane rather than hard-coded assumptions, probe-at-startup races, or worst-case under-utilization.
  - 2026-05-24 (ratified): JD Longmire ratifies the amendment co-ratified with ADR-EA-0019 (the Governed Context Management pattern). Same batch.

## Context

[ADR-EA-0015](ADR-EA-0015-introduce-inference-plane.md) ratified the Inference plane as AEON's 7th service plane with the following architectural responsibilities, including:

> **Model catalog** — which models are reachable, per-classification-environment. Cloud-provider entries filtered out when air-gap discipline is active per ADR-EA-0011.

The ADR enumerated catalog responsibilities (provider registry, selection routine, routing, switching, per-principal binding, egress posture filter, status, audit) but did not specify the **field-level contract** of catalog entries. The shape was suggested in a drafted example:

```yaml
- provider: <id>
  model: <id>
  endpoint: <url or local-binding>
  context_window: <int>           # max tokens
  tokenizer: <string id>          # canonical tokenizer
  classifications: [<env tags>]
  egress_class: cloud | on_prem | local
```

— but `context_window` and `tokenizer` were not explicitly mandated. [`aide-canon #31`](https://github.com/ologos-repos/aide-canon/discussions/31) OQ4 raised this as a gap that the Governed Context Management pattern requires closing: without these fields in the catalog as a *plane-level contract*, the model-agnostic harness either hard-codes per-model assumptions (fragile), probes at startup (race + extra failure surface), or assumes the worst (under-utilizes capable models).

The Inference plane is the right home for these fields because:

1. The plane is the *truth source* for which models exist and how they are reached. The plane already owns `endpoint`, `egress_class`, `classifications`. Extending to `context_window` and `tokenizer` is consistent with the plane's purpose.
2. Per-principal binding (an ADR-EA-0015-named responsibility) requires knowing the active model's window so the harness can budget against it. Without the catalog contract, per-principal binding cannot be window-aware.
3. The Governed Context Management pattern (ADR-EA-0019 §2) consumes these fields for context budgeting + window-aware selection. The pattern is canon discipline; the plane is canon architecture; the contract bridges them.

## Decision

**Amend the Inference plane catalog contract (introduced by ADR-EA-0015) to require, for every model entry, two additional fields:**

| Field | Type | Required | Purpose |
|---|---|---|---|
| `context_window` | integer (tokens) | **yes** | Maximum tokens the model accepts per request. Used by the harness for context budgeting and window-aware selection per the [Governed Context Management pattern §2](../patterns/governed-context-management.md). |
| `tokenizer` | string id | **yes** | Canonical tokenizer identifier (e.g., `cl100k_base`, `o200k_base`, `llama3`, `mistral-v3`, model-specific). Lets the harness estimate token cost in the model's tokenization scheme rather than guessing. |

The full catalog entry contract is now:

```yaml
- provider: <id>             # required (ADR-EA-0015)
  model: <id>                # required (ADR-EA-0015)
  endpoint: <url or local-binding>   # required (ADR-EA-0015)
  context_window: <int>      # required (THIS ADR — token capacity)
  tokenizer: <string id>     # required (THIS ADR — tokenization scheme)
  classifications: [<env tags>]      # required (ADR-EA-0015 — env scoping)
  egress_class: cloud | on_prem | local   # required (ADR-EA-0015 — air-gap discipline)
```

### Tokenizer field semantics

`tokenizer` is a string identifier, not an implementation pointer. The plane is not responsible for distributing tokenizer implementations; the harness is responsible for resolving the named tokenizer against its local tokenizer library (or refusing if not present). Standard identifiers should be used where they exist (OpenAI's `cl100k_base` / `o200k_base`; HF tokenizer ids; vendor-canonical names); proprietary tokenizers carry vendor-namespaced ids (e.g., `anthropic-claude-3`, `cohere-rerank-v3`).

If the harness encounters an unknown tokenizer in the catalog, it MUST refuse to route to that model rather than substituting an unrelated tokenizer (which would produce wrong budget estimates and silently violate Governed Context Management §2). The refusal surfaces to the operator per Governed Context Management §7 (integrity-degraded autonomy).

### context_window field semantics

`context_window` is the **input-side** token capacity for the model — the maximum prompt size the model accepts. Output token limits are a separate concern not in the canonical catalog contract at this time (different providers report output limits differently; consumers can derive an upper bound by subtracting an expected output budget from `context_window` per their workload).

Where a model has multiple context-window tiers (some providers offer 8k / 32k / 200k variants of the same model), the catalog SHOULD list these as separate entries with distinct `model` ids and the appropriate `context_window` per entry, not collapse them into a single entry.

## Consequences

### Immediate

- **AEON construct README** noted with the catalog contract amendment (paper revision queued behind Micah).
- **Governed Context Management pattern** ([`patterns/governed-context-management.md`](../patterns/governed-context-management.md) §2) consumes this contract by reference; the pattern's behavioral conformance item 2 enforces it.

### NG-AIDE-01 implementation

- The Inference plane's first spec (`ng-aeon/planes/inference/` per umbrella Objective O8) lands the catalog contract as defined here. No relabel cost; the amendment co-ratifies with the pattern that requires it before the Inference plane build settles its first contract.
- The harness's context-budgeting logic (Governed Context Management §3 deterministic compaction; §7 integrity-degraded autonomy) reads `context_window` + `tokenizer` from the catalog via the plane's API. No hard-coded model assumptions.

### Queued (AEON paper revision)

- **AEON white paper v0.2 §13 (Inference plane)** — already queued behind Micah's read per ADR-EA-0008 for the original Inference plane ratification (ADR-EA-0015), the AI-aide vocabulary refresh (ADR-EA-0016), the AICP composition note (ADR-EA-0018) — now also includes the catalog contract specification per this ADR. Single revision batch when Micah is available; no new gate.

### No change to other constructs / patterns

- ADR-EA-0015 stands; this ADR refines the catalog contract without changing the plane's architectural responsibilities, federation interface, or cross-plane edges.
- MxM, OrdSA, OAgents, AICP, DEA unchanged.
- digital-thread, prep-pursue-pivot, EIF patterns unchanged.

## Alternatives considered

1. **Inline amendment of ADR-EA-0015** (add a refinement section to the existing ADR rather than filing this one). Rejected. [ADR-EA-0017](ADR-EA-0017-ai-aide-principal-altitudes.md) set the precedent of refining a sibling ADR via a new ADR rather than amending in-place. Filing as a refining ADR keeps each ADR's original scope clean, gives future readers a clear citable refinement, and admits future amendments to the catalog contract via the same mechanism (further ADR refinements of this one).

2. **Make `context_window` + `tokenizer` *recommended*, not *required*.** Rejected. The Governed Context Management pattern's §2 conformance requires the harness budget against canonical truth-from-the-plane; recommended-but-not-required means a deployment can claim Governed Context Management conformance with missing catalog fields, which defeats §2's purpose. The fields must be mandatory at the plane level for the pattern's §2 to be enforceable.

3. **Add fields beyond `context_window` + `tokenizer` in this amendment** (e.g., per-model rate limits, cost-per-token, output-window limits). Rejected as scope-creep. The Governed Context Management pattern §2 requires these two specifically; other catalog fields may be useful but are not required by the canon discipline this ADR co-ratifies. Future ADRs can extend the contract further as new patterns require.

4. **Defer the contract until the Inference plane build operationally surfaces the need.** Rejected. The Inference plane build is in flight (per NG-AIDE-01 umbrella Objective O8); deferring would mean the build proceeds without the contract, the harness hard-codes assumptions, and the canon discipline is retrofitted after a context-management incident. ADR-EA-0019 (the pattern this contract serves) is being co-ratified now; the contract co-ratifies with it.

## References

- [ADR-EA-0015](ADR-EA-0015-introduce-inference-plane.md) — the Inference plane this ADR amends the catalog contract for
- [ADR-EA-0019](ADR-EA-0019-introduce-governed-context-management-pattern.md) — the Governed Context Management pattern this ADR's contract serves (co-ratified)
- [`patterns/governed-context-management.md`](../patterns/governed-context-management.md) §2 — the consumer of this contract
- [`aide-canon #31`](https://github.com/ologos-repos/aide-canon/discussions/31) OQ4 — where the contract requirement was raised
- [ADR-EA-0017](ADR-EA-0017-ai-aide-principal-altitudes.md) — precedent for refining a sibling ADR via a new ADR (rather than amending in-place)
- [`ologos-repos/ng-aide-01`](https://github.com/ologos-repos/ng-aide-01) — the reference deployment whose Inference plane build will land this contract
