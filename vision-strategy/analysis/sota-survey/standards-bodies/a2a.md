# Standards / protocol — A2A (Agent2Agent Protocol)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Slice cadence: **slow** (formal-protocol deliverables) — but A2A has moved fast through 2025–2026, so treat the version header below as the dated snapshot.

**Version / status header**

| Field | Value |
|---|---|
| **Analyzed version** | A2A **v1.0** (the 1.0 milestone — "production readiness and stability") |
| **Version timeline** | v0.1 (Apr 2025, Google announce) → v0.2.x → v0.3.0 → **v1.0** (released ~Jan 2026; 1.0 milestone post Apr 21 2026) |
| **Status** | **Released / ratified-as-1.0**; under neutral governance. v1.0 carries **breaking changes** to the AgentCard schema vs v0.3 (e.g. `url`/`protocolVersion` moved into a `supportedInterfaces` structure); backward-compat is opt-in (`enable_v0_3_compat`), **not** default |
| **Governance** | **Linux Foundation** — Agent2Agent Protocol Project; Google **donated** A2A to LF **Jun 23 2025**; Apache-2.0 |
| **Origin** | **Google** (cross-ref the [`google-cloud`](../vendor-stacks/google-cloud.md) vendor entry, which surveys Google's *adoption* of A2A as a runtime/orchestration surface, and ADK as the build-side) |
| **Successor ref** | none (v1.0 is current head; this entry updates on the next breaking spec revision) |
| **Geography** | jurisdiction-neutral (LF) |

## 1. What it is

**A2A is an open wire protocol for cross-agent interoperability** — a common language by which **independent, opaque** AI-aides (built on different frameworks, by different vendors) discover each other, negotiate interaction modality, and coordinate stateful work **without exposing internal state, memory, or tools** to one another. It is deliberately the *complement* to Anthropic's MCP: MCP wires an AI-aide to its tools/context (vertical), A2A wires AI-aides to each other (horizontal). The core data model:

- **AgentCard** — a JSON discovery document published at a well-known path (`/.well-known/agent.json` in the original v0.1–v0.2 line; standardized to **`/.well-known/agent-card.json`** in later/v1.0 docs — note both forms appear in the wild). It advertises identity (name, description, version, provider), service-endpoint URLs / `supportedInterfaces`, supported features (`streaming`, `pushNotifications`, `extendedAgentCard`), an array of **AgentSkills**, default input/output modes, and **SecuritySchemes** (APIKey / HTTPAuth / OAuth2 / OpenIdConnect / MutualTLS). v1.0 adds **AgentCardSignature** for cryptographic integrity of the card.
- **AgentSkill** — an advertised, addressable unit of work the agent offers: `id`, human-readable description, routing `tags`, supported `inputModes`/`outputModes`, and call examples.
- **Task** — the stateful unit of collaborative work, with a unique id and a defined lifecycle: `submitted → working`, branching to `input-required` (interrupted), and terminal `completed` / `failed` / `canceled` / `rejected`.
- **Message** — one communication turn (`role` = user|agent) carrying one or more **Parts** (text / bytes / file-url / structured data).
- **Artifact** — a task output (document, image, structured data), also composed of Parts.

A2A is, in aide-canon terms, an **interface/transport standard** — an *interop contract between AI-aides at the integration boundary*, not a governance corpus. It says how two AI-aides talk; it is silent on *whose authority* either acts under.

## 2. Source links

- Official spec: `a2a-protocol.org/latest/specification/` (v1.0); v1.0 announce `a2a-protocol.org/latest/announcing-1.0/` and `.../whats-new-v1/`; project repo `github.com/a2aproject/A2A` (Apache-2.0, LF).
- Donation / governance: Google → Linux Foundation, **Jun 23 2025** (LF Agent2Agent Protocol Project).
- v1.0 milestone + backward-compat: *"The A2A 1.0 Milestone"* (Google Cloud Community, Apr 21 2026) — documents the AgentCard breaking changes and `enable_v0_3_compat`.
- Original announce: Google Developers Blog, *"A2A — a new era of agent interoperability"* (Apr 2025).
- In-canon prior research: A2A is listed as a standards/protocol to map in [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md) ("Future external systems to map"); the Google-origin note lives in the [`google-cloud`](../vendor-stacks/google-cloud.md) vendor entry §2.

## 3. Map against AIDE

A2A's relevant surface is **AEON's Integration plane** and the **Orchestration-runtime / Identity** planes, plus the canon's **cross-entity federation contract** (which is where A2A's silence becomes load-bearing).

