# standards-bodies/

Survey of formal standards efforts and de-facto protocols shaping the agentic-AI ecosystem.

## In scope

**Formal standards bodies:**

- **NIST** — AI RMF + CAISI initiatives; foundational alignment surface for OAgents
- **IEEE** — Ethically Aligned Design (EAD), P7000 series (7000/7001/7002/7003/7007…), CertifAIEd. *(Note: IEEE 2089-2021 is age-appropriate-digital-services / online age verification — not general AI ethics; corrected per the `ieee-ead.md` survey finding.)*
- **OASIS** — AI / agent-related TCs as they spin up
- **IETF** — AI-related working groups (e.g., observability, security)
- **ISO/IEC** — JTC 1/SC 42 AI series (ISO/IEC 22989, 23053, 42001)
- **W3C** — adjacent semantic-web standards relevant to agent interop

**De-facto protocols (vendor-proposed, ecosystem-adopted):**

- **MCP** (Model Context Protocol) — Anthropic-proposed; tool/context interface
- **A2A** (Agent-to-Agent) — Google-proposed; agent interop
- **ANP** (Agent Network Protocol) — community proposal; agent-network identity + comms
- **OAuth Agent extensions** — IETF drafts for delegated-authority agents
- **Cap'n Proto / Protobuf** in agent-mesh contexts — protocol substrates as they get agent-specific extensions

## Out of scope

- Pure inference protocols (gRPC etc) without agent-specific extensions
- Cryptographic primitive standards (TLS, JWT) — relevant only if extended for agents
- Application-specific protocols (FHIR, FIX) — unless explicitly engaging agentic shape

## Per-entry shape

Standards efforts often span long periods with multiple deliverables (drafts, RFCs, ratified versions). The recommended shape:

```
{body-slug}/
├── README.md  (body overview + tracking)
└── {effort-slug}.md  (per-effort detail with timeline)
```

Or for single-effort tracking:

```
{body-slug}-{effort-slug}.md
```

## Sources to canvass per entry

- **Official working-group pages + drafts**
- **Public mailing list traffic** — direction-of-travel signal
- **Ratified deliverables + their dates**
- **Adoption signals** — which vendors / OSS frameworks reference the standard
- **Cross-body coordination** (e.g., NIST CAISI ↔ IEEE EAD overlap)

## AIDE-mapping anchor

Standards efforts map most cleanly to OAgents (which is explicitly NIST AI RMF-aligned) and to AEON's authority + evidence service planes. The mapping captures:

| Standard / protocol | AIDE construct / plane | Alignment status |
|---|---|---|
| NIST AI RMF | OAgents (explicit) + AEON authority plane | *AIDE ahead* — OAgents is a profile implementation; AIDE has the working spec |
| MCP | AEON capability plane + tool integration | *AIDE behind* on first-party MCP support; *AIDE ahead* on capability-composition semantics |
| A2A | AEON orchestration runtime + integration plane | *In flight elsewhere* — A2A overlaps with AEON inter-deployment integration; convergence question open |
| ... | | |

OAgents being NIST-AI-RMF-aligned gives the canon a specific *AIDE ahead* anchor in the formal-standards slice — worth surfacing in survey entries.

## Special considerations

**Versioning awareness.** Standards often have multiple concurrent versions in different adoption stages (draft / ratified / superseded). Each entry should be explicit about *which version* it analyzes; mark the version date, status, and successor reference (if any) at the top.

**Geographic specificity.** Some standards bodies are jurisdictionally bounded (US NIST, EU AI Act-adjacent work, UK AISI). Where geography is material to applicability, note it in the entry.

## Landed entries

Unlike the vendor/framework slices (where the verdict is "different altitude, compose-not-compete"), standards map by **alignment status** — the canon *aligns with*, *consumes*, *extends*, or *differentiates from* each.

| Entry | Standard / protocol | Alignment posture |
|---|---|---|
| [`nist-ai-rmf.md`](nist-ai-rmf.md) | NIST AI RMF (+ GenAI Profile, CAISI) | **AIDE ahead** — OAgents is an explicit RMF *profile* (working spec); CAISI Agent Interoperability Profile (Q4-2026) = converge frontier |
| [`iso-iec-sc42.md`](iso-iec-sc42.md) | ISO/IEC JTC1 SC42 (42001/22989/23053/23894) | **Consume-at-org-altitude, extend-below**; AIDE behind on certifiable AIMS maturity (42001 is the recognized standard) |
| [`eu-ai-act.md`](eu-ai-act.md) | EU AI Act (regulation, EU) | **Compliance-enabling** — AIDE *evidences* high-risk obligations; does not confer compliance |
| [`ieee-ead.md`](ieee-ead.md) | IEEE EAD / P7000 series / CertifAIEd | Complementary — AIDE ahead on runtime deontic envelope; behind on IEEE 7001 graded transparency taxonomy (catch-up target) |
| [`mcp.md`](mcp.md) | Model Context Protocol (Anthropic→AAIF) | **Consumed/convergent** — the canon rides MCP (α1 skills as MCP servers); ahead on envelope/authority over tool calls |
| [`a2a.md`](a2a.md) | Agent2Agent (Google→Linux Foundation) | Consume/extend at the interface; **differentiate at authority altitude** (AgentCard advertises, doesn't govern) |
| [`aicp.md`](aicp.md) | AICP — Agent Identity Card Protocol (Micah/Ologos, MIT) | **Ologos-family / converge** — identity-wire-below + governance-above; phase-gated tool projection aligns with envelope direction |
| [`anp.md`](anp.md) | Agent Network Protocol (community) | Emerging; ALIGN-candidate on decentralized (DID) identity; AIDE ahead on authority/governance |
| [`oauth-spiffe.md`](oauth-spiffe.md) | OAuth/OIDC · RFC 8693 · SPIFFE/SPIRE · IETF agent-delegation drafts | **Consumed/foundational substrate** — OrdSA ordinal authority builds above flat token delegation |
| [`otel-genai.md`](otel-genai.md) | OpenTelemetry GenAI semantic conventions (CNCF) | **Adopted + extended** — the canon's evidence-schema base (ADR-EA-0027 shared evidence object); extends with governance fields |

**The load-bearing finding:** OAgents being an explicit **NIST-AI-RMF profile** is the canon's strongest *AIDE-ahead* anchor in the whole survey — a working spec implementing the authoritative framework. And the canon already **consumes/adopts** the two settled de-facto wires (MCP, OTel-GenAI), so its position is "ride the interfaces, govern above them," not reinvent.

## Status

Scaffolding established 2026-05-22. **Ten standards/protocol entries landed 2026-06-01** (NIST AI RMF, ISO/IEC SC42, EU AI Act, IEEE EAD, MCP, A2A, AICP, ANP, OAuth/SPIFFE, OTel-GenAI). Slice is built out. *Watched, not yet entried* (emerging / thin agentic surface): OASIS AI TCs, W3C semantic-web-for-agents, Cap'n Proto/Protobuf agent-mesh extensions — add when they reach substantive agentic shape.
