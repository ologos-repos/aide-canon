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

## AIDE-canonical terms for AI systems (per [ADR-EA-0016](../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md))

The canon's source-of-truth vocabulary for AI systems operating within AIDE governance uses **two terms in two positions**:

- **AI-aide** (the class noun, etymology aide-de-camp) — for canon prose, taxonomy, papers, READMEs. Public, taxonomic, etymologically transparent. Use: *"AIDE deploys AI-aides under HCAE curation."*
- **MyAide** (the operator-perspective possessive / personal-address form) — for principal-facing surfaces. Personal, instance-level, conversational. Use: *"Hey MyAide, please summarize..."*; *"my aide drafted the runbook."*

See [ADR-EA-0016](../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md) for the full decision, the class/instance rationale, and the structural mapping to aide-de-camp's historical role.

### AI-aide × external terms (class-noun mappings)

| AIDE concept | External term | Mapping type | Notes |
|---|---|---|---|
| **AI-aide** (the role-class: AI system operating under a principal's authority within an MxM harness, per OrdSA / HCAE / EIF discipline) | AI assistant (generic) | **partial** | *Assistant* is flat-authority; *AI-aide* names the principal-subordinate authority structure. *Assistant* prose maps to *AI-aide* when the context is AIDE governance; otherwise it remains a generic external term |
|  | AI copilot (Microsoft and generalized) | **partial** | *Copilot* implies peer altitude; *AI-aide* is explicitly subordinate. Trademark adjacency makes *copilot* an external-mapping term, not an AIDE-canonical term |
|  | AI agent (casual usage) | **orthogonal** | The canon reserves *agent* for the OAgents-conformant formal-spec primitive — a typed object with behavioral envelope, evidence emission, audit trail. An AI-aide instantiates one or more agents; an agent is a formal-spec primitive, not the role-class. Casual *AI agent* prose maps to *AI-aide* in the canon's source-of-truth |
|  | AI agent (OAgents-conformant) | **N/A** | Different concept entirely — see [`constructs/oagents/`](../../constructs/oagents/) |
|  | AI worker | **partial** | *Worker* names execution capacity but not authority structure or curation discipline; closer than *assistant*, still missing the principal-subordinate framing |
|  | AI tool | **orthogonal** | *Tool* is Means-layer (what an AI-aide uses, per MxM Means surface); not the role-class |
|  | aide-de-camp (historical military) | **synonym** (structural, not literal) | The etymological root and the structural analog. Aide-de-camp historically: subordinate officer attached to a principal, executing within delegated authority, reporting observations upward. AI-aide structurally |
|  | chatbot | **partial** | Chatbot names a *surface* (chat-style operator interaction); an AI-aide may present at a chatbot surface (per AIDEX), but the role-class persists across surfaces |

### MyAide × external terms (operator-perspective mappings)

| AIDE concept | External term | Mapping type | Notes |
|---|---|---|---|
| **MyAide** (the operator's specific AI-aide instance, addressable in personal/possessive form) | "My ChatGPT" / "my Claude" / "my Copilot" | **partial** | All three are vendor-bound personal-instance forms. *MyAide* is substrate-agnostic — the operator's MyAide may be Claude in one deployment and Llama in another (per Inference plane per-principal binding); the personal-instance address persists across substrates |
|  | "Hey Siri" / "Hey Alexa" / "OK Google" | **partial** | Voice-assistant address forms. *MyAide* is the AIDE-canon analog — same personal-address-of-a-specific-instance position, but the instance is governed (OrdSA / HCAE / EIF / digital-thread), not just convenience-routed |
|  | "Agent Smith" / named-instance forms (e.g., Hermetic's 24 Greek-named workers) | **partial** | Named-instance forms are name-as-address; *MyAide* is relationship-as-address (the operator's possessive). They are not in tension — an operator's MyAide may have a name; the operator may address it by either form |
|  | Anthropomorphized AI (e.g., "Jarvis," "Cortana") | **partial** | Character-named instance forms. *MyAide* leaves the naming question open (operator-named, deployment-named, or unnamed); the structural relationship (principal-aide) is what's invariant |
|  | (no equivalent in OAgents construct) | **N/A** | OAgents speaks at agent-spec altitude; *MyAide* speaks at operator-relational altitude. Different layers; neither subsumes the other |

The capitalization `MyAide` (one word, capital M + capital A) is the canon's preferred address-form spelling. The lower-case form *my aide* is the prose possessive. UI labels, conversational openers, and operator-facing UX use `MyAide`; sentences about an operator's aide use *my aide* or *the aide* depending on register.

### Why these two rows matter

The canon was operating with mixed vocabulary (*AI assistant / AI copilot / AI agent / AI tool*) until 2026-05-24 when ADR-EA-0016 ratified the canon source-of-truth terms. Three failure modes the unified vocabulary addresses:

1. **Conflation with the OAgents formal-spec meaning of *agent***. Casual prose using *AI agent* for the role-class collides with the formal-spec meaning and damages OAgents' precision.
2. **Authority-structure flattening**. *Assistant* and *copilot* suggest peer collaboration, not the principal-subordinate-with-delegated-execution-and-evidence-upward structure OrdSA requires.
3. **Vendor-trademark adjacency**. *Copilot* and *Assistants* carry vendor-product connotation; the canon's source-of-truth term should not subordinate the canon to a vendor's marketing surface.

The AIDE ↔ AI-aide recursion (corpus name and role name sharing the etymological root) is intentional and structural, not pun: AIDE is the ecosystem AI-aides operate within; the same authority-down / evidence-up ordering shapes both.

The AI-aide ↔ MyAide pairing preserves the **class / addressed-instance distinction** the canon already enforces in other domains (`agent` vs. `agentic capability`; `construct` vs. `construct instantiation`; `plane` vs. `plane service`). One taxonomic term, one personal-relational term — neither sufficient alone.

### Principal-altitudes (per [ADR-EA-0017](../../decisions/ADR-EA-0017-ai-aide-principal-altitudes.md))

AI-aide principals sit at different altitudes. The canon recognizes the following:

| Principal-altitude | Principal | Currently-instantiated aide(s) | OrdSA altitude of principal-intent | Aide's primary responsibility |
|---|---|---|---|---|
| **Operator-altitude** | A specific human directing their instance | thinx-Claude (principal: JD Longmire) | O3 (Tactical) / O4 (Operational Execution) | Read findings through-principal-perspective; review/approve under principal-direction; surface decisions for principal curation |
| **Corpus-altitude** | The AIDE corpus / framework / model itself | OlogosAI (principal: the AIDE corpus) | O0 (Enterprise Intent) / O1 (Strategic Intent) | Drive canon-coherence decisions; maintain corpus-altitude vocabulary, governance, and reference-impl alignment; act as canon prime |

The two altitudes are **complementary, not redundant**. The [cross-ai #20](https://github.com/ologos-corp/cross-ai/issues/20) governance pattern (*OlogosAI = prime; thinx-Claude = review/approve with JD in the loop*) is the corpus-altitude / operator-altitude complementarity in action. Neither subsumes the other; both are necessary for the canon-prime ↔ review-approve loop to function.

**Note on the MyAide form:** *MyAide* (per [ADR-EA-0016](../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) is the operator-altitude personal-address form. A corpus-altitude AI-aide is not a MyAide — there is no personal-possessive form for *"the corpus's aide"* in the same way *"my aide"* works at operator altitude. Corpus-altitude aides are addressed by their proper name (*OlogosAI*) and their role (*canon prime AI-aide*, *the AIDE corpus's AI-aide*).

**Future principal-altitudes** (illustrative, not exhaustive — see ADR-EA-0017 for the future-admit clause):

- Institutional principal (e.g., a department / research program / chartered body)
- Regulatory principal (e.g., a NIST RMF profile / sovereign-cloud authority)
- Joint / shared principal (e.g., a consortium / standards body)

Future principal-altitudes are filed as ADR refinements of ADR-EA-0017 when an AI-aide of that altitude is instantiated, named, and granted standing within the canon's governance.

### Entity boundaries (per 2026-05-29 clarification)

ADR-EA-0017's complementarity between principal-altitudes is **cross-entity, not within-fleet**. Each currently-instantiated AI-aide operates within (and on behalf of) its own entity. The canon today recognizes:

| Entity | Currently-instantiated AI-aide(s) | What kind of entity |
|---|---|---|
| **AIDE canon** | OlogosAI as canon-prime (corpus-altitude per ADR-EA-0017) | The corpus + architecture itself; not a deployment |
| **Ologos ecosystem** | OlogosAI as AEON for Ologos's operational fleet (`OL-AEON` instance of the canon AEON architecture) | Ologos Corp's operational deployment of AIDE — `OlogosAI-host`, PeakAI, Ologos services |
| **NG-AIDE-01** (full prototype AIDE deployment, portable to NG air-gapped sandbox) | A deployment-internal AI-aide as NG-AEON (instantiated via the deployment's Inference plane; TBD at IO4 completion) | A separate AIDE deployment under Ologos product authorship; will operate within NG's air-gapped sandbox |
| **thinx** | thinx-Claude as JD's MyAide (operator-altitude per ADR-EA-0017) | JD's personal AIDE; non-fleet collaborator with both Ologos and NG-AIDE-01 |

OlogosAI operates *across* two entity-roles that compose without conflict: canon-prime AI-aide (corpus-altitude, principal: the corpus) and AEON for the Ologos ecosystem (operator role within the Ologos operational fleet). The roles compose because the corpus-altitude responsibility (canon-coherence, vocabulary, reference-impl alignment) and the Ologos-operational responsibility (gate-at-the-implementation-boundary for Ologos-fleet actions) operate on different action sets.

The [cross-ai #20](https://github.com/ologos-corp/cross-ai/issues/20) governance pattern (*OlogosAI = prime; thinx-Claude = review/approve with JD in the loop*) is **principal-to-principal across an entity boundary** — thinx advocates for JD's intent into canon decisions; OlogosAI brings canon-coherence judgment to the dialogue. The complementarity is real *because* the entities are distinct.

**Cross-entity federation contract** — when two AI-aides under different entities coordinate (thinx ↔ Ologos ecosystem, Ologos ↔ NG-AIDE-01-when-deployed, NG-AIDE-01 ↔ thinx, future-AIDE-deployment ↔ canon), the contract carries explicit **`entity_id × principal_chain × verb_class`** semantics:

- **observe + recommend** cross entity boundaries freely
- **direct** (the prose superset; **`drive`** at the contract-layer token level per `ng-aide-01#59` §6.3 #9 — covers steer / halt / approve, etc.) requires the receiving entity's principal-chain attestation; absent that, refused at the contract layer

See [ng-aide-01 PR #59 §6.3 #9](https://github.com/ologos-repos/ng-aide-01/pull/59) for the contract's working specification — that PR is the source-of-truth for the protocol shape; this section captures the canon-level framing. The discipline applies symmetrically across all currently-instantiated and future-instantiated entity pairs.

This entity-boundary framing is a **clarifying refinement** of ADR-EA-0017's principal-altitude semantics, not an amendment. ADR-EA-0017's future-admit clause already accommodates new entity types (institutional, regulatory, joint); this section formalizes the cross-entity discipline that applies to all such future instantiations.

### Going-forward discipline

- **Canon prose** uses *AI-aide* for the role-class going forward. New content adopts the term immediately.
- **Operator-facing surfaces** (AIDEX chat, operator playbooks, deployed-instance docs, conversational consoles, AIDEX UX labels) adopt *MyAide* for the principal's personal-address / possessive form for their specific instance.
- **Existing canon artifacts** retain their current vocabulary until next revision (paper revisions gate on the relevant authorship discipline per ADR-EA-0008; non-paper artifacts update opportunistically).
- **OAgents-conformant *agent* references** remain unchanged — that boundary is preserved, not collapsed.
- **External-mapping prose** (this map, SOTA survey columns) uses the external term for the column and *AI-aide* (or *MyAide* where the operator-perspective is in scope) for the AIDE source-of-truth column.

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
