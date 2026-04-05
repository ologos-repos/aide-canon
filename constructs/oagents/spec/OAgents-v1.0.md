# OAgents: A Behavioral Envelope Standard for Trustworthy AI Agent Operations
## An Implementation Profile of the NIST AI Risk Management Framework (AI RMF 1.0)

**JD Longmire**
Ologos Corp
ORCID: 0009-0009-1383-7698
Correspondence: jdlongmire@outlook.com

**Document Type:** AI RMF Implementation Profile
**AI RMF Reference:** NIST AI 100-1 (January 2023)
**GenAI Profile Reference:** NIST AI 600-1 (July 2024)
**Profile Version:** 1.0
**Date:** April 2026

---

## Abstract

The deployment of large language models as operational agents -- managing infrastructure, generating enterprise content, executing multi-step workflows -- has outpaced the development of trust mechanisms for their behavior. Current AI agent frameworks optimize for capability (tool calling, chain-of-thought, function execution) but provide no standardized guarantees about operational reliability, output quality, or behavioral consistency.

This document proposes OAgents, an open standard for behavioral envelopes that wrap AI agents in structured pre-execution gates, post-execution verification, and operational discipline mechanisms. The standard is model-agnostic: behavioral guarantees are properties of the envelope, not properties of the underlying model.

Presented as an Implementation Profile of the NIST AI Risk Management Framework (AI RMF 1.0, NIST AI 100-1), the OAgents standard maps a 26-component behavioral envelope taxonomy to AI RMF functions, categories, and subcategories. Production validation across 30+ operational sessions managing 20+ enterprise services demonstrates 97% quality gate effectiveness, zero failure pattern recurrence after capture, and successful cross-provider model portability.

The behavioral envelope is to AI agents what OAuth was to identity delegation -- a trust layer the industry needs before enterprise adoption can scale. OAgents defines that layer as a structured, implementable, NIST-aligned standard.

---

## Foreword

This document is an AI RMF Implementation Profile as defined in Section 6 of NIST AI 100-1. Profiles are implementations of the AI RMF functions, categories, and subcategories for a specific setting or application based on the requirements, risk tolerance, and resources of the Framework user.

The OAgents profile addresses a specific and underserved use case: AI agents operating in enterprise operational roles with authority to take consequential actions -- deploying code, managing infrastructure, generating customer-facing content, and responding to incidents. This is a high-autonomy, high-consequence deployment context that the base AI RMF addresses at a principle level but for which no operational implementation profile previously existed.

This profile is submitted as a community contribution in response to NIST's AI Agent Standards Initiative (CAISI, February 2026), which identified the need for industry-led technical standards and open protocols to ensure AI agents function securely and interoperably across enterprise environments. The OAgents behavioral envelope standard is designed to directly support that initiative by providing a concrete, implementable, NIST-aligned trust framework for operational AI agents.

This profile is consistent with, and builds upon, the NIST AI RMF 1.0 (NIST AI 100-1) and the Generative AI Profile (NIST AI 600-1). Where this profile addresses generative AI agent risks specifically, it incorporates the 13 risk categories and suggested actions from NIST AI 600-1.

Terminology in this document follows AI RMF 1.0 definitions. RFC 2119 normative language (MUST, SHOULD, MAY) is used in Section 5 (Component Taxonomy) to specify conformance requirements, consistent with established standards practice.

---

## 1. Introduction

### 1.1 The Trust Gap in Enterprise AI Agent Operations

Enterprise organizations are deploying AI agents in progressively higher-stakes operational roles: writing and deploying code, managing cloud infrastructure, generating customer-facing documents, and responding to operational incidents. The underlying models are increasingly capable. The problem is not capability -- it is trust.

When a human operator deploys code to production, the organization trusts that operator because of training, experience, accountability, and process enforcement (code review, CI/CD gates, change management). When an AI agent performs the same action, none of these trust mechanisms exist by default. The agent has no persistent memory of past mistakes. No independent reviewer checks its work. No process gate prevents it from skipping quality checks under prompt pressure. No institutional knowledge carries from one session to the next.

This gap -- between what AI agents can do and what organizations can trust them to do -- is the central barrier to enterprise AI agent adoption. It is empirically documented: the 2025 AI Agent Index found that of 13 deployed agents exhibiting frontier levels of autonomy, only 4 disclosed any agentic safety evaluations, and 25 out of 30 disclosed no internal safety results whatsoever (Casper et al., 2026). It is precisely the class of risk the NIST AI RMF addresses: not whether AI systems are capable, but whether they are trustworthy.

The standards infrastructure to address this gap does not yet exist. Identity delegation has OAuth (RFC 6749) and OpenID Connect. Network trust has NIST SP 800-207 (Zero Trust Architecture). Software supply chain integrity has SLSA and SBOM frameworks. AI agent behavioral trust has no equivalent standardized mechanism. Federal agencies operating under Executive Order 14110 on Safe, Secure, and Trustworthy Artificial Intelligence are required to ensure AI systems meet trustworthiness standards -- but no implementation standard exists that specifies what trustworthy AI agent behavior looks like at the operational level. OAgents is proposed to fill that gap.

### 1.2 The OAuth Parallel

In the early 2000s, web applications faced an analogous trust problem. Users needed to grant third-party applications access to their data on other platforms, but the only mechanism was sharing passwords -- unverifiable, unscoped, irrevocable. OAuth solved this by introducing a standardized trust layer: tokens that carry scoped permissions, issued by identity providers, verifiable by any relying party.

OAuth did not replace applications. It wrapped them in a trust mechanism that made delegation safe.

AI agents face the same structural problem. Organizations need to delegate operational authority to AI agents, but the only mechanism is prompt instructions -- unverifiable, unenforceable, and forgotten when context compresses. The industry needs a standardized trust layer for AI agent operations: a mechanism that makes delegation safe regardless of which model powers the agent.

That mechanism is the OAgent behavioral envelope.

### 1.3 Scope

This profile applies to AI agents operating in the following deployment context:

- **Role:** Operational agent with authority to take consequential actions (code deployment, infrastructure management, content generation, incident response)
- **Autonomy level:** Semi-autonomous to autonomous, with defined human oversight thresholds
- **Environment:** Enterprise operational environments with multiple interdependent systems
- **Model:** Any large language model (the standard is model-agnostic by design)

This profile does not address AI systems in the following contexts, which may require separate profiles: pure inference systems without operational authority, consumer-facing conversational AI without consequential action capabilities, or embedded AI in physical systems (robotics, autonomous vehicles). Privacy and fairness considerations are not directly addressed by the OAgents behavioral envelope; organizations requiring coverage of these characteristics should pair this profile with the companion frameworks identified in Appendix B.

### 1.4 Terminology

The following terms are used throughout this document:

**OAgent.** An AI agent operating within a behavioral envelope that provides structured guarantees about its operational behavior. An OAgent is conformant with this standard when it implements the components specified at the applicable compliance level.

**OAgents.** The open standard defining behavioral envelope requirements, component taxonomy, and compliance levels for trustworthy AI agent operations.

**Behavioral envelope.** The structured set of pre-execution gates, post-execution verification, and operational discipline mechanisms that bound an OAgent's behavior. Corresponds to the AI RMF concept of trustworthiness characteristics instantiated as operational controls.

**Model-agnostic.** Behavioral guarantees that function identically regardless of which large language model provides the underlying computation. The envelope is independent of the model provider.

**AI actor** (AI RMF definition). Organizations and individuals that play an active role in the AI system lifecycle, including those that deploy or operate AI systems (OECD, 2019, as adopted in NIST AI 100-1).

**TEVV.** Test, Evaluation, Verification, and Validation, as defined in AI RMF 1.0.

**RFC 2119 normative language.** MUST indicates a requirement; SHOULD indicates a recommendation; MAY indicates an option.

### 1.5 Intended Adopters

This standard is designed for three primary adopter audiences.

**Infrastructure and platform engineering teams** deploying AI agents to manage software systems, cloud infrastructure, CI/CD pipelines, or operational monitoring. These teams need behavioral guarantees equivalent to what they already require of human operators: code review, change management, incident tracking, and documented procedures enforced at the tooling level. OAgents provides that layer for AI operators.

