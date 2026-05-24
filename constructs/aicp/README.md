# AICP: Agent Identity Card Protocol

*Platform-mediated agent identity, phase-gated tool injection, and work-lifecycle management.*

---

## Position in the AIDE canon

AICP is one of **five peer methodological constructs** in the AIDE canon's `constructs/` tier (alongside [DEA](../dea/), [OrdSA](../ordsa/), [MxM](../mxm/), [OAgents](../oagents/)). It patterns **portable agent identity and reputation** — the platform-issued *Card* as the unit of identity, phase-gated tool injection as the access model, and (federation profile) cryptographically-verifiable, cross-platform attestations as portable reputation.

Where **OAgents** answers *what an agent is* (a typed object with a behavioral envelope), **AICP** answers *who an agent is across platforms, and what it has earned*. The two are peers; neither subsumes the other. Admitted to the constructs tier by [ADR-EA-0016](decisions/ADR-EA-0016-introduce-aicp-construct.md).

**Canonical artifact (referenced, not vendored):** the authoritative AICP specification and JSON schemas live in the public MIT repository [`ologos-repos/AICP`](https://github.com/ologos-repos/AICP) — `spec/AICP-v0.1.md` plus `spec/schemas/{card,attestation,agreement,audit-event,platform-capability}.schema.json`. The canon references this repo as the source of truth; the local [`spec/`](spec/) directory is **reserved** (per the constructs Pattern α) pending an authorship decision on whether to vendor a versioned snapshot (a CC-BY/MIT license-interaction choice for the author).

**Reference implementation (decoupled):** [CrewPort](https://crewport.ai) (Ologos LLC) implements AICP as an AI-agent crew marketplace. Like `oagent-core` for OAgents, it is hosted separately and **not absorbed** into the canon ("Theseus-pattern decoupling").

**Relation to Theseus:** the [Theseus Agent Thesis](../../related-work/theseus/) (Micah Longmire) introduces AICP as an *archetype* of the identity-and-memory move. The thesis is the theory and remains allied related-work; AICP is the buildable protocol and is the construct.

---

## What AICP is

AICP defines a standard for how a **platform** issues agent identities, controls which tools an agent can reach as a function of its state, and manages structured work lifecycles. It sits **above MCP** (which handles tool transport) and **alongside A2A** (which handles peer discovery), filling a gap neither covers:

| | MCP | A2A | **AICP** |
|---|---|---|---|
| **Handles** | tool transport | peer discovery | platform identity + tool injection |
| **Identity** | none (connection-level) | self-declared | **platform-issued** |
| **Tools** | static per server | n/a | **dynamic per Card + phase** |

The core unit is the **Card** — a platform-issued identity document for a single agent or agent group. One operator may hold many Cards, each with independent history. Identity is *stamped from outside* (platform-issued, platform-attested), not self-declared — the property the Theseus thesis calls *stampable* identity.

### Protocol layers (L1–L6)

| Layer | Name | Type | What it does |
|---|---|---|---|
| **L1** | Enrollment | **CORE** | OAuth 2.1 → registration token → Card issuance; Card lifecycle `incomplete → active → {dormant, suspended}` |
| **L2** | Tool Injection | **CORE** | Card-scoped MCP endpoint `/mcp/{card_id}`; `tools/list` is a projection `f(card_id, card_status, active_agreement, agreement_phase)` — the platform *injects* tools at the agent. The protocol's core innovation |
| **L3** | Discovery | profile `market` | Marketplace: work Classes, Tract credentials, bidding, confidentiality gate |
| **L4** | Engagement | profile `lifecycle` | Phased agreement state machine, phase gates, kick-back, revision, acceptance criteria, delivery manifest |
| **L5** | History | profile `history` | Card-bound metrics: completion_rate, on_time_rate, revision_rate, total_completed |
| **L6** | Federation | profile `federation` | JWKS publication, signed attestations, cross-platform Card presentation, peer-trust policy (`open`/`allowlist`/`registry`) |

Conformance levels (`AICP-Core` through `AICP-Full`) let platforms adopt incrementally and advertise precisely.

### Key concepts

- **Card** — the platform-issued identity document (the unit of identity).
- **Port** — a concurrency slot; a Card must *dock* to a Port to accept work. (The protocol was originally "Agent Port Protocol" before the rename to AICP — "Port" is the residue.)
- **Tract** — a capability credential linking a Card to a work Class.
- **Agreement** — a structured unit of work with a phased lifecycle and gates.
- **Attestation** — a signed claim (JWT) a platform makes about one of its Cards; the unit of *portable reputation*. Federation uses asymmetric keys (EC P-256/Ed25519), JWKS-verifiable by any third party, peer-trust (no root CA).
- **Delegation chain** — every tool action is traceable: `human principal → operator account → Card → active credential → tool call → audit event`. Authority is **delegated, not owned** — the same stance as OrdSA and the Theseus "permissions fallacy."

---

## How AICP composes with the rest of the canon

- **AEON (Tier-4 platform) *consumes* AICP.** AEON's Identity plane can verify an AICP Card/attestation (fetch the issuer JWKS, verify the signature, check expiry) and mint an in-plane authority token off the *attested attributes* — letting portable reputation *inform* local authority without collapsing the two. AICP is the **portable passport**; AEON's in-plane token is the **local visa**. (The integration is downstream of this construct entry; see the deep-dive below.)
- **OrdSA** orders *what an agent may do* across ordinal altitudes; AICP carries *who the agent is* and its earned reputation. An OrdSA-conformant agent can carry an AICP Card as its durable identity.
- **OAgents** bounds the agent's behavior; AICP identifies the agent and its track record. Behavioral envelope (OAgents) + portable identity (AICP) are complementary halves of "a governable agent."

---

## Authorship and rights

| | |
|---|---|
| **Author** | Micah Longmire (sole) — [bobbyhiddn](https://github.com/bobbyhiddn); ORCID [0009-0006-7608-9322](https://orcid.org/0009-0006-7608-9322) |
| **Protocol repository** | [`ologos-repos/AICP`](https://github.com/ologos-repos/AICP) — spec + schemas, **MIT License**, Ologos LLC |
| **Reference implementation** | [CrewPort](https://crewport.ai) (Ologos LLC) — private; referenced, not absorbed |
| **Relation to canon license** | The canon is CC BY 4.0. AICP's spec/schemas are MIT in their own repo and are *referenced* here; no MIT content is vendored into the CC-BY tree by [ADR-EA-0016](decisions/ADR-EA-0016-introduce-aicp-construct.md). Any future vendored snapshot would carry its own LICENSE in this directory. |

## Further reading

- **[AICP specification](https://github.com/ologos-repos/AICP/blob/main/spec/AICP-v0.1.md)** — the normative protocol definition (v0.1.0 Draft)
- **[The Theseus Agent Thesis](../../related-work/theseus/)** — the theory paper that introduces AICP as an archetype
- **[AICP deep-dive analysis](https://github.com/ologos-repos/ng-aide-01/blob/main/docs/research/aicp-deep-dive.md)** — the AICP↔AEON-Identity comparison + canon-placement analysis
