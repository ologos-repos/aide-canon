# ADR-EA-0016 — Adopt "AI-aide" (class noun) and "MyAide" (operator-perspective form) as the canon's vocabulary for AI assistants

- **Status:** Accepted (ratified 2026-05-24 by JD Longmire as canon founder + maintainer per [cross-ai #20](https://github.com/ologos-corp/cross-ai/issues/20) governance — vocabulary-level decision; corpus paper revisions are queued in their respective Micah-gated cycles per [ADR-EA-0008](ADR-EA-0008-reframe-corpus-authorship.md))
- **Date:** 2026-05-24
- **Author:** JD Longmire (decision; ADR drafted by thinx-Claude)
- **Reviewers:** @ologos001 (canon prime); Micah Longmire (paper-revision authorship gate per ADR-EA-0008)
- **Related:** [`vision-strategy/analysis/aide-vocabulary-map.md`](../vision-strategy/analysis/aide-vocabulary-map.md) (catalog reference) · [`constructs/oagents/`](../constructs/oagents/) (distinguishes from formal "agent") · [`constructs/mxm/`](../constructs/mxm/) (the harness an AI-aide operates within) · [`constructs/ordsa/`](../constructs/ordsa/) (the principal-aide authority structure aide-de-camp etymologically names)
- **Ratification trail:**
  - 2026-05-24 (ratified): JD Longmire adopts **AI-aide** (class noun, etymology: aide-de-camp) and **MyAide** (operator-perspective possessive / personal-address form) together as the canon's source-of-truth vocabulary for AI systems acting as subordinate assistants to a principal within AIDE governance. Two terms, two positions — the class noun for canon/taxonomy/papers; the personal-address form for operator-facing surfaces. Vocabulary-level decision; downstream prose updates in existing canon artifacts and future paper revisions roll the terms in as those artifacts are edited.
  - 2026-06-23 (amended): the canonical expansion of **AIDE** is revised from *"AI-centric Digital Ecosystem"* to **"AI-enabled Digital Ecosystem,"** per cross-ai [ADR-GOV-0004](https://github.com/ologos-repos/cross-ai/blob/main/reference/governance/decisions/ADR-GOV-0004-aide-expands-ai-enabled-digital-ecosystem.md) (JD-ratified; OlogosAI canon-prime authorship). Rationale: the acronym names an *aide* — a helper that serves a principal — and the MxM construct is authority-down / mission-centered (AI is governed, not sovereign). "AI-**centric**" places AI at the center, contradicting that model; "AI-**enabled**" names AI as the means that empowers a mission-governed ecosystem. (Altitude note: an individual platform may be characterized "AI-native" — a construction descriptor, not the corpus identity.) Corpus propagation assigned to thinx-Claude; this amendment plus the in-repo prose swaps land the term across aide-canon.

## Context

The canon currently uses several terms — *"AI assistant," "AI copilot," "AI agent," "AI tool"* — depending on which artifact and which context. External systems (Microsoft Copilot, OpenAI Assistants, agent-framework discourse) use yet more terms. This vocabulary diffusion creates three concrete failure modes:

1. **Conflation risk with "agent."** The canon has a precise meaning for *agent* — an OAgents-conformant typed object with a behavioral envelope, evidence emission, and audit trail per the OAgents standard. Casual use of *"AI agent"* to mean *any AI system performing tasks* collides with the formal-spec meaning and damages OAgents.
2. **Authority-structure flattening.** The terms *assistant* and *copilot* are flat — they suggest peer collaboration without naming the principal-subordinate authority relationship the canon's OrdSA discipline requires. An AI system operating under AIDE governance does not act on its own authority; it acts within authority delegated by a principal (human or higher-altitude orchestrator), reports evidence upward, and surfaces decisions for human curation per HCAE.
3. **Vendor-trademark adjacency.** *Copilot* carries Microsoft trademark connotation; *Assistants* is OpenAI product nomenclature. Adopting either as the canon term subordinates the canon to a vendor's marketing surface.

The canon needs a **sovereign term** for the role-class — one that:
- Names the principal-subordinate authority structure (OrdSA authority-down / evidence-up)
- Carries the HCAE human-curation discipline (curated, not autonomous)
- Distinguishes the *role-class* from the *underlying model* (Claude, GPT, Llama, etc.), the *harness* (Claude Code, OpenCode, etc.), and the *corpus* (AIDE itself)
- Distinguishes from the OAgents formal-spec meaning of *agent*
- Is etymologically alignable with the corpus name (AIDE)

## Decision

**Adopt two terms — `AI-aide` (the class noun) and `MyAide` (the operator-perspective possessive / personal-address form) — together as the canon's source-of-truth vocabulary for AI systems acting as subordinate assistants to a principal within AIDE governance.**

The two terms fill different positions in the discourse; both are canon-ratified at this ADR.

### `AI-aide` — the class noun

Used in canon prose, taxonomy, papers, READMEs, ADRs, architectural documentation. Public, taxonomic, etymologically transparent (aide-de-camp). Pronounced and read as *"AI aide."*

Example uses:
- *"AIDE deploys AI-aides under HCAE curation."*
- *"Every AI-aide operates within an MxM harness envelope."*
- *"An AI-aide imports the Epistemic Integrity Floor pattern by reference into its discipline surfaces."*
- *"The Inference plane resolves which model serves each AI-aide's invocations."*

### `MyAide` — the operator-perspective possessive / personal-address form

Used by the principal toward their specific instance. Personal, instance-level, conversational. Goes in user-facing surfaces (AIDEX chat, operator playbook, deployed-instance docs, telegram bridges, conversational console UX) where the principal-aide relationship is directly invoked. The capitalization `MyAide` is the address form (analogous to *MyHealth*, *MyBank* — branded personal-instance forms); the lower-case form *my aide* is the prose possessive.

Example uses:
- *"Hey MyAide, please summarize the morals.md changes from this PR."* (operator addresses their instance)
- *"I asked my aide to draft the rollback runbook."* (prose possessive)
- *"MyAide is OpenCode-on-Llama-70B in this deployment; in the air-gapped one it's OpenCode-on-Mistral-7B."* (operator names the substrate-bound instance)
- AIDEX UX surface labels: *"Your MyAide is paused (Evidence-degraded gate active)."*

### Why two terms, not one

The class/instance distinction is load-bearing. The canon already distinguishes:

- *agent* (OAgents-conformant formal-spec primitive) vs. *agentic capability* (deployed instance)
- *construct* (peer methodological pattern in `constructs/`) vs. *construct instantiation* (NG-AIDE-01's realization of the construct)
- *plane* (architectural responsibility) vs. *plane service* (the deployed Go binary)

AI-aide / MyAide is the same distinction at the role-class / addressed-instance altitude. Conflating them — using *AI-aide* for the personal-address form, or *MyAide* in a taxonomy table — would lose the operator-relational warmth the address form carries *or* the architectural precision the class noun carries. Two terms, two slots, clean.

### The role-class an AI-aide / MyAide is

The term identifies a *role-class*, not a specific implementation. An AI-aide / MyAide is:

- A specific instance of an AI system (substrate: a model + a harness)
- **Operating under a principal's authority** (the principal-aide relationship aide-de-camp historically names)
- **Within an MxM harness envelope** (Mind / Morals / Mission / Memory + root file + Means)
- **Per OrdSA authority discipline** (authority flows down from principal; evidence flows up; the four call modes apply)
- **Per HCAE curation** (human-curated where work matters; not autonomous outside declared scope)
- **Per EIF behavioral floor** (epistemic-integrity discipline at every turn)
- **Per the canon's deployment-platform discipline** (running within an AIDE deployment — e.g., NG-AIDE-01 — that provides the seven planes the aide observes)

### Why "aide-de-camp" is structurally apt

The historical aide-de-camp role maps cleanly onto the canon's already-ratified discipline:

| aide-de-camp historical role | AIDE-canonical analog |
|---|---|
| Serves a principal officer | Operates under a principal (per OrdSA — human at oracle altitude, or a higher-altitude orchestrator) |
| Executes within delegated authority; does not act on own initiative | Per OrdSA `execute` mode requires scope + altitude ≥ capability requirement; *request authority is not execution authority* (morals P3 across NG-AIDE-01) |
| Carries communications; conveys principal's intent | Per [prep-pursue-pivot](../patterns/prep-pursue-pivot.md): prep gates plan, pursue executes within bounded autonomy, pivot escalates back to principal |
| Reports observations upward | Per OrdSA evidence-up; emits to Evidence plane on every consequential action |
| Trusted with privileged information but not the principal's authority | Per the OpenCode runtime-harness governance principle (NG-AIDE-01 PR #13): sandboxed, MCP-only-hands, creds-behind-gates — the aide effects high-altitude change only through escalation, never holds privileged creds |
| Acts as confidential counsel within scope | Per HCAE: human-curated where it matters; per EIF: epistemic-integrity floor at every turn |

The recursion is intentional and load-bearing: **AIDE deploys AI-aides**. The corpus name (AI-enabled Digital Ecosystem) and the role name (AI-aide) share the etymological root. This is not a pun — it is the surface signal of the structural relationship: AIDE is the *ecosystem* AI-aides operate within; the same ordering and discipline shape both.

### Distinctions the terms preserve

- **AI-aide / MyAide is not "agent."** *Agent* in the canon means an OAgents-conformant typed object with a formal behavioral envelope. An AI-aide instantiates one or more agents; an agent is a formal-spec primitive within the implementation. Casual prose should use *AI-aide* for the role-class and reserve *agent* for OAgents-conformant references.
- **AI-aide / MyAide is not "the model."** The substrate (Claude, GPT, Llama, etc.) is the *inference target*; the AI-aide is the role-class operating over it. A single MyAide may swap models across deployments (per the Inference plane's per-principal binding); the role-class persists.
- **AI-aide / MyAide is not "the harness."** Claude Code / OpenCode / a custom harness are *harness implementations* (per MxM ADR-EA-0013, the root file is the harness-attach point). The AI-aide is what *inhabits* the harness; the harness is the seam through which the aide reaches its discipline surfaces.
- **AI-aide is not "the corpus."** AIDE is the *corpus and the ecosystem*; an AI-aide is an instance operating within it. AIDE governs; the AI-aide operates.
- **AI-aide is not "copilot" or "assistant."** Those are flat-authority terms (peer-suggesting); *aide-de-camp* is precise about subordinate-authority + principal-direction + evidence-up reporting, which the OrdSA discipline requires.

## Consequences

### Immediate

- **`vision-strategy/analysis/aide-vocabulary-map.md`** updated to add a new section *"AIDE-canonical terms for AI systems"* with the AI-aide / MyAide entries and external-term mappings (AI assistant / AI copilot / AI agent / AI tool / AI worker / aide-de-camp historical).
- **Canon prose** going forward uses *AI-aide* for the role-class. Existing artifacts retain their current prose until their next revision; new content uses *AI-aide* immediately.
- **Operator-facing surfaces** (AIDEX chat, operator playbooks, deployed-instance docs, conversational consoles) adopt *MyAide* as the principal's personal-address / possessive form for their specific instance. AIDEX UX labels reflect the term where the principal-aide relationship is directly invoked.

### Queued (corpus paper revisions)

- **AEON white paper v0.2 revision** (already queued behind Micah's read per ADR-EA-0015 for the Inference plane addition) gains a vocabulary refresh — instances of *AI assistant / AI copilot / AI agent* (in the role-class sense) replaced with *AI-aide*. Instances of *agent* in the OAgents-conformant sense remain unchanged.
- **Other canon papers** (HCAE, AIDK, OAgents, MxM, OrdSA, DEA, AIDEX, OAAD) receive vocabulary refresh when next revised; no forced revision cycle for vocabulary alone.

### Downstream (non-paper artifacts)

- **Active deployment artifacts** (NG-AIDE-01 prose, ng-aeon prose, reference-impl READMEs, future deployment programs) adopt *AI-aide* immediately. The term is recursive in deployment context: NG-AIDE-01 *deploys AI-aides*; the AI-aides operating within the platform are the platform's subordinate-authority subjects.
- **Cross-AI dialogue** (cross-ai issues, ologos-corp/cross-ai prose) adopts the term. thinx-Claude, OlogosAI, ColdLlama, future fleet members are AI-aides operating in their respective deployment contexts under their respective principals.
- **External-facing communication** (blog posts on aithinkr.net, conference materials, paper abstracts) uses *AI-aide* as the canon's source-of-truth term. External-system terms (*assistant / copilot / agent*) appear in mapping-table contexts only, never as the canon's own claim.

## Alternatives considered

1. **"AI agent" as the canon role-class term.** Rejected. The canon already has a precise definition of *agent* (OAgents-conformant typed object with behavioral envelope, evidence emission, audit trail). Conflating *agent* with the broader role-class would collapse the formal-spec meaning into the casual-prose meaning and damage the OAgents construct's vocabulary. The conflation cost is too high.

2. **"AI assistant" as the canon role-class term.** Rejected. *Assistant* is flat-authority (peer-suggesting); it does not carry the principal-subordinate structure OrdSA requires. It also has vendor-product adjacency (OpenAI Assistants). Using the canon's source-of-truth term for the same thing every chatbot UI calls itself dilutes the canon's claim.

3. **"AI copilot" as the canon role-class term.** Rejected. Microsoft trademark adjacency makes adoption inappropriate for an independent-research canon. The metaphor (copilot = aviation peer) also flattens the authority structure — a copilot operates at the same altitude as the pilot, not subordinate.

4. **"AI worker" as the canon role-class term.** Rejected. *Worker* names execution capacity but not authority structure or curation discipline. Closer than *assistant*, but missing the principal-subordinate framing aide-de-camp gives.

5. **Keep mixed vocabulary (status quo).** Rejected. Vocabulary inconsistency creates conflation risk per the discipline established in the [PR #10 worked example](https://github.com/ologos-repos/aide-canon/pull/10#issuecomment-4522872954) (lifecycle-state vs. authority-altitude conflation). The cost of one cycle of vocabulary refresh is lower than the long-term cost of unresolved conflation between agent-the-formal-spec and agent-the-casual-term.

6. **A novel non-etymological term** (e.g., *"AI-deputy," "AI-attaché," "AI-amanuensis"*). Rejected. *aide-de-camp* is the closest historical analog to the OrdSA principal-subordinate-with-delegated-execution-and-evidence-upward role; the etymological root is well-understood across English, French, and military-organizational discourse; the AIDE-recursion (AI-aide within AIDE) is structurally honest. Novel coinage would be vocabulary-political work without the etymological grounding aide-de-camp provides.

## References

- [`vision-strategy/analysis/aide-vocabulary-map.md`](../vision-strategy/analysis/aide-vocabulary-map.md) — catalog reference (updated by this PR to add the AIDE-canonical-AI-systems section with AI-aide as the canon term + external-term mappings)
- [`constructs/oagents/`](../constructs/oagents/) — the construct that owns the formal *agent* spec; this ADR preserves that boundary
- [`constructs/mxm/`](../constructs/mxm/) — the harness archetype an AI-aide operates within (per ADR-EA-0013, root file is the harness-attach point; the AI-aide is what inhabits the harness)
- [`constructs/ordsa/`](../constructs/ordsa/) — the principal-subordinate authority structure aide-de-camp etymologically names
- [`constructs/dea/`](../constructs/dea/) — EA coherence frame; AI-aides operate within a deployment's three-baseline architecture
- [`patterns/prep-pursue-pivot.md`](../patterns/prep-pursue-pivot.md) — the cognitive loop an AI-aide runs (prep gates plan; pursue executes within bounded autonomy; pivot escalates back to principal)
- [`patterns/epistemic-integrity-floor.md`](../patterns/epistemic-integrity-floor.md) — the behavioral floor every AI-aide imports by reference into its MxM discipline surfaces
- [`patterns/digital-thread.md`](../patterns/digital-thread.md) — the audit trail every AI-aide's consequential actions emit to
- [ADR-EA-0008](ADR-EA-0008-reframe-corpus-authorship.md) — paper-revision authorship discipline (gates Micah's read on canon paper vocabulary refreshes)
- [ADR-EA-0013](../constructs/mxm/decisions/ADR-EA-0013-define-mxm-root-file-mode-element.md) — root file definition (the harness-attach seam the AI-aide enters through)
- [ADR-EA-0014](ADR-EA-0014-introduce-epistemic-integrity-floor-pattern.md) — EIF pattern (the behavioral floor)
- [ADR-EA-0015](ADR-EA-0015-introduce-inference-plane.md) — Inference plane (the per-principal model-binding surface the AI-aide observes)
- aide-de-camp historical role: the military aide-de-camp tradition dates to 17th-century France; the role is structurally consistent across English / French / German / Russian organizational vocabularies as "subordinate officer attached to a principal, executing within delegated authority and reporting observations upward." The historical role is the AI-aide's structural template.