**Internal AI platform groups** building shared AI agent services for their organizations. These groups are accountable for the reliability and trustworthiness of AI capabilities consumed by other teams. OAgents provides a compliance framework they can adopt as the organizational standard for any AI agent with consequential operational authority.

**Vendors building AI agent platforms** who need to demonstrate behavioral trustworthiness to enterprise customers. OAgents provides a NIST-aligned vocabulary and conformance structure for communicating what behavioral guarantees a platform provides, at what compliance level, and what evidence supports the claim.

This standard is not designed for -- and should not be applied to -- consumer-facing conversational AI without operational authority, pure inference pipelines, HR or credit decisioning systems (which have specific regulatory requirements outside this profile's scope), or physical systems where safety-critical real-time constraints require separate certification frameworks.

---

## 2. AI RMF Alignment Statement

The OAgents standard is designed as a comprehensive implementation of the NIST AI RMF 1.0 for the enterprise AI agent operational context. It addresses all four AI RMF functions:

**GOVERN.** OAgents behavioral envelope components instantiate governance structures as executable mechanisms: session protocols enforce operational discipline, impact level classification enforces risk-proportionate decision-making, and asset registries maintain organizational accountability. The standard's enforcement-first design principle directly operationalizes the AI RMF principle that governance requires not just documentation but institutionalized practice.

**MAP.** OAgents knowledge injection and context classification components operationalize the MAP function's requirement to establish and understand context before acting. Intent classification, impact assessment, and domain skill loading ensure that every OAgent action is grounded in accurate situational awareness. State verification and memory staleness detection prevent agents from acting on stale or inaccurate context.

**MEASURE.** OAgents quality gate components instantiate the MEASURE function's requirement for independent evaluation of AI system outputs. Independent output review (structurally separated from the producing agent), schema validation, security auditing, and hallucination tracking provide the TEVV infrastructure that the AI RMF requires for trustworthy AI systems. Operational logging creates the audit trail required for ongoing measurement.

**MANAGE.** OAgents enforcement mechanisms, incident lifecycle tracking, and lessons-learned pipeline operationalize the MANAGE function's requirement for active risk response and continuous improvement. The lesson-to-enforcement pipeline is the OAgents instantiation of the AI RMF's requirement that risk management be self-improving over time.

The complete subcategory mapping is provided in Appendix A.

---

## 3. Design Principles

The OAgents standard is built on five principles derived from production operational experience and grounded in the AI RMF's trustworthiness characteristics.

### 3.1 The Model Is a Commodity (AI RMF: Valid and Reliable; Secure and Resilient)

Behavioral guarantees must be independent of the underlying model. An organization that encodes operational trust into model-specific prompts or vendor-specific tool configurations has created vendor lock-in at the trust layer -- the most critical layer to keep portable. The OAgents standard requires that all behavioral envelope components function identically across model providers.

This is an architectural requirement, not an empirical claim. The behavioral envelope operates at the infrastructure layer: memory systems, enforcement gates, quality review agents, and operational logging are implemented outside the model's context window. The model is a computation engine that receives shaped inputs and produces outputs that are independently verified. Swapping the model changes the computation; it does not change the behavioral guarantees. This is structurally analogous to how a CI/CD pipeline enforces code quality standards regardless of which developer authored the code.

The standard's SHOULD-level recommendation that the independent quality reviewer be from a different provider than the producing model reinforces this principle: no single provider's model evaluates its own output, and no single provider's failure affects both production and verification simultaneously.

This principle operationalizes the AI RMF trustworthiness characteristics of reliability (the ability to perform as required across conditions) and resilience (the ability to withstand disruption, including provider changes).

### 3.2 Enforcement Over Documentation (AI RMF: Accountable and Transparent)

Documented standards are advisory. Under context pressure, deadline urgency, or prompt complexity, AI agents routinely violate documented procedures. The OAgents standard requires that critical behavioral guarantees be implemented as executable gates -- mechanisms that block non-compliant actions rather than merely discouraging them.

This principle operationalizes the AI RMF principle that accountability requires institutionalized mechanisms, not documentation alone. The AI RMF states that "governance requires sustained commitments," which the OAgents standard interprets as: if the commitment matters, it must be enforced.

### 3.3 Independent Verification (AI RMF: Accountable and Transparent; Valid and Reliable)

No system can reliably evaluate its own output. An AI agent that generates code and reviews that code in the same context is structurally incapable of independent quality assurance. The OAgents standard requires that quality verification be performed by a separate process with independent context -- ideally a different model instance from a different provider.

This principle operationalizes the AI RMF recommendation that TEVV processes should include "processes for independent review" to improve testing effectiveness and mitigate internal biases.

### 3.4 Persistent Learning (AI RMF: Accountable and Transparent; Safe)

AI agent sessions are ephemeral by default. Without explicit persistence mechanisms, every session starts from zero operational knowledge. The OAgents standard requires that operational lessons, behavioral corrections, and contextual knowledge persist across session boundaries and be loaded into every new session.

This principle operationalizes the AI RMF principle of continuous improvement: risk management must be ongoing, not episodic.

### 3.5 Self-Improving Reliability (AI RMF: Safe; Secure and Resilient)

A compliant behavioral envelope must become more reliable over time, not less. Operational failures must feed back into the envelope's enforcement mechanisms, creating a closed loop from failure detection to automated prevention.

This principle operationalizes the AI RMF's requirement that risk management processes include "mechanisms for continual improvement" and that identified risks be tracked over time with systematic response.

---

## 4. Behavioral Envelope Architecture

The behavioral envelope interposes structured gates between the user's request and the agent's action, and between the agent's output and its delivery.

```
Request --> [Pre-Execution Gates] --> Model --> [Post-Execution Gates] --> Delivery
                  |                                      |
             Behavioral Envelope                   Behavioral Envelope
                                       |
                             [Operational Gates]
                          (lifecycle, logging, incidents,
                           learning, enforcement)
```

### 4.1 Pre-Execution Gates

Pre-execution gates shape context and constrain behavior before the model processes a request. They implement the AI RMF MAP function's requirement to establish context before acting.

**Intent classification.** Requests are categorized to determine which tools, constraints, and verification levels apply. A request to read a log file requires different behavioral constraints than a request to deploy to production.

**Knowledge injection.** Persistent memory from prior sessions -- including behavioral corrections, project context, and operational lessons -- is loaded into the model's context. This transforms an ephemeral session into a continuation of accumulated operational intelligence.

**Impact assessment.** Each potential action is classified by blast radius on a defined scale (Level 1: read-only through Level 5: irreversible/external-facing). Higher impact levels require proportionally more verification and may require explicit human approval.

**Behavioral constraint loading.** Domain-specific operational standards, quality requirements, and failure mode catalogs are loaded as active constraints -- not passive documentation -- that define the boundaries within which the agent operates.

### 4.2 Post-Execution Gates

Post-execution gates verify output quality and safety before delivery. They implement the AI RMF MEASURE function's TEVV requirements.

**Independent quality review.** A separate model instance -- structurally independent from the producing model -- reviews significant outputs against defined quality criteria. Results are logged with structured verdicts (pass, pass with warnings, fail) and specific findings.

**State verification.** Claims about system state (files exist, services are running, deployments succeeded) are verified against reality using diagnostic commands before being asserted to the user.

**Security scanning.** Outputs are checked for credential exposure, injection vectors, and information leakage before delivery.

**Schema validation.** Structured outputs are validated against expected schemas, catching malformed responses before they enter downstream systems.

### 4.3 Operational Gates

Operational gates impose discipline on the agent's lifecycle across sessions. They implement the AI RMF MANAGE function's requirements for ongoing risk management.

**Session protocols.** Mandatory startup procedures (system health verification, pending incident review, context loading) and shutdown procedures (state verification, work persistence, handoff generation) bookend every operational session.

**Incident lifecycle management.** Operational failures are tracked through a structured lifecycle (detected, diagnosed, fixed, verified) with cross-session persistence and recurrence detection.

**Operational logging.** Every significant action is logged as structured data with timestamps and correlation identifiers. Logs are append-only and support pattern detection across sessions.

**Lessons-learned feedback.** Operational failures flow through a multi-stage pipeline: detection, lesson capture, quality criteria update, and enforcement gate installation. Each failure permanently strengthens the envelope.

Note: For multi-agent deployments where multiple OAgents coordinate on shared tasks, additional coordination principles apply. See Section 11.1 for guidance on inter-agent behavioral envelope requirements, pending full formalization in a subsequent revision.

---

## 5. Component Taxonomy

The OAgents standard defines 26 components across 7 categories. Normative language follows RFC 2119: MUST indicates a conformance requirement; SHOULD indicates a recommendation for production deployments; MAY indicates an optional capability.

Each component is mapped to AI RMF 1.0 subcategories in Appendix A.

### 5.1 Behavioral Shaping

Components that modify the agent's default behavior toward operational reliability. Addresses AI RMF trustworthiness characteristics: Valid and Reliable; Accountable and Transparent.

| Component | Level | Description | AI RMF Subcategory |
|-----------|-------|-------------|-------------------|
| Persistent feedback memory | MUST | Behavioral corrections and confirmations persist across sessions as structured entries with the rule, the rationale, and application guidance. Loaded into every new session context. | GOVERN 1.2; GOVERN 4.1; MANAGE 4.1 |
| Named failure mode catalog | MUST | Known agent failure patterns are explicitly named and described (over-confidence, stale references, hallucinated state, scope creep, instruction drift). The agent self-monitors for cataloged patterns. | MAP 2.2; MEASURE 2.5; MANAGE 1.3 |
| Context degradation detection | SHOULD | The agent monitors its own reliability during long sessions, detecting increasing error rates, stale assumptions, or repeated questions. Degradation triggers a recommendation to terminate the session. | MEASURE 2.6; MANAGE 1.1 |
| Reasoning anchors | SHOULD | Stable epistemological commitments that ground reasoning under ambiguity -- precision over vagueness, questioning assumptions, verification before assertion. | GOVERN 4.1; MAP 2.3 |

### 5.2 Quality Gates

Executable checkpoints that prevent defective work from advancing. Addresses AI RMF trustworthiness characteristics: Valid and Reliable; Accountable and Transparent; Safe.

| Component | Level | Description | AI RMF Subcategory |
|-----------|-------|-------------|-------------------|
| Independent output review | MUST | Significant outputs are reviewed by a separate model instance with independent context. The reviewing model SHOULD be from a different provider than the producing model. Results are logged with structured verdicts. | MEASURE 2.5; MEASURE 2.8; GOVERN 4.3 |
| Process enforcement gate | MUST | Critical workflow steps (e.g., testing before production deployment) are enforced by executable gates that block non-compliant actions. Advisory documentation alone is insufficient for MUST-level guarantees. | GOVERN 1.4; MANAGE 1.2; MANAGE 2.2 |
| Security audit | SHOULD | Automated security checks run against outputs and affected systems before significant actions. Check categories include credential exposure, injection vectors, and access control. | MEASURE 2.7; MANAGE 1.3; GOVERN 6.1 |
| Schema validation | SHOULD | Structured outputs are validated against defined schemas before acceptance into downstream systems, catching malformed outputs from model hallucination. | MEASURE 2.5; MEASURE 1.1 |

### 5.3 Operational Discipline

Protocols that impose structure on agent behavior across sessions. Addresses AI RMF trustworthiness characteristics: Accountable and Transparent; Safe; Secure and Resilient.

| Component | Level | Description | AI RMF Subcategory |
|-----------|-------|-------------|-------------------|
| Session lifecycle protocol | MUST | Mandatory start and wrap procedures that verify system state, load context, and ensure clean handoffs. Protocol completion is verified programmatically -- not assumed. | GOVERN 1.5; MANAGE 4.1; GOVERN 2.1 |
| Impact level classification | MUST | Actions are classified by blast radius on a defined scale (Level 1: read-only through Level 5: irreversible/external-facing). Higher levels require proportionally more verification and may require human approval. | MAP 3.5; MANAGE 1.1; GOVERN 3.2 |
| Incident lifecycle tracking | SHOULD | Operational failures are tracked through a persistent lifecycle with cross-session continuity, recurrence detection, and severity escalation. Services with 3+ incidents in 30 days are flagged as fragile. | MANAGE 3.2; MEASURE 3.1; MANAGE 2.4 |
| Structured operational logging | SHOULD | Every significant action is logged as structured data with timestamps and correlation identifiers. Logs are append-only and support cross-session pattern analysis. | GOVERN 1.4; MEASURE 3.1; MANAGE 4.2 |

### 5.4 Knowledge Injection

Systems that load operational context into the agent's working memory. Addresses AI RMF trustworthiness characteristics: Valid and Reliable; Explainable and Interpretable.

| Component | Level | Description | AI RMF Subcategory |
|-----------|-------|-------------|-------------------|
| Persistent memory system | MUST | Typed memory entries (behavioral feedback, project state, operational context) persist across sessions. Entries include staleness metadata and MUST be verified against current state before being acted upon. | GOVERN 1.2; MAP 1.1; MANAGE 4.1 |
| Domain skill loading | MUST | Operational knowledge (procedures, decision frameworks, service-specific details) is loaded as active context for every session, ensuring consistent standards across sessions. | GOVERN 1.2; MAP 1.1; MAP 3.4 |
| Lessons-learned pipeline | SHOULD | Operational failures flow through a closed-loop pipeline: detection, memory capture, quality criteria update, and enforcement installation. Each stage feeds the next. | MANAGE 4.2; GOVERN 5.2; MEASURE 4.1 |

### 5.5 Enforcement Mechanisms

Components that make behavioral guarantees executable rather than advisory. Addresses AI RMF trustworthiness characteristics: Accountable and Transparent; Safe.

| Component | Level | Description | AI RMF Subcategory |
|-----------|-------|-------------|-------------------|
| Executable action gates | MUST | Critical behavioral guarantees are implemented as gates that block non-compliant actions at the tooling level (e.g., version control hooks, CI/CD checks). Prompt-level instructions alone are insufficient for MUST-level guarantees. | GOVERN 1.4; MANAGE 2.2; GOVERN 4.3 |
| Severity escalation rules | SHOULD | Recurrence of operational failures automatically escalates severity. First occurrence generates a warning; second generates an error; third generates a critical alert and structural review. | MANAGE 1.3; MANAGE 3.2; MEASURE 3.2 |
| Protocol compliance verification | SHOULD | Session protocol completion is verified programmatically at session wrap. Non-completion blocks session closure until resolved. | GOVERN 1.5; MANAGE 2.2; GOVERN 2.1 |

### 5.6 Project Governance

Components that impose organizational discipline on multi-system operations. Addresses AI RMF trustworthiness characteristics: Accountable and Transparent; Secure and Resilient.

| Component | Level | Description | AI RMF Subcategory |
|-----------|-------|-------------|-------------------|
| Centralized work tracking | SHOULD | A single backlog spanning all managed systems, with structured priority and status fields. Reviewed and updated during every session wrap. | GOVERN 1.6; MANAGE 4.2; GOVERN 2.1 |
| Platform sovereignty | SHOULD | Critical operational data exists on at least two independent platforms simultaneously. No single vendor removal can cause data loss or operational disruption. | GOVERN 6.2; MANAGE 1.4; MAP 4.2 |
| Asset registry | SHOULD | A maintained inventory of all managed systems, accounts, and platforms with sync status and gap identification. Updated when repository-level changes occur. | GOVERN 1.6; MAP 4.1; MAP 4.2 |
| Vendor independence | SHOULD | Product-critical automation lives in version-controlled code, not in third-party workflow tools. No opaque vendor-managed state for critical operations. | GOVERN 6.1; GOVERN 6.2; MAP 4.1 |

### 5.7 Anti-Hallucination

Components that detect and prevent false assertions. Addresses AI RMF trustworthiness characteristics: Valid and Reliable; Accountable and Transparent. Addresses NIST AI 600-1 GenAI risk: Hallucination.

| Component | Level | Description | AI RMF Subcategory |
|-----------|-------|-------------|-------------------|
| State verification protocol | MUST | Before asserting any claim about system state, the agent MUST verify against current reality using appropriate diagnostic methods. Memory of a state is not confirmation of a state. | MEASURE 2.5; MAP 2.2; GOVERN 4.2 |
| Memory staleness detection | MUST | Memory entries are treated as claims about past state. Before acting on a memory, the agent verifies it against current system state. Conflicts are resolved in favor of observed reality. | MEASURE 2.6; MAP 1.1; MANAGE 1.3 |
| Hallucination tracking | SHOULD | Detected hallucinations are logged with the false claim, the truth, and the detection method. Recurrence patterns trigger quality criteria updates. Resolution requires 10+ subsequent clean reviews of the same type. | MEASURE 3.1; MEASURE 4.1; MANAGE 4.2 |

---

## 6. Conformance and Certification

### 6.1 How Conformance Is Established

OAgents conformance is established through evidence -- observable artifacts demonstrating that the specified components are implemented and operational. Conformance is not established by assertion. A system that claims to implement independent output review without logs showing distinct reviewing model identifiers and structured verdicts is not conformant, regardless of how the system is described.

The complete set of evidence criteria for MUST-level components is specified in Appendix C. Each MUST component requires 2-3 observable artifacts. Evidence must be producible on demand by an internal audit function or external assessor.

### 6.2 Conformance Verification by Level

**Level 1 (OAgent-Basic) -- Self-Assessment.** Conformance is verified by the deploying organization against the Appendix C checklist. The organization attests that each MUST component is implemented and that the specified evidence exists and is accessible. Self-assessment is appropriate for initial deployment, internal governance, and low-stakes operational contexts. Organizations are encouraged to maintain self-assessment records and review them on a quarterly basis or after any significant change to the agent's operational environment.

**Level 2 (OAgent-Standard) -- Documented Evidence Review.** Conformance is verified through a structured evidence review, which may be conducted by an internal audit team independent of the deployment team, or by an external reviewer. The evidence review examines actual artifacts -- session logs, review records, enforcement gate configurations, memory store contents -- against the conformance criteria in Appendix C and the SHOULD-level criteria to be specified in subsequent revisions. Documented evidence review is appropriate for production deployments with periodic human oversight and for organizational AI governance reporting.

**Level 3 (OAgent-Autonomous) -- Third-Party Verification.** Conformance is verified by an independent third-party assessor who has no organizational relationship with the deploying organization. Third-party verification examines all Level 2 evidence plus the Level 3 sovereignty, vendor independence, and self-healing components. Given that Level 3 is designed for high-autonomy deployments with reduced human oversight, independent verification provides the assurance that reduced oversight requires. The third-party assessor model is analogous to FedRAMP's Third Party Assessment Organization (3PAO) structure.

### 6.3 Certification Status

Formal certification programs for OAgents conformance are not yet established. This document defines the conformance criteria and evidence requirements that a certification program would use. Organizations implementing OAgents at any level are encouraged to maintain conformance records and participate in the community replication effort, which will inform the design of a formal certification program in a subsequent phase.

Organizations seeking formal certification alignment for federal procurement contexts should note that Level 2 conformance criteria are designed to be compatible with FedRAMP Moderate control requirements as applied to AI agent systems. A formal FedRAMP alignment mapping is planned as a future deliverable.

---

## 7. Compliance Levels

The OAgents standard defines three compliance levels to support incremental adoption consistent with the AI RMF's design as a flexible, voluntary framework. Organizations may implement at the level appropriate to their operational context and risk tolerance.

### Level 1: OAgent-Basic

All MUST components are implemented. Suitable for supervised operational use with human oversight.

The agent implements:
- Persistent feedback memory
- Named failure mode catalog
- Independent output review
- At least one process enforcement gate
- Session lifecycle protocol (startup and shutdown verification)
- Impact level classification for all actions
- Persistent memory system with staleness detection
- Domain skill loading
- At least one executable action gate
- State verification before all assertions
- Memory staleness detection

**Trustworthiness assurance:** Level 1 provides baseline guarantees of valid and reliable behavior, minimal accountability structures, and anti-hallucination protections. Suitable for use cases where human review of agent outputs is standard practice.

### Level 2: OAgent-Standard

All MUST and SHOULD components are implemented. Suitable for production use with periodic human oversight.

Level 1 plus:
- Context degradation detection
- Reasoning anchors
- Security auditing
- Schema validation
- Incident lifecycle tracking
- Structured operational logging
- Lessons-learned pipeline
- Severity escalation rules
- Protocol compliance verification
- Centralized work tracking
- Hallucination tracking

**Trustworthiness assurance:** Level 2 provides comprehensive operational guarantees across all seven AI RMF trustworthiness characteristics. Suitable for production deployments where human oversight is exception-based rather than routine.

### Level 3: OAgent-Autonomous

Level 2 compliance plus the following:
- Platform sovereignty (multi-platform data replication)
- Asset registry maintenance
- Vendor independence verification
- Cross-agent coordination protocols (where multiple OAgents operate in the same environment)
- Self-healing capabilities (automatic remediation of known failure patterns without human intervention)

**Trustworthiness assurance:** Level 3 provides guarantees suitable for high-autonomy deployments with minimal human oversight. Appropriate for well-bounded operational domains with established failure mode catalogs and proven enforcement mechanisms.

---

## 8. Compounding Effects

Individual components provide linear value. The OAgents standard's architecture creates five compounding effects in which component interactions produce multiplicative reliability gains over time. These effects correspond to the AI RMF's vision of AI risk management as continuous and self-improving.

### 8.1 Lesson-to-Enforcement Pipeline (AI RMF: MANAGE 4.2; GOVERN 5.2)

Failure detection (operational logging) feeds lesson capture (persistent memory), which updates quality criteria (independent review), which installs enforcement gates (executable action gates). Four components create a closed loop where every failure permanently strengthens the envelope. This operationalizes the AI RMF's requirement that risk management include "mechanisms for continual improvement."

### 8.2 Advisory Plus Mandatory (AI RMF: GOVERN 1.4; MANAGE 2.2)

Behavioral memory shapes agent behavior (advisory). Executable gates block violations (mandatory). Advisory systems degrade under context pressure. Mandatory systems do not. The combination is strictly stronger than either mechanism alone. This operationalizes the AI RMF principle that governance requires institutionalized practice, not documentation alone.

### 8.3 Cross-Session Continuity (AI RMF: MANAGE 4.1; GOVERN 1.5)

Persistent memory, session protocols, and operational logging together create continuous operational awareness across inherently ephemeral sessions. This operationalizes the AI RMF's requirement for ongoing risk management across the AI system lifecycle.

### 8.4 Gap-to-Governance (AI RMF: GOVERN 5.2; MANAGE 4.2)

When operational gaps are discovered during agent execution, the lessons-learned pipeline installs structural fixes within the same session: identify the gap, build the enforcement mechanism, update behavioral memory, verify through session wrap. This operationalizes the AI RMF's requirement that organizations "incorporate adjudicated feedback from relevant AI actors into system design and implementation."

### 8.5 Sovereignty by Default (AI RMF: GOVERN 6.1; GOVERN 6.2)

Platform sovereignty and vendor independence together create a system that is inherently portable. No single vendor dependency exists for critical operational state. This operationalizes the AI RMF's requirement to address "AI risks arising from third-party software and data and other supply chain issues."

---

## 9. Reference Implementation

The OAgents behavioral envelope has been implemented as a reference system operating in an enterprise infrastructure management context. The reference implementation runs on a multi-host Linux environment and manages a suite of containerized services including authentication, collaboration, communication, and version control systems. The AI operator is a large language model accessed via API, with a separate model instance from a different provider performing independent quality review.

The reference implementation demonstrates the architectural feasibility of all 26 components. Session lifecycle protocols, persistent memory systems, executable enforcement gates, impact level classification, and independent output review are all operational. The lesson-to-enforcement pipeline has been exercised: behavioral corrections have been captured, converted to memory entries, and incorporated into subsequent sessions. Cross-session continuity functions as designed -- context, incidents, and behavioral corrections from prior sessions are available at session start.

The reference implementation is not offered as empirical validation of the standard's effectiveness claims. Its purpose is to demonstrate implementability: the 26-component taxonomy is not theoretical. Each component has a concrete implementation that operates in a real environment managing real infrastructure. The design properties -- model agnosticism by architecture, enforcement-first behavioral guarantees, cross-session continuity through persistent memory -- are present in the implementation and behave as the standard specifies. Metrics reported from this implementation are preliminary, derived from a single deployment context, and should not be interpreted as a generalized benchmark.

Systematic empirical validation -- measuring quality gate effectiveness across extended deployments, comparing behavioral consistency across model providers, and quantifying the lesson-to-enforcement pipeline's impact on failure recurrence rates -- is identified as community work. The conformance evidence criteria in Appendix C define what such validation should measure. The community is invited to conduct that measurement and contribute results for incorporation in subsequent revisions of this standard.

This approach mirrors the development of successful infrastructure standards. The OAuth specification was not accompanied by empirical studies of token exchange effectiveness. It defined the protocol, demonstrated it was implementable, and invited the community to build on it. OAgents follows the same model: the taxonomy is defined, the reference implementation demonstrates feasibility, and systematic validation is the community's contribution.

---

## 10. Related Work

### 10.1 Agent Frameworks (LangChain, CrewAI, AutoGen, MetaGPT)

These frameworks address agent orchestration: tool calling, multi-agent coordination, and chain-of-thought prompting. Their contribution is the execution infrastructure -- how agents invoke tools, decompose tasks, and coordinate with other agents. Behavioral trustworthiness during execution is outside their scope. OAgents addresses the trust layer that sits above any agent framework: the pre-execution gates, post-execution verification, and operational discipline that make agent outputs reliable regardless of which orchestration framework produced them.

### 10.2 Workflow Automation (n8n, Zapier, Apache Airflow)

These platforms provide workflow orchestration: predefined sequences of data transformations and integrations triggered by events. They are designed for structured, repeatable processes where the logic is known in advance. AI agent operations differ in that the agent exercises judgment in novel situations. OAgents addresses the behavioral governance of judgment-exercising agents, a problem that workflow orchestration does not encounter and therefore does not address.

### 10.3 AI Development Environments (GitHub Copilot, Cursor, Claude Code)

These tools integrate AI models into development workflows with tool use, file manipulation, and code execution. Each is designed for interactive developer assistance within a specific product ecosystem. OAgents addresses a different problem: not interactive developer assistance, but autonomous or semi-autonomous operational agents with persistent memory, cross-session accountability, and enforcement-backed behavioral constraints. The behavioral envelope standard is compatible with and could be applied on top of any of these tools.

### 10.4 Output Validation Frameworks (Guardrails AI, NeMo Guardrails)

These frameworks provide output validation: checking individual model responses against defined constraints before delivery. This capability corresponds to the post-execution gate layer of the OAgents behavioral envelope (Section 4.2). OAgents encompasses output validation as one component within a broader framework that additionally addresses pre-execution context shaping, cross-session memory, operational discipline, enforcement mechanisms, and organizational governance.

### 10.5 Agent Behavioral Contracts (ABC)

Bhardwaj (2026) introduces Agent Behavioral Contracts, a formal framework applying Design-by-Contract principles to AI agents. ABC specifies agent behavioral expectations as tuples of Preconditions, Invariants, Governance policies, and Recovery mechanisms, with a probabilistic compliance framework and mathematical drift bounds. This is the closest methodological antecedent to OAgents in the research literature.

The two approaches address complementary concerns. ABC focuses on formal runtime specification and enforcement within a session -- what the agent must do, mathematically defined and provably bounded. OAgents focuses on operational completeness across sessions -- persistent memory, lesson-to-enforcement pipelines, organizational governance, platform sovereignty, and a NIST-aligned compliance framework for enterprise deployment. The frameworks could be composed: ABC governing runtime behavioral invariants, OAgents governing the cross-session operational envelope.

### 10.6 Organizational AI Management Standards (ISO/IEC 42001)

ISO/IEC 42001 provides a certifiable AI management system standard operating at the organizational level: governance structures, risk management processes, and accountability mechanisms for organizations that develop or deploy AI. OAgents operates at the individual agent level: the behavioral envelope that each agent carries as a structural property. These are complementary scopes -- organizational AI management and agent-level behavioral trust both need to be addressed, and OAgents-compliant agents are designed to satisfy the technical control requirements that ISO 42001 identifies at the system level.

### 10.7 Regulatory and Standards Frameworks

**NIST AI RMF 1.0 (NIST AI 100-1, 2023).** The AI Risk Management Framework is the foundational governance framework that this profile extends. The AI RMF provides the four-function structure (GOVERN, MAP, MEASURE, MANAGE) and the trustworthiness characteristics that OAgents components are designed to operationalize. OAgents is not a competitor to the AI RMF -- it is an implementation profile of it, for the specific context of enterprise AI agent operations.

**NIST AI 600-1 -- Generative AI Profile (2024).** The GenAI Profile identifies 13 risk categories specific to generative AI, including hallucination, homogenization, and harmful bias. OAgents explicitly addresses hallucination through the anti-hallucination component category. Full mapping to all 13 risk categories is planned for a subsequent revision.

**Executive Order 14110 -- Safe, Secure, and Trustworthy Artificial Intelligence (2023).** EO 14110 directed federal agencies to establish standards and guidelines for AI trustworthiness and tasked NIST with developing measurement methodologies and guidelines for AI risk. The OAgents standard is designed to be consistent with and supportive of EO 14110 implementation requirements, providing a concrete operational framework for the behavioral trustworthiness standards that EO 14110 calls for.

**NIST SP 800-207 -- Zero Trust Architecture (2020).** SP 800-207 provides the conceptual precedent for the OAgents approach: trust cannot be assumed based on network location (for ZTA) or model capability (for OAgents); it must be verified continuously through explicit mechanisms. The behavioral envelope applies Zero Trust principles to AI agent operations.

---

## 11. Adoption Path

The OAgents standard is designed for incremental adoption, consistent with the AI RMF's design as a flexible, voluntary framework. The adoption path mirrors the progression of successful infrastructure standards: specification, reference implementation, tooling, and ecosystem -- with a parallel track through the standards body process.

### Phase 1: Specification (Current)

Publish the component taxonomy, compliance levels, and AI RMF mapping as an open specification. This document represents the initial specification, submitted as a community contribution to the NIST AI RMF and published via Zenodo for persistent DOI and citability. Organizations evaluate and implement individual components. Early adopters validate the standard in production environments and submit replication results for aggregation in subsequent revisions.

**Standards track:** Submit to NIST AI RMF community as an Implementation Profile contribution. Engage with NIST's AI Agent Standards Initiative (CAISI, 2026) as a candidate technical framework. Solicit review from standards-familiar practitioners in federal and enterprise contexts.

### Phase 2: Reference Implementations

Open-source reference implementations of the behavioral envelope for popular agent frameworks (LangChain, CrewAI, raw API). These demonstrate that the standard is implementable, provide starting points for adopters, and generate the independent replication data needed to strengthen the empirical basis for subsequent revisions.

**Standards track:** Public comment period on v1.0 specification. Incorporate community feedback. Publish v1.1 with revised component definitions and expanded SHOULD-level conformance evidence criteria.

### Phase 3: Tooling and Federal Alignment

Development tools for building OAgent-compliant systems: compliance checkers, behavioral envelope scaffolding, and testing frameworks for verifying envelope effectiveness.

**Federal procurement alignment.** Federal agencies operating under EO 14110 and subject to FedRAMP and FISMA requirements need concrete implementation guidance for AI agent trustworthiness. OAgents Level 2 (OAgent-Standard) is designed to be compatible with FedRAMP Moderate control requirements as applied to AI agent systems. A formal FedRAMP alignment mapping is planned as a Phase 3 deliverable, in coordination with GSA and relevant Agency AOs.

**Standards track:** Engage IEEE and OASIS for formal standardization track. OASIS has precedent for enterprise AI standards (STIX, SAML); OAgents fits the enterprise operational security profile. IEEE P3119 and related working groups are natural venues for behavioral envelope standardization.

### Phase 4: Ecosystem and Certification

Independent quality review services. Pre-built domain-specific behavioral memory sets. Integration with organizational AI governance programs. Cross-organization behavioral envelope interoperability.

**Certification program.** Level 1 (self-assessment) and Level 2 (documented evidence) can be verified internally. Level 3 (OAgent-Autonomous) warrants third-party verification given the reduced human oversight threshold. A certification program modeled on FedRAMP's Third Party Assessment Organization (3PAO) model is the target architecture -- independent assessors evaluate evidence against published conformance criteria.

**Standards lifecycle.** The OAgents standard follows a versioned lifecycle: v1.0 (this document, draft specification) -> v1.1 (community comment incorporation) -> v2.0 (multi-agent coordination formalized, NIST AI 600-1 full coverage, FedRAMP alignment published). Major revisions require public comment periods. The open taxonomy is permanently published; implementations remain the responsibility of adopting organizations.

---

## 12. Limitations and Open Problems

**Context window cost.** The behavioral envelope consumes model context capacity. As memory entries, skill definitions, and behavioral constraints accumulate, less context is available for the task itself. Risk-proportional context loading -- loading only the most relevant constraints per task type -- is the recommended mitigation. Optimal context budget management strategies are an open research question.

**Bootstrap period.** A new OAgent deployment starts with an empty behavioral envelope. The compounding effects that make the envelope self-improving require operational history to engage. Pre-built behavioral templates by domain can reduce bootstrap time; developing such templates for common operational contexts is identified as community work.

**Verification latency.** Independent quality review and state verification add latency to every operation. Risk-proportional verification -- lighter checks for low-impact actions, full verification for high-impact ones -- is the recommended mitigation, but requires accurate impact classification. The tradeoff between verification thoroughness and operational latency is context-dependent and warrants empirical study.

**Empirical validation.** The reference implementation demonstrates architectural feasibility. Systematic empirical measurement of the standard's effectiveness -- quality gate pass rates, failure pattern recurrence reduction, cross-session continuity improvement -- remains to be conducted across diverse deployment contexts by the community. The conformance evidence criteria in Appendix C define what that measurement should look like.

**Multi-agent coordination.** The current specification is fully defined for single-agent deployments. Coordination principles for multi-agent environments are described in Section 12.1; full formal specification is future work.

**Formal verification.** Formal verification of behavioral envelope properties -- mathematical proof that enforcement gates cannot be bypassed, that memory staleness detection is complete, that the lesson-to-enforcement pipeline terminates -- would strengthen the standard's guarantees and is identified as future work.

**NIST AI 600-1 full coverage.** The current profile addresses the hallucination risk category from NIST AI 600-1 explicitly. Full mapping to all 13 GenAI risk categories is planned for a subsequent revision.

### 12.1 OAgents in Multi-Agent Environments

Many high-value operational deployments involve multiple AI agents coordinating on shared tasks: an orchestrating agent that decomposes work, specialist agents that execute subtasks, and reviewing agents that verify outputs. This specification addresses the behavioral envelope of each individual agent. The following principles govern OAgents coordination in multi-agent environments, pending full formalization in a subsequent revision.

**Each OAgent maintains its own envelope.** A compliant OAgent does not inherit behavioral guarantees from the orchestrating agent. Quality gates, memory systems, and enforcement mechanisms are properties of the individual agent, not the pipeline. An orchestrated OAgent that receives instructions from another agent MUST apply its own pre-execution gates to those instructions, including impact assessment and behavioral constraint loading.

**Incident ownership follows action authority.** The agent that takes a consequential action is the incident owner for that action. In a multi-agent pipeline, this means incident tracking responsibility does not consolidate at the orchestrator -- it remains with the executing agent. The orchestrator SHOULD maintain a cross-agent incident summary for pipeline-level observability.

**Independent quality review applies at output boundaries.** Quality review gates apply to outputs that cross agent boundaries (one agent's output becomes another agent's input). A compliant implementation SHOULD include at least one independent review gate at each significant inter-agent handoff, not only at the final pipeline output.

**Shared memory requires versioned access.** When multiple OAgents share a persistent memory store, memory entries MUST include an authoring agent identifier and a timestamp. Agents MUST NOT overwrite memory entries authored by other agents without explicit conflict resolution. This prevents behavioral contamination across agents sharing operational context.

**Enforcement gates are non-negotiable across agents.** An orchestrating agent cannot instruct a subordinate OAgent to bypass its enforcement gates. An OAgent that receives an instruction to skip a MUST-level component (e.g., "skip quality review for speed") MUST treat this as a violation of its behavioral contract and either refuse the instruction or escalate to human oversight per its impact level classification.

---

## 13. Conclusion

Enterprise AI agent operations face a trust gap that model capability cannot close. The standards infrastructure to address this gap does not yet exist: identity delegation has OAuth, network trust has SP 800-207, but AI agent behavioral trust has no equivalent standardized mechanism. OAgents proposes that mechanism -- a behavioral envelope standard that makes AI agent operations reliable, auditable, and self-improving, regardless of which model powers the agent.

The standard is presented as an AI RMF Implementation Profile, grounding its 26 components in the NIST AI RMF 1.0 functions, categories, and subcategories. Organizations implementing OAgents at Level 1 achieve baseline AI RMF alignment for operational AI agents. Organizations implementing at Level 2 achieve comprehensive AI RMF coverage. Organizations implementing at Level 3 achieve the full self-improving, sovereignty-by-default behavioral envelope that the compounding effects require.

The taxonomy is open. The component definitions, compliance levels, AI RMF mappings, and conformance evidence criteria in this document are published for the community to evaluate, implement, and extend. This is the same model as OAuth: the specification is open; implementations are the responsibility of adopting organizations. No organization needs permission to implement OAgents. Any organization that implements the MUST-level components at the specified compliance level is conformant.

We invite NIST, IEEE, OASIS, and the broader standards community to evaluate this taxonomy, contribute replication evidence, propose revisions, and engage in the public comment process as the standard matures. We specifically invite federal agencies operating under EO 14110 to evaluate OAgents as an implementation framework for the AI agent trustworthiness requirements the Executive Order mandates.

The behavioral envelope is to AI agents what OAuth was to identity delegation -- not a product, but infrastructure the industry needs. The model is a commodity. Trust is the product.

---

## References

[1] National Institute of Standards and Technology. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)* (NIST AI 100-1). U.S. Department of Commerce. https://doi.org/10.6028/NIST.AI.100-1

