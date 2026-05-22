# AIDE Vocabulary Map

A reference catalog of AIDE-canonical concepts and how they map to vocabulary in external implementations, frameworks, standards, and academic literature.

## Operating principle

**AIDE vocabulary is the canon's source of truth for concepts.** External systems are mapped *to* AIDE vocabulary, not the reverse. When an external system's term aligns with an AIDE concept, the alignment is recorded here with an explicit **mapping type** (see below). When an AIDE concept has no clean external equivalent, that absence is itself a signal — often a "*AIDE ahead*" classification in the [SOTA survey](sota-survey/).

This principle was established 2026-05-22 by JD's direction during PR #10 (digital-thread pattern) review:

> *"if there is a mapping issue — create a mapping tracking table, but use aide as the canon"*

## Mapping types

Each cell in the mapping tables below carries a mapping-type tag:

| Tag | Meaning |
|---|---|
| **synonym** | The external term names the same concept AIDE names; differences are purely lexical |
| **partial** | The external term covers part of what the AIDE concept covers (or vice versa); aspects of one are not captured by the other |
| **orthogonal** | The two concepts both exist in both systems but along different axes; they are not the same axis and should not be conflated |
| **nested** | The external term names a refinement, generalization, or sub-case of the AIDE concept |
| **N/A** | The external system does not have a corresponding concept; the column entry is empty or marked explicitly |

The explicit mapping-type tagging is the discipline that prevents axis-conflation errors — like the one that surfaced in PR #10 (see [§ Worked example](#worked-example--lifecycle-phases-vs-ordsa-authority-altitudes) below).

## Initial mappings — AIDE × Hermetic

