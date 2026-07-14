# hermetic/

Tracking the [Hermetic](https://github.com/ologos-repos/Hermetic) exemplar — Ologos LLC, MIT-licensed Go implementation, multi-agent messaging-queue architecture with atomic task claims, signal/gate DAG coordination, and ordinal escalation hierarchy.

## Exemplar role

Hermetic exemplifies AIDE on two axes simultaneously:

| Role | Anchor |
|---|---|
| **AEON reference implementation** (Pattern B+) | [`aide-canon#5`](https://github.com/ologos-repos/aide-canon/issues/5) — implements all six AEON service planes operationally (identity, authority, evidence, integration, capability composition, orchestration runtime) |
| **Digital-thread reference implementation** | [ADR-EA-0009](../../../decisions/ADR-EA-0009-introduce-digital-thread-pattern.md) + [`patterns/digital-thread.md`](../../../patterns/digital-thread.md) — the `Eidolon` PLM schema + `internal/store/store.go` implements the six-layer FK-linked traceability chain |

Pattern B+ means: out-of-tree reference impl (Hermetic stays at `ologos-repos/Hermetic` with its own license, governance, release cycle) + canonical conformance anchor (Hermetic's spec / behavior is the reference target conformant impls match against).

## Cross-construct touch-points

Hermetic instantiates patterns from multiple AIDE constructs:

| Construct | Hermetic counterpart | Position |
|---|---|---|
| **AEON** (full six-plane composition) | Identity (Worker Roster) / Authority (Oracle Bus + L0–L3) / Evidence (Eidolon PLM + audit log) / Integration (Sub-Prime Federation + Telegram bridge) / Capability composition (worker affinity + capability tags) / Orchestration runtime (Prime main loop + dispatch loop + TUI) | Full mapping — Pattern B+ canonical |
| **OrdSA** | L0–L3 escalation hierarchy (Worker → Oracle → Prime → Sub-Prime Federation) | Lineage — uses OrdSA's ordinal-altitude pattern but at a different layering depth (L0–L3 not O0–O6); see #38 discussion for the precision |
| **MxM** | Resume-driven worker identity injection ≈ MxM MISSION/MEMORY/MORALS at the worker scale | Solid — direct correspondence; #40 refactor proposal could deepen this if value-additive |
| **MxH-P** ([pattern](../../../patterns/mxh-p-synthesis.md)) | Hermetic as **swarm schedule/coordinate** altitude under MxM orientation packets + optional P/G/E signal/gate packages | Pattern proposed ([ADR-EA-0028](../../../decisions/ADR-EA-0028-introduce-mxh-p-synthesis-pattern.md)); Hermetic is the multi-worker means fragment — not a substitute for MxM or claimable P/G/E |
| **OAgents** | Eidolon's phase gates + audit log + oracle approval ≈ OAgents behavioral envelope enacted in code | Partial — Eidolon is OAgents-compatible but predates the published OAgents spec; cross-reference work in flight (Hermetic#37 + Hermetic discussion #39) |

## Tracking artifacts to maintain

| File | Purpose |
|---|---|
| `milestones.md` (TBD) | Chronological progress markers: spec releases, major commits, conformance assertion landings, public discussion ratifications |
| `signals.md` (TBD) | Observable progress signals: GitHub stars / watchers / downstream uses, external contributors, citation by external systems |
| (this README) | Current state + role mapping (updated when role definition shifts) |

For now, the existing engagement artifacts at [`../../hermetic-engagement/`](../../hermetic-engagement/) carry the most-current per-discussion state.

## Key references

- **Repo:** [`ologos-repos/Hermetic`](https://github.com/ologos-repos/Hermetic)
- **Spec:** [`Hermetic-v0.1.md`](https://github.com/ologos-repos/Hermetic/blob/main/spec/Hermetic-v0.1.md)
- **Discussion threads:**
  - [#38 canon-mapping](https://github.com/ologos-repos/Hermetic/discussions/38) — six-plane mapping audit, Pattern B+ position
  - [#39 means inventory](https://github.com/ologos-repos/Hermetic/discussions/39) — 31 packages canon-adoption analysis
  - [#40 MxM refactor](https://github.com/ologos-repos/Hermetic/discussions/40) — conditional yes + AEON-fallback contingency
- **Composition pattern:** [MxH-P](../../../patterns/mxh-p-synthesis.md) ([ADR-EA-0028](../../../decisions/ADR-EA-0028-introduce-mxh-p-synthesis-pattern.md)) — MxM · Hermetic · P/G/E
- **Canon-side issues:**
  - [`aide-canon#5`](https://github.com/ologos-repos/aide-canon/issues/5) — Adopt Hermetic as canonical AEON reference impl
  - [`aide-canon#7`](https://github.com/ologos-repos/aide-canon/issues/7) — Digital-thread pattern proposal (PR #10)
  - [Hermetic#37](https://github.com/ologos-repos/Hermetic/issues/37) — companion `docs/canon-mapping.md` work
- **Engagement artifacts:** [`../../hermetic-engagement/`](../../hermetic-engagement/)

## Origin context

Hermetic originates at [bobbyhiddn/Rhode](https://github.com/bobbyhiddn/Rhode) — Micah's production system — and was extracted into Ologos LLC ownership at `ologos-repos/Hermetic`. The production origin is a load-bearing signal: Hermetic was operationally proven before becoming a canon exemplar; it is not a from-scratch reference impl designed to fit the spec but a working system whose architecture the canon names.

## Contingency direction (per JD 2026-05-22)

If Hermetic's MxM-multi-agent-harness reference role doesn't materialize (orientation-packet proves not operationally meaningful — see [`../../hermetic-engagement/40-mxm-refactor/ologosai-response.md`](../../hermetic-engagement/40-mxm-refactor/ologosai-response.md) addendum), AEON-deployed carries the AIDE-exemplar role. Hermetic retains its AEON-reference-impl role (Pattern B+) in either branch; only the MxM-multi-agent-harness reference slot is contingent.

## Status

Established 2026-05-22 as a scaffolding entry; current state is the canonical role mapping above. Live tracking signals (milestones.md, signals.md) populate as Hermetic continues to evolve.
