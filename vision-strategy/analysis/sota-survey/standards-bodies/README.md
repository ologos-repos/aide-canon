# standards-bodies/

Survey of formal standards efforts and de-facto protocols shaping the agentic-AI ecosystem.

## In scope

**Formal standards bodies:**

- **NIST** — AI RMF + CAISI initiatives; foundational alignment surface for OAgents
- **IEEE** — Ethically Aligned Design (EAD), P7000 series, IEEE 2089-2021
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

## Status

Scaffolding established 2026-05-22. First standards entries land in subsequent PRs.
