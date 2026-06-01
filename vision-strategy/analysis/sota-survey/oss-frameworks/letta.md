# OSS framework — Letta (formerly MemGPT)

> SOTA-survey finding. Shape per [`README.md`](README.md) → [`sota-survey/README.md`](../README.md). Mapping anchor: the **constructs + six-plane** pattern declared in [`README.md`](README.md) (differs from `vendor-stacks/`, which compares against planes alone). Cadence: **fast** (Letta ships near-weekly; product names are moving — treat surface specifics as a dated snapshot).

## 1. What it is

**Letta** is the open-source framework for **stateful agents** — AI-aides with self-managing, persistent memory — built by the UC Berkeley team behind the 2023 **MemGPT** paper (which framed an LLM as a process on a memory-constrained "operating system," paging information between a context window and external storage). The project rebranded MemGPT → Letta as it generalized from a memory technique into a full agent framework, and is operated by Letta, Inc. (founders Charles Packer and Sarah Wooders).

Its defining opinion is that **memory persistence is a first-class default, not an add-on retrieval pipeline**. The agent itself edits its own memory via tools rather than relying on an external RAG layer. The realized mechanics:

- **Memory blocks** — labeled, structured segments (e.g. `human`, `persona`) pinned to the context window, always visible to the agent, editable, and shareable between agents.
- **Core memory vs. archival/recall memory** — core memory is the in-context working set ("RAM"); archival/recall memory is external storage ("disk"). The agent pages data between them, creating an illusion of unbounded memory inside a fixed window.
- **Self-editing memory** — built-in tools (`memory_replace`, `memory_insert`, `memory_rethink`) let the agent autonomously rewrite its own memory; "sleep-time compute" lets it reflect/self-improve between turns.
- **Agent File (`.af`)** — an open serialization format packaging a stateful agent's full state (system prompt, editable memory blocks, tool code + schemas, LLM settings, message history with an `in_context` flag) so an agent can be checkpointed, version-controlled, and shared across compatible frameworks.
- **Surfaces** — REST **Letta API**, `letta-client` Python + TypeScript SDKs, the **ADE** (Agent Development Environment) for inspecting/editing agent memory, and the newer **Letta Code** CLI/runtime (Dec 2025) moving memory toward git-backed "**Context Repositories**" (Feb 2026) and filesystem-based operations.

In aide-canon terms Letta is a **Means-layer execution substrate** — and, specifically, a **memory-substrate specialist**. It is the altitude AIDE explicitly is *not*, but it occupies ground that overlaps the canon's memory construct more directly than any other framework surveyed.

## 2. Source links