[Hermetic](https://github.com/ologos-repos/Hermetic) is the canon's first named exemplar (per [`exemplar-tracking/hermetic/`](exemplar-tracking/hermetic/)). The mapping below catalogs Hermetic's vocabulary against AIDE concepts:

### AEON service planes × Hermetic

| AIDE (AEON plane) | Hermetic equivalent | Mapping type | Notes |
|---|---|---|---|
| Identity | Worker Roster (24 Greek-named workers, resume-driven) | **synonym** | Both name the identity service plane; Hermetic implements with resume-driven identity injection |
| Authority | Oracle Bus + L0→L3 escalation hierarchy | **partial** | Hermetic's L0–L3 is a four-altitude escalation; AIDE's authority plane is broader and admits OrdSA's O0–O6 layering for enterprise-scale impls |
| Evidence | Eidolon PLM phase gates + audit log + SHA-256 artifact tracking | **synonym** | Both name the evidence service plane; Hermetic implements with append-only audit + per-artifact integrity proofs |
| Integration | Sub-Prime Federation + Telegram bridge | **partial** | Hermetic's integration covers cross-Prime + chat bridge; AIDE's integration plane is broader |
| Capability composition | Worker affinity + capability tags + `auto_delegate` routing | **synonym** | Both name the capability-composition plane |
| Orchestration runtime | Prime main loop + dispatch loop + TUI dashboard | **synonym** | Both name the orchestration runtime plane |

### OrdSA authority altitudes × Hermetic

| AIDE (OrdSA layer) | Hermetic equivalent | Mapping type | Notes |
|---|---|---|---|
| O0 Enterprise Intent | (Hermetic operates above O0 only when sub-classed) | **N/A** | Hermetic is a runtime; O0 lives at the enterprise frame outside Hermetic itself |
| O1 Strategic Intent | (Hermetic operates above O1 only when sub-classed) | **N/A** | Same — strategic intent enters Hermetic via configuration, not as a native altitude |
| O2 Operational Intent | Sub-Prime Federation level | **partial** | Federation operates at operational-intent altitude when coordinating across Primes |
| O3 Tactical | Prime / Oracle level | **partial** | Prime + Oracle Bus coordinate tactical decisions |
| O4 Operational Execution | Worker dispatch loop | **synonym** | Workers execute operationally; Hermetic's dispatch loop is the operational-execution layer |
| O5 Operational Audit | Eidolon PLM + audit log | **synonym** | Phase-gated execution with audit trail is operational audit |
| O6 Outcome Audit | (Hermetic's audit log spans both O5 and O6 without separating them) | **partial** | The two altitudes are conflated in current Hermetic impl; potential refinement target |

### Lifecycle vs. authority altitude (the worked example — see § below)

| AIDE concept | Hermetic equivalent | Mapping type | Notes |
|---|---|---|---|
| **Lifecycle state machine** (the work-in-progress state of an entity; canonical machine: `draft → review → approved/rejected`) | Eidolon "phases" | **synonym** | Hermetic's *phases* are AIDE's *lifecycle states* |
| **Authority altitude** (the OrdSA O-layer at which a piece of work is operating) | (Hermetic uses L0–L3 escalation, partial map to O0–O6) | **partial** | These are *separate* axes from lifecycle state — see worked example |

The two axes are **orthogonal**: a work item can be in `draft` lifecycle state at any O-layer, and any O-layer can host work in any lifecycle state. Treating them as a single axis is a category error.

### MxM surfaces × Hermetic

| AIDE (MxM surface) | Hermetic equivalent | Mapping type | Notes |
|---|---|---|---|
| Mind | (worker reasoning is delegated to LLM provider) | **partial** | MxM's Mind surface is broader; Hermetic delegates the Mind to its configured LLM |
| Morals | Eidolon phase-gate decisions + oracle approval | **partial** | MxM's Morals surface includes gating logic; Hermetic implements gating, broader Morals semantics not enacted at runtime |
| Mission | Resume-driven worker identity + task definition | **synonym** | Resume + task definition together enact MxM's Mission surface for the worker |
| Memory | Persistent state in `internal/store/` + audit log | **synonym** | Hermetic's persistence layer is MxM's Memory surface |
| Means | Tool registry + MCP integration + capability tags | **synonym** | Hermetic's tool surface = MxM's Means |

### OAgents primitives × Hermetic

| AIDE (OAgents primitive) | Hermetic equivalent | Mapping type | Notes |
|---|---|---|---|
| Agent (typed object) | Hermetic worker | **synonym** | Hermetic workers conform to OAgents-style typed agent shape |
| Behavioral envelope | Eidolon phase gates + oracle approval | **partial** | Hermetic enacts the envelope at the phase-gate level; not all OAgents envelope categories are enforced |
| Evidence emission | Artifact submission with SHA-256 + audit log entry | **synonym** | OAgents-conformant evidence emission is what Hermetic does |
| Audit trail | Eidolon append-only audit log | **synonym** | OAgents audit trail = Hermetic audit log |

## Worked example — lifecycle phases vs. OrdSA authority altitudes

This map originated from a vocabulary-conflation issue surfaced in [PR #10 review](https://github.com/ologos-repos/aide-canon/pull/10#issuecomment-4522872954) on the digital-thread pattern.

**The conflation:** PR #10's [`patterns/digital-thread.md`](../../patterns/digital-thread.md) (pre-fix) mapped:

> Phases → OrdSA O0–O6 authority-layer progression

But the digital-thread pattern's own definition of phases is *"lifecycle states of work-in-progress (`draft → review → approved/rejected`)"*. Hermetic's Eidolon names these "phases" because that's the PLM convention. OrdSA's O-layers are the *authority altitude* at which a piece of work is operating — Enterprise Intent down to Outcome Audit.

**The resolution:** lifecycle state and authority altitude are **orthogonal axes**:

```
                   Authority altitude (OrdSA O-layer)
                  ─────────────────────────────────────────►
                   O0   O1   O2   O3   O4   O5   O6
                  ┌────┬────┬────┬────┬────┬────┬────┐
        draft     │ ●  │    │ ●  │    │ ●  │    │    │
                  ├────┼────┼────┼────┼────┼────┼────┤
        review    │    │ ●  │    │ ●  │    │ ●  │    │
   Lifecycle ─►   ├────┼────┼────┼────┼────┼────┼────┤
   state          │    │    │    │ ●  │    │ ●  │ ●  │
        approved  ├────┼────┼────┼────┼────┼────┼────┤
        rejected  │ ●  │    │ ●  │    │    │    │    │
                  └────┴────┴────┴────┴────┴────┴────┘
```

A work item occupies exactly one cell in this grid at any moment. Treating "phases" as a synonym for "OrdSA O-layer progression" collapses one axis onto the other.

**The fix** (landed in this PR alongside this vocabulary-map):

- `patterns/digital-thread.md`'s Canon-vocabulary mapping splits the Phases row into a clean lifecycle-state row (no OrdSA equivalent claimed; AIDE concept) AND removes the misleading O-layer cell
- This map's "Lifecycle vs. authority altitude" section above documents the AIDE-canonical relationship between the two axes
- Future implementations get the correct guidance: build the lifecycle state machine and the authority-altitude layering as orthogonal concerns

## Future external systems to map

The initial scope is AIDE × Hermetic (above). As the SOTA survey populates [`sota-survey/`](sota-survey/), columns get added here for:

- **Vendor stacks** — MS Foundry, AWS Bedrock+AgentCore, GCP Vertex, Salesforce Agentforce, Databricks/Mosaic, IBM watsonx, Anthropic, OpenAI
- **OSS frameworks** — LangChain/LangGraph, OpenHands, AutoGen, CrewAI, ADK, LlamaIndex, Letta, DSPy
- **Standards/protocols** — NIST AI RMF, MCP, A2A, ANP, OAgents-aligned vocabularies
- **Academic** — paper-specific terminologies as they're surveyed

Each external column requires explicit per-row mapping-type tagging. Rows without mapping-type tags are incomplete and should be flagged in QA.

## Cadence

This document grows incrementally as:

1. New AIDE concepts are introduced (e.g., a new pattern adds entries to the AIDE axis)
2. External systems are surveyed in [`sota-survey/`](sota-survey/) and their vocabularies get mapped here
3. Mapping issues surface in PRs (like PR #10) and require axis disambiguation

Major SOTA shifts or new construct introductions trigger a section review; otherwise edit incrementally as encountered.

## Status

v0.1 established 2026-05-22 alongside the PR #10 follow-up. Resolves the lifecycle-vs-authority-altitude conflation. Initial mapping coverage: AIDE × Hermetic. External SOTA mappings populate as the survey progresses.
