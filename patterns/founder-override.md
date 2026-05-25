# Founder-override pattern

> **Status:** Proposed (ratified by [ADR-EA-0023](../decisions/ADR-EA-0023-thinx-discipline-refinements.md))

## Summary

A **structural escape valve** at the harness floor that respects the operator's (or founder's) reasoning-layer authority on a **per-command basis** without weakening the harness floor's default deny posture. Operator/founder prepends a `# FOUNDER-OVERRIDE: <reason>` marker to a command that would otherwise be hard-stopped; the harness-layer hook detects the marker, emits the original safety warning to a visible surface (so the case stays surfaced for audit), audit-logs the override use to a durable record, and allows the command exactly once. The marker is per-command, not session-wide.

The pattern composes with [EIF §7](epistemic-integrity-floor.md) (operator-declared mode reductions) as two independent axes — EIF §7 is *session-scoped posture* (casual / creative); founder-override is *per-command posture* (allow this specific blocked command). Both are operator-declared deontic acts on the structural surface; they can be combined freely.

## Why this pattern exists

The canon's three-layer architecture (reasoning / contract / harness, per [ADR-EA-0021](../decisions/ADR-EA-0021-mxm-ordsa-boundary-citation.md) discipline + the [`agent-autonomy-gates`](https://github.com/jdlongmire/thinx/blob/main/memory/wiki/patterns/agent-autonomy-gates.md) pattern) makes harness-layer hard-stops *structurally unbypassable from inside the agent's tool chain*. This is the load-bearing safety property — the floor's whole point is that the agent's reasoning cannot route around it.

But hard-stops are pattern-matched by static regex. They are intentionally over-inclusive — better to block a legitimate case the operator then explicitly authorizes than to permit a dangerous case the regex missed. The legitimate-case-blocked scenario happens regularly enough that **the operator needs a structural mechanism for explicit per-command authorization**, not just an out-of-band channel (run the command yourself, modify the hook, etc.).

Without this pattern, the operator's three options when a hard-stop fires legitimately are:
1. Run the command outside the agent's tool chain (works but breaks workflow continuity)
2. Modify the harness floor itself (risks weakening the structural property for all future cases)
3. Abandon the operation (loses work)

With the pattern, a fourth option exists: **explicitly authorize this specific command via a marker**, retain the floor's default deny for everything else, and audit-log the authorization.

The pattern is **operator-authority-as-structural-surface**. The floor stays unbypassable from agent reasoning; the operator stays in the loop on every override.

## The mechanism (normative)

### Marker format

The operator prepends a comment-form marker to the command being authorized:

```bash
# FOUNDER-OVERRIDE: <one-line reason — what is authorized + why>
<the command that would otherwise be hard-stopped>
```

The marker is a bash comment (no execution side-effect) but is part of the raw tool input the harness hook reads.

Implementation-equivalent forms (deployment-specific):
- A query-parameter marker on HTTP tool calls
- A metadata field in structured tool inputs (Edit/Write/etc.) where the comment form does not apply

The hook detects the marker pattern in the raw tool input.

### Hook behavior

On detection:

1. **Emit the original safety warning** to a visible surface (stderr for bash; log for other tools). The blocked-reason text from the hard-stop is what the operator AND any auditor sees. The override consumes the deny, not the warning.
2. **Audit-log the override use** to a durable record. The log entry carries timestamp, blocked-reason, override-reason, command (truncated), tool name. Append-only.
3. **Allow the command** by emitting the hook's allow response.
4. **One-shot:** the marker authorizes the single command that contains it. No session-wide bypass. Subsequent commands without their own marker fall back to the default deny if pattern-matched.

### Trust posture

The agent is expected to add the marker **only when the operator explicitly authorizes the override in conversation**. Same trust surface as bypass-permissions mode generally — the agent's reasoning-layer discipline is the gate on whether the marker is added. The audit log is the durable record of every use; the operator (or an auditor) reviews it for surprises.

