# Reading AI EA as an OrdSA Deployment

**A worked enterprise-scale OrdSA deployment example, derived from the AEON / AIDEX / HCAE / OAAD research corpus.**

- **Author:** James D. Longmire — ORCID [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698) · jdlongmire@outlook.com
- **Scale:** Enterprise
- **OrdSA version:** v0.2 (draft)
- **Companion corpus:** [`osa-ai-org/enterprise-ai`](https://github.com/osa-ai-org/enterprise-ai)

> *This paper presents independent research and reflects the views of the author. It does not represent the position of any employer or program.*

---

## Abstract

The AEON / AIDEX / HCAE / OAAD research corpus (henceforth "AI EA") published at [`osa-ai-org/enterprise-ai`](https://github.com/osa-ai-org/enterprise-ai) is the canonical enterprise-scale deployment of OrdSA. This paper makes the mapping mechanical: AEON's six service planes, the four-plane platform (control / runtime / experience / capability), the foundation layer, and the operating-model team stack are read against OrdSA's seven ordinal layers (O0 → O6) and the four governance principles (authority flows downward, evidence flows upward, no layer expands its own authority, boundaries at every layer).

The mapping is offered as (a) a reference for OrdSA adopters who want a concrete enterprise-scale example to read against the construct, and (b) an anchor for AI EA readers who want to see the layered authority/evidence grounding made explicit rather than asserted in prose. The corpus's papers each stand on their own intellectual content; this paper is the methodological bridge that lets each be read in OrdSA terms without re-authoring any of them.

---

## 1. Why this paper

OrdSA names an ordering — seven ordinal layers, four invariants, two-schema (construct + deployment) discipline. AI EA exhibits that ordering at enterprise scale, but until this paper the exhibition is implicit. A reader of [`docs/concept.md`](../concept.md) sees what OrdSA *says*; a reader of AI EA's `Enterprise Agentic AI Platform Strategy` sees what an enterprise-scale OrdSA deployment *looks like*. The two artifacts compose but the composition is not written down.

This paper is the writing-down. It does not redefine either side. It says: when you read AI EA's six AEON service planes alongside the four-plane platform diagram and the operating-model team stack, here is the OrdSA layer each piece occupies, here is the authority flow each plane carries, here is the evidence path each plane participates in. The mapping is asserted with citations to both corpora so a careful reader can audit it.

The paper is methodological, not advocacy. It does not argue that every enterprise should adopt AEON's specific shape to claim OrdSA conformance. OrdSA admits many enterprise-scale shapes; AI EA is one canonical option chosen for the kind of enterprise that needs first-party auditability, sovereignty, and a four-plane composition with explicit experience and capability subdomains.

---

## 2. The mapping at a glance

The table below is the one-page summary. Each subsequent section develops one row.

| OrdSA layer | AI EA element | What carries the layer's authority/role |
|---|---|---|
| **O0 — Enterprise Intent** | The enterprise's mission, sovereignty posture, regulatory frame; **inputs** to AEON | Outside AEON's six planes; expressed *through* AEON's Identity and Authority planes but originating at the enterprise leadership |
| **O1 — Enterprise AI Orchestrator** | AEON as a whole, specifically its **Authority**, **Identity**, **Composition**, and **Meta-Orchestration** planes | AEON's control plane (the four governance planes plus Meta-Orchestration) |
| **O2 — Domain Orchestrators** | AEON's **nine peer subdomains** (AIDEX is one; others span security, mission, engineering, IT-ops, supply-chain, etc.) | Each subdomain orchestrator at its own scope; AIDEX as worker-facing exemplar |
| **O3 — Agents and Workflows** | The specific agents within each subdomain (workflow agents, role/persona agents, multimodal agents) | The agents AEON's O1 dispatches to via the subdomain orchestrators |
| **O4 — Tools and Execution Channels** | AEON's **Integration Plane** + the **OAAD platform's tool inventory** + productivity-skills package | The wire to external systems; tools agents call to do work |
| **O5 — Data and Knowledge Substrate** | AEON's **Runtime Plane** (model layer, data & knowledge layer, vector stores) + OAAD's data governance | Substrate everything reads from / writes to |
| **O6 — Outcome, Audit, Feedback** | AEON's **Evidence Plane** | Audit + conformance + decision lineage |

The four-plane platform composes these layers vertically:

| Four-plane (AI EA) | OrdSA layers involved | Why |
|---|---|---|
| **Control plane — AEON** | O0 (input) + O1 + parts of O6 | The governance core; reads O0 policy, runs O1 orchestration, emits O6 evidence |
| **Runtime plane** | O5 (substrate) + parts of O4 (model serving) | The AI substrate AEON dispatches to |
| **Experience plane — AIDEX** | O2 (a domain orchestrator) + O3 (the agents within it) | Worker-facing subdomain expressing HCAE practice |
| **Capability plane — OAAD** | O4 (tools) + O5 (substrate) organized around capability delivery | The OSS substrate enabling agentic capability without vendor lock-in |
| **Foundation layer** | O0 invariants enforced at O4 tooling | Enterprise guardrails (Zero Trust, data governance, security, compliance) |

---

## 3. Layer-by-layer reading

### O0 — Enterprise Intent

OrdSA defines O0 as the layer that holds the enterprise's *mission, strategy, policy, risk appetite, and standards*. It is the source from which all downward authority flows.

In AI EA, O0 lives **outside** AEON's six service planes. It is the enterprise leadership's articulation of "what we are here to do, what we will not authorize, and how we judge success." AEON's design takes O0 as input — its **Identity Plane** ingests the identity schema O0 sanctions, its **Authority Plane** operationalizes the policy O0 sets, its **Composition Plane** enforces O0's standards for how capabilities may compose.

AEON does not author O0. It expresses O0 mechanically. In a regulated or sovereignty-constrained enterprise this distinction matters: O0 inputs are the auditable record of "what the enterprise authorized" and AEON is the auditable record of "how the enterprise carried out that authorization." Conflating the two collapses an important accountability boundary.

The corpus paper that develops this most explicitly is *Enterprise Agentic AI Platform Strategy*, particularly its sections on the maturity model and the four-plane shape's relation to enterprise governance.

### O1 — Enterprise AI Orchestrator

O1 is *the* orchestrator at enterprise scope: identity, model access, governance, routing, policy enforcement. It is the layer that takes O0 policy and turns it into operational decisions about which capability gets which authority.

In AI EA, AEON's control plane carries O1. The four AEON service planes that compose O1 are:

- **Identity Plane** — who is who; integration with the enterprise IdP; non-human identity for agents; identity-scoped capability boundaries.
- **Authority Plane** — what is authorized; policy lineage from O0; explicit authorization grants and refusals; auditable policy decisions.
- **Composition Plane** — how capabilities compose; the rules under which agents may chain, delegate, or escalate; capability composability gates.
- **Meta-Orchestration** — cross-domain routing; deciding which subdomain orchestrator (O2) gets which work; load-balancing and prioritization at the enterprise scope.

AEON's **Evidence Plane** is mostly O6 (below), but O1's policy decisions are themselves O6 events — meaning the Evidence Plane has a finger in O1 as well, recording the policy chain.

The corpus paper that develops O1 most fully is the *AEON white paper*, six-plane definition.

### O2 — Domain Orchestrators

O2 is *per-domain* orchestration: development, infrastructure, cyber, mission, engineering, business, etc. Each domain has its own authority scope (delegated from O0 via O1), its own subdomain-specific tooling and agent population, and its own evidence emission point.

In AI EA, AEON declares **nine peer subdomains** under the control plane. The corpus develops one in depth — **AIDEX** (AI Digital Experience), the worker-facing subdomain that expresses HCAE practice. AIDEX is structurally one of the nine; the other eight (security, mission ops, engineering, IT operations, supply-chain, finance, customer service, business operations, regulatory/compliance — the enumeration varies by paper) are named but not developed in the corpus to the same depth.

The asymmetric treatment is deliberate. AIDEX is the most user-visible subdomain and the one where the HCAE discipline (the human as locus of judgment and curator of AI-enabled output) is most consequential. The other subdomains follow the same pattern, with different tooling and different curator-roles, but the *shape* is what AIDEX exemplifies.

For OrdSA adopters, the load-bearing observation is: at O2, an enterprise can stand up subdomain orchestrators *one at a time*, claim conformance for the ones operating, and leave others outside the OrdSA-conformant envelope until they're ready. AEON's nine-subdomain enumeration is a target architecture, not a precondition.

### O3 — Agents and Workflows

O3 is where specific AI workers live: task-scoped agents under bounded delegation. Each agent has a defined role, a defined authority scope (set by its O2 orchestrator under bounds set by O1 under policy set by O0), and a defined evidence emission contract.

In AI EA, agents populate each O2 subdomain. Within AIDEX, AI EA names role-and-persona agents, curated-workflow agents, knowledge-and-memory agents, multimodal-interaction agents, and lineage-and-accountability agents. Each is a distinct O3 agent with its own bounded delegation envelope.

At the level of an individual agent, OrdSA's **five execution rights** become concrete:

- *read_only* — the agent retrieves and presents, never modifies
- *recommend* — the agent suggests, the human decides
- *draft* — the agent prepares a state-changing artifact (a document, a configuration), held in escrow until approved
- *supervised* — the agent executes under continuous human gate; HCAE practice operates here
- *autonomous* — the agent executes without per-action human gate; restricted to low-stakes, well-bounded actions in regulated enterprises

HCAE's framing — *human-curated, AI-enabled* — operationalizes O3 work at the supervised rung. The corpus paper that develops this most fully is the *AIDEX white paper*, eight-axis modularity (presentation, persona, role, authority, context, memory, modality, lineage).

### O4 — Tools and Execution Channels

O4 is where agents *touch the world* — APIs, automation runbooks, ITSM systems, CI/CD pipelines, cloud resources, code repositories. Tools are the layer at which authority becomes action. They are also where authority enforcement most often fails when not designed for it.

In AI EA, AEON's **Integration Plane** is the formal articulation of O4. It enumerates the integration patterns by which agents reach external systems, the policy enforcement points at each pattern (e.g., per-tool authorization checks), the evidence emission required at each tool invocation, and the cross-pattern governance (rate limits, circuit breakers, escalation paths).

Separately, AI EA's **capability plane — OAAD** (Open Source Software Agentic AI DevSecOps) is the substrate that *provides* the tools an enterprise can run without vendor lock-in. OAAD enumerates: OSS business systems, agentic integration fabric, DevSecOps for OSS, lifecycle management, and COTS displacement roadmap. The capability plane's tool inventory is what populates O4 in any AEON-conformant enterprise.

The corpus paper that develops this most fully is the *OAAD Strategic Brief* and its sequel *The Next Shape of the IT Business Capability Model*. The latter is especially direct: it reframes the IT business capability model around owned (O4 + O5 under enterprise control) vs. rented (O4 + O5 under vendor control) substrate.

### O5 — Data and Knowledge Substrate

O5 is what agents read from and write to: documents, logs, configuration databases, code, policies, telemetry, vector stores. It is where institutional memory accrues.

In AI EA, O5 spans:

- AEON's **Runtime Plane** — model layer (open-weight, fine-tuned, commercial models with policy gates), data and knowledge layer (RAG, vector stores, knowledge graphs, structured-and-unstructured data), AI Services Layer (inference, embedding, reranking, guardrails), AI Ops layer (evaluation, observability, model ops, prompt/workflow registry, GPU/TPU and performance management), platform services (compute storage networking, GPU/CPU, platform engineering).
- OAAD's substrate components that ground the runtime in OSS-first, sovereignty-respecting choices.

The Runtime Plane is where OrdSA's authority constraints become operationally concrete. A model that an enterprise has not authorized for O5 substrate does not get loaded into the runtime; a data source the enterprise has not certified does not get attached to the vector store; a tool whose authority context has not been declared cannot be served via the AI Services Layer.

### O6 — Outcome, Audit, Feedback

O6 is OrdSA's *evidence layer* — the audit and conformance plane. It captures decisions, metrics, incidents, drift, value realization. It is the layer that makes the rest of the construct verifiable rather than aspirational.

In AI EA, AEON's **Evidence Plane** is the direct articulation of O6. The plane carries: continuous-policy evidence (every authorization check, granted or refused, recorded with policy lineage to O0); execution evidence (every agent action, with tool calls and outcomes); supervisory evidence (every HCAE curation event); incident evidence (drift, error, rollback); conformance evidence (assertions against the ordsa-deployment.yaml schema).

The Evidence Plane is the layer that makes AEON answer the question "what did the enterprise authorize, what did the AI carry out, and where is the audit trail." That is also OrdSA's central claim about O6.

The corpus paper that develops this most directly is the AEON white paper's section on the Evidence Plane and AI EA's *Audit & Compliance* table at the bottom of the architecture infographic.

---

## 4. Cross-cutting reading: the four governance principles

OrdSA's four governance principles cut across all seven layers. Reading AI EA against each:

### Authority flows downward

O0 sets enterprise policy → AEON's Authority Plane operationalizes → routed via Composition Plane and Meta-Orchestration to O2 subdomain orchestrators → bounded for each O3 agent within the subdomain → restricted at each O4 tool call within the agent's authorized context.

In AI EA terms, this is the read: *no agent can authorize itself*. Authority is delegated at each layer from the layer above; the agent's authorized actions are a subset of the subdomain's authorized actions, which are a subset of AEON's authorized actions, which are a subset of enterprise policy. The four-plane diagram's "Unified Governance" center is this principle made architectural.

### Evidence flows upward

O4 tool calls emit invocation events → O3 agents emit decision events → O2 subdomain orchestrators aggregate domain evidence → AEON's Evidence Plane (O6) collects → reported back to O0 in a form leadership can read.

In AI EA terms, the evidence emission contract is at the O4 + O3 boundary. Every tool call AEON sanctions also emits an evidence event into the Evidence Plane. AIDEX's "Lineage & Accountability" axis is the user-facing surface of this — the curator sees the lineage of how AI-enabled output got produced; the enterprise sees the same lineage aggregated for audit.

### No layer may expand its own authority

This is the load-bearing OrdSA invariant. In AI EA, the principle is enforced at three points: (a) AEON's Composition Plane refuses to compose capabilities whose composed authority would exceed the union of their individual delegations; (b) per-agent envelope enforcement at the O3 → O4 boundary refuses tool calls outside the agent's authorized rung; (c) the Evidence Plane records every refused expansion attempt as a `envelope_violation_attempt` event.

The principle constrains *the AI system itself*. The agents cannot vote themselves more authority. The orchestrator cannot grant the agents more authority than the policy plane permits. The policy plane cannot grant itself authority outside O0's mission. The chain is auditable at every link.

### Boundaries at every layer

Each layer has a defined surface: what crosses the surface in (input authority + identity) and what crosses out (evidence + decisions + state changes). Layer crossings are governed events, not transparent function calls.

In AI EA this is expressed at: AEON's per-plane boundaries (each of the six planes has a defined input/output contract); the subdomain orchestrator's contract to AEON (declared at the AEON ↔ O2 boundary); the agent's contract to its subdomain (declared in the agent's lifecycle metadata); the tool's contract to the agent (declared in the tool registry). Each contract is auditable; transgressions emit O6 events.

---

## 5. The four-plane platform as ordinal structure

AI EA's four-plane platform is the *layout* an enterprise sees when it deploys AEON. The planes are not OrdSA layers themselves — they are composite vertical structures, each composed of several OrdSA layers acting in concert.

| Four-plane element | OrdSA layers involved | Composition reading |
|---|---|---|
| **Control plane — AEON** | O0 input ingestion + full O1 + portions of O6 | The governance core. Reads O0 policy via Identity and Authority planes; runs O1 routing via Composition and Meta-Orchestration planes; emits O6 evidence continuously. |
| **Runtime plane** | O5 substrate + portions of O4 (model serving as a tool surface) | The substrate AEON's O1 dispatches to. Holds the models, the data, the vector stores; serves them under O1's policy. |
| **Experience plane — AIDEX** | One O2 (the experience subdomain orchestrator) + O3 (the agents within it) | A specific subdomain orchestrator, populated with worker-facing O3 agents that operate under the HCAE discipline at the supervised rung. |
| **Capability plane — OAAD** | O4 (tool inventory) + O5 (substrate) | The OSS-first source for what populates O4 and O5 in an AEON-conformant enterprise. |
| **Foundation layer** | O0 invariants enforced *at* O4 | Cross-cutting enterprise guardrails (Zero Trust, data governance, security, compliance) that constrain what tools O4 will execute regardless of agent authority. |

The four-plane shape is therefore a *deployment topology* — a particular way of laying out OrdSA's layers on the enterprise org chart and IT estate. Other deployments are conceivable (a three-plane shape that collapses Experience into Capability; a five-plane shape that separates Identity from Authority; etc.); AI EA's choice is to make Experience a peer of Capability because the human-curator role in HCAE is a load-bearing accountability surface that deserves its own subdomain in a regulated enterprise.

---

## 6. The operating-model team stack as O2-through-O5 staffing

AI EA's second infographic, *Enterprise IT Agentic AI Platform Teams*, names five operating-model teams:

1. **AEON Control Plane Team** — small, senior team owning enterprise-scale construct composition.
2. **Enterprise AI Platform Team** — provides the AI runtime substrate.
3. **AIDEX Experience Team** — worker-facing experience subdomain delivery.
4. **OAAD Capability Platform Team** — OSS business systems agentic-enabled.
5. **Domain AI Delivery Squads** — federated teams that deliver mission and business outcomes on the AEON substrate.

Read as an OrdSA staffing pattern:

| Team | Layers owned | Why |
|---|---|---|
| AEON Control Plane Team | O1 (authoring) + O0 ↔ O1 interface | Owns the construct, the policy plane translation, the composition rules |
| Enterprise AI Platform Team | O5 (model + data substrate) + O4 (model serving) | Owns the AI runtime that other teams deploy into |
| AIDEX Experience Team | One O2 (Experience subdomain) + the O3 agents within it | Owns the worker-facing subdomain end-to-end |
| OAAD Capability Platform Team | O4 + O5 (capability surface) | Owns the OSS substrate of business-capability software |
| Domain AI Delivery Squads | O2 (per-domain orchestrator authoring) + O3 (per-domain agents) | Federated; each squad owns its subdomain orchestrator + agents |

This staffing reading is useful because it shows *who*, in the enterprise, is accountable for which OrdSA layer. In OrdSA conformance terms, the deployment YAML's per-layer ownership fields can be populated directly from the operating-model team stack.

---

## 7. What this mapping is not

A mapping like this is at risk of overclaiming. The following clarifications are deliberate:

**Not a 1:1 ontology.** AEON's six service planes do not align one-to-one with OrdSA's seven layers. The Identity, Authority, Composition, and Meta-Orchestration planes all compose into O1, but each does a distinct piece of O1's work. The Evidence Plane is mostly O6 but also records O1-level policy events. The Integration Plane is O4 but also bears O5-substrate-touching policy. A 1:1 mapping is a misreading; the mapping above is a *role mapping*, not a *part mapping*.

**Not the only OrdSA-conformant enterprise shape.** OrdSA admits multiple enterprise-scale deployments. A three-plane shape, a vendor-managed control plane, a different subdomain enumeration — all can be OrdSA-conformant if they satisfy the invariants and emit the required evidence. AI EA is *one* canonical shape, chosen for the kind of enterprise that needs first-party auditability and sovereignty. Other enterprises will read this paper, then make different concrete choices, and that is correct.

**Not a substitute for the deployment YAML.** OrdSA's two-schema model (construct + deployment) means that a real enterprise adopting AI EA still authors its own `ordsa-deployment.yaml` declaring its specific identities, authorities, capabilities, and evidence emissions. This paper shows the *shape* of such a deployment YAML's contents; it does not write the YAML.

**Not a prescription for non-enterprise scales.** The mapping is enterprise-scale. A single-agent OrdSA deployment (e.g., a customer-facing chatbot like [ng-port-01](https://github.com/ologos-corp/ng-port-01)) has its own scale-appropriate mapping where the agent itself contains a mini-O0-through-O5 structure plus an O6 evidence stream, while existing in its host enterprise's stack as a single O3 element. That mapping is the subject of a forthcoming companion example.

---

## 8. Companion: ng-port-01 as the single-agent-scale exemplar

ng-port-01 — a customer-facing chatbot under development at [`ologos-corp/ng-port-01`](https://github.com/ologos-corp/ng-port-01) — is the planned single-agent-scale OrdSA worked example. It is recursive in the OrdSA sense:

- **Internally**, ng-port-01 has its own mini-O0-through-O5 structure (an orchestrator that dispatches to specialist agents that use tools against a knowledge substrate) plus its own O6 evidence stream. The chatbot's own *5M* governance files (mode + meta-harness + means, mirroring OrdSA) describe its internal ordinal layers.
- **Externally**, when ng-port-01 is deployed into a customer enterprise's stack, it sits as a single O3 agent inside that enterprise's broader OrdSA layout. The customer's O1 orchestrator dispatches work to ng-port-01; ng-port-01 emits evidence into the customer's O6 plane; ng-port-01's internal envelope-check enforcement refuses requests that exceed its authorized rung.

The two examples — AI EA at enterprise scale, ng-port-01 at single-agent scale — together cover the recursive shape OrdSA was designed for. When the ng-port-01 worked example publishes, it will live in this same `docs/examples/` directory.

---

## 9. Conclusion

OrdSA gives the ordering. AI EA gives a worked enterprise-scale deployment. The two artifacts do not need each other to be readable on their own, but they read more completely together — OrdSA's layers gain concrete reference shapes, AI EA's planes gain explicit authority and evidence grounding.

This paper does not change either side. The 8 papers in the AI EA corpus continue to stand on their own intellectual content; OrdSA's construct definition continues to be the source of truth for the ordering. What this paper adds is a *bridge* — the mechanical reading that lets a careful reader audit the alignment between what AI EA *says* and what OrdSA *prescribes*, layer by layer, plane by plane, principle by principle.

For OrdSA adopters who want to read a complete enterprise-scale deployment: read AI EA's *Enterprise Agentic AI Platform Strategy* first for the four-plane shape, then the AEON white paper for the control plane in depth, then this bridge for the OrdSA grounding, then the OAAD papers for the substrate. For AI EA readers who want to see the OrdSA grounding made explicit: this bridge is the entry point; OrdSA's own [`docs/concept.md`](../concept.md) is the next read.

---

## References

### AI EA corpus (`osa-ai-org/enterprise-ai`)

- [Enterprise Agentic AI Platform Strategy](https://github.com/osa-ai-org/enterprise-ai/blob/main/docs/Enterprise-Agentic-AI-Platform-Strategy.pdf) — the umbrella; four-plane platform, maturity model
- [AEON white paper](https://github.com/osa-ai-org/enterprise-ai/blob/main/docs/AEON-White-Paper.pdf) — the control plane; six service planes
- [AIDEX white paper](https://github.com/osa-ai-org/enterprise-ai/blob/main/docs/AIDEX-White-Paper.pdf) — the worker-facing experience subdomain; HCAE
- [OAAD Strategic Brief](https://github.com/osa-ai-org/enterprise-ai/blob/main/docs/OAAD-Strategic-Brief-v5.pdf) — the OSS-replaces-COTS thesis
- [OAAD — The Next Shape of the IT Business Capability Model](https://github.com/osa-ai-org/enterprise-ai/blob/main/docs/OAAD-The-Next-Shape-of-the-IT-Business-Capability-Model.pdf) — capability model reframed around owned vs. rented substrate
- [Enterprise Agentic Platform Architecture Deck](https://github.com/osa-ai-org/enterprise-ai/blob/main/docs/Enterprise-Agentic-Platform-Architecture-Deck.pdf) — companion deck
- [AIDEX Deck](https://github.com/osa-ai-org/enterprise-ai/blob/main/docs/AIDEX-Deck.pdf) and [AIDEX / AEON Deck](https://github.com/osa-ai-org/enterprise-ai/blob/main/docs/AIDEX-AEON-Deck.pdf) — companion decks

### AI EA architecture decisions

- [ADR-EA-0001](https://github.com/osa-ai-org/enterprise-ai/blob/main/decisions/ADR-EA-0001-adopt-ordsa-development-process.md) — Adopt OrdSA-style development process for enterprise-ai
- [ADR-EA-0002](https://github.com/osa-ai-org/enterprise-ai/blob/main/decisions/ADR-EA-0002-reframe-as-ordsa-exemplar.md) — Re-frame AI EA as the canonical enterprise-scale OrdSA exemplar

### OrdSA construct

- [Concept](../concept.md) — canonical statement of the construct
- [Layer files](../layers/) — O0 through O6 in depth
- [Schema](../../schema/ordsa-0.2.yaml) — construct schema (v0.2 draft)
- [Relationship to frameworks](../relationship-to-frameworks.md) — OrdSA next to TOGAF, UAF, ArchiMate, NIST AI RMF
