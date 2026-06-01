# Vendor stack — AWS (Bedrock + AgentCore)

> SOTA-survey finding. Shape per [`../README.md`](../README.md) → [`sota-survey/README.md`](../../sota-survey/README.md). Cadence: **fast** (AWS ships and renames agent surfaces on the re:Invent cycle — treat product specifics as a dated snapshot, not a fixed spec).

## 1. What it is

The **AWS agentic stack** is the *build-and-run* substrate for AI-aides on AWS — not a governance corpus. As of the October–December 2025 GA wave it is organized around a few surfaces:

- **Amazon Bedrock** — the managed foundation-model plane (Anthropic Claude, Amazon Nova, Meta Llama, Mistral, and others) plus inference, guardrails, and knowledge bases.
- **Amazon Bedrock AgentCore** — the GA (Oct 2025) managed agent platform, deliberately framework- and model-agnostic ("any framework, any model, any protocol"). It is a *set of modular services usable together or independently*: **Runtime** (serverless, session-isolated, 8-hour windows, MCP + A2A), **Gateway** (turns APIs/Lambda/services into MCP tools), **Identity** (agent identity + inbound/outbound auth + token vault), **Memory** (short/long-term, now episodic), **Observability** (OTEL-compatible, CloudWatch-backed), **Code Interpreter** + **Browser** (sandboxed capability), and — added at re:Invent 2025 — **Policy** (Cedar/natural-language deterministic guardrails), **Evaluations**, **Registry** (governed agent/tool/skill catalog), and **Payments** (x402).
- **SageMaker AI / SageMaker Unified Studio** — the ML/data development environment (training, tuning, deployment) with agentic Amazon Q Developer chat integrated (Unified Studio GA Mar 2025).
- **Amazon Q** — **Q Developer** (agentic coding/dev assistant, CLI + IDE) and **Q Business** (enterprise RAG assistant over org data).
- **Amazon Nova** / **Nova 2** (GA, re:Invent 2025), **Nova Act** (browser-automation model, GA), and the **Strands Agents SDK** — AWS's open-source model-driven agent SDK (Python + TypeScript-in-preview), the recommended authoring layer that deploys onto AgentCore Runtime.

The enterprise value proposition is **managed runtime at scale, framework neutrality, AWS-grade security/networking (VPC, PrivateLink, CloudFormation), and a now-broad agent operations toolchain (memory, eval, observability, policy, registry)**. In aide-canon terms this is a **Means-layer build-and-run substrate** — the altitude AIDE explicitly is *not*.

## 2. Source links

- Official: `aws.amazon.com/bedrock`, AgentCore docs (`docs.aws.amazon.com/bedrock-agentcore/`), AgentCore overview + FAQs (`aws.amazon.com/bedrock/agentcore/faqs/`), SageMaker Unified Studio (`aws.amazon.com/sagemaker/unified-studio/`), Amazon Q Developer (`aws.amazon.com/q/developer/`), Strands Agents (`strandsagents.com`, `github.com/strands-agents`), re:Invent 2025 recap (`aboutamazon.com/news/aws/aws-re-invent-2025-ai-news-updates`).
- In-canon prior research: the vendor-`Agent`/`Skill`/`Tool` mapping discipline in [`../../aide-vocabulary-map.md`](../../aide-vocabulary-map.md); the sibling [`langchain.md`](langchain.md) finding (same altitude argument; LangGraph/LangSmith are first-class AgentCore framework/observability integrations, so the two stacks compose).
- (Product naming is rebrand-prone — "Bedrock Agents" → **AgentCore**, the steady stream of new AgentCore sub-services, and Nova → Nova 2 are recent examples; verify surface names and GA/preview status at read time.)

## 3. Map against AIDE

### Against the four AIDE planes

