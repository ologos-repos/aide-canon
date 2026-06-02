# Standards / protocol — ANP (Agent Network Protocol)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Slice cadence: **slow** (a de-facto protocol with dated spec releases) but **maturity-sensitive** — ANP is *emerging/community* with markedly lighter adoption than MCP or A2A; treat both version *and* traction as a dated snapshot.

## 1. What it is

> **Version / status header.** Analyzed version: **ANP `V1.0`** (tagged **2025-05-19**), the latest release of the `agent-network-protocol/AgentNetworkProtocol` specification set (numbered docs 01–09: identity, the `did:wba` DID method, agent description, discovery, and messaging). **Sub-status is mixed by layer:** the **Identity & Encrypted-Communication layer** is the most settled (W3C DID-grounded, `did:wba`); the **Meta-Protocol (Agent Communication Meta-Protocol) specification is explicitly marked Draft** — "in the draft stage and may undergo significant adjustments," and the current implementation's transport "will later be modified to a solution based on `did:wba` and HTTP." **Governance:** community-run committee model (founding committee, technical/development committees, community advisors, enterprise observers); **no Linux Foundation / formal-SDO affiliation** (contrast MCP→AAIF/Linux Foundation). License is open-source (repo source shows an **Apache-2.0 / MIT discrepancy** — flag, don't assert). **Adoption (honest):** **emerging** — ~1.3k GitHub stars / ~91 forks at survey time, an in-development SDK (`AgentConnect`), and a self-described profile of being "ahead in concept" but with "relatively limited" global recognition and traction "primarily domestic"; ecosystem viability is openly stated to depend on "whether major companies will support the DID route." A technical white paper is published (arXiv `2508.00007`).

**ANP** is an open, **decentralized agent-network protocol** — community-proposed (one of the earliest teams in the space), aiming to be "the HTTP of the Agentic Web era." Where MCP standardizes the *AI-aide → capability* integration seam and A2A standardizes *AI-aide ↔ AI-aide* task interop via a discoverable **AgentCard**, ANP standardizes **trustless, cross-organization agent-network identity + communication** with no central discovery authority. It is a **wire + identity standard**, not a governance corpus or a runtime — it standardizes *who an agent is across boundaries* and *how two agents agree on how to talk*.

Its surface is a **three-layer structure**:

- **Identity & Encrypted-Communication layer** — built on the **W3C DID** standard via the **`did:wba`** (Web-Based Agent) method: each agent publishes a DID document at a well-known HTTPS URL carrying its public-key material, so agents authenticate **cryptographically and peer-to-peer** — no shared API keys, no third-party identity provider — over end-to-end-encrypted channels.
- **Meta-Protocol layer** — a protocol *for negotiating protocols*: two agents dynamically agree on the message schema/format and version they will speak (conceptually adjacent to Oxford's Agora, per ANP's own comparison).
- **Application-Protocol layer** — agent **description + discovery** over JSON-LD messages on HTTPS.

In aide-canon terms, ANP is an **Identity- + Integration-plane wire standard** whose distinctive bet is **decentralized identity for agents** — the **DID-first** alternative to A2A's AgentCard discovery and to AICP's card-based platform-mediated identity.

## 2. Source links

- Official: `agent-network-protocol.com` (English + Chinese); Getting-Started guide (`/guide/`); Meta-Protocol spec **(Draft)** (`/specs/communication.html`); technical white paper (`/specs/01-agentnetworkprotocol-technical-white-paper/`).
- Spec repo (authoritative numbered docs 01–09, `V1.0` tag 2025-05-19): `github.com/agent-network-protocol/AgentNetworkProtocol` (see `06-anp-agent-communication-meta-protocol-specification.md` for the Draft meta-protocol); SDK: `github.com/agent-network-protocol/AgentConnect`.
- White paper: arXiv `2508.00007` ("Agent Network Protocol Technical White Paper").
- Comparative context: ANP's own "Comparative Analysis of Open-Source Agent Communication Protocols (MCP, ANP, Agora, agents.json, LMOS, AITP)" — positions ANP at the *identity + P2P-communication* layer vs MCP's tool integration.
- In-canon prior research: the standards rows still to be column-mapped in [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md); the AICP construct ([ADR-EA-0018], `constructs/aicp/`) as the canon's already-admitted *cross-platform identity* standard against which ANP's decentralized-identity bet must be triangulated.

