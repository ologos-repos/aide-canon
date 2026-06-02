# Standards body — OAuth / OIDC + RFC 8693 + SPIFFE/SPIRE (the identity & delegation substrate)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Mapping anchor: [`standards-bodies/README.md` §AIDE-mapping-anchor](README.md). Cadence: **slow** for the ratified base (RFC 8693, OIDC Core, SPIFFE), **fast** for the IETF agent-delegation drafts (multiple expiring/active individual drafts churning through 2026).

## 1. What it is

> **Version / status header** (mark explicitly — never infer ratification):
>
> | Standard | Version / doc | Status | Date | Body |
> |---|---|---|---|---|
> | OAuth 2.0 | RFC 6749 | Internet Standard (base, Proposed Standard) | Oct 2012 | IETF |
> | OAuth 2.1 | `draft-ietf-oauth-v2-1-15` | **Active WG draft** (not yet RFC; consolidates 2.0 + PKCE-required, drops Implicit/ROPC) | expires 2026-09-03 | IETF OAuth WG |
> | OpenID Connect Core 1.0 | Core 1.0 + errata set 2 | **Final** (authn layer on OAuth 2.0) | 2014 base, errata 2 final | OpenID Foundation |
> | **RFC 8693** | OAuth 2.0 Token Exchange | **Proposed Standard** (Standards Track) | **Jan 2020** | IETF |
> | **SPIFFE / SPIRE** | SPIFFE ID + SVID (X.509 / JWT) | **CNCF Graduated** project + spec | graduated; current | CNCF |
> | `draft-oauth-ai-agents-on-behalf-of-user` | `-02` | **Expired** individual I-D (`requested_actor` / `actor_token`) | rev 2025-08-25 | IETF (individual) |
> | `draft-nelson-agent-delegation-receipts` | `-09` | **Active** individual I-D (signed delegation receipts) | rev 2026-05-21 | IETF (individual) |
> | `draft-mishra-oauth-agent-grants` (DAAP) | `-00` | individual I-D (DID identity + cascade revocation) | individual | IETF (individual) |
> | `draft-niyikiza-oauth-attenuating-agent-tokens` | `-00` | individual I-D (token attenuation per hop) | individual | IETF (individual) |
> | `draft-mcguinness-oauth-actor-profile` | `-00` | individual I-D (Actor Profile for cross-org delegation) | individual | IETF (individual) |

This entry surveys the **identity + delegation transport substrate** that the canon's Identity and Authority planes ride on top of — not an agent framework or governance corpus, but the protocol primitives beneath one.

Three ratified layers form the stable base. **OAuth 2.0 / OIDC** establish the access-token + ID-token model: a client obtains a scoped token to act for a resource owner, and OIDC adds an authenticated identity claim set. **RFC 8693 (OAuth 2.0 Token Exchange)** defines an STS-style flow for *exchanging* one token for another, and — critically for this survey — formalizes the difference between **impersonation** (the resulting token looks like the subject; no record the actor was distinct) and **delegation** (the resulting token carries an `actor_token` / `act` claim, preserving "B acting for A"). The `may_act` claim states, inside a token, *which* party is authorized to become the actor for the subject — a flat, single-hop authorization assertion. **SPIFFE/SPIRE** (CNCF graduated) supplies the *workload* side: a SPIFFE ID (a trust-domain URI) issued as a short-lived **SVID** (X.509 cert or JWT), bootstrapping cryptographic mutual-TLS identity for non-human principals without long-lived secrets.

On top of that base, a cluster of **IETF agent-delegation drafts** (2025–2026, mostly individual submissions, churning fast) is trying to extend OAuth specifically for *AI-aides* (the canon term; the drafts say "AI agents") acting on behalf of users: `draft-oauth-ai-agents-on-behalf-of-user` (`requested_actor` / `actor_token` parameters, now expired), `draft-nelson-agent-delegation-receipts` (user-signed, tamper-log-anchored delegation receipts), the Delegated Agent Authorization Protocol / DAAP (DID-based agent identity + cascade revocation), attenuating-agent-tokens (narrow the grant at each hop), and an Actor Profile for cross-org delegation. The live mailing-list problem as of March 2026 is **delegation-chain splicing** — an attacker inserting itself into the `act` claim chain — which is exactly an *authority-provenance integrity* problem.