| A2A concept | AIDE construct / plane | Alignment status |
|---|---|---|
| **AgentCard discovery** (`/.well-known/agent-card.json`) | **AEON Integration plane** — inter-deployment integration / capability advertisement | *In flight elsewhere* — A2A is the convergent wire standard for the advertise-and-discover half of Integration |
| **AgentSkill** (advertised work unit) | **OAgents Integration / OAAD capability surface** — what an AI-aide exposes outward | *In flight elsewhere* — convergent on the *advertise* shape; **vocab collision, see below** |
| **Task lifecycle** (`submitted/working/input-required/completed/...`) | **AEON Orchestration-runtime** + [`workflow-orchestration`](../../../../patterns/workflow-orchestration.md) pattern | *In flight elsewhere* — A2A's task states overlap the orchestration pattern's shared-evidence/lifecycle object; **AIDE ahead** on the envelope-refinement composition law A2A does not carry |
| **Message / Part / Artifact** | AEON Integration transport / Evidence emission | *In flight elsewhere* — convergent transport primitives |
| **SecuritySchemes + AgentCardSignature** (authN of the *card/connection*) | **AEON Identity plane** | *In flight elsewhere* on identity primitives; **AIDE ahead** on principal-altitude semantics A2A's card lacks |
| **(absent) authority / principal delegation** | **OrdSA authority altitudes (O0–O6)** + **OAgents behavioral envelope** + the **cross-entity federation contract** (`entity_id × principal_chain × verb_class`) | **AIDE ahead** — the spec advertises *capability* and authenticates a *connection*; it does **not** govern *authority-altitude* or per-action behavioral envelope. See §4 |

### Cross-entity federation note

A2A's AgentCard is the cross-agent **discovery + transport** layer. The canon's **cross-entity federation contract** (per the [vocabulary map entity-boundaries section](../../aide-vocabulary-map.md), 2026-05-29 clarification) is the **authority** layer that A2A presupposes but does not supply: when two AI-aides under **different entities** coordinate, the canon requires explicit **`entity_id × principal_chain × verb_class`** semantics — `observe`/`recommend` cross entity boundaries freely, while `direct`/`drive` (steer/halt/approve) is **refused at the contract layer absent the receiving entity's principal-chain attestation**. A2A's SecuritySchemes authenticate *that a caller is who it claims*; they do not encode *under whose authority, at what altitude, with what verb-class permission* a Task may be driven. An A2A connection between two AI-aides is necessary but not sufficient for a canon-conformant cross-entity `direct` — A2A is the pipe, the federation contract is the gate on it.

### Vocabulary collision