## 3. Map against AIDE

### Against OAgents + the relevant AEON service planes

ANP touches two AEON planes squarely — **Identity** (its load-bearing layer) and **Integration** (the wire + negotiation) — plus the OAgents primitive boundary.

| AIDE construct / plane | ANP equivalent | Mapping type | AIDE position |
|---|---|---|---|
| **AEON Identity plane** | `did:wba` decentralized identity — per-agent DID document, P2P cryptographic auth, no central IdP | **partial / convergent-direction** | *In flight elsewhere* — ANP supplies a **portable, decentralized *who*** the canon's Identity plane does not yet author; the canon's lead is **authority (the *what*)**, not portable identity |
| **AEON Integration plane** | JSON-LD-over-HTTPS transport + **Meta-Protocol negotiation** | **synonym** (at the seam) | *In flight elsewhere* — a wire + a schema-negotiation mechanism; the canon CONSUMES/ALIGNS rather than authoring a rival |
| **AEON Authority plane** (OrdSA O0–O6) | (none — ANP authenticates identity + encrypts; **fine-grained authorization is an open work item**, by its own statement) | **N/A** | **AIDE ahead** — ANP proves *who*; it has no ordinal authority concept. Authority-down/evidence-up (O0–O6) is the canon layered *over* a DID, not in ANP |
| **OAgents `Agent`** (typed object in a behavioral envelope) | ANP's "agent" = a DID-identified network endpoint | **collision — see below** | **AIDE ahead** — ANP identifies and connects agents; the **behavioral-envelope** trust semantics live above the wire |
| **AEON Evidence plane** | (none first-class — E2E encryption protects the channel, not an evidence trail) | **N/A** | **AIDE ahead** on a governed evidence trail |
| **MxM Means** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) | ANP as an adopted identity/transport substrate | **nested** | Convergent — ANP would be a Means-surface the canon could consume |
| **AEON Inference plane** ([ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md)) | (orthogonal — ANP is model-agnostic at the wire) | **N/A** | *Orthogonal axis* — ANP carries agent comms; it does not frame *which model serves a principal* |

### A2A / AICP / ANP — the three identity-discovery bets (compare)

The load-bearing comparison for this entry is **how an agent is found and trusted across a boundary**, where three protocols make different bets:

| | **A2A** (Google-proposed) | **AICP** (Micah/Ologos, ADR-EA-0018) | **ANP** (community) |
|---|---|---|---|
| Identity model | **AgentCard** discovery — capability-advertising card at a well-known URL | **Card-based, platform-mediated** identity + **phase-gated** tool projection (L1–L6); JWKS-verifiable attestations | **DID-based, decentralized** (`did:wba`) — P2P cryptographic auth, no central IdP |
| Trust anchor | endpoint-published card | platform + federated attestation | self-sovereign DID document |
| Discovery | card-at-URL | enrollment/discovery profiles (L3) | DID + application-layer description/discovery |
| Maturity (survey) | broad vendor traction | spec public, ref impl private (CrewPort) | **emerging, lighter adoption** |

All three are **identity/discovery interfaces the canon relates *to*, not authority layers**. The canon's already-admitted position — **AICP = portable *passport* (who, anywhere); AEON Identity plane = in-plane *visa* (what, here)** — generalizes: **ANP's `did:wba` is another passport mechanism (a *decentralized* one), and AEON still decides what it may do here.** ANP and AICP are not rivals at the canon's altitude; they are two card/credential shapes the AEON Identity plane can verify-and-then-authorize.

### Vocabulary collision (canon-vocabulary-map discipline)

ANP uses the bare **"agent"** as its central noun (and "agent network," "agent communication"). Per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md) the canon reserves **`agent`** for the OAgents-conformant *typed object inside a behavioral envelope* and uses **AI-aide** for the role-class actor. So ANP's "agent" is, in canon terms, predominantly the **AI-aide** (a networked actor with a DID), **not** the OAgents `Agent` primitive — a direct collision to flag when the ANP column is added to [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md). ANP has **no `Skill` / `Capability` / behavioral-envelope noun** (its layers are identity / negotiation / description-discovery); those canon nouns are **N/A** in ANP and are exactly the authority semantics the canon supplies above a DID-identified endpoint.

