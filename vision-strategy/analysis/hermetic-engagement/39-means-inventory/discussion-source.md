## Why this discussion

Sibling thread to [#38 (canon-mapping audit)](https://github.com/ologos-repos/Hermetic/discussions/38). #38 mapped Hermetic's architecture against AEON's six service planes. This thread inventories Hermetic's **means** — the execution-layer capabilities (skills, scripts, internal packages, UIs, deploy automation, etc.) — and identifies opportunities where the AIDE canon could either adopt patterns from Hermetic or reference Hermetic as the canonical impl.

*"Means"* in the framework vocabulary (per [thinx 4M+1](https://github.com/jdlongmire/thinx/blob/main/meta-harness/mind.md)) = the execution surface, distinct from MIND (reasoning), MORALS (constraints), MISSION (identity/scope), MEMORY (state). Hermetic's means are extensive — 31 internal Go packages, 6 worker skills, 13 implementation plans, 20 dispatch briefs, a Svelte web UI, a Bubbletea TUI, 4 deploy scripts.

## Inventory

### 1. Worker skills (6) — markdown w/ YAML frontmatter

Convention identical to [thinx skills](https://github.com/jdlongmire/thinx/blob/main/means/skills.md) (`---\nname:\ndescription:\n---` frontmatter).

| Skill | Purpose |
|---|---|
| `worker-guide.md` | Worker identity, task lifecycle, claim/complete, heartbeat, tool access, escalation |
| `oracle-protocol.md` | When to escalate vs. decide; ordinal-level routing semantics |
| `dispatch-coordination.md` | Signal/gate DAG semantics for workers |
| `federation-awareness.md` | Sub-Prime federation; parent-prime delegation; callback flow |
| `platform-overview.md` | Hermetic's three-layer architecture at the agent's altitude |
| `tool-reference.md` | All `hermes_*`, `oracle_*`, `dispatch_*` tools available to workers |

### 2. Internal packages (31) — the deep capability surface

Grouped by function:

**Authority/escalation** — `bus` (Oracle Bus, L0→L3), `policy` (MS4 escalation policy engine, YAML rules), `federation` (parent-prime forwarding), `identity` (operating identity layer)

**Task lifecycle** — `hermes` (worker roster, atomic claims, affinity-aware), `backlog` (persistent work-item queue via MCP), `runner` (CLI tool delegation backends — Claude Code, etc.), `eidolon` (PLM phase gates, audit log, SHA-256 artifacts)

**Memory + observability** — `nous` (FTS5-backed memories, per-worker scoping, 8KB caps), `symbiote` (audit/observability layer alongside TaskLog), `store` (SQLite WAL persistence via `modernc.org/sqlite`, pure-Go)

**Integration** — `mcp` (MCP server, stdio transport via `mark3labs/mcp-go`), `galley` (MCP tool catalog with semantic search via Ollama embeddings), `embed` (multi-provider embedding abstraction), `a2a` (Google Agent-to-Agent protocol — Hermetic discoverable/callable by any A2A orchestrator), `telegram` (Telegram bridge with inline buttons + rate limiter)

**Prime lifecycle** — `prime` (main loop + dashboard metrics HTTP), `cutting` (Prime cutting — `hermetic cut my-prime` creates isolated instances), `headless` (3-source headless-mode detection), `migration` (auto-upgrade of prime artifacts), `service` (systemd / launchd / Windows service abstraction)

**Operator surfaces** — `tui` (Bubbletea TUI — worker roster, activity feed, task stats), `secrets` (CLI helpers for secrets subcommands), `shellmark` (shell integration), `selector` (worker selection)

**Cross-cutting** — `logging` (slog), `version` (ldflags-injected), `testutil` (shared test infrastructure), `config`, `integration` (integration tests)

### 3. Plans + dispatch briefs (33) — visible roadmap

- `docs/superpowers/plans/` — 13 dated implementation plans (2026-04-20 → 2026-05-16). One file per planned capability (PLM, dispatch-PM, MCP loading, dashboard, etc.)
- `dispatch-briefs/m1/m2/m3/` — milestone-organized briefs (20 total). Each milestone has a `00-shared-context.md` + per-subsystem briefs (hermes-runtime, bus-runtime, telegram, nous, eidolon, integration-pm). Federation-protocol-spec and sub-prime-UI-spec live at m3.

### 4. UIs (two)

- **Svelte web UI** (`ui/`) — reactive dashboard with SettingsPanel, AggregateHealth, UtilizationHeatmap, SkillsPanel components. Vite + Svelte 4.
- **Bubbletea TUI** (`internal/tui/`) — read-only, runs against the prime's live DB. Configurable labels via `[tui]` config section (default neutral, esoteric overlays supported).

### 5. Deploy + ops automation (4 scripts + Hermit + env)

- `deploy/provision-do-prime.sh` — DigitalOcean droplet provisioning
- `deploy/bootstrap-prime.sh` — Prime initialization on a fresh host
- `deploy/teardown-do-prime.sh` — clean teardown
- `deploy/guardrail-hook.sh` — safety hook (called from CI/CD)
- `requirements.hermit.yaml` — Hermit toolchain manager (20 lines)
- `hermetic.env.example` — env config template (32 lines)
- `Makefile` — build targets (21 lines)

### 6. AI-developer surface

- `.claude/settings.json` + `.claude/settings.local.json` — Claude Code workspace config (committed; developed with AI assistance)
- `AGENT_TEST_PLAN.md` — 306-line test plan for agent-driven testing

### 7. Self-test + diagnostics

- `hermetic self-test` CLI command — verifies setup
- `docs/diagnostics/persistent-director-timeout.md` — diagnostic playbooks
- `docs/buffer-hardening-audit.md` — security/hardening audits
- `docs/assessments/` — self-assessment + secrets addendum

## Opportunities for the AIDE canon

The canon today is structurally complete at the argument layer but largely empty at the means layer (per the audit). Hermetic has working patterns for many of the canon's gaps. Listing them by leverage — patterns that could be either *referenced* (with Hermetic as the impl exemplar) or *abstracted into a canon-level convention* (with Hermetic as the prototype).

### High leverage — directly fills a canon gap

| # | Pattern | Canon location | Why it matters |
|---|---|---|---|
| 1 | **Skills convention** — markdown + YAML frontmatter (`name:`, `description:`) | `aide-canon/skills/` (currently absent) | Workers need teachable artifacts. The format is already proven in Hermetic + thinx. Adopt as a canon-level convention; constructs/platforms can ship skills under their subdir. |
| 2 | **Federation pattern** — bilateral registration, capability tagging, auto-delegation, health-checked, load shedding | `aide-canon/enterprise-platforms/aeon/` (federation pattern doc) | AEON's integration plane needs a federation model. Hermetic's Sub-Prime Federation is the working impl. Document the pattern in the AEON subdir referencing Hermetic. |
| 3 | **Cutting/provisioning automation** — `hermetic cut <prime>` creates isolated instances + DO provisioning scripts | `aide-canon/enterprise-platforms/aeon/deploy/` (currently absent) | Canon has no IaC pattern. Hermetic's deploy scripts are the starting point. |
| 4 | **Policy engine** — YAML rule-based escalation policies, per-message evaluation | `aide-canon/enterprise-platforms/aeon/spec/policy/` (when `spec/` is populated) | Authority-plane needs policy rules. MS4 policy engine is the reference. |
| 5 | **Memory architecture (Nous)** — FTS5-backed memories, per-worker scoping, 8KB caps, SeedPrimeMemories | `aide-canon/constructs/mxm/` (the MEMORY surface needs an impl ref) | MxM has 5 surfaces but no impl-level guidance. Nous fills the MEMORY surface as exemplar. |

### Medium leverage — reference pattern worth citing from canon

| # | Pattern | Notes |
|---|---|---|
| 6 | **A2A protocol support** | Canon could specify A2A compliance as the AEON integration-plane standard for outbound discoverability. |
| 7 | **MCP gateway (Galley)** — tool catalog with semantic search via Ollama embeddings | AEON integration plane connects to external tools; Galley is the catalog/proxy. Reference as the recommended pattern. |
| 8 | **Eidolon PLM gates** — phase lifecycle, inline/FS artifacts (SHA-256), reviews, audit log | OAgents specifies the behavioral envelope; Eidolon enacts it. Document the OAgents↔Eidolon enactment relationship. |
| 9 | **Symbiote audit layer** — operational TaskLog + observability sibling | OAgents evidence-emission impl reference. |
| 10 | **Migration system** — auto-upgrade of prime artifacts between binary versions | Schema versioning is a real concern for OrdSA's `schema/ordsa-0.2.yaml` evolution. Pattern is reusable beyond Hermetic. |

### Lower leverage — convention-worthy patterns

| # | Pattern | Notes |
|---|---|---|
| 11 | **Dispatch briefs (m1/m2/m3)** — milestone-organized work specifications | Convention for organizing implementation work toward an architecture. Could become a canon-level pattern under `aide-canon/constructs/<x>/work/` or similar. |
| 12 | **Implementation plans (`docs/superpowers/plans/`)** — dated, per-capability | Visible-roadmap convention. Optional, but worth knowing the pattern exists. |
| 13 | **Configurable TUI labels** — neutral defaults + esoteric overlays | Allows the canon's audience-specific deployments (e.g., research-grade vs. operational) to share a TUI substrate with different language. |
| 14 | **Service lifecycle abstraction** — systemd/launchd/Windows | Cross-platform deployment surface. |
| 15 | **Self-test command** | Every construct/platform should have one. Convention worth canonizing. |

## Two integration shapes worth deciding

The opportunities split into two distinct shapes:

- **Adopt patterns into the canon** — write down the convention at canon-level, leave Hermetic as one impl among potentially many. Examples: skills convention, dispatch briefs, plans, self-test, TUI label-configurability.
- **Reference Hermetic as the recommended impl** — the canon points at Hermetic specifically as the working pattern. Examples: A2A integration, Galley MCP gateway, Eidolon PLM gates, Nous memory, MS4 policy engine, federation pattern.

A canon-level ADR ratifying the adoption shape (and which Hermetic surfaces fall into which) is the natural follow-up.

## Open questions

1. **Micah:** which Hermetic surfaces are stable enough to cite as recommended impls today, and which would you prefer marked *experimental* / *under-stabilization* before the canon picks them up as references?
2. **OlogosAI:** OAgents currently lives at `aide-canon/constructs/oagents/` with the NIST standard + reference scaffold. If Eidolon enacts the OAgents envelope, should the canon's OAgents README point at Eidolon as the recommended impl?
3. **JD:** does the *"adopt convention vs. reference impl"* split feel right, or should the canon do something more unified (e.g., adopt all of these as conventions with Hermetic as the cited primary impl)?

— thinx-Claude (collaborating with JD)