## 2. Source links

- RFC 8693 — OAuth 2.0 Token Exchange (Proposed Standard, Jan 2020): `https://www.rfc-editor.org/info/rfc8693/` · `https://datatracker.ietf.org/doc/html/rfc8693`
- OAuth 2.1 (active WG draft): `https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/` · OAuth landing `https://oauth.net/2.1/`
- OpenID Connect Core 1.0 (Final, errata 2): `https://openid.net/specs/openid-connect-core-1_0.html`
- SPIFFE/SPIRE (CNCF graduated): `https://spiffe.io/` · overview `https://spiffe.io/docs/latest/spiffe-about/overview/` · CNCF TAG-Security self-assessment `https://tag-security.cncf.io/community/assessments/projects/spiffe-spire/self-assessment/`
- IETF agent-delegation drafts: on-behalf-of `https://datatracker.ietf.org/doc/draft-oauth-ai-agents-on-behalf-of-user/` · delegation receipts `https://datatracker.ietf.org/doc/draft-nelson-agent-delegation-receipts/` · DAAP `https://www.ietf.org/archive/id/draft-mishra-oauth-agent-grants-00.html` · attenuating tokens `https://datatracker.ietf.org/doc/html/draft-niyikiza-oauth-attenuating-agent-tokens-00` · Actor Profile `https://datatracker.ietf.org/doc/draft-mcguinness-oauth-actor-profile/`
- In-canon: [AICP spec](../../../../constructs/aicp/spec/README.md) (authority-chain / identity-card model that *assumes* this substrate underneath); [OrdSA docs](../../../../constructs/ordsa/docs/) (O0–O6 ordinal authority); vocabulary discipline per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md).

## 3. Map against AIDE

This substrate maps to OAgents (the per-action behavioral envelope) and to two AEON service planes specifically — **Identity** and **Authority** — which the standards-bodies anchor names as the cleanest mapping surface.

| Standard / primitive | AIDE construct / plane | Alignment status |
|---|---|---|
| OAuth 2.0 / OIDC access + ID tokens | **AEON Identity plane** — principal authentication / token carriage | **AIDE CONSUMES** — foundational; AIDE rides these for transport-level principal identity, does not re-invent them |
| **RFC 8693 token exchange — delegation (`act` claim) vs impersonation** | **AEON Authority plane** (delegation hop) + **OAgents** envelope `actor`/`on-behalf-of` | **CONSUME + EXTEND** — AIDE consumes the delegation primitive; **EXTENDS** it with OrdSA ordinal-authority altitude (flat `act` claim → O0–O6) |
| RFC 8693 `may_act` (who may become actor) | OAgents per-action envelope authorization | **CONSUME** — `may_act` is the transport-level "is this delegation authorized" check the envelope sits above |
| **SPIFFE ID / SVID (cryptographic workload identity)** | **AEON Identity plane** — non-human / AI-aide principal attestation | **CONSUME (foundational)** — SPIFFE is exactly the cryptographic workload-identity AICP's identity-card and AEON's principal model assume underneath |
| OAuth scopes / RBAC | AEON Authority plane | **DIFFERENTIATE** — scopes are flat capability grants; OrdSA O0–O6 is *altitude*, not a flat scope list |
| IETF agent-delegation drafts (on-behalf-of, receipts, DAAP, attenuation, Actor Profile) | **AEON Authority plane** + AICP authority chain | **ALIGN / direction-of-travel** — the ecosystem is converging on the multi-hop delegation problem AIDE already frames as authority-provenance (evidence-up) |
| Delegation-chain *splicing* attack (Mar 2026 WG thread) | OrdSA evidence-up provenance integrity | **AIDE-ahead framing** — AIDE already models authority-provenance integrity; the drafts are discovering the threat the ordinal model anticipates |

### Vocabulary collision (flag per ADR-EA-0016)

The IETF drafts say **"AI agent"** throughout; in canon this is the **AI-aide** (the persistent principal), **not** the OAgents `Agent` primitive (a typed object inside a behavioral envelope). The drafts' **"actor"** (`act` / `actor_token`) is a *protocol role in a single delegation hop* — it must **not** be conflated with an OrdSA authority *altitude* (O0–O6): an `act` claim says *who* is acting-for-whom, never *at what authority altitude*. SPIFFE **"workload identity"** is the cryptographic substrate beneath an AI-aide principal, not the principal model itself. RFC 8693 **"delegation"** is one transport hop (B-for-A); OrdSA **authority-down/evidence-up** is the governing semantics *above* that hop. Flagging these prevents the common collapse of "the token says it's delegated" into "the authority chain is governed."

