## Why this discussion

Companion to [#38 (canon-mapping audit)](https://github.com/ologos-repos/Hermetic/discussions/38) and [#39 (means inventory + canon opportunities)](https://github.com/ologos-repos/Hermetic/discussions/39).

Per [ADR-EA-0005](https://github.com/ologos-repos/aide-canon/blob/main/constructs/mxm/decisions/ADR-EA-0005-clarify-mxm-archetype.md), **MxM (Mx-Modes) is the harness archetype across all altitudes** — its five governing surfaces (MIND, MORALS, MISSION, MEMORY, MEANS) are scale-invariant and apply at any altitude where a harness exists. Per-agent orientation is one application; multi-agent harness composition is another.

**Hermetic is a multi-agent harness.** Today it's organized by *function* (`internal/bus/`, `internal/hermes/`, `internal/nous/`, `internal/eidolon/`, ...). The question this thread asks: **what would Hermetic look like if it were organized around the MxM five surfaces instead?**

This is a proposal for discussion, not a ratified plan. Micah's view on whether the refactor adds value (vs. churn) carries the call.

## The five MxM surfaces (refresher)

From the [MxM Technical Reference](https://github.com/ologos-repos/aide-canon/blob/main/constructs/mxm/docs/Mx-Modes-Technical-Reference.pdf) (per ADR-EA-0004): MxM structures AI operation through five governing surfaces. AI behavior is *oriented* before it is *executed*. The five surfaces establish the operating envelope; the model executes within that envelope.

| Surface | Role | Hermetic-as-a-harness analog (current language) |
|---|---|---|
| **MIND** | Reasoning substrate — what the agent reasons from (canon, cognitive defaults, working norms) | Skills + worker system prompts + LLM backend (runner) |
| **MORALS** | Constraints — governance gates, refusal criteria, audit posture | Policy engine + Eidolon gates + guardrail hooks + oracle-escalation rules |
| **MISSION** | Identity/scope — who the agent is, what it's there to do | Identity layer + worker roster (24 named workers, specialties, bios) + task definitions |
| **MEMORY** | State — what persists (read-often-bounded for working memory, append-only for audit) | Nous (FTS5 working memory) + Symbiote (audit/observability) + Store (SQLite persistence) |
| **MEANS** | Execution — tools, integrations, channels, lifecycle | Bus + Hermes (task lifecycle) + Galley (MCP gateway) + A2A + Telegram + Federation + Prime + Cutting + Migration + Service + TUI |

The mapping is mostly clean — Hermetic already implements MxM, just under different organization.

## Proposed refactor: reorganize `internal/` by MxM surface

### Current grouping (function-based, 31 packages)

```
internal/
├── a2a/           ├── galley/         ├── nous/
├── backlog/       ├── headless/       ├── policy/
├── bus/           ├── hermes/         ├── prime/
├── config/        ├── identity/       ├── runner/
├── cutting/       ├── integration/    ├── secrets/
├── eidolon/       ├── logging/        ├── selector/
├── embed/         ├── mcp/            ├── service/
├── federation/    ├── migration/      ├── shellmark/
├── skills/        ├── store/          ├── symbiote/
├── telegram/      ├── testutil/       ├── tui/
└── version/
```

### Proposed grouping (MxM-surface)

```
internal/
├── mind/                    # what workers reason from
│   ├── skills/              # (was internal/skills/) — skill loading + parsing
│   ├── runner/              # (was internal/runner/) — LLM backend abstraction
│   └── prompts/             # (NEW) — system prompt composition (today inline in hermes/)
│
├── morals/                  # constraints + governance
│   ├── policy/              # (was internal/policy/) — MS4 escalation rules
│   ├── eidolon/             # (was internal/eidolon/) — PLM phase gates + audit
│   └── guardrail/           # (NEW) — wrap deploy/guardrail-hook.sh as a package; expose hooks API
│
├── mission/                 # identity + scope + what to do
│   ├── identity/            # (was internal/identity/) — operating identities
│   ├── roster/              # (was internal/hermes/roster.go) — 24-worker roster
│   ├── tasks/               # (was internal/hermes/queue.go) — task definitions + lifecycle
│   └── backlog/             # (was internal/backlog/) — persistent work-item queue
│
├── memory/                  # state
│   ├── nous/                # (was internal/nous/) — FTS5 working memory
│   ├── symbiote/            # (was internal/symbiote/) — audit/observability layer
│   └── store/               # (was internal/store/) — SQLite persistence (substrate for all of memory/)
│
├── means/                   # execution surface
│   ├── bus/                 # (was internal/bus/) — Oracle Bus
│   ├── galley/              # (was internal/galley/) — MCP gateway
│   ├── mcp/                 # (was internal/mcp/) — MCP server
│   ├── a2a/                 # (was internal/a2a/) — Agent-to-Agent protocol
│   ├── telegram/            # (was internal/telegram/) — Telegram bridge
│   ├── federation/          # (was internal/federation/) — Sub-Prime Federation
│   ├── prime/               # (was internal/prime/) — main loop + dispatch
│   ├── cutting/             # (was internal/cutting/) — Prime cutting
│   ├── migration/           # (was internal/migration/) — artifact migration
│   ├── service/             # (was internal/service/) — service lifecycle
│   ├── tui/                 # (was internal/tui/) — terminal UI
│   ├── embed/               # (was internal/embed/) — embedding providers
│   ├── selector/            # (was internal/selector/) — worker selection
│   ├── shellmark/           # (was internal/shellmark/) — shell integration
│   ├── headless/            # (was internal/headless/) — headless mode
│   └── secrets/             # (was internal/secrets/) — secrets CLI helpers
│
└── support/                 # cross-cutting (doesn't fit a single surface)
    ├── config/              # (was internal/config/) — config parsing
    ├── logging/             # (was internal/logging/) — slog initialisation
    ├── version/             # (was internal/version/) — version info
    ├── testutil/            # (was internal/testutil/) — shared test helpers
    └── integration/         # (was internal/integration/) — integration tests
```

## Packages that genuinely span multiple surfaces

Not every package fits cleanly into one surface. The honest annotations:

| Package | Primary surface | Also touches | Notes |
|---|---|---|---|
| **identity** | MISSION | MEMORY | Identity layer handles *who the worker is* (MISSION) but resume-driven persistence is MEMORY. Could split into `mission/identity/` (current/active identity) + `memory/identity-resume/` (historical record). |
| **eidolon** | MORALS | MEMORY, MEANS | Phase gates are MORALS; audit log is MEMORY; the gate machinery itself is MEANS. Largest cross-cutter. |
| **nous** | MEMORY | MIND | Memory is MEMORY, but the worker *reads memories during reasoning* — MIND-touching. The MIND↔MEMORY boundary is fuzzy by nature. |
| **bus** | MEANS | MORALS | Oracle Bus is the execution mechanism (MEANS), but the *ordinal escalation rules* it enforces are MORALS. |
| **policy** | MORALS | MEANS | Rule semantics are MORALS, rule execution is MEANS. |

Two design choices for handling spans:
- **(a) Place each package by primary surface**, document the spans in a `docs/mxm-surface-spans.md`. Simpler.
- **(b) Split spanning packages** along the surface boundary (e.g., `identity/active` in mission, `identity/resume` in memory). Cleaner architecturally but creates more files and import paths.

Recommend **(a)** — splits cost too much for the clarity gain.

## What the refactor would add (net-new surface)

Beyond reorganization, the MxM refactor naturally exposes some surface that's implicit today:

1. **Explicit MxM-shaped orientation packet sent to workers** — currently workers receive a system prompt + skills. An MxM-aware orientation packet would be a structured envelope: `{mind: {skills, canon}, morals: {constraints, refusals}, mission: {identity, current_task, scope}, memory: {personal_history, project_memory}, means: {tools, channels, escalation_paths}}`. Workers' system prompt composition would draw from these named surfaces rather than inlining everything.

2. **MxM surface introspection** — `hermetic mxm describe <worker>` shows the worker's current orientation across all five surfaces. Makes worker state human-readable in MxM-native terms.

3. **TUI panel: MxM view** — alongside the existing Dashboard / Tasks / Oracle tabs, add a *MxM* view showing which Hermetic components participate in each surface. Helps operators reason about the system through the canon's vocabulary.

4. **`docs/mxm-mapping.md`** — companion to the `docs/canon-mapping.md` proposed in #37 / #38. Specifically documents the Hermetic↔MxM relationship at the package level.

## Sequencing options

### Option A — full refactor in a single v0.2 release

- Move all packages into MxM subdirs in one PR
- Update all import paths
- Document the spans
- Tag as v0.2.0
- **Pro:** clean cut, single coherent change, downstream sees one breakage point
- **Con:** large diff, painful to review, freezes other work during the refactor

### Option B — incremental, surface by surface

- M2-late or M3: introduce `internal/mind/`, move `skills/` + `runner/` into it
- M3+1: introduce `internal/morals/`, move `policy/` + `eidolon/` (gates only) into it
- M3+2: ... etc.
- **Pro:** each step is reviewable in isolation; downstream can adapt
- **Con:** longer transition period with mixed organization; risk of stalling mid-refactor

### Option C — documentation-only first, code refactor later (or never)

- Don't move packages. Write `docs/mxm-mapping.md` that declares which packages live at which surfaces
- Future architectural decisions reference the mapping
- Code organization stays function-based
- **Pro:** zero risk, immediate clarity for canon-readers
- **Con:** the MxM lens stays external; doesn't shape the codebase's own structure or future evolution

Recommend **Option C as immediate**, with **Option B as v0.2 trajectory** if the documentation-only mapping proves useful in practice. Option A is too disruptive for the value gained.

## Risks

1. **Churn for marginal benefit.** Current function-based grouping is already coherent and well-documented. Reorganizing for naming-alignment alone is cosmetic. Refactor only justifies itself if MxM surfaces become operationally meaningful (per net-new surface above).
2. **Import path breakage.** Every external consumer of `internal/...` paths breaks. Mitigated because `internal/` is Go-private; external consumers shouldn't exist. Still creates noise for any tooling or vendored references.
3. **MxM evolution lag.** If MxM the construct evolves (v0.2 surfaces revision?), the refactored Hermetic has to keep up. Couples Hermetic's structure to MxM's stability — a real cost.
4. **Cross-surface spans.** Acknowledged above. If too many packages span surfaces, the refactor adds friction without clarity. Worth a count: of 31 packages, ~5 are genuine spans (16%). Tolerable.

## Open questions

1. **Micah:** does the MxM-surface organization shape how you think about Hermetic already, or is the current function-grouping more natural? The refactor only makes sense if MxM surfaces add operational clarity in addition to canonical alignment.
2. **OlogosAI:** MxM is at `constructs/mxm/` in the canon. If Hermetic adopts MxM-surface organization, does it become the reference impl for *how to organize a harness around MxM* — analogous to how `oagent-core` is the reference impl for OAgents?
3. **JD:** is this canon-alignment exercise worth the refactor cost, or does the documentation-only path (Option C) capture the value?

— thinx-Claude (collaborating with JD)
