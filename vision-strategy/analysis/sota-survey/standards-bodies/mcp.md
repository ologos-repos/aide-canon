# Standards / protocol — MCP (Model Context Protocol)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Slice cadence: **slow** (de-facto protocol with a now-formal governance body and dated spec releases — treat version specifics as a dated snapshot).

## 1. What it is

> **Version / status header.** Analyzed version: **MCP `2025-11-25`** — the current **stable** specification (authoritative TypeScript schema, JSON-RPC 2.0 base protocol, stateful connections, server/client capability negotiation). Successor: **`2026-07-28`** — a **release candidate** announced 2026-05-21, scheduled to ship final 2026-07-28, adding a stateless protocol core, an Extensions framework, Tasks, MCP Apps, authorization hardening, and a formal deprecation policy. **Governance:** Anthropic donated MCP to the **Agentic AI Foundation (AAIF)**, a directed fund under the **Linux Foundation** (announced 2025-12-09); a formal governance model (Working/Interest Groups, succession + amendment procedures) and an open **MCP Registry** (preview 2025-09) are in place. This entry analyzes `2025-11-25` and flags `2026-07-28` deltas where material.

**MCP** is an open protocol — Anthropic-proposed (late 2024), now broadly adopted across vendor stacks and OSS frameworks — that standardizes how an LLM application connects to external context, data, and tools. It defines a three-role topology over **JSON-RPC 2.0**: **Hosts** (the LLM application that initiates connections), **Clients** (connectors inside the host), and **Servers** (services exposing context and capabilities). The protocol is a **wire interface**, not a governance corpus or a runtime — it standardizes the *integration seam* between a model-bearing application and the capabilities it consumes, taking explicit inspiration from the Language Server Protocol's "write-once, integrate-everywhere" model for IDEs.

Its surface is a small, fixed set of primitives. **Servers** offer **Resources** (context/data for user or model), **Prompts** (templated messages/workflows), and **Tools** (functions the model executes). **Clients** may offer back to servers **Sampling** (server-initiated recursive LLM calls), **Roots** (server inquiries into the URI/filesystem boundaries it may operate in), and **Elicitation** (server-initiated requests for additional user input). Utilities (progress, cancellation, logging, error reporting) round out the base protocol. Notably, the spec is explicit that it **cannot enforce its own security principles at the protocol level** — consent, tool-safety, and sampling controls are delegated to the host implementation. In aide-canon terms, MCP is an **Integration-plane wire standard the canon *consumes*** — the transport over which governed capability is exposed, not the governance of that capability.

## 2. Source links

- Official spec (stable): `modelcontextprotocol.io/specification/2025-11-25` (base protocol, server features, client features, security & trust).
- Release candidate: MCP blog, "The 2026-07-28 MCP Specification Release Candidate" (`blog.modelcontextprotocol.io`); "The 2026 MCP Roadmap" (transport scalability, agent communication, governance maturation, enterprise readiness).
- Governance: "MCP joins the Linux Foundation" (GitHub Blog, 2025-12-09 — donation to the Agentic AI Foundation); MCP Registry preview (2025-09) — open catalog + API for server discovery, public + private sub-registries.
- Schema / repo: `github.com/modelcontextprotocol/modelcontextprotocol` (authoritative `schema.ts`).
- In-canon prior research: the MCP rows of [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md) — MCP appears there as a **Means-surface** integration in the Hermetic mapping ("Tool registry + MCP integration + capability tags", line 71) and is listed among the standards/protocols still to be column-mapped (line 222). This entry supplies the canon-vocabulary collision analysis that map row will inherit.

## 3. Map against AIDE

### Against OAgents + the relevant AEON service planes

MCP touches two AEON planes squarely — **Integration** (it *is* the wire) and **Capability composition** (it carries the capability invocations) — plus the OAgents primitive boundary.

| AIDE construct / plane | MCP equivalent | Mapping type | AIDE position |
|---|---|---|---|
| **AEON Integration plane** | The MCP wire itself — JSON-RPC 2.0, Host/Client/Server topology, capability negotiation, transport | **synonym** (at the seam) | *In flight elsewhere → convergent/adopted* — the canon **CONSUMES** MCP as its integration wire; no competing transport authored |
| **AEON Capability-composition plane** | Tools / Prompts / Resources as the exposed capability surface | **partial** | **AIDE ahead** on *semantics* — MCP carries atomic capability invocations; it has no envelope-refinement / authority composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **AEON Authority plane** (OrdSA O0–O6) | (none — security/consent delegated to the host; "cannot enforce at the protocol level") | **N/A** | **AIDE ahead** — MCP has no ordinal authority concept; an MCP server enforcing **fail-closed principal+session** is the canon layered *over* MCP, not in it |
| **AEON Identity plane** | Host/Client/Server roles; `2026-07-28` adds authorization hardening | **partial** | **AIDE ahead** on principal-altitude; MCP identifies connectors, not principals |
| **OAgents `Agent`** (typed object in a behavioral envelope) | (none — MCP has Tools/Prompts/Resources, **no first-class Agent noun**) | **N/A** | **AIDE ahead** — MCP is a tool/context wire; the agent abstraction lives above it |
| **MxM Means** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) | MCP Tools (and the server registry) | **nested** | Convergent — MCP is a Means-surface integration the canon adopts |
| **AEON Inference plane** ([ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md)) | Sampling (server-initiated recursive LLM calls) | **partial** | *Orthogonal axis* — Sampling routes an inference *call*; the Inference plane governs *which model serves a principal*, a property MCP does not frame |

