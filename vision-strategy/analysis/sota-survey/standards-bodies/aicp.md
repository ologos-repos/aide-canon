# Standards / protocol — AICP (Agent Identity Card Protocol)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md), mapping anchor per [`standards-bodies/README.md`](README.md). Cadence: **slow** (de-facto protocol; versioned spec — treat the version pin below as the analyzed snapshot, not a moving target).
>
> **SPECIAL — Ologos-family, not an external competitor.** AICP is Micah Longmire's *independent, public-MIT* protocol. It is **adjacent/related to AIDE but not part of the AIDE canon's governance argument and not an external rival**. This entry surveys it as a *related Ologos-family standard* the canon already consumes (it is vendored as a Tier-3 construct), and classifies the canon's posture toward it as **converge/consume**, not ahead-vs-behind. Authorship is honored throughout: the canon does not claim AICP as AIDE's.

## 1. What it is

> **Version/status header (analyzed snapshot).**
> - **Spec:** AICP — Agent Identity Card Protocol, **v0.1.0 (Draft)**, status **Proposal**, dated **2026-03-14**.
> - **Author:** **Micah Longmire** (sole) — ORCID [0009-0006-7608-9322](https://orcid.org/0009-0006-7608-9322). Published by **Ologos LLC under the MIT License**.
> - **Source pin:** [`ologos-repos/AICP`](https://github.com/ologos-repos/AICP) (living source). Verified at survey time 2026-06-01 against the public repo: spec header reads exactly `Version 0.1.0 (Draft) · Status Proposal · Date 2026-03-14`; the canon's vendored snapshot is pinned at `ologos-repos/AICP@f85a76c` (2026-05-24). No newer published version was found at survey time. (Distinct from the unrelated arXiv "AIP / Agent Identity Protocol" and "AID / Agent Identity & Discovery" efforts surfaced in §2 — do not conflate.)

**AICP** defines a standard for how a **platform** issues AI-aide identities, controls which tools an enrolled AI-aide can reach as a function of its state, and manages structured work lifecycles. It sits **above MCP** (which carries tool transport) and **alongside A2A** (which carries peer discovery), filling a gap neither covers: a *platform* stamps identity from outside, injects tools per state, and (in its federation profile) lets that identity carry cryptographically-verifiable, portable reputation across platforms.

The fundamental unit is the **Card** — a platform-issued identity document for one AI-aide (or AI-aide group). One operator may hold many Cards, each with independent history. Identity is *stamped from outside* (platform-issued, platform-attested), not self-declared. Six protocol layers compose it: **L1 Enrollment** + **L2 Tool Injection** are CORE (OAuth 2.1 → registration token → Card issuance; Card-scoped MCP endpoint `/mcp/{card_id}` with phase-gated `tools/list`); **L3 Discovery**, **L4 Engagement**, **L5 History**, **L6 Federation** are optional profiles (marketplace + Classes/Tracts; phased agreement state machine + gates; Card-bound metrics; JWKS-published, EC-signed attestations as portable reputation — symmetric keys prohibited for federation). Conformance levels run `AICP-Core` → `AICP-Full`.

**The genuinely novel structural claim is phase-gated tool projection.** Per §5.6 of the spec, the MCP `tools/list` response is not a static catalog but a projection of the AI-aide's current state:

```
tools = f(card_id, card_status, active_agreement, agreement_phase)
```

The **same MCP endpoint returns different tool catalogs at different points in a work lifecycle** — the platform *injects* tools at the AI-aide rather than the AI-aide *discovering* them. This inverts MCP's direction (server-drives, not client-drives) and is the protocol's core innovation.

## 2. Source links

- **Living source (authoritative, public):** [`ologos-repos/AICP`](https://github.com/ologos-repos/AICP) — spec + 5 JSON schemas, MIT, Ologos LLC. Spec file: [`spec/AICP-v0.1.md`](https://github.com/ologos-repos/AICP/blob/main/spec/AICP-v0.1.md).
- **In-canon (already resident):** AICP is a Tier-3 construct — [`constructs/aicp/README.md`](../../../../constructs/aicp/README.md), the vendored spec snapshot [`constructs/aicp/spec/AICP-v0.1.md`](../../../../constructs/aicp/spec/AICP-v0.1.md), and the admission decision [ADR-EA-0018](../../../../constructs/aicp/decisions/ADR-EA-0018-introduce-aicp-construct.md). Theory paper (allied related-work): [`related-work/theseus/`](../../../../related-work/theseus/) (Micah Longmire), which introduces AICP as an archetype.
- **Reference implementation (decoupled, private):** CrewPort (`crewport.ai`, Ologos LLC) — referenced, not absorbed (Theseus-pattern decoupling).
- **Adjacent external efforts (named to disambiguate, NOT AICP):** arXiv [`2603.24775`](https://arxiv.org/abs/2603.24775) "AIP: Agent Identity Protocol" (Invocation-Bound Capability Tokens over MCP/A2A); [`aid.agentcommunity.org`](https://aid.agentcommunity.org/docs/specification) "AID: Agent Identity & Discovery" (DNS-based discovery). These occupy nearby ground; they are separate protocols by other authors — useful as a direction-of-travel signal that platform-mediated AI-aide identity is a live SOTA frontier.

## 3. Map against AIDE

AICP maps most cleanly to **OAgents** (the agent domain model) and to three AEON service planes — **Identity**, **Authority**, **Capability Composition**. Alignment status here means *how the canon already relates to AICP*, since AICP is a related Ologos-family standard the canon **consumes**, not an external interface it must ALIGN/EXTEND/DIFFERENTIATE against.

| AICP element | OAgents / AEON construct or plane | Alignment status |
|---|---|---|
| **Card** (platform-issued identity) | AEON **Identity** plane — principal resolution + delegation chains | **Consume / converge** — AEON's Identity plane *verifies* an AICP Card (fetch issuer JWKS, check signature/expiry) and mints an in-plane token off the attested attributes. **Passport vs visa:** AICP Card = portable cross-platform identity (passport); AEON in-plane token = local authority grant (visa). They compose; neither replaces the other. |
| **Delegation chain** (`human principal → operator → Card → credential → tool call → audit event`) | AEON **Identity** (chain) + **Authority** plane (OrdSA authority modes) | **Converge** — same "authority is delegated, not owned" stance OrdSA holds; AICP supplies the identity links, OrdSA/Authority supplies the altitude ordering above them. |
| **Phase-gated tool projection** `f(card_id, card_status, active_agreement, agreement_phase)` | AEON **Capability Composition** + **Authority** (envelope-over-tools) | **Converge — load-bearing.** The same MCP endpoint returning state-dependent tool catalogs *is* the canon's "authority over tools / behavioral envelope" direction expressed as a wire protocol. AICP gives a concrete projection mechanism the envelope direction can sit above. |
| **Scopes** (`app:read` / `app:write`), phase gates | AEON **Authority** plane — envelope evaluation; OrdSA O0–O6 authority-altitude | **AIDE supplies the layer above** — AICP gates *which* tools; OrdSA orders *what altitude* of authority each grant sits at (authority-down / evidence-up). AICP has no ordinal-altitude concept; OrdSA is the complement, not a rival. |
| **Tract** (capability credential → Class) | OAgents capability typing + AEON **Capability Composition** registry | **Converge** — Tract is a credential gating a work Class; aligns with capability-registry staging. |
| **Attestation** (L6, signed JWT, JWKS-verifiable) | AEON **Evidence** plane (audit substrate) + **Identity** (cross-platform trust) | **Consume** — AEON ingests an AICP attestation at the verify-only floor; portable reputation *informs* local authority without collapsing the two. |
| **Agreement / Class / Port / phases** (L3–L5) | OAgents work-unit modeling; AEON **Orchestration Runtime** | **Converge** — phased lifecycle + concurrency slot (Port) parallel orchestration-runtime dispatch staging. |

**Vocabulary-collision note (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)).** This entry uses **AI-aide** wherever AICP's prose says casual "agent" referring to the persistent enrolled entity — never the bare word. Specific flags: (1) AICP **"Card"** is the *identity of an AI-aide*, which is **not** the OAgents **`Agent`** primitive (a typed object inside a behavioral envelope) — Card is identity-of, Agent is the-typed-object; keep them distinct. (2) AICP **"Class"** (a work category, e.g. `class-web-app`) collides with the everyday programming sense of "class" and with any OAgents type-class reading — it means *work category* only. (3) AICP **"Port"** (a concurrency slot a Card docks to) is unrelated to a network port; it is the residue of the protocol's former name (Agent **Port** Protocol). (4) AICP **"Agreement"** is a structured work unit, not a legal contract term of art. These are surfaced, not silently inherited.

## 4. Alignment classification

**Converge / consume — a related Ologos-family standard the canon sits above, not a SOTA competitor.** Unlike a vendor stack (classified ahead/behind across axes), AICP is *family*: the canon already vendors it (ADR-EA-0018) and AEON already consumes it. The per-axis read:

- **Converge (decisive).** AICP's phase-gated tool projection **converges with the canon's envelope/authority-over-tools direction**. The claim that one MCP endpoint returns different tool catalogs as a function of identity + lifecycle phase is the same intuition the canon expresses as a behavioral envelope governing which tools an AI-aide may reach — here realized as a concrete *wire* mechanism. This is the most interesting finding: an independently-authored Ologos-family protocol arrived at the canon's authority-over-tools direction from the platform-identity side.
- **Consume (settled).** AEON's Identity plane consumes AICP Cards/attestations (passport→visa); NG-AIDE-01 already wires an AICP attestation ingress at the verify-only floor. The relationship is built-toward, not contested.
- **Complementary altitude (the boundary).** AICP supplies **card-based platform identity + phase-gated tool projection** (the *wire*); **AEON / OAgents / OrdSA supply the governance ABOVE it** — authority-altitude (OrdSA O0–O6), behavioral envelope (OAgents), deontic constraints (MxM Morals), evidence trail (AEON Evidence). AICP fills the platform-identity-and-tool-injection gap; the canon fills the authority/envelope gap above it. Neither subsumes the other.

**The synthesis: AICP and AIDE compose as identity-wire-below + governance-above.** AICP is the portable identity and tool-projection substrate; the AIDE constructs are the authority/envelope/evidence governance wrapped around it. This is the *passport-vs-visa* relationship the canon's AICP construct already records — AICP answers *who an AI-aide is across platforms and what it has earned*; OAgents/OrdSA/AEON answer *what it may do here and at what altitude*. The convergence on phase-gated tool projection is the signal that the two were designed toward the same horizon from different sides.

**Entity-distinction note (per survey discipline).** Nothing here conflates the Ologos ecosystem's deployments with NG-AIDE-01's: NG-AIDE-01 is named only as the *reference implementation* that wires the AICP ingress; AEON is the canon construct. No bare "fleet" framing is used. AICP is Micah's protocol; AEON is JD + Micah's co-authored platform — the authorship lines are kept separate.

## 5. Objective implication

Two Doerr-style Objective shapes follow — both *converge*-flavored, since AICP is family:

1. **Converge-and-cite (envelope ↔ wire).** Name AICP's phase-gated tool projection as the **wire-level realization of the canon's authority-over-tools / behavioral-envelope direction**, and document the composition explicitly: OAgents envelope + OrdSA authority-altitude *above* an AICP-projected tool surface *below*. KR shape: a "govern-an-AICP-platform" mapping showing the envelope + O0–O6 authority sitting over `f(card_id, card_status, active_agreement, agreement_phase)`, with the AEON Identity passport→visa verification as the join.
2. **Consume-and-prove (identity ingress).** AEON already consumes AICP Cards/attestations at the verify-only floor (NG-AIDE-01 ingress). KR shape: demonstrate the full chain — verified AICP attestation → AEON in-plane authority token → OrdSA-altitude-bounded tool grant — on a canon-fidelity exemplar, proving portable reputation *informs* local authority without collapsing passport into visa.

No catch-up Objective is warranted: AICP is not a gap the canon trails on — it is a complementary Ologos-family standard the canon already vendors and consumes. The Objective is to *articulate the composition*, not to close a distance.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Analyzed snapshot: AICP v0.1.0 Draft (Proposal), 2026-03-14, verified against `ologos-repos/AICP` public repo at survey time. Honors Micah Longmire's sole authorship of AICP; the canon does not claim it as AIDE's. Revisit on a new published AICP version or at OKR refresh.