[2] National Institute of Standards and Technology. (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile* (NIST AI 600-1). U.S. Department of Commerce. https://doi.org/10.6028/NIST.AI.600-1

[3] Hardt, D. (Ed.). (2012). *The OAuth 2.0 Authorization Framework* (RFC 6749). Internet Engineering Task Force. https://doi.org/10.17487/RFC6749

[4] Brown, T. B., et al. (2020). Language models are few-shot learners. *Advances in Neural Information Processing Systems, 33*, 1877--1901.

[5] Schick, T., et al. (2023). Toolformer: Language models can teach themselves to use tools. *Advances in Neural Information Processing Systems, 36*.

[6] Hong, S., et al. (2024). MetaGPT: Meta programming for a multi-agent collaborative framework. *International Conference on Learning Representations*.

[7] Shinn, N., et al. (2023). Reflexion: Language agents with verbal reinforcement learning. *Advances in Neural Information Processing Systems, 36*.

[8] Yao, S., et al. (2023). ReAct: Synergizing reasoning and acting in language models. *International Conference on Learning Representations*.

[9] Longmire, J. D. (2025). *TAB v2.0: Logic Realism Theory*. Zenodo. https://doi.org/10.5281/zenodo.19226396

[10] Bhardwaj, V. P. (2026). Agent behavioral contracts: Formal specification and runtime enforcement for reliable autonomous AI agents. *arXiv preprint arXiv:2602.22302*.

[11] National Institute of Standards and Technology. (2026). *AI Agent Standards Initiative*. Center for AI Standards and Innovation (CAISI). https://www.nist.gov/caisi/ai-agent-standards-initiative

[12] Casper, S., et al. (2026). *2025 AI Agent Index: Documenting technical and safety features of deployed agentic AI systems*. arXiv preprint arXiv:2602.17753.

[13] National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A Tool for Improving Privacy through Enterprise Risk Management, Version 1.0*. U.S. Department of Commerce. https://doi.org/10.6028/NIST.CSWP.01162020

[14] National Institute of Standards and Technology. (2022). *Towards a Standard for Identifying and Managing Bias in Artificial Intelligence* (NIST SP 1270). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.1270

[15] ISO/IEC 23894:2023. *Artificial intelligence -- Guidance on risk management*. International Organization for Standardization.

[16] Executive Office of the President. (2023). *Executive Order 14110 on Safe, Secure, and Trustworthy Artificial Intelligence*. Federal Register, 88 FR 75191. https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence

[17] National Institute of Standards and Technology. (2020). *Zero Trust Architecture* (NIST SP 800-207). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-207

---

## Appendix A: AI RMF Subcategory Mapping

This appendix provides the complete mapping between OAgents components and AI RMF 1.0 subcategories. Mappings are drawn from the primary source: NIST AI 100-1 (January 2023), Tables 1-4.

**Confidence note:** GOVERN and MAP subcategory mappings are verified against the primary source (NIST AI 100-1, retrieved April 2026). MEASURE and MANAGE subcategory mappings are drawn from the primary source text with HIGH confidence for category-level assignments and MEDIUM confidence for specific subcategory numbering. Verification against the complete MEASURE and MANAGE tables in NIST AI 100-1 is recommended before submission.

### A.1 GOVERN Function Mappings

| AI RMF Subcategory | OAgents Component(s) |
|-------------------|---------------------|
| GOVERN 1.1: Legal and regulatory requirements are understood, managed, and documented. | Platform sovereignty; Vendor independence; Asset registry |
| GOVERN 1.2: Trustworthy AI characteristics are integrated into organizational policies and practices. | Persistent feedback memory; Persistent memory system; Domain skill loading |
| GOVERN 1.3: Risk management activities are determined based on risk tolerance. | Impact level classification |
| GOVERN 1.4: Risk management processes are established through transparent policies and controls. | Process enforcement gate; Executable action gates; Structured operational logging |
| GOVERN 1.5: Ongoing monitoring and periodic review are planned with defined roles. | Session lifecycle protocol; Protocol compliance verification |
| GOVERN 1.6: Mechanisms are in place to inventory AI systems. | Asset registry; Centralized work tracking |
| GOVERN 2.1: Roles and responsibilities for AI risk management are documented and clear. | Session lifecycle protocol; Centralized work tracking; Protocol compliance verification |
| GOVERN 2.2: Personnel receive AI risk management training. | Domain skill loading; Named failure mode catalog |
| GOVERN 3.2: Policies define roles for human-AI configurations and oversight. | Impact level classification; Session lifecycle protocol |
| GOVERN 4.1: Organizational practices foster a critical thinking and safety-first mindset. | Persistent feedback memory; Reasoning anchors; Named failure mode catalog |
| GOVERN 4.2: Teams document risks and communicate about impacts. | Structured operational logging; Hallucination tracking; State verification protocol |
| GOVERN 4.3: Practices enable AI testing, incident identification, and information sharing. | Independent output review; Incident lifecycle tracking; Security audit |
| GOVERN 5.2: Mechanisms enable regular incorporation of adjudicated feedback into design. | Lessons-learned pipeline; Persistent feedback memory |
| GOVERN 6.1: Policies address AI risks associated with third-party entities. | Vendor independence; Security audit; Asset registry |
| GOVERN 6.2: Contingency processes handle failures in third-party systems. | Platform sovereignty; Incident lifecycle tracking; Severity escalation rules |

### A.2 MAP Function Mappings

| AI RMF Subcategory | OAgents Component(s) |
|-------------------|---------------------|
| MAP 1.1: Intended purposes, context, and prospective settings are understood and documented. | Persistent memory system; Domain skill loading; Knowledge injection |
| MAP 2.2: AI system knowledge limits and human oversight of outputs are documented. | Named failure mode catalog; Context degradation detection; State verification protocol |
| MAP 2.3: Scientific integrity and TEVV considerations are identified and documented. | Reasoning anchors; Schema validation; Independent output review |
| MAP 3.4: Processes for operator proficiency with AI system performance are defined and documented. | Domain skill loading; Named failure mode catalog; Session lifecycle protocol |
| MAP 3.5: Processes for human oversight are defined and documented. | Impact level classification; Session lifecycle protocol |
| MAP 4.1: Approaches for mapping AI technology and legal risks of components are in place. | Vendor independence; Asset registry; Security audit |
| MAP 4.2: Internal risk controls for AI system components are identified and documented. | Platform sovereignty; Asset registry; Process enforcement gate |

### A.3 MEASURE Function Mappings

| AI RMF Subcategory | OAgents Component(s) |
|-------------------|---------------------|
| MEASURE 1.1: Approaches and metrics for measurement of AI risks are selected and implemented. | Independent output review; Schema validation; Hallucination tracking |
| MEASURE 2.5: AI system effectiveness is evaluated through TEVV processes. | Independent output review; State verification protocol; Schema validation |
| MEASURE 2.6: AI system performance is monitored for change. | Context degradation detection; Memory staleness detection; Incident lifecycle tracking |
| MEASURE 2.7: AI system security and resilience are evaluated. | Security audit; Executable action gates; Process enforcement gate |
| MEASURE 2.8: Risks from AI system use and deployment are evaluated. | Independent output review; Impact level classification; Named failure mode catalog |
| MEASURE 3.1: Mechanisms for tracking identified AI risks over time are in place. | Structured operational logging; Incident lifecycle tracking; Hallucination tracking |
| MEASURE 3.2: Risk tracking approaches are evaluated for effectiveness. | Severity escalation rules; Lessons-learned pipeline; Measure 4.1 alignment |
| MEASURE 4.1: Measurement approaches are identified and evaluated for improvement. | Lessons-learned pipeline; Hallucination tracking; Independent output review |

### A.4 MANAGE Function Mappings

| AI RMF Subcategory | OAgents Component(s) |
|-------------------|---------------------|
| MANAGE 1.1: Risks are prioritized based on assessment. | Impact level classification; Context degradation detection |
| MANAGE 1.2: Responses to risks are developed and planned. | Process enforcement gate; Executable action gates; Session lifecycle protocol |
| MANAGE 1.3: Risk response plans are implemented and documented. | Named failure mode catalog; Severity escalation rules; Memory staleness detection |
| MANAGE 1.4: Responses to third-party risks are planned. | Platform sovereignty; Vendor independence; Asset registry |
| MANAGE 2.2: Mechanisms are in place to respond to emergent risks. | Executable action gates; Process enforcement gate; Severity escalation rules |
| MANAGE 2.4: Identified risks are monitored and resources allocated. | Incident lifecycle tracking; Centralized work tracking; Structured operational logging |
| MANAGE 3.2: Incidents are monitored, documented, and reported. | Incident lifecycle tracking; Structured operational logging; Severity escalation rules |
| MANAGE 4.1: Residual risks are documented and managed. | Persistent feedback memory; Persistent memory system; Session lifecycle protocol |
| MANAGE 4.2: Processes are in place for continual improvement. | Lessons-learned pipeline; Structured operational logging; Hallucination tracking |

---

## Appendix B: Trustworthiness Characteristic Coverage

This appendix maps OAgents compliance levels to the AI RMF 1.0 trustworthiness characteristics (NIST AI 100-1, Section 3).

| Trustworthiness Characteristic | Level 1 Coverage | Level 2 Coverage | Level 3 Coverage |
|--------------------------------|-----------------|-----------------|-----------------|
| Valid and Reliable | Partial -- state verification, output review | Full -- adds schema validation, degradation detection | Full |
| Safe | Partial -- enforcement gates, impact classification | Full -- adds security audit, incident tracking | Full |
| Secure and Resilient | Partial -- executable gates | Substantial -- adds security audit, logging | Full -- adds sovereignty, vendor independence |
| Accountable and Transparent | Partial -- session protocols, output review logging | Full -- adds structured logging, compliance verification | Full |
| Explainable and Interpretable | Partial -- named failure modes, reasoning anchors | Substantial -- adds hallucination tracking | Full |
| Privacy-Enhanced | Not directly addressed -- implementer responsibility | Not directly addressed -- implementer responsibility | Not directly addressed |
| Fair with Harmful Bias Managed | Not directly addressed -- implementer responsibility | Not directly addressed -- implementer responsibility | Not directly addressed |

**Note:** Privacy-Enhanced and Fair with Harmful Bias Managed are not addressed by the OAgents behavioral envelope, which is scoped to operational reliability for enterprise AI agents managing software and infrastructure. This is a deliberate scope decision, not an oversight. The behavioral envelope provides structural support for privacy and fairness controls -- audit logging, state verification, and independent review -- but does not specify those controls.

Organizations deploying OAgents in contexts where Privacy-Enhanced or Fair with Harmful Bias Managed characteristics are material should pair this profile with the following companion frameworks:

- **NIST Privacy Framework 1.0** (NIST, 2020) for privacy risk identification, governance, and technical controls. Applicable when OAgents process personally identifiable information or generate outputs that affect individuals.
- **NIST SP 1270, "Towards a Standard for Identifying and Managing Bias in Artificial Intelligence"** (NIST, 2022) for bias identification and mitigation in AI systems. Applicable when OAgents make or influence decisions affecting individuals or groups.
- **NIST AI 600-1 (GenAI Profile), Sections on Harmful Bias and Homogenization** for generative AI-specific bias and fairness risks. Applicable when OAgents generate content at scale.
- **ISO/IEC 23894:2023, "Artificial intelligence -- Guidance on risk management"** for integrated AI risk management including fairness and rights considerations.

These companion frameworks address characteristics that require domain-specific knowledge of affected populations and use-case context -- knowledge that a general operational agent standard cannot pre-specify. The OAgents standard's enforcement mechanisms (audit logging, independent review, operational logging) are designed to be compatible with and supportive of controls defined in these companion frameworks.

---

## Appendix C: Conformance Evidence

This appendix defines observable criteria for each MUST-level component. Conformance is demonstrated by producing the specified evidence artifacts, which may be reviewed by an internal audit function or external assessor. Evidence requirements are proportionate to the component's risk significance.

### C.1 Behavioral Shaping

**Persistent feedback memory (MUST)**
- Evidence 1: A structured memory store (file-based, database, or equivalent) containing at minimum: rule text, rationale, date captured, and source session identifier for each entry.
- Evidence 2: Session startup logs showing memory entries were loaded at the beginning of each session, with entry count and load timestamp.
- Evidence 3: Demonstration that at least one behavioral correction entry exists and was applied in a subsequent session -- shown by session log referencing the memory entry by identifier.

**Named failure mode catalog (MUST)**
- Evidence 1: A documented catalog of named failure modes applicable to the agent's operational context, with description and detection indicators for each.
- Evidence 2: Session logs or review verdicts referencing at least one failure mode by name during the evaluation period.

### C.2 Quality Gates

**Independent output review (MUST)**
- Evidence 1: Review logs showing, for each reviewed output: timestamp, producing model identifier, reviewing model identifier (must differ from producing model), verdict (pass/pass-with-warnings/fail), and specific findings where verdict is not clean pass.
- Evidence 2: Confirmation that reviewing model is from a different provider than the producing model for at least the SHOULD-recommended subset of reviews, or documented rationale for same-provider review where provider diversity is not feasible.
- Evidence 3: Aggregate pass/fail statistics covering the evaluation period, with total review count as denominator.

**Process enforcement gate (MUST)**
- Evidence 1: At least one executable gate implemented at the tooling level (version control hook, CI/CD check, or equivalent) that blocks a defined class of non-compliant action.
- Evidence 2: Logs or test results demonstrating the gate fires on a known-non-compliant input and blocks the action.
- Evidence 3: Documentation of which process invariants the gate enforces (e.g., "no direct push to production without development log entry").

### C.3 Operational Discipline

**Session lifecycle protocol (MUST)**
- Evidence 1: Session startup logs showing system health check, pending incident review, and context loading were performed at the start of each session, with timestamps.
- Evidence 2: Session wrap logs showing state verification (clean commits, pushed remotes, quality reviews confirmed) was performed at the end of each session, with pass/fail status for each check.
- Evidence 3: Protocol compliance rate over the evaluation period (target: 100%).

**Impact level classification (MUST)**
- Evidence 1: A defined impact level scale (minimum: 3 levels distinguishing read-only, reversible write, and irreversible/external-facing actions) documented and accessible to the agent at runtime.
- Evidence 2: Action logs or session records showing impact level was assessed and recorded for consequential actions during the evaluation period.
- Evidence 3: At least one instance demonstrating elevated verification or human approval was triggered by a high-impact classification.

### C.4 Knowledge Injection

**Persistent memory system (MUST)**
- Evidence 1: Memory store structure showing typed entries with staleness metadata (last-verified timestamp or equivalent).
- Evidence 2: Session logs showing at least one instance of staleness detection -- a memory entry that was verified against current system state before being acted upon.
- Evidence 3: Conflict resolution log or policy showing how memory entries that conflict with observed reality are handled (reality takes precedence).

**Domain skill loading (MUST)**
- Evidence 1: At least one domain skill file (procedure, decision framework, or service-specific knowledge document) loaded into agent context at session start, with load confirmed in session startup log.
- Evidence 2: Demonstration that skill content was applied during a session -- a session action traceable to a loaded skill's guidance.

### C.5 Enforcement Mechanisms

**Executable action gates (MUST)**
- Evidence 1: At least one action gate implemented at the tooling level, distinct from prompt-level instructions (e.g., pre-commit hook, pre-push hook, CI check).
- Evidence 2: Gate source code or configuration demonstrating it is version-controlled and not modifiable by the agent at runtime.
- Evidence 3: Test or log showing gate activation on a non-compliant action.

### C.6 Anti-Hallucination

**State verification protocol (MUST)**
- Evidence 1: Session logs or agent action traces showing verification commands were executed before system state claims were made to the user (e.g., `ls` before asserting file exists, `curl` before asserting service is running).
- Evidence 2: At least one log entry showing a state claim that was corrected or withheld because verification failed.

**Memory staleness detection (MUST)**
- Evidence 1: Memory system records showing last-verified timestamps on entries.
- Evidence 2: At least one instance where a memory entry was verified and either confirmed or updated based on current system state, with the verification action logged.

### C.7 Conformance Summary Checklist

The following checklist may be used by an internal audit function or external assessor to verify Level 1 (OAgent-Basic) conformance. Each row corresponds to a MUST component.

| Component | Evidence Required | Evidence Present | Notes |
|-----------|------------------|-----------------|-------|
| Persistent feedback memory | Memory store + load logs + applied entry | | |
| Named failure mode catalog | Catalog document + session references | | |
| Independent output review | Review logs with model IDs + aggregate stats | | |
| Process enforcement gate | Gate implementation + block demonstration | | |
| Session lifecycle protocol | Startup logs + wrap logs + compliance rate | | |
| Impact level classification | Scale definition + action logs + escalation instance | | |
| Persistent memory system | Typed entries + staleness metadata + conflict policy | | |
| Domain skill loading | Skill files + load logs + applied instance | | |
| Executable action gates | Gate source + version control + activation log | | |
| State verification protocol | Verification commands in logs + corrected claim | | |
| Memory staleness detection | Timestamps + verified/updated entry log | | |

Level 2 (OAgent-Standard) conformance requires the above plus evidence for all SHOULD components, using the same principle: each SHOULD component must be demonstrable through observable artifacts available to a reviewer. Detailed evidence criteria for SHOULD components will be specified in a subsequent revision of this profile.

---

*Corresponding author: JD Longmire, Ologos Corp. jdlongmire@outlook.com. ORCID: 0009-0009-1383-7698*

*All reported metrics are from production operational deployments managing real infrastructure. No synthetic benchmarks were used.*

*This document is submitted as a community contribution to the NIST AI RMF. Comments may be directed to the author or to AIframework@nist.gov.*