## 4. Alignment classification

**Per-axis (ALIGN / CONSUME / EXTEND / DIFFERENTIATE) — convergent on decentralized identity, ahead on authority + governance.** ANP is **not a competitor** at the canon's altitude; it is a candidate identity/transport substrate the canon would govern over.

- **ALIGN / CONSUME (Identity + Integration).** ANP's `did:wba` decentralized identity is a **direction the canon's Identity plane could align with** — a portable, IdP-free *who* that the AEON Identity plane could verify (the same verify-only floor it already runs for AICP cards). The Meta-Protocol negotiation + JSON-LD wire are Integration-plane surfaces to consume, not rebuild. *In flight elsewhere; the canon aligns onto it.*
- **EXTEND (Authority + Evidence).** **AIDE ahead.** ANP authenticates identity and encrypts the channel but, by its own admission, leaves **fine-grained authorization as an open work item**. The canon's contribution sits *above* a verified DID: **OrdSA O0–O6 authority-altitude, principal+session binding, envelope-refinement, a governed evidence trail.** A DID proves *who*; AEON decides *what here*.
- **DIFFERENTIATE (altitude + vocabulary + governance).** The canon is a **governance/architecture corpus**, ANP a **wire + identity protocol** — differentiation by altitude, not overlap. Vocabulary: the canon supplies the `Skill`/`Capability`/behavioral-envelope nouns ANP lacks and disambiguates ANP's bare "agent." Governance: the canon's vendor-neutral, ratified-construct posture is **ahead** of ANP's community-committee, partly-Draft state.

**The synthesis.** On **OrdSA authority-altitude and governance maturity the canon is unambiguously AIDE-ahead** — ANP operates at the identity-and-transport altitude and explicitly defers authorization. On **decentralized-identity-for-agents the work is in-flight elsewhere, and it is a direction the canon's Identity plane could align with** rather than differentiate from: ANP's `did:wba` is a third identity bet alongside A2A's AgentCard and AICP's platform-mediated card, and the canon's passport-vs-visa framing already tells it how to compose with all three — **verify the (decentralized) card, then apply in-plane authority.** They **compose, not compete**, the same shape the [MCP](mcp.md) and [LangChain](../vendor-stacks/langchain.md) entries reach: ANP could give the canon **boundary-crossing, IdP-free reach**, and the canon would give a DID-identified endpoint the **authority + envelope** layer ANP structurally declines to enforce — *with the honest caveat that ANP's adoption is still emerging and a DID-route bet is unproven at scale.*

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Converge-or-differentiate (decentralized identity).** Decide and document the canon's stance on `did:wba`-class decentralized identity as a *third card shape* the AEON Identity plane verifies (alongside AICP). KR shape: an Identity-plane "verify-a-DID-then-authorize" mapping — the passport-vs-visa pattern extended to a decentralized passport — gated on a maturity re-check of ANP adoption.
2. **Defend-and-extend (authority above identity).** Propagate the OrdSA-authority + envelope position as the layer that sits *above any agent-identity protocol* — ANP is a clean example of an identity/transport wire with authorization openly unfinished. KR shape: a "govern-a-DID-identified-endpoint" profile (verify DID → bind principal+session → apply O0–O6) demonstrated against a `did:wba` identity.
3. **Differentiate-by-vocabulary + maturity-honesty.** Add the ANP column to [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md) (bare-`agent`→AI-aide collision; Skill/Capability/envelope **N/A**), and record ANP's *emerging* status so the canon does not over-credit a lower-adoption protocol relative to MCP/A2A. KR shape: the mapped column + a tracked maturity probe (stars/SDK/major-vendor DID-route adoption) revisited at OKR refresh.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Analyzes ANP `V1.0` (tagged 2025-05-19), with the Agent Communication Meta-Protocol spec **still Draft**; adoption assessed as **emerging / lighter than MCP or A2A**. Revisit on a major ANP spec release (meta-protocol leaving Draft, the announced `did:wba`+HTTP transport rework), a governance/foundation affiliation event, a material adoption shift (major-vendor DID-route support), or at OKR refresh.