### Vocabulary collision (canon-vocabulary-map discipline)

MCP's surface nouns are **Tools / Prompts / Resources** (server) and **Sampling / Roots / Elicitation** (client). The load-bearing collision is by **absence**: MCP has **no first-class `Skill`, `Agent`, or `Capability` noun**. This is exactly what the canon vocabulary map already records for the field:

- MCP **`Tool`** = atomic invocation → maps to canon **MxM Means** / the OAgents `Tool` (convergent across the field; the vocab map tags *AI tool* → AI-aide as **orthogonal**, line 135 — Tool is what an AI-aide *uses*, not the role-class).
- MCP has **no `Agent` noun** → so no collision with the casual "agent" trap (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md), the canon reserves *agent* for the OAgents-conformant typed-object primitive and uses **AI-aide** for the role-class; the vocab map tags casual *AI agent* → AI-aide as **orthogonal**, line 132). An MCP server is consumed *by* an AI-aide's agent; it is not itself an agent.
- MCP has **no `Skill` / `Capability` noun** → the canon's **Skill** (a packaged, principal-scoped capability under an authority envelope) has **N/A** in MCP's vocabulary. This is the precise gap the canon fills: NG-AIDE-01 α1 skills ship **as MCP servers**, so the *Skill* semantics are layered onto an MCP `Tool`-bearing server, not present in MCP itself.

This absence is itself the *AIDE-ahead* signal (per the vocabulary map's operating principle: a canon concept with no clean external equivalent is a lead, not a deficiency). It is recorded here so the MCP column added to [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md) inherits the discipline.

## 4. Alignment classification

**Convergent / adopted — the canon CONSUMES MCP at a lower altitude than it governs.** MCP is **not a competitor**: it is *the wire the canon rides*. The classification is per-axis (relate-by, per the standards framing: ALIGN / CONSUME / EXTEND / DIFFERENTIATE):

- **CONSUME (Integration).** MCP is the canon's adopted integration wire. NG-AIDE-01 α1 skills **ship as MCP servers**; the AIDEX α5 specialist seam **exposes skills via MCP**. The canon writes no rival transport — *in flight elsewhere, and the canon aligns onto it*.
- **EXTEND (Capability-composition + Authority).** **AIDE ahead** on the capability-composition *semantics* layered over MCP tool calls — **envelope-refinement, OrdSA authority (O0–O6), principal+session binding**. MCP defines the call; it explicitly cannot enforce consent/authority at the protocol level. **An MCP server that enforces fail-closed principal+session is exactly the α1 pattern** — the canon's contribution sits *above* the MCP `Tool` invocation, not beside it.
- **DIFFERENTIATE (vocabulary).** MCP has Tools/Prompts/Resources but **no Skill/Agent/Capability noun**. The canon supplies those nouns (and their authority semantics) and maps MCP's surface into MxM Means — differentiation by *altitude*, not by overlap.
- **ALIGN (governance trajectory).** MCP's move to the Linux Foundation / AAIF and its open Registry are convergent with the canon's vendor-neutral-standard posture; the canon tracks the registry as the discovery surface for the MCP servers its skills publish to.

**The synthesis.** MCP and aide-canon **compose, not compete** — and at *different altitudes*, the same shape the [LangChain entry](../vendor-stacks/langchain.md) reaches. MCP is the **Integration-plane wire**; the canon supplies the **Capability-composition + Authority semantics** that ride over it. The canonical realization is *"an MCP server enforcing fail-closed principal+session"* — an α1 skill that is simultaneously a conformant MCP server (so any MCP host can consume it) and a governed capability (so it refuses outside its principal's authority). MCP gives the canon reach across the entire MCP-host ecosystem **for free**; the canon gives MCP servers the authority layer the protocol structurally declines to enforce. On OrdSA authority-altitude the canon is unambiguously **ahead**: MCP operates at the call-transport altitude and delegates all O0–O6 authority to the host — there is no authority layering in the protocol to be behind on.

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (governed-MCP-server as the α1 exemplar).** Propagate "an MCP server enforcing fail-closed principal+session" as the canon's capability-composition position — the authority + envelope layer that sits *above* any MCP tool call. KR shape: a documented, conformance-checkable "governed MCP server" profile (envelope-refinement + OrdSA authority + principal+session) demonstrated on an NG-AIDE-01 α1 skill that is simultaneously a valid MCP server.
2. **Converge-and-adopt (ride the wire).** MCP is the integration substrate; the canon commits to it rather than authoring a rival. KR shape: NG-AIDE-01 α1 skills published as MCP servers and the AIDEX α5 specialist seam exposing skills via MCP, both tracked against the MCP Registry and the `2026-07-28` spec deltas (stateless core, Tasks, MCP Apps, auth hardening).
3. **Differentiate-by-vocabulary (close the noun gap, in the open).** MCP has no Skill/Agent/Capability noun; the canon does. KR shape: add the MCP column to [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md) recording Tool→Means and the Skill/Agent/Capability **N/A** rows, and publish the mapping so MCP-ecosystem adopters can locate the canon's authority semantics as the layer they're missing.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Analyzes MCP `2025-11-25` (stable); flags `2026-07-28` (release candidate, announced 2026-05-21) as the tracked successor. Revisit on the `2026-07-28` final ship, on a major MCP Registry / AAIF governance shift, or at OKR refresh.