| AIDE plane | AWS equivalent | Position |
|---|---|---|
| **Control** (AEON governance) | AgentCore **Policy** (Cedar) + **Registry** governed catalog + Observability — deterministic guardrails and approval workflow, but **no authority-altitude or trust-envelope governance model** | *AIDE ahead* on ordinal authority / behavioral envelope; *behind* on shipped deterministic enforcement (Policy) |
| **Runtime** | AgentCore **Runtime** — serverless, session-isolated, MCP + A2A, 8-hr windows | *AIDE behind* on realized runtime / *in flight elsewhere* (strong overlap) |
| **Experience** (AIDEX) | SageMaker Unified Studio + Q Developer (builder/developer UX, not operator-as-curator console) | *AIDE ahead* — no HCAE operator-curation experience model |
| **Capability** (OAAD) | Gateway (API→MCP tools), Code Interpreter, Browser, Strands tool ecosystem | *In flight elsewhere* (mature, MCP-native capability breadth) |

### Against the six AEON service planes

| AEON plane | AWS equivalent | AIDE position |
|---|---|---|
| **Identity** | AgentCore **Identity** — distinct agent identity, inbound IdP federation (Cognito/Entra/Okta), outbound OAuth (2LO/3LO) + token vault; "on behalf of users or by themselves" | *In flight elsewhere* — strong identity/credential primitives; scope-based, **no principal-altitude / ordinal model** |
| **Authority** | Scope/role-based access + AgentCore **Policy** (Cedar, intercepts every tool call *outside the execution boundary*) | **AIDE ahead** on ordinal authority — OrdSA O0–O6 authority-down/evidence-up is absent — but the gap **narrows**: Cedar Policy is deterministic, prompt-independent enforcement, closer to MxM-Morals altitude than plain RBAC |
| **Evidence** | AgentCore **Observability** (OTEL/CloudWatch, full execution traces) + **Evaluations** (13 pre-built evaluators) | **AIDE behind** — built, GA, OTEL-standard; AIDE's evidence trail is emit-only spec |
| **Integration** | Gateway + MCP/A2A + Strands; broad SaaS connectors (Salesforce/Slack/JIRA/Zoom) | *In flight elsewhere* — broad, protocol-native |
| **Capability composition** | Strands multi-agent patterns (Agents-as-Tools, Swarms, Graphs, Workflows); Harness loop | *In flight elsewhere* — strong; but no **envelope-refinement** composition law (cf. [`../../../../patterns/workflow-orchestration.md`](../../../../patterns/workflow-orchestration.md)) |
| **Orchestration runtime** | AgentCore **Runtime** + Strands model-driven agent loop | **AIDE behind** on realized runtime; *converging* via the workflow-orchestration pattern |