- **A2A "Agent"** = an opaque, network-addressable AI system advertised by an AgentCard — this is the canon's **AI-aide** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)), **not** the OAgents `Agent` primitive (a typed object inside a behavioral envelope). Use **AI-aide** for the system-under-a-principal; reserve casual "agent." Do **not** read A2A's network of advertised agents as a "fleet" — they are not the Ologos operational fleet nor NG-AIDE-01.
- **A2A "AgentSkill"** = an *advertised, addressable work unit* on the wire. This is a **third, distinct** sense of "Skill" and must be flagged: it is **not** the canon **Skill ↦ MxM Means** (a packaged capability the substrate composes), and it is **not** the OAgents `Agent` primitive. It is closest to "an externally-callable capability endpoint." (Contrast Google **ADK's** `Skill` — the field's most rigorous *packaging* protocol, L1/L2/L3 progressive disclosure, surveyed in [`google-cloud`](../vendor-stacks/google-cloud.md) §3 — which maps to Means; A2A's AgentSkill is the *advertise-on-the-wire* counterpart, not the package itself.)
- **A2A "Task"** = a stateful unit of cross-agent work — convergent with the orchestration pattern's lifecycle object; safe to use the external term in this column, AI-aide-side semantics governed by the workflow-orchestration pattern.

## 4. Alignment classification

**In flight elsewhere / convergent — at the interface altitude; AIDE ahead at the authority altitude.** Per the canon framing, a standard is an *interface*, and the AIDE posture toward an interface is **align / consume / extend / differentiate**. A2A's classification is per-axis:

- **CONSUME / ALIGN (Integration + transport).** A2A is the convergent, LF-governed wire standard for cross-agent discovery + task transport. AEON's Integration plane should **consume** A2A as the inter-deployment interop interface rather than reinvent AgentCard/Task/Message. This is the *in-flight-elsewhere → converge* outcome from the survey README's three-way scheme: A2A occupies the same ground as AEON inter-deployment integration and is evolving in a direction AIDE aligns with.
- **EXTEND (Orchestration-runtime).** A2A's Task lifecycle is a transport-level state machine; the canon's [`workflow-orchestration`](../../../../patterns/workflow-orchestration.md) pattern ([ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md)) supplies the **envelope-refinement composition law** A2A tasks do not enforce. AIDE **extends** A2A here.
- **DIFFERENTIATE / AIDE ahead (Authority + behavioral envelope).** This is the load-bearing finding. A2A's AgentCard **advertises capability and authenticates a connection; it does not govern authority-altitude or per-action behavioral envelope.** The canon carries exactly that missing layer: **OrdSA O0–O6** authority-altitude (authority-down / evidence-up), the **OAgents behavioral envelope** (per-action governance), and the **cross-entity federation contract** (`entity_id × principal_chain × verb_class`). On the OrdSA axis the canon is structurally **ahead** — A2A operates entirely below the authority-altitude line; it is an O0/O1-level capability/transport interface with no ordinal authority concept.

**Synthesis — they compose, not compete (same shape as the [`langchain`](../vendor-stacks/langchain.md) finding, one altitude down).** A2A is the *interface* AIDE wraps governance **around**, not a rival corpus: AEON consumes A2A as the cross-agent Integration wire, the workflow-orchestration pattern governs the Task lifecycle as an extension, and OrdSA + the OAgents envelope + the cross-entity federation contract supply the authority/principal-chain semantics the AgentCard structurally lacks. A canon-conformant cross-entity `direct` is "an A2A call **gated by** a principal-chain-attested federation contract." A2A advertises *what an AI-aide can do*; the canon governs *under whose authority, at what altitude, within what envelope* it may be driven to do it.

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Converge (consume A2A as the Integration interface).** Adopt A2A as AEON's canonical cross-agent discovery/transport wire rather than a bespoke interop format. KR shape: a documented "AEON-Integration-over-A2A" mapping (AgentCard ↔ AI-aide advertisement; Task ↔ orchestration lifecycle object; SecurityScheme ↔ Identity-plane authN), pinned to A2A **v1.0** and tracking the breaking-change cadence.
2. **Extend (authority over the AgentCard).** Specify the **cross-entity federation contract as the authority layer over an A2A connection** — the canonical artifact showing `entity_id × principal_chain × verb_class` gating a `direct`/`drive` A2A call, with `observe`/`recommend` passing freely. KR shape: a worked "govern-an-A2A-link" mapping analogous to the LangChain "govern-a-deployment" KR, demonstrating the principal-chain attestation A2A's SecuritySchemes do not encode.
3. **Differentiate (defend the authority-altitude lead).** Propagate the OrdSA-authority + OAgents-envelope position as the trust layer that sits *above any cross-agent protocol* — A2A is the clean example of a mature, widely-adopted interop standard with **no** authority-altitude or per-action-envelope concept. KR shape: surface "A2A advertises capability, it does not govern authority" as the canonical *AIDE-ahead* talking point in the standards-bodies slice (alongside the NIST-AI-RMF / OAgents anchor).

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Pinned to A2A **v1.0** (Linux Foundation; breaking-change vs v0.3). Revisit on the next A2A breaking spec revision or at OKR refresh; cross-check against the [`google-cloud`](../vendor-stacks/google-cloud.md) (A2A as runtime surface) and forthcoming MCP / ANP standards-bodies entries.
