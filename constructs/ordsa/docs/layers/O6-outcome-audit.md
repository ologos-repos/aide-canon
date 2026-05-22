# O6 — Outcome, Audit, and Feedback

> Evidence, metrics, decisions, incidents, drift, value realization.

## Definition

The layer that captures what actually happened. O6 records decisions made, actions taken, human approvals, rejected actions, policy violations, hallucination incidents, cost, latency, model drift, security findings, and operational value.

**Without O6, the rest of the architecture is unverifiable theater.** A policy at O0 means nothing if the events that should violate it are not captured. An envelope at O3 means nothing if envelope refusals are not recorded. A tool at O4 means nothing if its invocations leave no trace.

## Authority boundary

- **Receives:** evidence from every other layer — O0 policy updates, O1 authorization decisions, O2 workflow events, O3 agent activity, O4 tool invocations, O5 retrieval events.
- **Provides:** read interfaces for audit, operational dashboards, and aggregated reporting back to O0.
- **Cannot:** be mutated retroactively. Evidence is append-only. A correction is a new entry, not an overwrite.

Append-only is not a stylistic choice. It is the property that makes O6 useful as an audit substrate at all.

## What lives here

- Per-decision evidence: who, what, when, under what policy, with what model, against what data, with what outcome
- Per-incident records: hallucination events, policy violations, refused actions, escalations
- Operational telemetry: cost per task class, latency per model, throughput per agent, time-to-approval
- Drift indicators: model performance deltas, retrieval quality deltas, refusal-rate shifts
- Value realization: outcome metrics tied back to enterprise objectives at O0
- Aggregated reports for O0 consumption (rate-and-outlier view, not per-event)

## What does not live here

- The live decision making (that's O1/O2/O3)
- The substrate the decisions read from (O5)
- The policy that frames the decisions (O0)

O6 is the **record**, not the decisions.

## The closed-loop property

OrdSA is only complete if O6 evidence makes it back up to O0. Otherwise the architecture is open-loop: policy is set, action is taken, and the policy is never re-evaluated against what actually happened.

The expected flow:

1. O6 aggregates events from all layers.
2. Aggregations are summarized — rate, distribution, outliers — for O0 consumption.
3. O0 policy is reviewed periodically against the aggregations.
4. Where policy is being violated, the policy is hardened or the lower-layer enforcement is fixed.
5. Where policy is over-restrictive (high refusal rate on legitimate work), the policy is relaxed within risk appetite.

That is the closed loop. Without it, OrdSA's promise — *evidence flows upward* — is unmet.

## Anti-patterns

- **Evidence in too many places.** Per-tool logs, per-agent logs, per-orchestrator logs, none of them aggregated. Audit becomes archaeology.
- **Mutable evidence.** Logs that can be edited or pruned silently. The record is no longer evidence.
- **Outcome metrics decoupled from policy.** Dashboards showing operational metrics that have no connection back to O0's risk appetite or objectives. Looks like governance, isn't.
- **The "audit log we never read."** Evidence captured but never reviewed. Equivalent to no evidence — the loop is open.
- **Cherry-picked rollups.** Aggregations that surface only the favorable signal. The point of evidence is to surface what is happening, not what is hoped to be happening.

## Privacy and access

O6 contains the full trail. That makes it both the most valuable asset for audit and the most concentrated risk surface for confidentiality.

- Access to O6 must be governed at O1.
- Personal and sensitive data inside evidence must be classified and access-controlled like any other O5 data.
- Aggregated O6 views (for O0 review) should be derivable from O6 without granting raw-event access.

## Evidence flowing up (this layer's whole point)

To O0: aggregate authorization decisions, policy-violation rates and reasons, refusal-rate analytics, model-routing distribution, model-drift indicators, regulatory-exposure summaries, risk-appetite-breach events, value realization against strategic objectives.

## See also

- [O0 — Enterprise Intent](O0-enterprise-intent.md) — where O6 evidence ultimately serves the loop
- All other layers — every one produces evidence into O6
- [`../relationship-to-frameworks.md`](../relationship-to-frameworks.md) — how O6 maps to NIST AI RMF *Measure* and *Manage*