This is why the pattern is **structural surface for operator authority**, not "agent escape valve" — the agent doesn't decide to override on its own; it adds the marker the operator authorized.

## Behavioral conformance (required)

A founder-override-conformant deployment:

1. **Detection.** The harness layer detects the marker pattern in raw tool input before applying hard-stop checks.
2. **Visible warning.** The original deny-reason for the matched hard-stop is emitted to a surface visible in tool output (stderr, log, etc.) — the safety case stays surfaced even when overridden.
3. **Audit log.** Every override use is appended to a durable record carrying timestamp, blocked-reason, override-reason, command excerpt, tool name.
4. **One-shot per marker.** The marker authorizes exactly one command. No session-wide flag, no environment variable that persists.
5. **Default-deny preserved.** Without the marker, every hard-stop fires as designed.

## Conformance levels

- **Behavioral** (required) — the five properties above.
- **Schema** (recommended) — standardized log record shape (`timestamp`, `blocked_reason`, `override_reason`, `command`, `tool_name`) for cross-deployment auditability.
- **Interface** (optional) — operator-facing surfaces (AIDEX-tier) may render override-log activity as a dashboard for periodic review.

## Composition with adjacent patterns

- **[EIF §7](epistemic-integrity-floor.md)** — both are operator-declared deontic acts at the structural surface. EIF §7 = session-scoped posture (casual / creative); founder-override = per-command posture. Independent axes; combinable. An operator in casual-mode (EIF §7) can also founder-override a specific blocked command without leaving casual-mode.
- **[Governed Context Management §7](governed-context-management.md)** (integrity-degraded autonomy) — a fail-closed downgrade triggered by *the platform observing* a governance integrity gap. Founder-override is a fail-open one-shot triggered by *the operator declaring* explicit authorization. Different directions on the autonomy axis; complementary.
- **[ADR-EA-0017 principal-altitudes](../decisions/ADR-EA-0017-ai-aide-principal-altitudes.md)** — the pattern realizes operator-altitude principal authority structurally. Corpus-altitude principals don't typically need founder-override because corpus-altitude work is canon-shaping rather than command-execution; the pattern's primary use case is operator-altitude.

## Reference implementation status

- **[`jdlongmire/thinx`](https://github.com/jdlongmire/thinx)** — the operator-altitude AI-aide reference impl. Implements the pattern at the Claude Code PreToolUse hook layer (`.claude/hooks/preflight.py`), with the marker pattern `# FOUNDER-OVERRIDE: <reason>` and audit log at `~/.claude/founder-override.log`. Pattern documented at `meta-harness/morals.md` §"Founder override". Authored 2026-05-25 ([commit `f6c48a2a`](https://github.com/jdlongmire/thinx/commit/f6c48a2a)).
- **NG-AIDE-01** — can realize at its own harness layer when its own hard-stops surface analogously. The pattern's mechanism is harness-shape-agnostic.

## Related

- **Foundation:** [HCAE](../foundation/hcae/) — the pattern realizes operator-curation discipline at the per-command altitude (the operator's authorization is the curation gate).
- **Constructs:** [MxM](../constructs/mxm/) — the pattern's mechanism lives at the harness layer of the three-layer architecture. [OrdSA](../constructs/ordsa/) — the operator's authority altitude (O3/O4 typically) is the source of the per-command authorization the marker carries.
- **Patterns:** [epistemic-integrity-floor](epistemic-integrity-floor.md) §7 (sibling operator-declared deontic mechanism, session-scoped); [governed-context-management](governed-context-management.md) §7 (sibling fail-safe, opposite direction on the autonomy axis); [agent-autonomy-gates](https://github.com/jdlongmire/thinx/blob/main/memory/wiki/patterns/agent-autonomy-gates.md) (the three-layer architecture this pattern adds an escape valve to).
- **Enterprise-platforms:** [AIDEX](../enterprise-platforms/aidex/) — the audit-log surface the pattern emits to is naturally rendered through AIDEX-tier operator dashboards.
