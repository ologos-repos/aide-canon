# OSS framework — PydanticAI

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../../sota-survey/README.md). AIDE-mapping anchor per [`README.md`](README.md) ("AIDE-mapping anchor" — constructs + service planes). Cadence: **fast** (PydanticAI ships weekly point releases — treat version/feature specifics as a dated snapshot).

## 1. What it is

**PydanticAI** is the **typed agent framework** from the Pydantic team — "agents, the Pydantic way." Its organizing thesis is *schema-first, type-safe agent construction*: an agent is a first-class, fully type-annotated Python object whose **structured output is a Pydantic model** (JSON-Schema-constrained generation + validation, so the agent's return is *guaranteed* to satisfy a declared type), whose **tools** are decorated functions (`@agent.tool`) with auto-generated schemas and validated parameters, and whose runtime context is supplied through **type-safe dependency injection** (`RunContext` parameterized by `deps_type`). It moves whole classes of agent errors from runtime to write-time (IDE/type-checker catches them).

It is **model-agnostic** at the provider level (OpenAI, Anthropic, Gemini, DeepSeek, Grok, Cohere, Mistral, Perplexity, plus cloud and custom backends). Beyond the typed core it provides: a **graph** abstraction and **durable execution** (progress preserved across failures) for complex workflows; **MCP** (Model Context Protocol) integration for external tools/data; an **evals** harness for systematic performance testing; **human-in-the-loop tool approval** (flag a tool call as requiring approval before execution); and **observability via Pydantic Logfire**, the team's **OpenTelemetry**-grounded platform (tracing, cost tracking, evals-based monitoring — optional, and any OTel-compatible backend works in its place).

In aide-canon terms PydanticAI is a **Means-layer implementation substrate** — the build altitude AIDE explicitly is *not*. Its interest to the canon is a specific convergence: of all the surveyed frameworks, PydanticAI is the **closest in spirit to OAgents' schema-first, typed-object ethos** (see §3, §4).

## 2. Source links

- Official docs: `pydantic.dev/docs/ai/overview/` (formerly `ai.pydantic.dev`, 301-redirects), `pydantic.dev/docs/ai/`.
- Repository + releases: `github.com/pydantic/pydantic-ai` — **v1.104.0 (2026-05-29)** at survey time; v1.0 stable shipped 2025-09; ~16k+ GitHub stars by early 2026.
- Logfire (observability): `github.com/pydantic/logfire`, `pydantic.dev/docs/logfire/integrations/llms/pydanticai/` — `logfire.instrument_pydantic_ai()`, OpenTelemetry-based.
- PyPI: `pypi.org/project/pydantic-ai/` (and `pydantic-ai-slim` with the `logfire` optional group).
- In-canon prior research: the framework rows of [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md) (the `Agent`/`Skill`/`Tool` mapping discipline this entry inherits).

## 3. Map against AIDE

### Against the four AIDE constructs

| AIDE construct | PydanticAI equivalent | AIDE position |
|---|---|---|
| **OAgents** (typed agent envelope) | The **typed `Agent` + Pydantic structured output + typed tools/DI** — the most convergent surface in the field | *In flight elsewhere (most convergent)* on the **typed-object/schema discipline**; **AIDE ahead** on the **behavioral envelope** PydanticAI lacks (OAgents §10 — trust/governance *above any framework*) |
| **OrdSA** (O0–O6 authority) | (not addressed; human-in-the-loop tool approval is the nearest, but it is a gate, not an authority altitude) | **AIDE ahead** — ordinal authority-down / evidence-up is absent |
| **MxM** (5-surface harness) | Agent + tools + DI + graph compose an app, but there is no Morals/deontic surface and no harness-mode decomposition | *In flight elsewhere* — comparable component decomposition, different vocabulary; **AIDE ahead** on the Morals surface |
| **DEA** (deontic / enterprise architecture framing) | (none — PydanticAI is a build library, construct-unaware) | **AIDE ahead** — no architecture/governance altitude |

### Against the six AEON service planes

| AEON plane | PydanticAI equivalent | AIDE position |
|---|---|---|
| **Identity** | No agent-identity primitive (an `Agent` is a typed code object, not a principal with stable identity) | **AIDE ahead** — no principal-altitude identity model |
| **Authority** | RBAC/authority absent; human-in-the-loop tool approval is a per-call gate | **AIDE ahead** — OrdSA O0–O6 is absent |
| **Evidence** | **Logfire** — OpenTelemetry tracing, evals, cost/behavior monitoring | **AIDE behind** — Logfire is built + mature (and *OTel-grounded*, which the canon's evidence direction already targets); AIDE's evidence trail is emit-only spec |
| **Integration** | MCP support; broad model-provider integrations | *In flight elsewhere* — mature, convergent (MCP is the shared de-facto surface) |
| **Capability composition** | Tools + graph + durable execution + DI compose capability | *In flight elsewhere* — strong typed composition; but **no envelope-refinement composition law** (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | Graph + durable execution | *In flight elsewhere* / **AIDE behind** on realized runtime; *converging* via the workflow-orchestration pattern |

*(Inference is AEON's 7th plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md): PydanticAI is model-provider-agnostic at the integration level, but model-agnosticism is a config property, not a first-class **governance** property the way the Inference plane frames it.)*

### Vocabulary collision note

- **`Agent`** — PydanticAI's `Agent` is a **typed code object** that conducts LLM conversations with structured output. This is *closer* to the OAgents **`Agent`** primitive (a typed object) than most frameworks' "Agent" (which usually denotes an **AI-aide** — a persistent AI-under-principal, per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md), and must never be casually called "agent"). The DNA overlap is real (see §4) — but the OAgents `Agent` lives *inside a behavioral envelope*; PydanticAI's does not. **Flag:** do not read PydanticAI's `Agent` as the OAgents `Agent` outright — the typed-object layer matches, the envelope does not.
- **No `Skill` primitive.** PydanticAI bundles capability as tools + graphs + (informally) "capabilities"; there is no `Skill` first-class concept. Where peer frameworks expose a `Skill`, that surface maps to MxM **Means** — here there is simply nothing to map, which is itself a finding.
- **`Tool`** = atomic invocation (`@agent.tool`) — convergent across the field; same sense as the canon's `Tool`.
- **Entity discipline:** PydanticAI is an external OSS project; nothing here is conflated with the Ologos ecosystem or the NG-AIDE-01 instance, and no bare "fleet" usage applies.

## 4. Classification

**Mixed — "in flight elsewhere (most convergent on the typed axis)," at a different altitude.** As with every Means-layer framework, the comparison is per-axis, not global — aide-canon is a **governance corpus**, PydanticAI is a **build library**:

- **AIDE ahead** — the **behavioral envelope** (OAgents §10 names exactly this gap: a framework's "behavioral trustworthiness during execution is outside their scope"), **Authority** (OrdSA O0–O6), **Identity** (principal altitude), the **Morals/deontic surface** (MxM), and architecture/governance framing (DEA). PydanticAI has typed structure but no trust layer wrapping it.
- **AIDE behind** — **Evidence/observability** (Logfire is built, mature, and OTel-grounded), realized **orchestration runtime** (graph + durable execution), and — decisively — **adoption and the fact that it is a shipping, widely-used product** where AIDE is design-first with enforcement largely unbuilt.
- **In flight elsewhere (most convergent)** — the **typed-output / schema-first discipline**. This is the load-bearing, *interesting* finding: **OAgents' typed-`Agent`-in-an-envelope and PydanticAI's typed-agent share DNA.** Of all surveyed frameworks PydanticAI is the closest to OAgents' schema-first ethos — Pydantic-validated structured outputs and type-safe tools/DI are precisely the typed-object rigor OAgents asserts. The difference is the **envelope**: OAgents adds the behavioral/trust/authority layer *around* the typed object that PydanticAI structurally lacks.

**The synthesis:** they **compose, not compete** — and they compose *more naturally than most*, because the schema discipline already agrees. aide-canon is the governance layer one wraps *around* a PydanticAI build: PydanticAI's typed `Agent` as the OAgents `Agent`-object's natural substrate, Logfire as the Evidence/eval plane, with **OAgents' envelope + OrdSA authority + MxM Morals supplying the trust/governance the framework does not provide**. This is the OAgents §10 thesis made concrete on the framework whose typed core already half-meets it — the same canon-spec ↔ platform-substrate relationship documented with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/).

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (envelope over the convergent substrate).** Propagate the OAgents-envelope / OrdSA-authority position as the trust layer that sits *above* a typed-agent framework — PydanticAI is the *most favorable* example because its typed core already agrees with OAgents on schema discipline, so the envelope is the *only* missing piece. KR shape: a documented "govern-a-PydanticAI-build" mapping (OAgents `Agent`-object over PydanticAI's typed `Agent`; envelope + authority + Morals as the wrapper), exhibited as the cleanest typed-substrate worked example.
2. **Converge-or-differentiate (typed-object schema discipline).** Recognize PydanticAI as the SOTA convergence point on schema-first typing and articulate the OAgents differentiation explicitly. KR shape: a side-by-side spec showing OAgents' typed `Agent` ⊇ PydanticAI's typed agent + behavioral envelope — convergent on typing, differentiated by trust/authority.
3. **Catch-up (evidence tooling, OTel-grounded).** Logfire is mature and built on OpenTelemetry — the same evidence shape the canon's workflow-orchestration pattern already targets. KR shape: adopt OTel-GenAI as the canonical evidence object (cf. the workflow-orchestration shared evidence object) and demonstrate Logfire-grade trace/eval/cost observability on an AIDE exemplar.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime) against PydanticAI **v1.104.0** (2026-05-29). Revisit on the next PydanticAI major shift (point releases are weekly — watch for any identity/authority/trust surface, which would move the *AIDE-ahead* envelope axis) or at OKR refresh.