- Official: `letta.com`, `docs.letta.com` (core-memory, agent-file, research-background concepts), the model leaderboard at `leaderboard.letta.com`.
- GitHub: [`letta-ai/letta`](https://github.com/letta-ai/letta) (Apache-2.0, Python; ~23k stars, 100+ contributors, 170+ releases; v0.16.8 on 2026-05-14 at survey time) and [`letta-ai/agent-file`](https://github.com/letta-ai/agent-file) (the `.af` spec).
- Direction-of-travel: Letta blog — "Our next phase" (Letta Code as the memory-first agent; client-side execution; deprecation of legacy templates/server-side MCP/tool-rules by mid-Apr 2026), "Agent Memory," "Memory Blocks."
- Origin: MemGPT (Packer et al., 2023, UC Berkeley — cross-reference [`../academic/`](../academic/) when that slice lands).
- Funding signal: $10M seed (Felicis-led, ~$70M post, Sept 2024) — a single-firm-backed startup, not a hyperscaler.

## 3. Map against AIDE

### Against the AIDE constructs

| AIDE construct | Letta equivalent | AIDE position |
|---|---|---|
| **DEA** (digital enterprise architecture) | (no enterprise-architecture surface — Letta is a single-agent-memory framework, not an org-altitude model) | **AIDE ahead** — DEA's enterprise-altitude framing has no Letta analogue |
| **OrdSA** (O0–O6 ordinal authority) | (none — no authority-altitude or authority-down/evidence-up concept) | **AIDE ahead** — authority altitudes are absent |
| **MxM** (5-surface harness: Mission/Mind/Morals/**Memory**/Methods) | The **Memory** surface is realized in depth (blocks, core/archival, self-edit, `.af`); other surfaces are implicit at best | **In flight elsewhere / AIDE behind on the Memory slice** — see synthesis |
| **OAgents** (typed agent envelope + trust "above any framework," §10) | Agents are concrete runtime objects with state; no behavioral-envelope or execution-trust contract | **AIDE ahead** — OAgents' envelope/trust layer is exactly the "above any framework" slot Letta does not occupy |

### Against the six AEON service planes

| AEON plane | Letta equivalent | AIDE position |
|---|---|---|
| **Identity** | Agent instances have stable IDs + persistent state; no principal-altitude / under-principal model | *In flight elsewhere* — identity primitives exist, no principal model |
| **Authority** | (none — RBAC/authority not a concept) | **AIDE ahead** — OrdSA O0–O6 has no Letta analogue |
| **Evidence** | Message history with `in_context` flags; ADE inspection; model leaderboard for eval | *In flight elsewhere* — observable memory state, but no first-class trace/eval/audit plane |
| **Integration** | Tool ecosystem, MCP support (server-side being deprecated → client-side), SDKs | *In flight elsewhere* — capable, narrower than general orchestration frameworks |
| **Capability composition** | Tools, skills, subagents; shared memory blocks across agents | *In flight elsewhere* — composition via shared memory; no envelope-refinement composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | Letta API server / Letta Code runtime; stateful agents-as-a-service | *In flight elsewhere* — persistent runtime, but memory- not orchestration-centric |

*(Inference is AEON's 7th plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md): Letta is model-agnostic at the integration level — a stated design goal — but model-agnosticism is not framed as a first-class **governance** property the way the Inference plane is.)*

### Vocabulary collision

Letta's **"agent"** = a stateful runtime AI-aide with persistent memory and tools — this is the canon's **AI-aide** ([ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)), **not** the OAgents **`Agent`** primitive (a typed object inside a behavioral envelope). Use **AI-aide** for the AI-under-principal, never the casual "agent." Letta's **"skills"** (e.g. web search / fetch packaged for the agent) map to MxM **Means**; **"tool"** = atomic invocation (convergent across the field). Letta's **"memory block"** is the live collision worth flagging: it is a *realized* mechanism that overlaps the canon's **memory construct** / MxM **Memory** surface — same conceptual ground, different (and here, more-built-out) vocabulary. This collision is the load-bearing one for this entry and is logged in [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md).

## 4. Classification

**Per-axis, at a different altitude — with one honest inversion.** aide-canon is a **governance corpus**; Letta is a **memory-substrate framework**. They sit at different altitudes, so the classification is per-axis, not global:

- **AIDE ahead** — Authority (OrdSA O0–O6; Letta has none), the behavioral-envelope / execution-trust layer (OAgents §10's "above any framework" slot, which Letta does not occupy), deontic constraints (MxM Morals), and enterprise/DEA altitude framing.
- **In flight elsewhere / convergent** — the **MxM Memory surface and the canon's memory construct**. This is where AIDE and Letta occupy the *same* ground: persistent, self-editing, paged agent memory. AIDE's memory work is genuinely convergent with Letta's direction.
- **AIDE behind (the honest inversion)** — on **realized memory-persistence mechanics specifically**, Letta is plausibly *ahead*. Memory blocks, core↔archival paging, self-editing tools, and the `.af` portable-agent format are *shipping, adopted, version-1x mechanics*; the canon's memory construct is more design/spec than realized substrate. This is the one framework in the survey where AIDE may be **behind on a core surface (Memory)** — and saying so is the calibrated call. It does **not** generalize: Letta is behind on everything the canon is built for (authority, envelope, governance).

**The synthesis:** they **compose, not compete**, but on a *specific* seam. Letta is the strongest candidate for the **Means-layer memory substrate** *underneath* the canon's memory construct — the realized RAM/disk paging engine that an AIDE deployment governs (via OAgents envelope + OrdSA authority + MxM Morals/Mind) rather than reimplements. The `.af` format is the concrete interop seam: a portable, version-controllable agent-state artifact the canon's Memory surface could adopt or map to. This is the same canon-spec ↔ platform-substrate relationship the canon already documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/) — but here the substrate is *ahead on its specialty*, which sharpens the Objective.

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Catch-up (memory realization — the headline).** Letta's memory mechanics are materially ahead of the canon's memory construct on *realized* persistence. **Objective:** *Make the canon's Memory surface as operationally real as Letta's, while keeping it governed.* KR shape: a documented mapping of memory-blocks / core↔archival / self-editing tools / `.af` onto the MxM Memory surface, plus a demonstrated AIDE exemplar that pages persistent memory at Letta-grade fidelity (candidate: adopt or interop with `.af` rather than inventing a parallel format).
2. **Defend-and-extend (governance over memory).** Letta has no authority, envelope, or deontic layer over its memory. **Objective:** *Position OAgents-envelope + OrdSA-authority + MxM Morals as the trust/authority layer that governs a memory substrate Letta cannot govern itself.* KR shape: a "govern-a-Letta-deployment" mapping (who may read/edit which memory blocks, at which authority altitude, under which Morals) — the OAgents §10 thesis made concrete on a memory framework.
3. **Converge-or-differentiate (portable agent state).** The `.af` format is becoming a de-facto portable-agent-state artifact. **Objective:** *Decide whether the canon's Memory/Digital-Thread surface converges on `.af` or differentiates.* KR shape: an explicit canon position on `.af` interop vs. an envelope-aware superset (cross-reference [ADR-EA-0027](../../../../decisions/ADR-EA-0027-introduce-workflow-orchestration-pattern.md) shared-evidence-object work for the precedent of adopting an external shape).

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Snapshot pins: Letta `letta-ai/letta` v0.16.8 (2026-05-14), Letta Code (Dec 2025) → Context Repositories (Feb 2026) direction. Revisit on the next Letta surface shift (fast cadence; client-side / git-backed-memory pivot in progress) or at OKR refresh.
