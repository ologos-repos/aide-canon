# OSA Relative to Existing Frameworks

OSA is **complementary** to existing enterprise-architecture and AI-governance frameworks. It does not replace any of them. It supplies what they currently lack for Enterprise AI: a **control grammar** for authority across AI capability layers.

This file lays out the relationship per framework.

---

## TOGAF — The Open Group Architecture Framework

**What TOGAF gives you:** A method (the ADM — Architecture Development Method) for developing enterprise architecture across business, data, application, and technology architectures. A governance discipline. A vocabulary for stakeholder concerns, requirements management, and architecture views.

**What it does not give you for AI:** TOGAF does not name the distinction between *delegated execution actors* (agents) and *applications*. In TOGAF terms an agent is just an application component — which collapses authority questions OSA exists to surface.

**Where OSA plugs in:**

- TOGAF's **Business Architecture** is the natural home for OSA's O0 (Enterprise Intent).
- TOGAF's **Application Architecture** is where O1, O2, and O3 (orchestrators and agents) live, but with the authority layering OSA names.
- TOGAF's **Technology Architecture** is where O4 (tools) and O5 (data substrate) live.
- TOGAF's **Architecture Governance** discipline operates over O6 (outcome / audit / feedback).

OSA gives a TOGAF practitioner a way to populate the AI-specific portions of those architectures with a consistent authority model rather than ad-hoc per-project decisions.

## UAF — Unified Architecture Framework

**What UAF gives you:** Mission-driven, systems-of-systems modeling. Multi-viewpoint architecture (strategic, operational, services, resources, security, projects, standards, actual resources, personnel). Strong fit for systems where mission alignment is central — defense, aerospace, large-program engineering.

**What it does not give you for AI:** UAF's view stack does not have a viewpoint specifically for **AI authority layering**. AI components show up in services and resources views, but the authority chain between them is not part of the standard.

**Where OSA plugs in:**

- UAF's **Strategic** viewpoint maps to O0.
- UAF's **Operational** viewpoint, in an enterprise-AI context, is where O1 and O2 (orchestrators) sit.
- UAF's **Services / Resources** viewpoints are where O3, O4, O5 live.
- UAF's **Security** viewpoint and OSA's authority discipline are complementary — UAF gives you the security-controls model, OSA gives you the AI-specific authority-flow model that those controls protect.

For mission-engineering organizations already using UAF, OSA can be expressed as an additional viewpoint specifically for AI capability authority.

## ArchiMate

**What ArchiMate gives you:** A modeling language for describing, analyzing, and visualizing relationships across business, application, and technology layers of an enterprise. Pairs naturally with TOGAF.

**What it does not give you for AI:** ArchiMate's elements describe relationships and components, but the *authority semantics* between AI components — which one may delegate, which one may execute, what envelope a tool runs under — are not part of the language.

**Where OSA plugs in:**

- ArchiMate elements at the **Business Layer** model O0 policies and objectives.
- ArchiMate **Application Layer** elements model O1 orchestrators, O2 domain orchestrators, and O3 agents — with OSA-defined authority relationships drawn between them.
- ArchiMate **Technology Layer** elements model O4 tools and O5 substrates.
- ArchiMate **Implementation & Migration** elements track OSA layer maturity over time.

A practical extension: define an ArchiMate stereotype set for OSA — `«osa:O1-orchestrator»`, `«osa:O3-agent»`, etc. — to make authority-layer membership explicit in the visual model.

## NIST AI Risk Management Framework (AI RMF)

**What NIST AI RMF gives you:** A risk-management vocabulary structured around four functions — *Govern*, *Map*, *Measure*, *Manage* — for AI systems. Sector-neutral. Useful for organizing AI risk practice across the lifecycle.

**What it does not give you:** The AI RMF is a risk-management overlay. It does not specify *what the AI system architecture looks like* such that the four functions can be applied with consistent granularity.

**Where OSA plugs in:**

- AI RMF **Govern** maps to O0 (Enterprise Intent) — policy, principles, risk appetite, accountability structures.
- AI RMF **Map** maps to O1 (Enterprise AI Orchestrator) — knowing what is happening, by whom, with what model, under what envelope.
- AI RMF **Measure** maps to O6 (Outcome, Audit, Feedback) — evidence, metrics, drift, incidents.
- AI RMF **Manage** maps to the closed loop from O6 back to O0 — adjusting policy, hardening enforcement, refining envelopes.

OSA gives an AI RMF practitioner the **target architecture** against which the four functions are exercised. AI RMF tells you what to govern, map, measure, and manage; OSA tells you the structural surface on which those activities take place.

---

## Combined view

| If you have... | Pair it with OSA for... |
|---|---|
| TOGAF | An AI-specific authority model populating the Application and Technology architectures |
| UAF | An AI-capability authority viewpoint complementing the existing UAF stack |
| ArchiMate | A stereotype set and authority-relationship vocabulary for AI components |
| NIST AI RMF | The structural target the four functions are exercised over |

None of these frameworks are wrong about what they cover. OSA does not try to be a method, a modeling language, a viewpoint stack, or a risk vocabulary. It is a **control grammar** — and a control grammar is composable with all of the above.