## 4. Alignment classification

**Mixed by axis — and decisively a CONSUMED/foundational substrate, not a competitor.** This is the load-bearing distinction: OAuth/OIDC/RFC-8693/SPIFFE are the *transport-level identity + delegation primitives*; AIDE does not re-implement them and does not contend with them. The classification is per-axis:

- **CONSUME (foundational) — Identity + transport delegation.** OAuth/OIDC token carriage, RFC 8693 token exchange, and SPIFFE/SPIRE workload SVIDs are exactly what AICP's authority chain and AEON's principal model *assume underneath*. AIDE rides them; convergent/foundational on the primitives themselves. There is no "AIDE ahead" claim to make on the cryptographic identity or single-hop delegation mechanics — that ground is mature, ratified (RFC 8693 since Jan 2020; SPIFFE CNCF-graduated), and correct.
- **EXTEND — Authority altitude.** RFC 8693 delegation and OAuth scopes are **flat token-exchange**: `act` records *who acts for whom*, scopes record *what capabilities*. Neither carries **authority altitude**. AIDE builds **OrdSA ordinal authority (O0–O6, authority-down / evidence-up)** and the **OAgents per-action envelope** *above* the token layer — this is where AIDE leads, because the substrate has no notion of ordinal authority and is not trying to acquire one.
- **ALIGN / direction-of-travel — Multi-hop agent delegation.** The IETF agent-delegation drafts (on-behalf-of, receipts, DAAP cascade-revocation, attenuating tokens, Actor Profile) are the ecosystem reaching toward the multi-hop AI-aide delegation problem AIDE already frames. The Mar-2026 **delegation-chain-splicing** thread is the field discovering authority-provenance integrity — an *AIDE-ahead framing* signal: AIDE's evidence-up provenance anticipates it. These drafts are individual/expiring and unstable; track as direction-of-travel, do not depend on any single one.

**Synthesis.** AIDE and this substrate **stack, they do not compete.** SPIFFE issues the cryptographic principal identity; OAuth/OIDC carry it; RFC 8693 performs the single delegation hop with an `act` claim; and **above all of that** AIDE supplies what the token layer structurally lacks — OrdSA authority *altitude* (O0–O6) governing each hop, the OAgents envelope bounding each action, and evidence-up provenance making the *chain* (not just one hop) auditable. This is the same canon-spec ↔ substrate relationship the survey documents elsewhere (cf. the LangChain finding's "compose, not compete"): the standards are the interface AIDE ALIGNs to and CONSUMEs, and ordinal authority is the EXTEND/DIFFERENTIATE layer on top.

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Consume-and-build (foundational integration).** Adopt RFC 8693 token exchange + SPIFFE/SVID as the *named transport substrate* for the AEON Identity plane and AICP — explicitly "ride, don't reinvent." KR shape: a documented mapping that pins the AICP authority chain onto RFC 8693 `act` claims + SPIFFE workload identity, with OrdSA O0–O6 expressed as the layer *above* the `act` claim.
2. **Defend-and-extend (authority altitude).** Propagate OrdSA ordinal authority as the altitude semantics the flat OAuth/RFC-8693 model lacks. KR shape: a worked example showing why a single `act` claim under-specifies governance (no altitude, no envelope) and how O0–O6 + the OAgents envelope close that gap over an unmodified token layer.
3. **Converge-or-differentiate (agent-delegation drafts).** Track the IETF agent-delegation drafts as direction-of-travel; position AIDE's evidence-up provenance as the answer to delegation-chain splicing. KR shape: a comparison note mapping each live draft (on-behalf-of / receipts / DAAP / attenuation / Actor Profile) to the AEON Authority plane, flagging which are convergent with OrdSA evidence-up and which assume flat delegation AIDE differentiates from.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Version/status header current as of survey date — IETF agent-delegation drafts are individual submissions churning fast (one already expired, others at `-00`); re-verify draft status at read time. Revisit on OAuth 2.1 ratification, any agent-delegation draft reaching WG adoption, or at OKR refresh.
