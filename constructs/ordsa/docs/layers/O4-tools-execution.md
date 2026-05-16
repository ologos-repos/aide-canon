# O4 — Tools and Execution Channels

> APIs, automation, ITSM, CI/CD, cloud consoles, repositories.

## Definition

The layer where AI begins to affect enterprise state. O4 contains the actual mechanisms through which actions happen: APIs, scripts, automation tools, CI/CD pipelines, ITSM integrations, cloud consoles, knowledge retrieval systems, engineering repositories, and data platforms.

Because this is where intent becomes effect, O4 requires the **strongest execution boundaries** in the architecture.

## Authority boundary

- **Receives:** invocations from O3 agents, carrying an authorization envelope established by O2 under O1 delegation.
- **Enforces:** the envelope. Every tool at O4 is responsible for refusing invocations whose envelope does not authorize the requested action.
- **Cannot:** trust the agent's word for what it is allowed to do. The envelope is a contract; the tool is the enforcer at point-of-action.
- **Must:** emit evidence to O6 for every invocation — accepted, refused, errored.

A tool that takes an action without verifying the envelope is the architectural equivalent of an unguarded admin console.

## The five execution rights, made concrete

OSA distinguishes five execution rights, each of which is a **separate ordinal permission**:

| Right | Effect | Typical use |
|---|---|---|
| Read-only | No state change | Inspection, analysis, retrieval |
| Recommend-only | No state change; produces candidate actions | Suggestion engines, advisory output |
| Draft-only | Creates inert proposals (PRs, change requests, plans) | Proposed PR, draft ticket, planned change |
| Supervised execution | State change with per-action human or higher-ordinal approval | Production-touching automation under review |
| Autonomous execution | State change inside the envelope without per-action approval | Well-bounded routine tasks, low-impact recoveries |

The envelope must specify which of these the invocation holds **per tool, per action class**. A blanket "this agent can use this tool" is too coarse.

## What lives here

- The tool itself (the API, the CLI, the integration, the pipeline)
- The tool's envelope-verification gate
- The tool's evidence-emission path to O6
- The tool's failure mode when the envelope refuses

## What does not live here

- The agent (O3) — the invoker is separate from the invoked
- The authorization envelope itself (set at O1/O2)
- The data the tool operates on (O5)
- The outcome record (O6)

## Anti-patterns

- **Tools that trust the caller.** A tool whose access control is "the caller has the API key" — that is identity, not authorization. The envelope is what tells the tool whether *this specific invocation* is authorized.
- **Tools without refusal evidence.** A tool that silently no-ops on a refused action, with no record to O6. Equivalent to a fire alarm with the speaker unplugged.
- **Blanket admin tools.** An "execute arbitrary shell" tool whose envelope cannot meaningfully constrain it. The blast radius is the entire reachable surface — making it unsuitable for any envelope short of (5) autonomous on a tightly-scoped surface.
- **Tool-side identity disguise.** Tools that operate as a single service principal regardless of upstream identity. Erases the attribution chain O1 worked to establish.

## Evidence flowing up

To O6 (read by O0, O1, O2, and audit roles): per-invocation record — what tool, what action, what envelope, what verdict (accepted / refused / errored), what state changed, what evidence was captured for the change.

## See also

- [O3 — Agents and Workflows](O3-agents-workflows.md) — what invokes O4
- [O5 — Data and Knowledge Substrate](O5-data-knowledge.md) — what O4 reads from and writes to
- [O6 — Outcome, Audit, Feedback](O6-outcome-audit.md) — where O4's evidence lands
