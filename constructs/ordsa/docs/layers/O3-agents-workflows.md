# O3 — Agents and Workflows

> Task-specific AI workers under bounded delegation.

## Definition

The execution layer where agentic systems operate. Agents are **subordinate execution structures**. They do not define their own authority, access, or policy. They receive bounded tasks from O2 orchestrators and operate within those bounds.

The single most important framing in OSA: **agents are workers, not governors.**

A capable agent is still a subordinate one. Capability is not a license to expand scope.

## Authority boundary

- **Receives:** a bounded task from O2, plus an authorization envelope (data scope, tool scope, impact ceiling, time budget).
- **May:** invoke O4 tools, read from O5 data substrate, surface intermediate output back to the orchestrator.
- **May not:** authorize itself, escalate its own privileges, register itself as available for tasks outside its declared specialty, retain state past its delegated session unless O2 explicitly persists it.

If an agent can "decide" to take an action that requires a higher authority, it must do so by **requesting** the action upward, not executing it.

## Examples

- Code assistant agent
- Ticket triage agent
- Root-cause analysis agent
- Threat enrichment agent
- Requirements analysis agent
- Architecture documentation agent
- Test generation agent
- Document summarization agent
- Knowledge-retrieval agent

Each one has a declared specialty, a known orchestrator parent, and an authorization envelope that the parent sets per task.

## What an agent looks like in OSA terms

| Property | Source |
|---|---|
| Identity | Registered at O1; presented to O4 via O1's identity binding |
| Specialty | Declared at registration; matched by O2 when dispatching tasks |
| Authorization envelope | Set per-task by O2 inside the O1 delegation |
| Tool affinities | Declared, but **gated** by the envelope, not by the declaration alone |
| Outputs | Surfaced back to O2; evidence to O6 |

An agent's *declaration* of what it can do is a hint. The *gate* is the envelope.

## Execution-rights distinction

Within an agent's tool invocations (at O4), there are at least five distinct rights:

1. **Read-only** — query only; no side effects.
2. **Recommend-only** — produce candidate actions for a human or higher-ordinal approver.
3. **Draft-only** — create proposed artifacts (PRs, change requests, plans) but not enact them.
4. **Supervised execution** — execute, with a human-or-higher-ordinal in the approval loop before each state change.
5. **Autonomous execution** — execute within the envelope without per-action approval.

These are **separate ordinal permissions**, not a single Boolean. An agent that holds (4) for one tool may hold (1) for another. The envelope specifies per-tool.

## Anti-patterns

- **The "general agent" with all rights everywhere.** Equivalent to handing a service-account credential to the model. Inverts the authority direction.
- **Self-elevating agents.** Agents that, having succeeded at task X, "remember" that they can do X and start volunteering for adjacent tasks Y outside the registration. Should not be possible at all in a correctly-built O1/O2.
- **Tool affinities as authorization.** "The agent has the tool available, therefore it may use the tool." Tools are *capabilities*, envelopes are *authorizations*. Conflating them collapses O3 and O4.
- **Stateful agents without governed state.** Agents that retain memory across sessions in a way O1 does not see. The retained context is itself authority — ungoverned state is a governance gap.

## Evidence flowing up

To O2 (and onward via O6): task completion / refusal, tool invocations attempted, envelope violations attempted (refused at O4), outputs surfaced, time spent inside the envelope, escalation requests raised.

## See also

- [O2 — Domain Orchestrators](O2-domain-orchestrators.md) — the layer that delegates to O3
- [O4 — Tools and Execution Channels](O4-tools-execution.md) — what O3 acts through
- [`../reference-implementations.md`](../reference-implementations.md) — concrete O3 agent standards (forward placeholder)
