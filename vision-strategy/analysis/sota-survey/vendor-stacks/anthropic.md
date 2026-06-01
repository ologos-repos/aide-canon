# Vendor stack — Anthropic (Claude)

> SOTA-survey finding. Shape per [`../README.md`](../README.md) → [`sota-survey/README.md`](../../sota-survey/README.md). Cadence: **fast** (Anthropic ships and rebrands frequently — "API" → "Claude Developer Platform"/"Claude Platform"; product surface names below are a dated snapshot, not a fixed spec). **Entity note:** this entry surveys *Anthropic the vendor/substrate*. Two canon exemplars — [Claude Code Workflow](../../exemplar-tracking/claude-code-workflow/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/) — are *built on* Anthropic models but are **not** Anthropic products in the canon sense; the canon, OAgents, OrdSA, and AIDE are all independent of Anthropic. Keep that distinction sharp throughout.

## 1. What it is

**Anthropic / Claude** is, in aide-canon terms, two things at once: the **Inference-plane substrate** for the canon's own working exemplars, and a fast-maturing **Means-layer agent stack**. It is *not* a governance corpus. The 2026 surface composes roughly seven products:

- **Claude (Enterprise / Team / Pro plans)** — the hosted assistant + admin tier: SSO/SAML, RBAC, role-scoped connector permissions, group spend limits, usage analytics, audit. The enterprise governance plumbing of running Claude in an org.
- **Claude Developer Platform** (rebrand of "the Claude API"; `platform.claude.com`) — frontier models + the build surface for apps and agents.
- **Claude Agent SDK** — "the same tools, agent loop, and context management that power Claude Code, programmable in Python and TypeScript." The agent-construction primitive.
- **Claude Skills** (`SKILL.md`) — a folder of instructions + scripts + resources with YAML frontmatter (`name`, `description`), loaded on demand via **progressive disclosure**. Anthropic's contract for "teach the model how to do a repeatable specialized task."
- **Claude Code** — the agent harness (CLI + IDE); also the substrate that the **Claude Code Workflow** exemplar's deterministic JS orchestration runs on.
- **Cowork** (GA on all paid plans, 2026) — Claude Code-class power for knowledge work; bundles skills, connectors, and **sub-agents** (ephemeral parallel workers; "Dynamic Workflows" plans/runs hundreds of parallel sub-agents in a session, research preview).
- **MCP (Model Context Protocol)** — Anthropic's open connect-the-model-to-tools standard (donated to the Linux Foundation's Agentic AI Foundation, Dec 2025; 10k+ public servers; de-facto industry standard).
- **Claude Managed Agents** (public beta) — composable cloud-hosted-agent APIs: sandboxed execution, checkpointing, credential management, scoped permissions, end-to-end tracing; self-hosted-sandbox option.

Anthropic's own field articulation of how these layer is the cleanest in the field and worth citing verbatim: **"skills are instructions, MCP servers are connections, plugins are commands"** (skills = how-to loaded on demand; MCP = transport to external tools; plugins = the installable bundle of skills/MCP/hooks/commands). That tripartite split is a genuine SOTA contribution at the Means altitude.

The enterprise value proposition is **frontier inference + a coherent agent-build stack (SDK / Skills / MCP / Managed Agents) + enterprise plumbing (SSO, RBAC, audit, spend control)**. It is a **Means-layer substrate + inference provider** — the altitude AIDE explicitly is *not* — and, distinctively, the substrate the canon's *own* exemplars are demonstrated on.

## 2. Source links

- Official: `claude.com`, `platform.claude.com/docs` (Claude Developer Platform / API), `code.claude.com/docs` (Claude Code + Agent SDK), `platform.claude.com/docs/en/agents-and-tools/agent-skills/overview` (Skills / `SKILL.md`), `claude.com/product/cowork`, `platform.claude.com/docs/en/managed-agents/overview`, `modelcontextprotocol.io` + `github.com/modelcontextprotocol` (MCP spec), `github.com/anthropics/skills` (open Skills repo).
- Skills/MCP/plugins framing: Anthropic engineering, *"Equipping agents for the real world with Agent Skills"* and *"Code execution with MCP"* (`anthropic.com/engineering/...`).
- In-canon prior research: the Anthropic/Claude rows of [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md); the workflow-orchestration reference impl in [`../../exemplar-tracking/claude-code-workflow/`](../../exemplar-tracking/claude-code-workflow/); the operator-altitude AIDEX impl in [`../../exemplar-tracking/thinx-aidex/`](../../exemplar-tracking/thinx-aidex/).
- (Product naming is **rebrand-prone** — "Claude API" → "Claude Developer Platform" → "Claude Platform"; surfaces fold into one another (Cowork ⊃ sub-agents; Managed Agents ⊃ sandboxing). Verify surface names at read time.)