*(Inference is AEON's 7th plane, ADR-EA-0015: Bedrock is the inference substrate and AgentCore is explicitly model-agnostic, but model-agnosticism is operational neutrality, not a first-class **governance** property the way the Inference plane frames it.)*

### Vocabulary collision

AWS's **"agent"** (an autonomous AI system that "reasons, uses tools, and maintains context," acting "on behalf of users or by themselves") is the canon's **AI-aide** (per [ADR-EA-0016](../../../../decisions/ADR-EA-0016-adopt-ai-aide-as-canon-vocabulary.md)) — never the OAgents **`Agent`** primitive (a typed object inside a behavioral envelope). AgentCore **`Skill`** (a Registry catalog resource) and Strands **`Tool`** map to MxM **Means** / atomic invocation respectively — convergent on `Tool`, collision on `Skill`/`Agent`. AgentCore **Identity** is an identity/access service; do not read it as the canon **Identity plane**'s principal model. Critically: AWS's framing of AgentCore as a way to run "agent platforms" / a "fleet" of agents must **not** be read as the Ologos fleet or NG-AIDE-01 — these are a vendor's customer-deployed AI-aides on a managed substrate, a different entity class.

## 4. Classification

**Mixed — "in flight elsewhere," at a different altitude.** aide-canon and the AWS stack are *different categories* — a **governance/architecture corpus** vs a **build-and-run platform** — so classification is per-axis, not global:

- **AIDE ahead** — Authority (OrdSA's O0–O6 ordinal layering; AWS has scope/role + Cedar policy, not ordinal precedence), behavioral envelope / trust layer (OAgents §10: the trust layer sits *above any agent framework* — AgentCore is exactly such a framework-agnostic substrate), HCAE operator-as-curator experience, vendor-neutral conformance criteria. **Caveat (honest):** AgentCore **Policy** (Cedar, out-of-band, prompt-independent) is the strongest *shipped* deterministic-constraint enforcement of any vendor surveyed and narrows the MxM-Morals/enforcement gap considerably — "ahead" here is about *ordinal authority and envelope semantics*, not about whether enforcement exists.
- **AIDE behind** — realized runtime (AgentCore Runtime), observability + eval (Observability/Evaluations, OTEL-native), governed catalog (Registry), enterprise plumbing (VPC/PrivateLink/CloudFormation), and — decisively — **adoption, distribution, and the fact that this is GA shipping product** where AIDE is design-first research with enforcement still largely unbuilt.
- **In flight elsewhere** — orchestration (AgentCore Runtime + Strands ↔ AEON Composition/Orchestration + the workflow-orchestration pattern); identity primitives (AgentCore Identity ↔ canon Identity plane); MCP/A2A integration and capability breadth.

**The synthesis:** they **compose, not compete**. aide-canon is the governance layer one would wrap *around* an AgentCore deployment — AgentCore Runtime as the Means/runtime, Observability/Evaluations as the Evidence plane, AgentCore Identity as the identity substrate, and Cedar **Policy** as a *partial* deontic-enforcement primitive — with OAgents' envelope + OrdSA ordinal authority + MxM Morals supplying the trust/authority semantics the platform still lacks. This is the OAgents §10 thesis made concrete on the most operationally mature vendor substrate surveyed, and the same canon-spec ↔ platform-substrate relationship the canon already documents with [Hermetic](../../exemplar-tracking/hermetic/) and [thinx-aidex](../../exemplar-tracking/thinx-aidex/).

## 5. Objective implication

Three Doerr-style Objective shapes follow:

1. **Defend-and-extend (authority + envelope lead).** Propagate OrdSA ordinal authority + the OAgents envelope as the trust/authority layer *above any agent framework* — AgentCore is the canonical mature framework-agnostic substrate with scope/role + Cedar policy but no ordinal-authority or envelope semantics. KR shape: a documented "govern-an-AgentCore-deployment" mapping (OrdSA O0–O6 + envelope + MxM Morals expressed partly *as Cedar policy* over Gateway/Runtime).
2. **Catch-up (evidence + eval tooling).** AgentCore Observability + Evaluations are OTEL-native and GA, materially ahead of AIDE's emit-only evidence spec. KR shape: adopt OTel-GenAI as the canonical evidence shape (already begun — workflow-orchestration v0.1.x shared evidence object) and demonstrate AgentCore-grade trace + eval on an AIDE exemplar.
3. **Converge-or-differentiate (deontic enforcement).** Cedar **Policy** is convergent evidence that out-of-band, prompt-independent constraint enforcement is the right shape for deontic rules. KR shape: articulate where MxM Morals + OrdSA authority *differentiate* from Cedar (ordinal precedence, evidence-up provenance, operator-as-curator) vs. where they should **compile down to** Cedar as the Means-layer enforcement target — convergent mechanism, differentiated semantics.

## 6. Date + reviewer

Surveyed **2026-06-01** by **OlogosAI** (canon-prime). Snapshot of the Oct–Dec 2025 GA wave (AgentCore GA Oct 13 2025; Policy/Evaluations/Registry/Nova 2/Strands-TS announced re:Invent 2025). Revisit on the next AWS agent-surface shift (rebrand-prone) or at OKR refresh.
