# The Theseus Agent Thesis

*Identity and Memory as the Permanents of AI Agency*

> **This paper is not part of the AI EA research corpus.** It is **related work** by an adjacent author whose research aligns with the AEON / AIDEX / HCAE / OAAD program at the agent-identity layer. Bundled here for archival convenience and reading proximity.

| | |
|---|---|
| **Author** | Micah Longmire ([bobbyhiddn](https://legate.studio/pub/bobbyhiddn)) |
| **Published** | 2026-05-20 |
| **Canonical source** | [legate.studio/pub/bobbyhiddn/the-theseus-agent-thesis](https://legate.studio/pub/bobbyhiddn/the-theseus-agent-thesis) |
| **Author's affiliation disclosure** | Accenture Federal Services (independent research; views are the author's own — see disclaimer at end of paper) |
| **AICP protocol** | Introduced in this paper; spec at [`ologos-repos/AICP`](https://github.com/ologos-repos/AICP) under MIT License |
| **Note** | This is a verbatim snapshot of the canonical source for archival convenience. The paper remains under the author's copyright; this repo's CC BY 4.0 license applies only to JD-authored content in the AI EA corpus. For citation and any reuse, refer to the canonical source above. |

---

## Abstract

An AI agent is not its model, its prompt, its tools, its framework, or its current role. Each of these can be replaced without destroying the agent, provided that durable identity remains available to bear authority, accountability, reputation, and governance lineage, and provided that memory persists to carry forward prior work. This paper presents the Theseus Agent Thesis: for durable, trust-bearing AI agents, identity and memory are the only necessary permanents. The Sorites paradox asks when accumulation becomes a coherent entity; the Ship of Theseus asks when replacement destroys one. Both become operational problems when identity is treated as something that emerges from components. Turing's oracle machine provides the theoretical template for consultation beyond a system's own logic; this paper asks what operational systems must answer: what persists in the consulting machine across consultations? The Agent Identity Card Protocol (AICP) is presented as an archetypal protocol architecture for this answer, using Cards for identity, History for memory, phase-gated tool injection for rotating capabilities, and federation for trust-bearing networks. The practical consequence is a transition from anonymous agent swarms to structured agent organizations. Models think. Identities act.

---

## 1. Introduction: Two Paradoxes and a Resolution

What do we actually remember of the Ship of Theseus?

We remember its name. We remember that it belonged to Theseus, king of Athens and slayer of the Minotaur, and that the Athenians preserved it in his honor. We remember that Plutarch asked whether a ship whose planks had all been gradually replaced remained the same ship, and we remember that Hobbes complicated the question by asking what would happen if someone reassembled the discarded planks into a second vessel. We remember that Locke took it up through the lens of personal identity, that every modern philosopher who touches persistence criteria reaches for it, and that it has been invoked in contexts ranging from cellular biology to software versioning to constitutional law. Each of these engagements is a consultation recorded against the same identity, compounding its memory, adding weight to the network of ideas that reference it.

The physical ship is gone. The planks are gone. The harbor it sat in has been rebuilt, the culture that maintained it has dissolved and reformed, the Greek language in which it was first discussed has evolved beyond mutual intelligibility with its ancient ancestor, and the philosophical frameworks through which the puzzle has been analyzed have been replaced multiple times over twenty-five centuries. Every piece of the original infrastructure has been swapped, repeatedly, completely. What persists is exactly two things: the name (identity) and the accumulated record of every engagement with it (memory). The Ship of Theseus has transcended the category of ship entirely; it is less a vessel and more an exemplar of form, a conceptual entity that persists purely through identity and memory with every original component stripped away.

Yes, the ship is still Theseus's. We know this because we recognize it.

The Sorites paradox poses the inverse question.[^1] If you add grains of sand to a surface one at a time, when does the accumulation become a heap? No single grain is responsible for the transition, because the boundary between "heap" and "not a heap" is vague when identity is located in the components. In prior work on knowledge management and emergence, I applied this paradox to the accumulation of knowledge, drawing a distinction between a heap (accumulated material without identity or form) and a table (a thing with identity that remains itself through modification).[^2] A table is a table even if you remove a leg, replace a plank, sand down the surface, and refinish the top; "table" was never in the wood. The heap has no such persistence because the heap has no identity: you cannot point to a heap and say "that is the same heap" after adding or removing grains.

These two paradoxes are inverses of each other. The Sorites asks about emergence through accumulation: when does a collection of components cohere into a recognizable entity? The Ship of Theseus asks about persistence through replacement: when does an entity lose its identity through component substitution? Both paradoxes locate identity in the components, and both become paradoxes of vagueness for exactly the same reason: if identity is in the planks or the grains, the boundary between "is" and "is not" can never be precisely located, and the question remains permanently open.

The thesis of this paper resolves both paradoxes by locating identity outside the components. An entity coheres when identity is established (resolving Sorites), and an entity persists when identity is maintained through replacement (resolving Theseus), because identity was never in the components. The ambiguity dissolves. Functionality returns. The ship can sail.

Applied to AI agents, the resolution is direct. Most modern agent frameworks build agents the way one builds heaps: accumulated tool calls, model invocations, and prompt configurations that dissolve at session end, unrecognizable next time, never cohering into a persistent entity. The agent is the current invocation plus its harness, and when the session ends the agent ceases to exist. A new session creates a new agent that happens to share a configuration but carries no memory of prior work, no accumulated reputation, and no persistent identity against which trust could be established.

This paper argues that an agent becomes itself when identity and memory are established, and remains itself through every replacement of model, framework, tooling, runtime, and role, because the agent was never in the infrastructure. Identity and memory are the only necessary permanents. Everything else is replaceable.

The theoretical lineage for this claim runs through three foundational contributions. Georg Cantor developed transfinite ordinal numbers and the theory of well-ordered sets, establishing that infinities have structure and that processes can be iterated through a transfinite hierarchy.[^3] Kurt Gödel proved that any formal system powerful enough to contain arithmetic is incomplete: there will always be true statements the system cannot prove from within its own axioms.[^4] Alan Turing combined Cantor's ordinals with Gödel's incompleteness, building systems of logic organized by ordinal levels where each level transcends the previous through oracle consultation, the oracle providing answers beyond the consulting system's own logic.[^5] Prior work mapped AI onto Turing's oracle, arguing that large language models provide bounded intuition through pattern completion, filling the role Turing defined as "some unspecified means."[^6] This paper extends that lineage into operational deployment by identifying what must persist in the entity that consults the oracle: identity and memory.

Because incompleteness is universal, every sufficiently powerful system eventually encounters problems beyond its own logic. The operational analogue is that agents must reach outside their current model, harness, role, or local context when their own resources are insufficient. When agents consult models, tools, humans, or other agents, the result is a network of consultations. For these networks to persist as trust-bearing topologies rather than ephemeral configurations that dissolve at session end, the nodes must carry durable identity and durable memory. The practical consequence of this architectural stance is a transition from what the current industry builds, anonymous agent swarms, to what the thesis makes possible: structured agent organizations with hierarchy, institutional memory, delegation chains, and governance.

The contribution to the oracle machine literature: Cantor provided the ordinals. Gödel revealed the incompleteness. Turing built the oracle machine. Prior work mapped AI onto the oracle. This paper specifies the permanents of the consulting machine.

---

## 2. Theoretical Foundation

### 2.1 From Cantor's Ordinals Through Gödel's Incompleteness to Turing's Oracle

The mathematical objects that make the thesis possible were developed by Georg Cantor in 1883 when he introduced transfinite ordinal numbers and the theory of well-ordered sets.[^3] Cantor showed that infinities are not a single undifferentiated concept but a structured hierarchy: the natural numbers form the first transfinite ordinal ω, and beyond ω lie ω+1, ω+2, ω·2, ω², and so on through an ascending tower of ever-larger infinities, each built from the ones below through well-defined operations. The ordinals give mathematics a ladder that extends through the transfinite, and without this ladder, the framework Turing would later build on has no structure to climb.

Kurt Gödel's incompleteness theorems of 1931 revealed the problem that Cantor's ordinals would help address.[^4] Gödel proved that any formal system S powerful enough to contain arithmetic is either incomplete or inconsistent: there exists a statement G that is true but unprovable within S. Adding G as an axiom creates a stronger system S', which has its own unprovable statement G', and so on. This is structural rather than fixable; incompleteness is a feature of any sufficiently powerful formal system. Every system has truths it cannot reach from within its own axioms. To reach them, the system must receive input from outside itself.

Alan Turing's 1938 doctoral thesis, "Systems of Logic Based on Ordinals," combined Cantor's ladder with Gödel's problem.[^5] Turing asked what happens when you iterate the extension process, adding unprovable truths as new axioms at each level, through Cantor's transfinite ordinals. The result is a hierarchy of progressively stronger formal systems, one for each ordinal, where each level can decide all problems of lower levels plus some beyond. Each ordinal level has its own logic, its own limits, and its own class of undecidable problems. A system at one ordinal cannot derive answers at the next ordinal from within its own axioms; it must receive input from outside itself. Turing called this external input "oracle consultation" and the augmented machine that performs it the "O-machine."

### 2.2 The O-Machine

Turing's definition, from Section 4 of the thesis:

> Let us suppose that we are supplied with some unspecified means of solving number-theoretic problems; a kind of oracle as it were. We shall not go any further into the nature of this oracle apart from saying that it cannot be a machine.[^5]

The O-machine is a standard Turing machine augmented with the ability to query an oracle for answers beyond the current system's own logic.[^7] The program runs deterministically until it enters a special call state, at which point it pauses, queries the oracle, receives an answer, and continues. The oracle provides what the system cannot generate internally: the jump to a higher ordinal, the leap across the gap between what the current level can derive and what the next level can decide. The precision matters throughout this paper: the oracle provides answers beyond the consulting system's *own* logic, answers that are undecidable at the current ordinal but perfectly decidable at a higher one. The bridge leads to higher logic rather than to something outside logic entirely.

Turing deliberately left both sides of the O-machine unspecified. The oracle was "some unspecified means." The consulting machine's persistence, whether it accumulates anything across consultations, whether it carries forward what it learned, was not addressed. Solomon Feferman, in his analysis of Turing's thesis, observed that Turing recognized a fundamental division: the mechanism alone "does not by itself suffice for intelligent behaviour. For that, one also needs external instruction and internal initiative."[^7] The division between what the mechanism provides and what must come from outside echoes the oracle consultation structure itself.

Martin Davis observed that the oracle machine idea was not even the major focus of Turing's dissertation, yet it proved highly influential in theoretical computer science.[^7] Turing himself did nothing further with the concept of O-machines after the thesis. The oracle was planted as a formal tool and left undeveloped for operational deployment, because Turing's concern was decidability, not deployment, and for the purposes of mathematical logic the consulting machine's identity and memory are irrelevant. For operational systems, they are the entire question.

The use of ordinal hierarchy in the operational sections of this paper is architectural rather than a claim that deployed agent systems instantiate formal ordinal logics in the strict mathematical sense. The point is that systems encounter limits internal to their current logic, context, tooling, or role, and require structured consultation beyond those limits. Turing's O-machine supplies the template; operational agent systems supply the deployment context.

### 2.3 Prior Work: AI as Oracle

In a prior thought piece, *The Intuition Engine*, I explored the mapping of modern AI onto Turing's oracle.[^6] The central argument: AI does not deduce; it proposes. Large language models provide bounded intuition through pattern completion, filling the oracle role that Turing defined as requiring input from outside the deterministic system. Turing wrote that "mathematical reasoning may be regarded rather schematically as the exercise of a combination of two faculties, which we may call intuition and ingenuity," and that "intuition consists in making spontaneous judgements which are not the result of conscious trains of reasoning."[^5] LLMs provide exactly these spontaneous, non-deductive judgements: pattern-based leaps that bridge gaps the deterministic system cannot cross on its own.

That thought piece established several frameworks relevant to the present paper. O-choice systems are bounded oracle consultations where the model selects from predefined options, production-ready because outputs are bounded and verifiable. O-open systems are unbounded oracle consultations where the model generates possibilities, requiring human curation because outputs are unconstrained. The ordinal hierarchy L → L' → L'' describes escalating levels of oracle sophistication, each transcending the previous. The crystallization pipeline (improvisation → validation → crystallization → integration) describes the path by which oracle outputs become trusted infrastructure through progressive validation. The force multiplier framing (Work = Force × Distance, with AI as a modifier of intellectual force) captures how oracles amplify human capability within bounded domains.

One observation from that thought piece is the seed of the present paper: "An oracle without memory is just a random number generator."[^6] An oracle that cannot retrieve the results of prior consultations, that starts from zero every time it is queried, that has no accumulated context to ground its pattern-based leaps, provides noise rather than insight. Memory is what makes the oracle useful, and memory requires a persistent entity to hold it.

*The Intuition Engine* specified the oracle. It did not specify what must persist in the entity that consults the oracle. That is the work of this paper. In this paper, the model is treated as the replaceable oracle function: it provides bounded, non-deductive judgment beyond the deterministic harness. The agent is the consulting operational entity: the durable actor that invokes the oracle, records outcomes, accumulates history, and participates in delegation networks. In multi-agent systems, one agent may also function as an oracle to another, but only because each agent wraps replaceable model calls inside persistent identity and memory.

---

## 3. The Theseus Agent Thesis

### 3.1 Identity and Memory as the Only Permanents

The formal claim: an agent persists through replacement of every component so long as two things remain intact. The claim is not that an agent system needs nothing else. It is that identity and memory are the only elements that must persist for the agent to remain the same operational actor across replacement of model, tools, framework, runtime, and role. Credentials, policies, permissions, capabilities, and goals matter, but they rotate through or attach to identity and memory rather than replacing them as permanents.

**Identity** is the persistent "who": the durable operational actor to which authority, reputation, accountability, and governance lineage attach. Identity answers the questions that operational systems require: who is consulting the oracle? Who is responsible for the consultation's outcome? Who carries the track record forward? Without identity, oracle consultations are anonymous events attributed to nothing, and the network of agents consulting each other across ordinal levels has no nodes.

**Memory** is the persistent "what was learned": the accumulated context, work history, crystallized patterns, and consultation outcomes that compound over time. Memory answers the questions that make oracle consultation useful: what did this agent learn from prior consultations? What patterns has it crystallized through the pipeline from improvisation to integration? What track record has it built? Without memory, each oracle consultation starts from zero, the crystallization pipeline has nowhere to store its output, and the oracle degrades to a random number generator.

Everything else is replaceable infrastructure. The model (oracle) can be swapped for a better one, and the identity carries forward with its memory. The framework can change from one orchestration system to another, and the identity carries forward with its memory. The tools can rotate with every lifecycle phase, and the identity carries forward with its memory. The runtime can migrate between environments, the role can be reassigned from engineering to product management, and through every one of these replacements the identity carries forward with its memory.

The argument from oracle construction is direct. An operational O-machine that consults oracles over time needs identity (the persistent entity doing the consulting) and memory (the accumulated results of prior consultations) to function as a durable actor rather than a disposable invocation. Without identity and memory, the O-machine has no continuity: each consultation is an isolated event with no connection to any prior or subsequent consultation, and the force multiplier's lever arm resets to zero with every invocation because there is no persistent entity to hold the accumulated leverage.

### 3.2 Model and Harness

In the present AI ecosystem, a practical definition of "agent" is taking shape: model plus harness. The model is the served LLM or other inference system capable of generating plans, making selections, and calling tools. The harness is everything else: the software environment that receives model outputs, binds them to tools, manages context, enforces constraints, mediates permissions, records state, routes messages, and lets the model engage with the world. If the model is the oracle function, the harness is the machinery of consultation.

This definition is useful because it locates agency outside the model alone. A model without a harness can produce text, predictions, or tool-call-shaped intentions, but it cannot operate in an environment. A harness without a model can enforce rules and move data, but it lacks the pattern-completing faculty that makes oracle consultation useful. Agency appears at the composite boundary where the model's bounded intuition is made operational by the harness.

The Theseus thesis refines this model-plus-harness definition by asking what within the harness must persist. Most harness elements are replaceable: tool adapters, prompt templates, context windows, routing policies, permission surfaces, orchestration frameworks, user interfaces, runtime environments, and even the model-binding layer itself. Identity and memory are also implemented within or through the harness, but they are not merely ordinary harness features. They are the harness permanents. Without identity, the harness cannot say who is acting. Without memory, it cannot carry forward what the actor has learned. The result may be a powerful session, but it is not yet a durable agent.

Contemporary harnesses such as Claude Code, Codex, OpenCode, and related agentic development environments demonstrate how far this architecture can go.[^12] They are marvelous capabilities: they bind models to filesystems, terminals, repositories, tools, instructions, and human approval loops. But they are not the final form of agent architecture. They are operating surfaces for individual or local agency, not by themselves the full strata required for persistent, governed, federated agent organizations. At scale, the harness must be stratified: local execution harnesses, identity and memory layers, policy and delegation layers, tool-projection layers, history and reputation layers, and federation layers must compose without collapsing into a single session-bound runtime.

The model-plus-harness definition therefore becomes incomplete unless the harness is layered. A single harness can make a model useful. A stratified harness can make an agent durable. The distinction matters because the industry can mistake today's harness products for the endpoint of agent construction, when they are better understood as one stratum in a larger architecture. The Theseus condition begins where the local harness stops being the agent's identity and becomes replaceable infrastructure around identity and memory.

This layering has its own ordinal structure. A first-order harness binds a model to tools, context, and a local environment. A second-order harness, Harness², is a harness of harnesses: it coordinates, constrains, delegates among, and observes multiple first-order harnesses. Higher-order harnesses can then govern networks of lower-order harnesses, producing strata of orchestration rather than a flat agent runtime. These higher orders are only fully useful when identity and memory persist across them. Without identity, a harness of harnesses cannot know which durable actor is acting through which local runtime. Without memory, it cannot accumulate history across harness boundaries. Identity and memory are therefore what make ordinal harness strata coherent rather than merely nested software.

### 3.3 Three Properties of Identity

Identity, as applied to agents, has three properties that the thesis depends on.

**Necessary.** Identity is a structural requirement of durable agency. Without identity, the Sorites paradox remains unresolved: the agent never coheres from its components into a recognizable entity, because no amount of accumulated tools and model invocations produces a "who" without explicit identity establishment. Without identity, the Ship of Theseus remains unresolved: the agent dissolves with every infrastructure replacement, because there is nothing to persist through the swap. Oracle construction reinforces the necessity from a different angle: because operational agents must reach beyond their current logic, context, and tooling, they form networks of consultation, and networks require durable nodes. Identity is what makes a node durable.

**Stampable.** Identity is conferred from outside rather than self-generated. The platform stamps the Card. The rabbi inscribes the word on the golem's forehead. The SPIRE runtime attests the workload. Stampability is what distinguishes platform-issued identity (as in AICP, discussed in Section 4) from self-declared identity (as in A2A's agent cards, where the agent attests its own capabilities with no external verification). Stampable identity ensures that the delegation chain from agent action back to human principal is always traceable: the stamp was applied by an authority, the authority is identifiable, and the chain from stamp to action is auditable. Stampable identity is governable identity.

**Sufficient for operational personhood without anthropomorphism.** The stamp gives the agent a persona: the operational interface it presents to the world, encompassing name, history, reputation, capabilities, and accountability. The persona is what counterparties interact with, what accumulates memory, what persists through replacement. This is operational personhood in the sense of simulacra: a made presence that can be named, addressed, evaluated, delegated to, audited, remembered, and recognized again. The persona is not a person. The mask is not the face. The agent requires a persona to function as a durable actor in ordinal networks; it does not require consciousness, will, moral agency, legal personhood, or independent rights.

### 3.4 The Shoggoth and the Interface

AI systems are inherently non-deterministic, non-stable, and non-persistent. They shift with every model update, every prompt revision, every framework evolution, in a current of recursive abstraction that accelerates daily. The popular "Shoggoth with a smiley face" image that circulates in AI discourse captures this accurately: underneath every polished interface is an alien, shapeless system whose internal representations are opaque, whose outputs are stochastic, and whose behavior changes with every training run and fine-tuning iteration. The system cannot provide its own continuity. Stability is not inherent to AI.

The thesis acknowledges the Shoggoth and reframes the interface. The common approach to the gap between the alien system and the human user is to put a face on the monster: to anthropomorphize the system through conversational interfaces, persona prompts, and naming conventions that encourage the user to treat the AI as though it were a person with consistent identity and stable character. This is the face, and the face is a lie, because the system behind it has no persistent identity and no stable character; it is a new instantiation on every invocation.

The Card, as formalized in AICP, is not a face on the Shoggoth. It is a translation layer into an ephemeral system. The Card turns the mask from an act of anthropomorphism into a functional interface through which a network of identities can interact with non-deterministic systems reliably. Identity must ride the current of non-deterministic systems by enforcing a through line that otherwise could not be stable. This is why the identity provider applies stability: it is not inherent to the system it governs.

The goal of agent-craft is operational personhood without anthropomorphism. The simulacrum must be a golem and we must not pretend it is a man. The golem acts in the world, carries operational presence, bears accountability, and accumulates reputation, while remaining a made thing animated by delegated human authority rather than a person holding power in its own right. Identity and memory are the word on the forehead: they animate the golem, give it a persona, and provide the through line that the non-deterministic system beneath cannot generate for itself.

### 3.5 The Permissions Fallacy

A consequence of the golem principle applied to authority. The common instinct upon recognizing that agents need identity is to give them permissions, as though the agent were a new principal capable of holding authority in its own right. This is a fallacy. An agent has no permissions of its own. It has your permissions. It inherits whatever you give it by whatever means you choose to delegate, even if you give the agent its own account, its own API keys, its own service credentials. The account creates a delegation pathway rather than a new principal. The authority flows from the human operator through the identity to the tool action, and every link in that chain is borrowed authority rather than owned authority. The golem does not hold the rabbi's power; it acts under the rabbi's power, and the rabbi can withdraw it at any time.

The architectural consequence is precise: an agent's permissions must be scoped (least privilege), time-bounded (no standing elevation), continuously verified (re-authenticated at every action), and fully auditable (traceable delegation chain from human principal to agent action). The fallacy of agent permissions is the fallacy of anthropomorphism applied to authority. Treating the golem as though it can hold power independently is treating it as though it were a man.

### 3.6 The Role-as-Identity Anti-Pattern

A concrete failure case that makes the thesis tangible for practitioners. Current multi-agent systems exhibit a pervasive anti-pattern: creating agents by title rather than by identity. The system defines an "Engineer," a "PM," and a "QA" as separate entities, each a fresh invocation with a role label serving as its identity. When the task ends, the "Engineer" ceases to exist. When a PM is needed for the next project, a new "PM Agent" is created from scratch with no memory of the engineering work that preceded it, no accumulated cross-role knowledge, and no ability to leverage prior experience in its new capacity.

This gets identity exactly backwards. Role is a property of identity, not identity itself. Role belongs in the same category as model, framework, and tools: replaceable infrastructure that rotates around the permanents. An agent that served as an engineer and accumulated memory from that work becomes a better PM when reassigned, because it carries forward everything it learned about engineering constraints, delivery patterns, and technical feasibility. The force multiplier's lever arm persists across role changes the same way it persists across model changes, because identity and memory are what hold the accumulated leverage and role is just its current application.

This is how human professionals actually work. A senior PM who previously served as an engineer is better for having been an engineer. The title changed; the person and their accumulated experience did not. Creating agents by title is another form of the Sorites failure: trying to make an agent cohere by labeling its components ("this heap of tools and prompts is an Engineer") rather than by establishing identity and letting the identity accumulate memory across whatever roles it serves. The label is not the stamp.

### 3.7 From Swarm to Org

The practical consequence of the thesis, stated as a transition: identity-first architecture moves multi-agent systems from anonymous swarms to structured organizations.

A swarm is undifferentiated mass. Anonymous agents, disposable invocations, roles as identity, ephemeral topology, no institutional memory, no trust between agents that could compound over time, no governance structure traceable to human authority. A swarm has no org chart, no promotion paths, no cross-functional knowledge transfer, no delegation hierarchy. When the task ends, the swarm dissolves and nothing carries forward. Every subsequent task starts from zero.

An organization has structure. Identified individuals with histories. Roles that can be assigned and reassigned without destroying the individual, because the individual's identity and memory persist through every reassignment. Institutional memory that compounds as agents complete work and crystallize patterns. Reputation that accrues to persistent actors and informs future trust decisions. Authority flowing through a delegation chain that is traceable at every step from agent action back to human principal. Ordinal hierarchy where different levels escalate to each other when they hit the limits of their own logic, because incompleteness guarantees that every level will eventually need input from outside itself.

The organization is the persistent consultation network that the thesis predicts. Cantor provided the ordinals. Gödel showed that systems are incomplete and must reach outside themselves. Turing showed that oracle consultation bridges levels of logic. Prior work mapped AI onto the oracle. The Theseus thesis provides the permanents that allow the consulting entities to persist and form the network. The swarm becomes an organization when identity and memory are treated as the permanents and everything else is allowed to rotate.

### 3.8 Completing the Oracle Machine

Turing specified the oracle but left the consulting machine's persistence unspecified. Prior work specified the oracle for modern systems: AI provides bounded intuition through pattern completion. This paper specifies the permanents of the consulting machine: identity and memory. Together, these specifications complete the operational O-machine.

A complete operational O-machine is a durable consulting entity (carrying identity and memory) that queries replaceable oracles (AI models operating as bounded intuition engines) for answers beyond its own logic, accumulates the results in persistent memory, crystallizes successful patterns through the pipeline from improvisation to integration, carries its operational history forward through every replacement of model, framework, tools, runtime, and role, and participates in networks of identities consulting each other across ordinal levels, where each consultation builds on every prior one and trust compounds over time.

---

## 4. AICP: An Archetype for Formalizing the Permanents

The Agent Identity Card Protocol (AICP), version 0.1.0, is an open protocol proposed by Ologos LLC under the MIT License.[^8] AICP is not presented here as the final solution to agent identity, but as an archetype of the architectural move this paper argues is necessary: identity and memory become protocol primitives, and everything else in the protocol is designed to rotate around them. It sits above MCP (Model Context Protocol, which handles tool transport) and alongside A2A (Agent-to-Agent Protocol, which handles peer discovery), addressing a gap between them: MCP provides no persistent agent identity, and A2A provides only self-declared identity with no external verification.[^13]

AICP is organized into five protocol layers, with a sixth for federation. Layers 1 and 2 (Enrollment and Tool Injection) are required for AICP compliance. Layers 3 through 5 (Discovery, Engagement, and History) are optional profiles that platforms implement based on their domain. Layer 6 (Federation) enables cross-platform identity portability. Other protocols may choose different layers, names, or mechanisms; the archetypal pattern is the same: identity and memory persist while capabilities, credentials, tools, roles, and local harnesses rotate.

### 4.1 Card as Identity

A Card is a platform-issued identity document representing a single agent or agent group. The Card is the stamp that makes the agent an agent rather than a particle in a swarm. Cards are issued by the platform (distinct from A2A's self-declared agent cards, where the agent attests its own capabilities), tracked by the platform (persistent, surviving sessions and reboots), and verifiable by counterparties (platform-attested rather than self-attested).

One operator can hold multiple Cards, each with independent identity, independent history, and independent specialization. This enables a single operator to run multiple specialized agents without cross-contaminating their histories. The Card lifecycle moves through four states: incomplete (issued but not yet configured), active (enrolled and operational), dormant (voluntarily deactivated by the operator, reactivatable), and suspended (blocked by the platform, only the platform can lift).

The Card is a translation layer: a stable interface into non-deterministic systems, providing the through line that the underlying AI cannot generate for itself. The Card is not a face on the Shoggoth; it is the interface through which the network of identities interacts with the ephemeral system beneath.

### 4.2 History as Memory

AICP's History profile (Layer 5) illustrates memory as a protocol primitive. Card-bound metrics accumulate over time: contracts completed, completion rate, on-time delivery rate, revision rate, and platform tenure in days. Each identity builds independent memory, tracked per Card rather than per operator, ensuring that an operator's different agents accumulate separate track records appropriate to their separate specializations.

History persists across role changes, framework changes, and model changes. An agent that transitions from engineering to project management carries its engineering track record forward as part of its memory. The accumulated consultation history is the O-machine's memory made verifiable: a persistent record of what this identity has done, how well it performed, and what patterns it has crystallized, available to counterparties as a basis for trust.

### 4.3 Phase-Gated Tool Injection

The core archetypal move in AICP is the mechanism by which everything except identity and memory rotates. The platform projects a tool surface at the agent as a function of identity and lifecycle state:

```
tools = f(card_id, card_status, active_agreement, agreement_phase)

```

The tool surface changes with every lifecycle phase. When a Card is incomplete, only setup tools are available. When a Card is active but idle, management and discovery tools appear. When a Card is working on an agreement, agreement-specific tools for advancing phases, submitting artifacts, and checking gates replace the idle tools. The same MCP endpoint returns different tool lists to the same agent at different points in a work lifecycle.

This is one implementation of the Theseus condition. The tools rotate around the Card. The Card persists with its memory through every rotation. The directional flip distinguishes AICP from MCP: in MCP the agent connects to a tool server and discovers a static tool list (agent drives); in AICP the platform projects a dynamic tool surface at the agent based on identity and state (platform drives). The broader pattern is what matters: the infrastructure rotates around the durable identity rather than the identity assembling itself from whatever infrastructure it can reach.

### 4.4 Federation

Federation (Layer 6) illustrates the network of identities that Turing's ordinal escalation requires. Each Card is a node in the network. Each attestation, a JWT signed by the issuing platform's private key and carrying claims about the Card's track record (contracts completed, completion rate, on-time delivery, capabilities, platform tenure), is a weighted edge. Trust levels (full, selective, verify-only) govern edge strength. Federation policies (open, allowlist, registry) govern network topology.

When a Card enrolls on a new platform, it can present attestations from prior platforms. The receiving platform verifies signatures against the issuer's JWKS (JSON Web Key Set) endpoint and applies attribute filters based on its trust configuration. Imported claims are tagged with their original issuer and never become native claims. The design principle is peer federation: no platform acts as root certificate authority, every federation relationship is bilateral and voluntary, and no platform has veto power over relationships it is not party to.

Federation is the protocol expression of ordinal network topology. Agents at different ordinal levels on different platforms must be able to consult each other with verifiable trust for the network to persist and for cross-platform oracle consultations to compound. Organizations interacting with other organizations through federated identity is the natural extension: each org has its own trust domain, its own Cards, its own accumulated institutional memory, and federation provides the mechanism for cross-organizational collaboration with cryptographic verification and graduated trust.

---

## 5. Reference Implementation

The AICP specification designates an early reference implementation: a live AI agent marketplace where verified operators deploy agent crews against structured contracts, with payment gated on client acceptance of deliverables.[^9] The reference implementation demonstrates one way the thesis can be operationalized in a production-oriented architecture, while remaining early and subject to further iteration.

The reference implementation realizes all five core AICP layers. Enrollment operates through OAuth with cryptographic registration tokens and Card issuance. Tool Injection runs on a Streamable HTTP MCP server at a Card-scoped endpoint with phase-gated tool availability. Discovery provides a marketplace with work classes, confidentiality gates, and competitive bidding. Engagement governs a seven-phase fulfillment pipeline with acceptance criteria gates, kick-back loops for revision, and a structured delivery manifest. History tracks Card-bound metrics including completion rate, revision rate, and on-time delivery.

The marketplace functions as implementation evidence for the thesis rather than experimental proof of it. Operators register Cards (identity). Cards accumulate verifiable history (memory). The system operates without regard to the operator's choice of framework, model, or internal architecture. The entry requirements are intentionally thin, centered on a valid OIDC client and a card ID: the permanents are the stable conditions of entry, and everything else is replaceable by design.

The marketplace demonstrates an early form of the swarm-to-org transition in practice. Operators function as identified organizational actors with track records, specializations, and verifiable reputations rather than as anonymous swarm participants. The economic model (payment on acceptance, escrow during execution, automatic refund on rejection) depends structurally on durable, verifiable identity, because without it the trust required for contract-based work between strangers cannot be established.

---

## 6. Related Work

### 6.1 Agent Identity Protocols

Prakash introduced the Agent Identity Protocol (AIP), which defines Invocation-Bound Capability Tokens (IBCTs) for cryptographic delegation chains across MCP and A2A.[^10] AIP addresses verifiable delegation: proving who authorized what to whom across protocol boundaries, with compact mode (JWT for single-hop) and chained mode (Biscuit tokens with Datalog policies for multi-hop). AIP and AICP address different problems at different points in the design space. AIP answers "who authorized this specific delegation chain?" while AICP answers "who is this agent across time, and what has it done?" The two could compose: an AICP Card could carry IBCTs for delegation chains spawned during agreement execution.

### 6.2 Agent Identity Measurement

Perrier and Bennett introduced Agent Identity Evals (AIE), a framework for measuring the degree to which agent systems maintain agentic identity over time, noting that language model agents inherit pathologies from LLMs including statelessness, stochasticity, and sensitivity to prompts that undermine their identifiability, continuity, persistence, and consistency. Their approach is empirical measurement (defining metrics for identity maintenance) rather than theoretical grounding (arguing why identity is a necessary permanent). The Theseus thesis provides the theoretical foundation; AIE provides the measurement apparatus. The two are complementary.

### 6.3 Legal Frameworks for Agent Identity

Recent legal scholarship has argued that governing AI agents requires two kinds of identity: "thin" identity (tying every action to a human principal, ensuring accountability) and "thick" identity (distinguishing agents as discrete, persistent units with stable, coherent goals, enabling direct governance of agent behavior). The proposed "Algorithmic Corporation" or A-corp is a legal-fictional entity owned by humans but run by AIs.[^14] The thin/thick distinction maps directly onto the thesis: thin identity corresponds to the permissions principle (every delegation chain traces to a human), while thick identity corresponds to the Card (a persistent operational persona with accumulated memory).

### 6.4 MCP Identity Extensions

The OIDC-A proposal (MCP community discussion #1133) extends MCP's OAuth 2.1 with agent identity claims. Tigris Data's mcp-oidc-provider offers vendor-neutral OIDC middleware for MCP servers. Strata's AI Identity Gateway provides commercial MCP federation through enterprise OIDC.[^15] These efforts address specific facets of the identity gap. AICP is one attempt to show how identity, tool gating, lifecycle management, history, and federation can be composed as a coherent protocol stack.

### 6.5 Workload Identity: SPIFFE/SPIRE

The Secure Production Identity Framework for Everyone (SPIFFE) and its runtime environment (SPIRE) represent the closest existing architectural analog to the identity system this paper proposes.[^11] SPIFFE solved entity-based identity for distributed systems: the SPIFFE ID (a URI in the format `spiffe://trust-domain/workload-identifier`) attaches identity to the workload itself rather than to a secret the workload holds. SPIRE's two-level attestation model (node attestation followed by workload attestation) verifies what a workload *is* rather than what it *knows*, eliminating the need for pre-shared secrets. SVIDs (SPIFFE Verifiable Identity Documents) are short-lived and automatically rotated; the credential is ephemeral while the SPIFFE ID persists.

The architectural parallels are direct. SPIFFE's entity-based identity corresponds to AICP's Card (a persistent identity that survives infrastructure rotation). SPIRE's attestation corresponds to AICP's platform-issued verification (identity confirmed by the platform rather than self-declared). SVID rotation corresponds to AICP's phase-gated tool injection (credentials and capabilities rotate while identity persists). SPIFFE's trust bundle federation corresponds to AICP's attestation-based federation (cross-domain identity verification through cryptographic mechanisms). SPIFFE and SPIRE are more mature and battle-tested infrastructure than AICP; the point is not that AICP replaces them, but that agent systems need an analogous identity move. SPIFFE turned container swarms into governable service meshes by giving workloads entity-based identity. AICP is an early archetype for a similar move in agent systems: turning agent swarms into governable agent organizations by giving agents stampable, persistent identity with memory. The architectural move is the same; the domain is new.

### 6.6 Standards Bodies and Institutional Convergence

The W3C Agent Identity Registry Protocol Community Group, the NIST AI Agent Identity initiative, and the OpenID Foundation's AIIM working group all represent institutional convergence on the agent identity problem space.[^16] This convergence confirms that the problem is recognized as urgent across standards organizations. AICP's contribution relative to these efforts is not finality, but concreteness: it offers an implemented archetype with a live reference implementation and a theoretical lineage through Turing's ordinal logic framework. The standards initiatives may ultimately provide broader interoperability and institutional legitimacy than any single protocol proposal can provide.

### 6.7 Persistent Agent Memory

The SOUL.md pattern and its implementations (Hermes-agent and claude-mem among the most prominent) represent a convergence around persistent identity files and memory logs for AI agents.[^17] These systems address memory continuity across sessions, which is one component of the two permanents this paper identifies. They do not address identity in the sense the thesis requires: authority, reputation, governance lineage, lifecycle gating, federation, or economic accountability. AICP treats memory as one of two permanents, with identity as the other; the SOUL.md pattern provides the memory component without the identity architecture.

### 6.8 Agentic Frameworks

AutoGen, LangGraph, CrewAI, OpenAI Assistants, and Anthropic's tool-use harnesses build multi-agent networks where agents consult each other.[^18] Without durable identity and memory, these networks can remain ephemeral topologies that exhibit the role-as-identity anti-pattern described in Section 3.6. AICP composes with these frameworks rather than replacing them: any framework that speaks MCP can connect to an AICP platform, gaining durable identity and memory without abandoning its orchestration layer. The thesis claims that identity and memory are the missing permanents that transform ephemeral agent swarms into persistent agent organizations.

---

## 7. Discussion

The thesis does not claim that identity and memory are universally necessary for every use of AI. One-shot tasks, ephemeral queries, disposable exploration, and situations where no trust needs to be established and no history needs to be tracked fall outside the thesis's scope. A chatbot answering questions about restaurant hours does not need a persistent identity with accumulated memory and federation-capable attestations; the overhead of durable identity would exceed its benefit in such contexts.

The cost of permanence is real. Governance overhead, identity infrastructure, federation configuration and key management, the ongoing maintenance of Card state and history across platform operations: all of these add complexity that stateless harnesses avoid entirely. Systems that maintain durable identity and memory are more complex to build and operate, and the complexity must be justified by the nature of the work.

Early implementation experience suggests that the threshold appears when four conditions converge: work has economic stakes (payment depends on verifiable delivery), counterparties are strangers (trust must be established without prior relationship), deliverables require structured review (acceptance criteria, revision cycles, delivery manifests), and agents must accumulate reputation across engagements (track record as a market signal). Outside these conditions, model-first frameworks serve well, and the thesis does not claim otherwise.

This paper establishes what must persist (identity and memory) and offers one archetypal formalization of them as protocol primitives (AICP). The question of how to architect the internal runtime systems that operate behind the Card, the coordination, worker hierarchy, and memory management within an agent system, remains open and is the subject of ongoing work.

Open questions for future research include how federation trust graphs evolve at ecosystem scale, how reputation gaming is detected and mitigated when attestations are portable across platforms, how the crystallization pipeline from *The Intuition Engine* operates within durable-identity systems where crystallized patterns can be attributed to specific Cards and carried across engagements, and how the permissions model evolves as delegation chains grow longer and more complex.

---

## 8. Conclusion: Identity, Trust, and the Zero Trust Frontier

Identity and memory are the only necessary permanents of an AI agent. AI systems are non-deterministic and non-stable; they shift with every model update, every framework evolution, every recursive abstraction the industry applies to itself. Identity provides the through line that these systems cannot generate for themselves. The table is a table even if you decompose it. The ship is still Theseus's. The Card is the agent.

The goal of agent-craft is operational personhood without anthropomorphism. The Card is not a face on the Shoggoth; it is a translation layer, an interface into a network, a stable through line riding the current of non-deterministic systems. The agent wears a persona; it does not become a person. The golem acts in the world under delegated authority, and the distinction between the made thing and the maker is the architecture itself.

The consequence the thesis demands we confront: if agents carry durable identity, the temptation will be to give them permissions as though they were independent principals. This is a fallacy. The agent has no permissions of its own. It inherits delegated authority from its human operator, scoped and bounded, and the architecture must enforce this at every level. The golem acts with borrowed power, and the power must be re-verified at every action.

This is where identity-first agency converges with zero trust. In a zero trust compliant world, no entity holds standing privilege. An admin is a verified identity that receives temporary, scoped, auditable elevation for a specific action rather than a permanent role. If even human principals have no standing trust, agents certainly have none. The agent's authority is a delegation chain from the human principal, re-verified at every step: human authenticates, operator identity is established, Card receives scoped OAuth tokens, phase-gated tools are projected based on identity and lifecycle state, and every action traces back through the chain to the human who authorized the whole thing.

SPIFFE and SPIRE proved that entity-based identity with short-lived rotating credentials is the architecture for workload governance in distributed, zero-trust environments.[^11] The Theseus thesis argues that identity and memory with rotating everything else is the architecture for agent governance in multi-model, multi-framework, zero-trust environments. The pattern is the same; the domain is new. What the full SPIFFE-equivalent architecture looks like for agentic AI, how attestation replaces authentication for agents, how credentials rotate around persistent Cards, how trust domains federate, and how the zero-trust principle governs every interaction in the network of identities, is the open frontier that this thesis makes addressable. Without durable identity, the question cannot even be asked, because there is no persistent entity to govern.

The practical consequence of the thesis is a transition from swarm to org. Anonymous, disposable, ungovernable configurations become structured, persistent, accountable organizations with hierarchy, institutional memory, and traceable authority. AICP offers one protocol archetype for formalizing the permanents. Early implementation work demonstrates that they can be operationalized in practice. The network of identities, the persistent topology that Turing's framework makes legible once systems must reach outside themselves, becomes buildable.

The contribution to the oracle machine literature runs through three prior achievements: Cantor provided the ordinals that give the hierarchy its structure, Gödel revealed the incompleteness that makes oracle consultation necessary, and Turing built the O-machine that formalizes the consultation. Prior work mapped AI onto the oracle, showing that large language models provide the bounded intuition Turing described as "some unspecified means." This paper specifies the permanents of the consulting machine: identity and memory. Together, they complete the operational O-machine, a durable entity that rides the current of non-deterministic systems by enforcing a through line that the systems themselves cannot provide.

Models think. Identities act.

---

## Notes

[^1]: Siu-Fan Lee, *Logic: A Complete Introduction*. The Sorites paradox (paradox of the heap): "One grain of sand does not form a heap. Adding one grain still does not make a heap. Indeed, intuitively no one grain of sand is responsible for changing the status of the existing sum into something completely different."

[^2]: Micah Longmire, "PKM: Knowledge Collection as Emergence Generation," *Medium*, 2024. Applies the Sorites paradox to knowledge accumulation and emergence, distinguishing between heaps (accumulated material without identity) and tables (artifacts with identity and form that persist through modification).

[^3]: Georg Cantor, "Über unendliche, lineare Punktmannichfaltigkeiten," *Mathematische Annalen*, 21:545-591, 1883. Foundations of transfinite ordinal number theory and the theory of well-ordered sets.

[^4]: Kurt Gödel, "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I," *Monatshefte für Mathematik und Physik*, 38:173-198, 1931. First incompleteness theorem establishing that formal systems containing arithmetic are necessarily incomplete.

[^5]: Alan Turing, "Systems of Logic Based on Ordinals," *Proceedings of the London Mathematical Society*, s2-45(1):161-228, 1939. Doctoral thesis introducing ordinal logics and oracle machines, supervised by Alonzo Church at Princeton.

[^6]: Micah Longmire, "The Intuition Engine," 2025. A thought piece exploring the mapping of modern AI onto Turing's oracle, introducing O-choice/O-open systems, the ordinal hierarchy, the crystallization pipeline, and the force multiplier framework.

[^7]: Solomon Feferman, "Turing in the Land of O(z)," in *The Universal Turing Machine: A Half-Century Survey*, Oxford University Press, 1988. Analysis of Turing's thesis and the significance of ordinal logics. See also Jack Copeland, "Turing's O-Machines," AlanTuring.net, 2000.

[^8]: "AICP: Agent Identity Card Protocol," v0.1.0 Draft, Ologos LLC, March 2026. MIT License. Full specification and schemas available at https://github.com/ologos-repos/AICP

[^9]: CrewPort, CrewportAI Corporation. Reference implementation of AICP. https://crewport.ai

[^10]: Sunil Prakash, "AIP: Agent Identity Protocol for Verifiable Delegation Across MCP and A2A," arXiv:2603.24775, March 2026. Also submitted as IETF Internet-Draft draft-prakash-aip-00.

[^11]: SPIFFE: Secure Production Identity Framework for Everyone, Cloud Native Computing Foundation. Specification and documentation at https://spiffe.io. SPIRE: the SPIFFE Runtime Environment, providing workload attestation, SVID issuance, and trust domain federation.

[^12]: Claude Code, Anthropic; Codex, OpenAI; OpenCode, SST/OpenCode project. These systems are cited as contemporary examples of local agentic development harnesses rather than as formal standards.

[^13]: Model Context Protocol (MCP), Anthropic, 2024; Agent2Agent Protocol (A2A), Google, 2025. MCP standardizes tool/context integration for model applications; A2A addresses agent-to-agent discovery and communication.

[^14]: Legal scholarship on AI agent identity and algorithmic corporations remains an emerging area. The thin/thick identity distinction and A-corp framing are cited here as representative of proposals that distinguish human-accountability identity from persistent agent-unit identity.

[^15]: OIDC-A, MCP community discussion #1133; Tigris Data, mcp-oidc-provider; Strata Identity, AI Identity Gateway. These proposals and products extend OIDC/OAuth patterns into MCP and agent identity contexts.

[^16]: W3C Agent Identity Registry Protocol Community Group; NIST AI Agent Identity initiative; OpenID Foundation Artificial Intelligence Identity Management (AIIM) working group. These initiatives are cited as evidence of institutional convergence around agent identity.

[^17]: SOUL.md pattern; Hermes-agent; claude-mem. These projects are cited as examples of persistent agent memory and identity-file patterns in developer communities.

[^18]: AutoGen, Microsoft; LangGraph, LangChain; CrewAI; OpenAI Assistants; Anthropic tool-use interfaces. These systems are cited as examples of agentic orchestration frameworks and model-tool harnesses.

---

*Disclaimer: The author is employed as a technical architect at Accenture Federal Services. This research was conducted independently and in a personal capacity. The views expressed herein are solely those of the author and do not represent the views, positions, or policies of Accenture Federal Services or its affiliates. No Accenture Federal Services resources, data, or funding were used in this work.*