## 3. Map against AIDE

### Against the four AIDE planes

| AIDE plane | Anthropic / Claude equivalent | Position |
|---|---|---|
| **Control** (AEON governance) | Enterprise RBAC + role-scoped connector permissions + Managed-Agents scoped permissions/tracing — but **no authority/trust governance layer** | *AIDE ahead* on governance; *behind* on operability |
| **Runtime** | **Claude Agent SDK / Claude Code / Managed Agents** — agent loop, sandboxes, checkpointing, the substrate the canon's exemplars run on | *In flight elsewhere* (deep overlap) / *AIDE behind* on realized runtime |
| **Experience** (AIDEX) | Cowork + Claude apps (a *power-user/builder* UX) — and, built on the substrate, [thinx-aidex](../../exemplar-tracking/thinx-aidex/) as the operator-as-curator console | *AIDE ahead* on the **operator-as-curator** model (HCAE) — but the canon's own AIDEX exemplar runs *on* Anthropic |
| **Capability** (OAAD) | Skills + MCP tool ecosystem | *In flight elsewhere* / **convergent** — the canon **adopts `SKILL.md` verbatim** (NG-AIDE-01 α1) |

### Against the six AEON service planes

| AEON plane | Anthropic / Claude equivalent | AIDE position |
|---|---|---|
| **Identity** | Plan auth / SSO / SAML; org + role identity | *In flight elsewhere* — identity primitives exist, no principal-altitude model |
| **Authority** | RBAC, scoped permissions, connector-per-role controls; **no ordinal authority concept** | **AIDE ahead** — OrdSA O0–O6 authority-down/evidence-up is absent |
| **Evidence** | Managed-Agents end-to-end tracing; Agent SDK run context; Cowork analytics/audit | **AIDE behind** on built tracing; *converging* on the OTel-GenAI evidence shape the canon's exemplars already emit |
| **Integration** | **MCP** — the de-facto standard, LF-governed, 10k+ servers | **AIDE behind / convergent** — the canon consumes MCP rather than competing; MCP is the integration substrate |
| **Capability composition** | Skills (progressive disclosure) + sub-agents + Managed-Agents composition | *In flight elsewhere* — strong; but no **envelope-refinement** composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)); the [Claude Code Workflow](../../exemplar-tracking/claude-code-workflow/) exemplar realizes the determinism gate fully but the `⊑` lattice only partially |
| **Orchestration runtime** | Cowork sub-agents / Dynamic Workflows / Claude Code Workflow tool | **AIDE behind** on realized runtime; *converging* via the workflow-orchestration pattern (the Workflow tool is the canon's reference impl) |

*(Inference is AEON's 7th plane, [ADR-EA-0015](../../../../decisions/ADR-EA-0015-introduce-inference-plane.md): Anthropic **is** an Inference-plane option — and the one the canon's exemplars actually use. But because OAgents is model-agnostic, Anthropic is **one** Inference-plane substrate, not the canon. Model-agnosticism is a first-class **governance** property here in a way no single-vendor stack frames it — the canon's exemplars run on Anthropic *by selection*, not by binding.)*

### Vocabulary collision (flag at every read)

Per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md), never use the casual "agent" for an AI system under a principal — that is the canon's **AI-aide**. Anthropic's **"agent"** (Agent SDK / Managed Agents / sub-agents) is the field-casual sense and maps to canon **AI-aide**, **not** the OAgents **`Agent`** primitive (a *typed object inside a behavioral envelope*). Anthropic's **`Tool`** = atomic invocation (convergent across the field; canon-aligned). Anthropic's **Skill** (`SKILL.md`) maps to MxM **Means** — and here the relationship is unusually tight: **the canon adopts the `SKILL.md` contract verbatim** (NG-AIDE-01 α1, route → skill → generator, progressive disclosure, template-first), so this is convergence-by-adoption, not collision. **Cowork sub-agent** = ephemeral parallel worker (an AI-aide spawned per-limb, not a standing principal). Flag all four mappings at read time.

## 4. Classification

**Mixed — heavier on "in flight / convergent" than other vendors, at a different altitude, plus a cited exemplar relationship.** aide-canon and the Anthropic stack are *different categories* — a **governance/architecture corpus** vs a **Means-layer substrate + inference provider** — so the classification is per-axis, and uniquely entangled because the canon's own exemplars run on this substrate:

- **AIDE ahead** — Authority (OrdSA O0–O6; absent here), the behavioral-envelope / trust layer (OAgents, which §10 of the spec frames as sitting *"above any framework"* — Anthropic's stack is a mature substrate whose per-execution behavioral-trustworthiness governance is out of its own scope), deontic constraints (MxM Morals), HCAE operator-as-curator experience, and vendor-neutral conformance criteria.
- **AIDE behind** — realized runtime (Agent SDK / Claude Code / Managed Agents), built tracing/evidence, enterprise plumbing (SSO/RBAC/audit/spend), and — decisively — **frontier inference, adoption, funding, and the fact that this is the shipping substrate the canon itself runs on**, where AIDE is design-first research with enforcement largely unbuilt.
- **In flight elsewhere / convergent** — Skills (`SKILL.md` **adopted verbatim**), MCP (**consumed** as the integration standard, not contested), orchestration (Claude Code Workflow **is** the workflow-orchestration reference impl), Inference (Anthropic is a selected Inference-plane option, ADR-EA-0015).

**The synthesis:** they **compose, not compete** — and more intimately than any other vendor in this slice. The canon is the governance layer wrapped *around* an Anthropic-substrate deployment: Claude Code / Agent SDK / Managed Agents as the Means/runtime, MCP as the Integration plane, `SKILL.md` as the Means/capability contract — with OAgents' envelope + OrdSA authority + MxM Morals supplying the trust/governance the substrate structurally lacks. The proof is already in-tree: [Claude Code Workflow](../../exemplar-tracking/claude-code-workflow/) (workflow-orchestration reference impl, on Anthropic) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/) (operator-altitude AIDEX, on Anthropic) are the canon-spec ↔ substrate relationship made concrete. **Critically: that the exemplars run on Anthropic does not make AIDE/OAgents/OrdSA Anthropic artifacts — the substrate is selected and replaceable; the governance is the canon's own.**

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (governance lead).** Propagate the OAgents-envelope / OrdSA-authority / MxM-Morals position as the trust layer that sits *above any substrate* — the Anthropic stack is the canonical example of a mature, fast-moving substrate with no ordinal-authority or behavioral-envelope governance of its own. KR shape: a documented "govern-an-Anthropic-deployment" mapping (envelope + authority + Morals over Agent SDK / Managed Agents / MCP), with the two existing exemplars cited as proof.
2. **Catch-up + converge (evidence / orchestration).** Managed-Agents tracing and the Claude Code Workflow run journal are ahead of AIDE's *designed* evidence trail. KR shape: hold the OTel-GenAI evidence object as the canonical shape (already begun — workflow-orchestration shared evidence object) and close criterion-2/5/7 gaps the Claude Code Workflow exemplar surfaces (the enforceable `envelope(child) ⊑ envelope(parent)` lattice and FK-aggregated evidence).
3. **Converge-by-adoption (Skills / MCP).** Keep the canon's `SKILL.md`-verbatim adoption (α1) and MCP-as-Integration-substrate posture explicit — differentiation is *not* on the capability/integration contract (the canon consumes Anthropic's), it is on the governance envelope wrapped around it. KR shape: ratify the `SKILL.md`-as-Means contract and an MCP-as-Integration-plane ADR so the convergence is canon-recorded, not implicit.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Cross-references the [Claude Code Workflow](../../exemplar-tracking/claude-code-workflow/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/) exemplar trackers (both on Anthropic substrate) and inherits the Anthropic/Claude vocabulary mapping ([`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md)). Revisit on the next Anthropic product shift (rebrand-prone — SDK/Platform/Managed-Agents surfaces fold rapidly) or at OKR refresh.
