**OAgents: A Pre-Standardization Draft Profile for Operational AI Agent
Trustworthiness**

*A Community-Authored Pre-Standardization Draft*

**JD Longmire**

Northrop Grumman Fellow (unaffiliated research)

ORCID: 0009-0009-1383-7698

jdlongmire@outlook.com

  -----------------------------------------------------------------------
  **Document Type**      Pre-Standardization Draft Profile
  ---------------------- ------------------------------------------------
  **AI RMF Reference**   NIST AI 100-1 (January 2023)

  **GenAI Profile        NIST AI 600-1 (July 2024)
  Reference**            

  **Profile Version**    1.0

  **Date**               April 2026

  **Submission Posture** Community-authored pre-standardization draft
                         intended to inform AI agent standards
                         development and public review

  **DOI**                https://doi.org/10.5281/zenodo.19425020
  -----------------------------------------------------------------------

Submission Note

This document is a community-authored pre-standardization draft
proposing a behavioral control and evidence profile for operational AI
agents. It is not a NIST-issued publication, a consensus standard, or a
formally adopted federal requirement. It is intended to inform AI agent
standards development, implementation profiling, and public review, and
to support routing into future NIST, NCCoE, IEEE, OASIS, IETF, or other
voluntary consensus processes.

Requested Reviewer Action

The author requests feedback on four questions:

-   Whether this document is appropriately structured as an AI RMF
    implementation profile for operational AI agents.

-   Whether the behavioral-envelope taxonomy is technically coherent and
    materially distinct from existing identity, authorization, and
    agent-interoperability efforts.

-   Which elements are best advanced through NIST or NCCoE guidance and
    which belong in voluntary consensus venues such as IEEE, OASIS, or
    IETF-adjacent workstreams.

-   Which control definitions, conformance artifacts, or mappings should
    be revised before broader circulation.

Abstract

Large language models are increasingly deployed as operational agents
that manage infrastructure, generate enterprise content, and execute
multi-step workflows. Capability has advanced faster than trust
mechanisms. Current agent frameworks support tool use, orchestration,
and function execution, but they do not provide standardized guarantees
for operational reliability, output quality, or behavioral consistency.

This document proposes OAgents, an AI RMF implementation profile and
candidate conformance framework for operational AI agent
trustworthiness. The profile defines a behavioral envelope: a structured
set of pre-execution gates, post-execution verification controls, and
operational-discipline mechanisms. It specifies 26 controls across 7
categories, 3 conformance levels, and observable evidence criteria. The
profile is model-agnostic. The behavioral guarantees are properties of
the envelope, not of the underlying model.

The OAgents profile maps its control taxonomy to AI RMF functions,
categories, and subcategories. A reference implementation demonstrates
architectural feasibility for all 26 controls in a
development-laboratory environment with live operational use. No
generalized empirical benchmarks are claimed. Broader validation across
diverse deployment contexts remains community work.

The central claim is practical. Enterprise adoption of operational AI
agents requires a portable trust layer above model execution. OAgents
proposes that layer as a structured, implementable pre-standardization
draft, offered for community review and intended to inform future AI
agent standards development.

Foreword

This document is a pre-standardization draft structured as an AI RMF
implementation profile, as described in Section 6 of NIST AI 100-1. It
is offered for technical review, comparison, and contribution to future
standards development. It is not a finalized or adopted profile.
Profiles apply AI RMF functions, categories, and subcategories to a
defined deployment setting based on the implementing organization's
requirements, risk tolerance, and resources.

The OAgents profile addresses a specific use case: AI agents operating
in enterprise roles with authority to take consequential actions such as
deploying code, managing infrastructure, generating customer-facing
content, and responding to incidents. This is a high-autonomy,
high-consequence environment. To the author's knowledge, no prior AI RMF
implementation profile has addressed this setting at the
operational-control level. The author welcomes correction, comparison,
and competing approaches.

This draft is offered as a community contribution aligned with NIST's AI
Agent Standards Initiative and related NIST and NCCoE work on agent
security, identity, authorization, and interoperability. Its purpose is
narrower than a general AI governance framework: to propose a concrete
trust architecture for operational agents as input to future standards
work.

The profile builds on NIST AI RMF 1.0 (NIST AI 100-1) and the Generative
AI Profile (NIST AI 600-1). It explicitly addresses the AI 600-1
confabulation risk category, commonly described as hallucination,
through the Anti-Hallucination control set. Full mapping to all 12 GAI
risk categories is left for a subsequent revision.

Terminology follows AI RMF 1.0 definitions. RFC 2119 normative language,
MUST, SHOULD, and MAY, is used in Section 5 to specify conformance
requirements.

**Development methodology.** This standard and its reference
implementation were developed using a Human-Curated, AI-Enabled (HCAE)
methodology. The human architect defined operational standards, curated
behavioral corrections, and determined conformance expectations; the AI
operator implemented and maintained the behavioral envelope under those
standards. The standard is a direct artifact of operating under its own
principles.

1\. Introduction

1.1 The Trust Gap in Enterprise AI Agent Operations

Enterprise organizations are deploying AI agents in progressively
higher-stakes operational roles: writing and deploying code, managing
cloud infrastructure, generating customer-facing documents, and
responding to operational incidents. Model capability is improving. The
barrier is trust.

When a human operator deploys code to production, the organization
trusts that operator because of training, experience, accountability,
and process enforcement (code review, CI/CD gates, change management).
When an AI agent performs the same action, none of these trust
mechanisms exist by default. The agent has no persistent memory of past
mistakes. No independent reviewer checks its work. No process gate
prevents it from skipping quality checks under prompt pressure. No
institutional knowledge carries from one session to the next.

This gap between agent capability and organizational trust is the
central barrier to enterprise adoption. The 2025 AI Agent Index
underscores the maturity problem: only 4 agents provide agent-specific
system cards, 25 of 30 disclose no internal safety results, and 23 of 30
disclose no third-party testing (Casper et al., 2026). This is the risk
class the AI RMF is designed to address. The issue is not raw
capability. The issue is trustworthy operation.

The supporting standards landscape is still immature. Identity
delegation has OAuth and OpenID Connect. Network trust has NIST SP
800-207. Software supply-chain integrity has SLSA and SBOM frameworks.
Operational AI agent trust has no widely adopted equivalent. Current
NIST and NCCoE work on agent security, identity, authorization,
interoperability, and evaluation makes the gap more visible, but
control-level guidance for trustworthy agent behavior is still emerging.
OAgents is proposed as one contribution to that landscape.

1.2 The OAuth Parallel

In the early 2000s, web applications faced an analogous trust problem.
Users needed to grant third-party applications access to their data on
other platforms, but the only mechanism was sharing passwords:
unverifiable, unscoped, and irrevocable. OAuth solved this by
introducing a standardized trust layer: tokens that carry scoped
permissions, issued by identity providers, verifiable by any relying
party.

OAuth did not replace applications. It added a trust layer that made
delegation safer and more portable.

AI agents face the same structural problem. Organizations need to
delegate operational authority to AI agents, but the only mechanism is
prompt instructions: unverifiable, unenforceable, and forgotten when
context compresses. A standardized trust layer for AI agent operations
would make delegation safe regardless of which model powers the agent.

The analogy has limits. OAuth addressed a tightly bounded authorization
problem with a defined protocol exchange. AI agent trust is broader: it
includes context management, output verification, incident governance,
cross-session memory, and organizational discipline. OAgents does not
claim OAuth's protocol precision. It claims a similar architectural
role: a trust layer above execution that makes delegated operation more
governable.

That mechanism is the OAgent behavioral envelope.

1.3 Scope

This profile applies to AI agents operating in the following deployment
context:

-   Role: Operational agent with authority to take consequential actions
    (code deployment, infrastructure management, content generation,
    incident response)

-   Autonomy level: Semi-autonomous to autonomous, with defined human
    oversight thresholds

-   Environment: Enterprise operational environments with multiple
    interdependent systems

-   Model: Any large language model (the profile is model-agnostic by
    design)

This profile does not address pure inference systems without operational
authority, consumer-facing conversational AI without consequential
action capabilities, or embedded AI in physical systems (robotics,
autonomous vehicles).

This profile is scoped to operational reliability and behavioral trust.
The AI RMF trustworthiness characteristics of Privacy-Enhanced and Fair
with Harmful Bias Managed are out of scope and are not addressed by the
behavioral envelope. Organizations deploying OAgents in contexts where
these characteristics are material should pair this profile with
companion frameworks identified in Appendix B.

1.4 Terminology

**OAgent.** An AI agent operating within a behavioral envelope that
provides structured guarantees about its operational behavior. An OAgent
is conformant with this profile when it implements the components
specified at the applicable compliance level.

**OAgents.** The open profile and candidate conformance framework
defining behavioral envelope requirements, component taxonomy, and
compliance levels for trustworthy AI agent operations.

**Behavioral envelope.** The structured set of pre-execution gates,
post-execution verification, and operational discipline mechanisms that
bound an OAgent's behavior. Corresponds to the AI RMF concept of
trustworthiness characteristics instantiated as operational controls.

**Model-agnostic.** Behavioral guarantees that function identically
regardless of which large language model provides the underlying
computation. The envelope is independent of the model provider.

**AI actor** (AI RMF definition). Organizations and individuals that
play an active role in the AI system lifecycle, including those that
deploy or operate AI systems (OECD, 2019, as adopted in NIST AI 100-1).

**TEVV.** Test, Evaluation, Verification, and Validation, as defined in
AI RMF 1.0.

**RFC 2119 normative language.** MUST indicates a requirement; SHOULD
indicates a recommendation; MAY indicates an option.

1.5 Intended Adopters

**Infrastructure and platform engineering teams** deploying AI agents to
manage software systems, cloud infrastructure, CI/CD pipelines, or
operational monitoring. These teams need behavioral guarantees
equivalent to what they already require of human operators: code review,
change management, incident tracking, and documented procedures enforced
at the tooling level.

**Internal AI platform groups** building shared AI agent services for
their organizations, accountable for the reliability and trustworthiness
of AI capabilities consumed by other teams.

**Vendors building AI agent platforms** who need to demonstrate
behavioral trustworthiness to enterprise customers. OAgents provides a
NIST-aligned vocabulary and conformance structure for communicating what
behavioral guarantees a platform provides, at what compliance level, and
what evidence supports the claim.

This profile is not designed for consumer-facing conversational AI
without operational authority, pure inference pipelines, HR or credit
decisioning systems, or physical systems where safety-critical real-time
constraints require separate certification frameworks.

2\. AI RMF Alignment Statement

**GOVERN.** OAgents behavioral envelope components instantiate
governance structures as executable mechanisms: session protocols
enforce operational discipline, impact level classification enforces
risk-proportionate decision-making, and asset registries maintain
organizational accountability.

**MAP.** OAgents knowledge injection and context classification
components operationalize the MAP function's requirement to establish
and understand context before acting.

**MEASURE.** OAgents quality gate components instantiate the MEASURE
function's requirement for independent evaluation of AI system outputs.
Independent output review, schema validation, security auditing, and
hallucination tracking provide the TEVV infrastructure the AI RMF
requires.

**MANAGE.** OAgents enforcement mechanisms, incident lifecycle tracking,
and lessons-learned pipeline operationalize the MANAGE function's
requirement for active risk response and continuous improvement.

The complete subcategory mapping is provided in Appendix A.

3\. Design Principles

3.1 Behavioral Guarantees Must Be Portable Across Model Providers (AI
RMF: Valid and Reliable; Secure and Resilient)

Behavioral guarantees must be independent of the underlying model. An
organization that encodes operational trust into model-specific prompts
or vendor-specific tool configurations has created lock-in at the trust
layer, the most critical layer to keep portable. The OAgents profile
requires that all behavioral envelope components function identically
across model providers.

This is a claim about trust-layer portability, not model equivalence.
The profile does not assert that all models perform identically or that
model selection is inconsequential. It asserts that the behavioral
envelope (memory systems, enforcement gates, quality review agents, and
operational logging) operates at the infrastructure layer, outside the
model's context window and independent of any model-specific API.
Swapping the model changes the computation; it does not change the
behavioral guarantees.

The SHOULD-level recommendation that the independent reviewer come from
a different provider reinforces this principle. One provider should not
both produce and evaluate the same consequential output, and one
provider failure should not compromise both production and verification.

3.2 Enforcement Over Documentation (AI RMF: Accountable and Transparent)

Documented standards are advisory. Under context pressure, deadline
urgency, or prompt complexity, AI agents routinely violate documented
procedures. The OAgents profile requires that critical behavioral
guarantees be implemented as executable gates: mechanisms that block
non-compliant actions rather than merely discouraging them. GOVERN 1.4
calls for risk management processes to be established through
transparent policies and controls. In this profile, that means
commitments with operational consequence should be enforced by
executable gates.

3.3 Independent Verification (AI RMF: Accountable and Transparent; Valid
and Reliable)

No system can reliably evaluate its own output. An AI agent that
generates code and reviews that code in the same context is structurally
incapable of independent quality assurance. The OAgents profile requires
that quality verification be performed by a separate process with
independent context, ideally a different model instance from a different
provider. This operationalizes the AI RMF recommendation that TEVV
processes include independent review.

3.4 Persistent Learning (AI RMF: Accountable and Transparent; Safe)

AI agent sessions are ephemeral by default. Without explicit persistence
mechanisms, every session starts from zero operational knowledge. The
OAgents profile requires that operational lessons, behavioral
corrections, and contextual knowledge persist across session boundaries
and be loaded into every new session. This operationalizes the AI RMF
principle of continuous improvement.

3.5 Self-Improving Reliability (AI RMF: Safe; Secure and Resilient)

A compliant behavioral envelope must become more reliable over time.
Operational failures must feed back into the envelope's enforcement
mechanisms, creating a closed loop from failure detection to automated
prevention. This operationalizes the AI RMF's requirement that risk
management processes include mechanisms for continual improvement.

4\. Behavioral Envelope Architecture

The behavioral envelope interposes structured gates between the user's
request and the agent's action, and between the agent's output and its
delivery.

![](media/d6e2ff775d5d39214322e93777dbcc0ecdd0e03f.png){width="6.25in"
height="3.8645833333333335in"}

*Figure 1. OAgents behavioral envelope architecture. All agent actions
pass through pre- and post-execution gates. Operational gates persist
across sessions. The model is replaceable; the envelope is not.*

4.1 Pre-Execution Gates

Pre-execution gates shape context and constrain behavior before the
model processes a request. They implement the AI RMF MAP function's
requirement to establish context before acting.

**Intent classification.** Requests are categorized to determine which
tools, constraints, and verification levels apply.

**Knowledge injection.** Persistent memory from prior sessions
(behavioral corrections, project context, operational lessons) is loaded
into the model's context.

**Impact assessment.** Each potential action is classified by blast
radius (Level 1: read-only through Level 5:
irreversible/external-facing).

**Behavioral constraint loading.** Domain-specific operational
standards, quality requirements, and failure mode catalogs are loaded as
active constraints.

4.2 Post-Execution Gates

Post-execution gates verify output quality and safety before delivery.
They implement the AI RMF MEASURE function's TEVV requirements.

**Independent quality review.** A separate model instance reviews
significant outputs against defined quality criteria. Results are logged
with structured verdicts (pass, pass with warnings, fail).

**State verification.** Claims about system state are verified against
reality using diagnostic commands before being asserted to the user.

**Security scanning.** Outputs are checked for credential exposure,
injection vectors, and information leakage before delivery.

**Schema validation.** Structured outputs are validated against expected
schemas, catching malformed responses before they enter downstream
systems.

4.3 Operational Gates

Operational gates impose discipline on the agent's lifecycle across
sessions. They implement the AI RMF MANAGE function's requirements for
ongoing risk management.

**Session protocols.** Mandatory startup and shutdown procedures bookend
every operational session.

**Incident lifecycle management.** Operational failures are tracked
through a structured lifecycle with cross-session persistence and
recurrence detection.

**Operational logging.** Every significant action is logged as
structured data with timestamps and correlation identifiers.

**Lessons-learned feedback.** Operational failures flow through a
multi-stage pipeline: detection, lesson capture, quality criteria
update, and enforcement gate installation.

When multiple OAgents operate in coordination, additional principles
govern envelope interactions. These coordination principles are
specified in Section 12.1.

5\. Component Taxonomy

The OAgents profile defines 26 components across 7 categories. Normative
language follows RFC 2119: MUST indicates a conformance requirement,
SHOULD indicates a recommendation for production deployments, and MAY
indicates an optional capability. Each component is mapped to AI RMF 1.0
subcategories in Appendix A.

5.1 Behavioral Shaping

Components that modify the agent's default behavior toward operational
reliability. Addresses AI RMF trustworthiness characteristics: Valid and
Reliable; Accountable and Transparent.

  ----------------------------------------------------------------------------
  **Component**   **Level**   **Description**                  **AI RMF
                                                               Subcategory**
  --------------- ----------- -------------------------------- ---------------
  Persistent      MUST        Behavioral corrections and       GOVERN 1.2;
  feedback memory             confirmations persist across     GOVERN 4.1;
                              sessions as structured entries   MANAGE 4.1
                              with the rule, the rationale,    
                              and application guidance. Loaded 
                              into every new session context.  

  Named failure   MUST        Known agent failure patterns are MAP 2.2;
  mode catalog                explicitly named and described   MEASURE 2.5;
                              (over-confidence, stale          MANAGE 1.3
                              references, hallucinated state,  
                              scope creep, instruction drift). 
                              The agent self-monitors for      
                              cataloged patterns.              

  Context         SHOULD      The agent monitors its own       MEASURE 2.6;
  degradation                 reliability during long          MANAGE 1.1
  detection                   sessions, detecting increasing   
                              error rates, stale assumptions,  
                              or repeated questions.           
                              Degradation triggers a           
                              recommendation to terminate the  
                              session.                         

  Reasoning       SHOULD      Stable epistemological           GOVERN 4.1; MAP
  anchors                     commitments that ground          2.3
                              reasoning under ambiguity:       
                              precision over vagueness,        
                              questioning assumptions,         
                              verification before assertion.   
  ----------------------------------------------------------------------------

5.2 Quality Gates

Executable checkpoints that prevent defective work from advancing.
Addresses AI RMF trustworthiness characteristics: Valid and Reliable;
Accountable and Transparent; Safe.

  ----------------------------------------------------------------------------
  **Component**   **Level**   **Description**                  **AI RMF
                                                               Subcategory**
  --------------- ----------- -------------------------------- ---------------
  Independent     MUST        Significant outputs are reviewed MEASURE 2.5;
  output review               by a separate model instance     MEASURE 2.8;
                              with independent context. The    GOVERN 4.3
                              reviewing model SHOULD be from a 
                              different provider than the      
                              producing model. Results are     
                              logged with structured verdicts. 

  Process         MUST        Critical workflow steps (e.g.,   GOVERN 1.4;
  enforcement                 testing before production        MANAGE 1.2;
  gate                        deployment) are enforced by      MANAGE 2.2
                              executable gates that block      
                              non-compliant actions. Advisory  
                              documentation alone is           
                              insufficient for MUST-level      
                              guarantees.                      

  Security audit  SHOULD      Automated security checks run    MEASURE 2.7;
                              against outputs and affected     MANAGE 1.3;
                              systems before significant       GOVERN 6.1
                              actions. Check categories        
                              include credential exposure,     
                              injection vectors, and access    
                              control.                         

  Schema          SHOULD      Structured outputs are validated MEASURE 2.5;
  validation                  against defined schemas before   MEASURE 1.1
                              acceptance into downstream       
                              systems, catching malformed      
                              outputs from model               
                              confabulation.                   
  ----------------------------------------------------------------------------

5.3 Operational Discipline

Protocols that impose structure on agent behavior across sessions.
Addresses AI RMF trustworthiness characteristics: Accountable and
Transparent; Safe; Secure and Resilient.

  -----------------------------------------------------------------------------
  **Component**    **Level**   **Description**                  **AI RMF
                                                                Subcategory**
  ---------------- ----------- -------------------------------- ---------------
  Session          MUST        Mandatory start and wrap         GOVERN 1.5;
  lifecycle                    procedures that verify system    MANAGE 4.1;
  protocol                     state, load context, and ensure  GOVERN 2.1
                               clean handoffs. Protocol         
                               completion is verified           
                               programmatically, not assumed.   

  Impact level     MUST        Actions are classified by blast  MAP 3.5; MANAGE
  classification               radius (Level 1: read-only       1.1; GOVERN 3.2
                               through Level 5:                 
                               irreversible/external-facing).   
                               Higher levels require            
                               proportionally more verification 
                               and may require human approval.  

  Incident         SHOULD      Operational failures are tracked MANAGE 3.2;
  lifecycle                    through a persistent lifecycle   MEASURE 3.1;
  tracking                     with cross-session continuity,   MANAGE 2.4
                               recurrence detection, and        
                               severity escalation. Services    
                               with 3+ incidents in 30 days are 
                               flagged as fragile.              

  Structured       SHOULD      Every significant action is      GOVERN 1.4;
  operational                  logged as structured data with   MEASURE 3.1;
  logging                      timestamps and correlation       MANAGE 4.2
                               identifiers. Logs are            
                               append-only and support          
                               cross-session pattern analysis.  
  -----------------------------------------------------------------------------

5.4 Knowledge Injection

Systems that load operational context into the agent's working memory.
Addresses AI RMF trustworthiness characteristics: Valid and Reliable;
Explainable and Interpretable.

  ------------------------------------------------------------------------------
  **Component**     **Level**   **Description**                  **AI RMF
                                                                 Subcategory**
  ----------------- ----------- -------------------------------- ---------------
  Persistent memory MUST        Typed memory entries (behavioral GOVERN 1.2; MAP
  system                        feedback, project state,         1.1; MANAGE 4.1
                                operational context) persist     
                                across sessions. Entries include 
                                staleness metadata and MUST be   
                                verified against current state   
                                before being acted upon.         

  Domain skill      MUST        Operational knowledge            GOVERN 1.2; MAP
  loading                       (procedures, decision            1.1; MAP 3.4
                                frameworks, service-specific     
                                details) is loaded as active     
                                context for every session,       
                                ensuring consistent standards    
                                across sessions.                 

  Lessons-learned   SHOULD      Operational failures flow        MANAGE 4.2;
  pipeline                      through a closed-loop pipeline:  GOVERN 5.2;
                                detection, memory capture,       MEASURE 4.1
                                quality criteria update, and     
                                enforcement installation. Each   
                                stage feeds the next.            
  ------------------------------------------------------------------------------

5.5 Enforcement Mechanisms

Components that make behavioral guarantees executable rather than
advisory. Addresses AI RMF trustworthiness characteristics: Accountable
and Transparent; Safe.

  ----------------------------------------------------------------------------
  **Component**   **Level**   **Description**                  **AI RMF
                                                               Subcategory**
  --------------- ----------- -------------------------------- ---------------
  Executable      MUST        Critical behavioral guarantees   GOVERN 1.4;
  action gates                are implemented as gates that    MANAGE 2.2;
                              block non-compliant actions at   GOVERN 4.3
                              the tooling level (e.g., version 
                              control hooks, CI/CD checks).    
                              Prompt-level instructions alone  
                              are insufficient for MUST-level  
                              guarantees.                      

  Severity        SHOULD      Recurrence of operational        MANAGE 1.3;
  escalation                  failures automatically escalates MANAGE 3.2;
  rules                       severity. First occurrence       MEASURE 3.2
                              generates a warning; second      
                              generates an error; third        
                              generates a critical alert and   
                              structural review.               

  Protocol        SHOULD      Session protocol completion is   GOVERN 1.5;
  compliance                  verified programmatically at     MANAGE 2.2;
  verification                session wrap. Non-completion     GOVERN 2.1
                              blocks session closure until     
                              resolved.                        
  ----------------------------------------------------------------------------

5.6 Project Governance

Components that impose organizational discipline on multi-system
operations. Addresses AI RMF trustworthiness characteristics:
Accountable and Transparent; Secure and Resilient.

  ----------------------------------------------------------------------------
  **Component**   **Level**   **Description**                  **AI RMF
                                                               Subcategory**
  --------------- ----------- -------------------------------- ---------------
  Centralized     SHOULD      A single backlog spanning all    GOVERN 1.6;
  work tracking               managed systems, with structured MANAGE 4.2;
                              priority and status fields.      GOVERN 2.1
                              Reviewed and updated during      
                              every session wrap.              

  Platform        SHOULD      Critical operational data exists GOVERN 6.2;
  sovereignty                 on at least two independent      MANAGE 1.4; MAP
                              platforms simultaneously. No     4.2
                              single vendor removal can cause  
                              data loss or operational         
                              disruption.                      

  Asset registry  SHOULD      A maintained inventory of all    GOVERN 1.6; MAP
                              managed systems, accounts, and   4.1; MAP 4.2
                              platforms with sync status and   
                              gap identification. Updated when 
                              repository-level changes occur.  

  Vendor          SHOULD      Product-critical automation      GOVERN 6.1;
  independence                lives in version-controlled      GOVERN 6.2; MAP
                              code, not in third-party         4.1
                              workflow tools. No opaque        
                              vendor-managed state for         
                              critical operations.             
  ----------------------------------------------------------------------------

5.7 Anti-Hallucination

Components that detect and prevent false assertions. Addresses AI RMF
trustworthiness characteristics: Valid and Reliable; Accountable and
Transparent. Addresses NIST AI 600-1 GAI risk: Confabulation
(colloquially, hallucination).

  ----------------------------------------------------------------------------
  **Component**   **Level**   **Description**                  **AI RMF
                                                               Subcategory**
  --------------- ----------- -------------------------------- ---------------
  State           MUST        Before asserting any claim about MEASURE 2.5;
  verification                system state, the agent MUST     MAP 2.2; GOVERN
  protocol                    verify against current reality   4.2
                              using appropriate diagnostic     
                              methods. Memory of a state is    
                              not confirmation of a state.     

  Memory          MUST        Memory entries are treated as    MEASURE 2.6;
  staleness                   claims about past state. Before  MAP 1.1; MANAGE
  detection                   acting on a memory, the agent    1.3
                              verifies it against current      
                              system state. Conflicts are      
                              resolved in favor of observed    
                              reality.                         

  Hallucination   SHOULD      Detected hallucinations are      MEASURE 3.1;
  tracking                    logged with the false claim, the MEASURE 4.1;
                              truth, and the detection method. MANAGE 4.2
                              Recurrence patterns trigger      
                              quality criteria updates.        
                              Resolution requires 10+          
                              subsequent clean reviews of the  
                              same type.                       
  ----------------------------------------------------------------------------

6\. Conformance, Evidence, and Certification Path

6.1 How Conformance Is Established

OAgents conformance is established through evidence: observable
artifacts demonstrating that the specified components are implemented
and operational. Conformance is not established by assertion. A system
that claims to implement independent output review without logs showing
distinct reviewing model identifiers and structured verdicts is not
conformant, regardless of how the system is described.

The complete set of evidence criteria for MUST-level components is
specified in Appendix C. Each MUST component requires 2-3 observable
artifacts. Evidence must be producible on demand by an internal audit
function or external assessor.

6.2 Conformance Verification by Level

**Level 1 (OAgent-Basic), Self-Assessment.** Conformance is verified by
the deploying organization against the Appendix C checklist.
Self-assessment is appropriate for initial deployment, internal
governance, and low-stakes operational contexts.

**Level 2 (OAgent-Standard), Documented Evidence Review.** Conformance
is verified through a structured evidence review conducted by an
internal audit team independent of the deployment team, or by an
external reviewer. The review examines actual artifacts (session logs,
review records, enforcement gate configurations, memory store contents)
against the conformance criteria in Appendix C. Documented evidence
review is appropriate for production deployments with periodic human
oversight.

**Level 3 (OAgent-Autonomous), Third-Party Verification.** Conformance
is verified by an independent third-party assessor who has no
organizational relationship with the deploying organization. The
third-party assessor model is analogous to FedRAMP's Third Party
Assessment Organization (3PAO) structure.

6.3 Certification Status

Formal certification programs for OAgents conformance are not yet
established. This document defines the conformance criteria and evidence
requirements that a certification program would use. Level 2 conformance
criteria are structured to support future mapping to FedRAMP
Moderate-relevant control families for AI agent deployments; a formal
alignment mapping is planned as a future deliverable.

7\. Compliance Levels

The OAgents profile defines three conformance levels to support
incremental adoption consistent with the AI RMF's design as a flexible,
voluntary framework.

![](media/6e0ceaf782b9f28ef3413ddd83ea0363f0637182.png){width="6.25in"
height="3.8645833333333335in"}

*Figure 2. OAgents compliance levels. Each level adds components and
increases conformance verification rigor.*

Level 1: OAgent-Basic

All MUST components are implemented. Suitable for supervised operational
use with human oversight. Implements: Persistent feedback memory, Named
failure mode catalog, Independent output review, At least one process
enforcement gate, Session lifecycle protocol, Impact level
classification, Persistent memory system with staleness detection,
Domain skill loading, At least one executable action gate, State
verification before all assertions, Memory staleness detection.

Trustworthiness assurance: Level 1 provides baseline guarantees of valid
and reliable behavior, minimal accountability structures, and
anti-hallucination protections.

Level 2: OAgent-Standard

All MUST and SHOULD components are implemented. Suitable for production
use with periodic human oversight. Adds to Level 1: Context degradation
detection, Reasoning anchors, Security auditing, Schema validation,
Incident lifecycle tracking, Structured operational logging,
Lessons-learned pipeline, Severity escalation rules, Protocol compliance
verification, Centralized work tracking, Hallucination tracking.

Trustworthiness assurance: Level 2 provides comprehensive operational
guarantees across all seven AI RMF trustworthiness characteristics.

Level 3: OAgent-Autonomous

Level 2 compliance plus: Platform sovereignty (multi-platform data
replication), Asset registry maintenance, Vendor independence
verification, Cross-agent coordination protocols consistent with Section
12.1, and self-healing capabilities (automatic remediation of known
failure patterns without human intervention).

Trustworthiness assurance: Level 3 provides guarantees suitable for
high-autonomy deployments with minimal human oversight.

8\. Compounding Effects

Individual components provide linear value. The OAgents profile
architecture creates five compounding effects in which component
interactions produce multiplicative reliability gains over time.

8.1 Lesson-to-Enforcement Pipeline (AI RMF: MANAGE 4.2; GOVERN 5.2)

Failure detection (operational logging) feeds lesson capture (persistent
memory), which updates quality criteria (independent review), which
installs enforcement gates (executable action gates). Four components
create a closed loop where every failure permanently strengthens the
envelope.

![](media/dec8ab540b792e74563af398c70a0543ad7f88d8.png){width="6.25in"
height="2.2083333333333335in"}

*Figure 3. Lesson-to-enforcement pipeline. Every operational failure
produces four layers of defense against recurrence. The system
strengthens from its failures rather than repeating them.*

**8.2 Advisory Plus Mandatory (GOVERN 1.4; MANAGE 2.2).** Behavioral
memory shapes agent behavior (advisory). Executable gates block
violations (mandatory). Advisory systems degrade under context pressure.
Mandatory systems do not. The combination is strictly stronger than
either mechanism alone.

**8.3 Cross-Session Continuity (MANAGE 4.1; GOVERN 1.5).** Persistent
memory, session protocols, and operational logging together create
continuous operational awareness across inherently ephemeral sessions.

**8.4 Gap-to-Governance (GOVERN 5.2; MANAGE 4.2).** When operational
gaps are discovered during agent execution, the lessons-learned pipeline
installs structural fixes within the same session.

**8.5 Sovereignty by Default (GOVERN 6.1; GOVERN 6.2).** Platform
sovereignty and vendor independence together create a system that is
inherently portable. No single vendor dependency exists for critical
operational state.

9\. Reference Implementation

The OAgents behavioral envelope has been implemented as a reference
system operating in a development laboratory context. The reference
implementation runs on a multi-host Linux environment and manages a
suite of containerized services including authentication, collaboration,
communication, and version control systems. This is a
single-organization development environment, not a scaled production
deployment; it is used for active development and operational management
of the Ologos Corp technical infrastructure. The AI operator is a large
language model accessed via API, with a separate model instance from a
different provider performing independent quality review.

A sanitized snapshot of the reference implementation, with credentials,
internal addresses, and identifying information removed but with all
structural artifacts, script logic, hook mechanisms, memory schemas, and
log formats intact, is published at
https://github.com/ologos-corp/OAgents-standard/tree/main/reference.
This snapshot constitutes the evidence artifacts that Appendix C
requires conforming implementations to produce.

**Human-Curated, AI-Enabled (HCAE) methodology.** The reference
implementation was developed and operated using an HCAE methodology: a
human architect defined operational standards, curated behavioral
corrections, and determined conformance expectations; an AI operator
implemented and maintained the behavioral envelope under those
standards. This is not incidental to the profile's design; it is the
operational model the profile is built to support and constrain.

9.1 Reference Stack Summary

  -----------------------------------------------------------------------------------------------------
  **Component          **Implementation       **Primary Artifact**     **Reference File**
  Category**           Approach**                                      
  -------------------- ---------------------- ------------------------ --------------------------------
  Behavioral Shaping   YAML-frontmatter       Structured memory        memory/example_feedback.md,
                       memory entries with    store + session startup  scripts/session-start.py
                       typed fields (rule,    load log                 
                       rationale, application                          
                       guidance, date)                                 

  Quality Gates        Separate model         QA review log with model qa-agent/agent.py,
                       instance (different    IDs and verdicts         ops/examples/qa_log.json
                       provider) called via                            
                       API; structured JSON                            
                       verdict                                         
                       (pass/warnings/fail)                            
                       logged per review                               

  Operational          Python session scripts Session startup and wrap scripts/session-start.py,
  Discipline           enforcing mandatory    logs with timestamps and scripts/session-wrap.py
                       start/wrap procedures; compliance status        
                       wrap script verifies                            
                       git clean, QA                                   
                       confirmed, logs pushed                          

  Knowledge Injection  Markdown skill files   Skill files + memory     skills/sysadmin.md,
                       and memory index       index with load          memory/MEMORY.md
                       loaded into model      confirmation in session  
                       context at session     log                      
                       start; staleness                                
                       metadata in memory                              
                       frontmatter                                     

  Enforcement          Git pre-commit hook    Hook source code         hooks/pre-commit, hooks/pre-push
  Mechanisms           blocks commit without  (version-controlled) +   
                       QA review completion;  activation log           
                       pre-push hook enforces                          
                       dev-first workflow and                          
                       security scan                                   

  Project Governance   Structured JSON ops    Ops log files with       ops/README.md,
                       logs (append-only);    schema definitions       ops/examples/sysadmin_log.json
                       centralized backlog                             
                       tracked in GitHub                               
                       Projects; asset                                 
                       registry in ops                                 
                       directory                                       

  Anti-Hallucination   State verification     Verification commands in skills/quality_assurance.md,
                       commands executed      session scripts; QA log  qa-agent/prompts/qa_review.md
                       before assertions;     entries flagging false   
                       memory staleness check assertions               
                       on load; confabulation                          
                       entries logged to QA                            
                       log                                             
  -----------------------------------------------------------------------------------------------------

9.2 Operational Metrics

The following metrics are drawn from live operational logs of the
reference implementation. The reference implementation operates as a
development laboratory environment: a single-organization system used
for active development and operational management, not a scaled
production deployment. Structured logging has been active since
2026-04-02; the underlying system has been in continuous operation since
approximately mid-March 2026.

  ---------------------------------------------------------------------------------
  **Metric**                                 **Count**   **Source**
  ------------------------------------------ ----------- --------------------------
  Git commits (each triggers pre-commit and  367         git log
  pre-push hook enforcement)                             

  Independent QA reviews executed            83          ops/qa_log.json

  QA pass rate                               97.6% (81   ops/qa_log.json
                                             pass, 2     
                                             fail)       

  Automated health check executions          349         ops/sysadmin_log.json

  Security audit runs                        4           ops/security_log.json

  Lessons learned captured                   9           ops/lessons_learned.json
  (lesson-to-enforcement pipeline)                       

  Behavioral correction memories accumulated 23          memory/feedback\_\*.md

  Total persistent memory entries            49          memory/\*.md

  Confabulation catches logged               2           ops/qa_log.json
  ---------------------------------------------------------------------------------

These figures demonstrate operational use, not empirical benchmarking.
The 367 commits with associated hook enforcement events show the
enforcement gate has been active across the full project lifetime. The
83 independent QA reviews, each performed by a model instance from a
different provider than the producing agent, show the independent review
mechanism has been exercised at meaningful volume. No repeat occurrence
of the same failure pattern has been observed after enforcement
installation.

9.3 Scope and Limitations

The reference implementation demonstrates the architectural feasibility
of all 26 components. It is not offered as empirical validation of the
profile's effectiveness claims. Systematic empirical validation is
identified as community work. The conformance evidence criteria in
Appendix C define what that measurement should look like. The community
is invited to conduct that measurement using the reference
implementation as a starting point and to contribute results for
incorporation in subsequent revisions.

The appropriate sequence for a v1.0 specification is: define the
taxonomy, demonstrate feasibility, invite community validation. That is
the sequence this document follows.

10\. Related Work

**Agent Frameworks (LangChain, CrewAI, AutoGen, MetaGPT).** These
frameworks address agent orchestration. Behavioral trustworthiness
during execution is outside their scope. OAgents addresses the trust
layer that sits above any agent framework.

**Workflow Automation (n8n, Zapier, Apache Airflow).** These platforms
provide workflow orchestration for structured, repeatable processes.
OAgents addresses the behavioral governance of judgment-exercising
agents, a problem that workflow orchestration does not encounter.

**AI Development Environments (GitHub Copilot, Cursor, Claude Code).**
These tools are designed for interactive developer assistance. OAgents
addresses autonomous or semi-autonomous operational agents with
persistent memory, cross-session accountability, and enforcement-backed
behavioral constraints.

**Output Validation Frameworks (Guardrails AI, NeMo Guardrails).** These
frameworks correspond to the post-execution gate layer of the OAgents
behavioral envelope. OAgents encompasses output validation within a
broader framework that additionally addresses pre-execution shaping,
cross-session memory, operational discipline, and governance.

**Agent Behavioral Contracts (ABC, Bhardwaj 2026).** ABC focuses on
formal runtime specification and enforcement within a session. OAgents
focuses on operational completeness across sessions. The frameworks
could be composed: ABC governing runtime behavioral invariants, OAgents
governing the cross-session operational envelope.

**ISO/IEC 42001.** Operates at the organizational management system
level. OAgents operates at the individual agent level. These are
complementary scopes.

**NIST AI RMF 1.0 (NIST AI 100-1, 2023).** The foundational governance
framework this profile extends. OAgents is not a competitor to the AI
RMF; it is an implementation profile of it, for the specific context of
enterprise AI agent operations.

**NIST AI 600-1, Generative AI Profile (2024).** OAgents explicitly
addresses confabulation through the anti-hallucination component
category. Full mapping to all 12 GAI risk categories is planned for a
subsequent revision.

**NIST CAISI and NCCoE AI agent activities (2026).** NIST's AI Agent
Standards Initiative and the NCCoE concept paper on software and AI
agent identity and authorization highlight an active federal interest in
agent security, interoperability, authorization, auditing, and
non-repudiation. OAgents is designed to be consistent with and
supportive of that emerging landscape.

**NIST SP 800-207, Zero Trust Architecture (2020).** SP 800-207 provides
the conceptual precedent: trust must be verified continuously through
explicit mechanisms, not assumed based on network location or model
capability. The behavioral envelope applies Zero Trust principles to AI
agent operations.

11\. Adoption Path

**Phase 1 \-- Specification (Current).** Publish the component taxonomy,
conformance levels, and AI RMF mapping as an open specification.
Published via Zenodo (DOI: https://doi.org/10.5281/zenodo.19425020).
Standards track: Share with NIST AI RMF community as an implementation
profile example and with CAISI and NCCoE as a candidate technical
framework for operational agent trust.

**Phase 2 \-- Reference Implementations.** Open-source reference
implementations of the behavioral envelope for popular agent frameworks
(LangChain, CrewAI, raw API). Standards track: Public comment period on
v1.0 specification. Publish v1.1 with revised component definitions and
expanded SHOULD-level conformance evidence criteria.

**Phase 3 \-- Tooling and Federal Alignment.** Development tools for
building OAgent-conformant systems: compliance checkers, behavioral
envelope scaffolding, and testing frameworks. Federal alignment: Level 2
(OAgent-Standard) is intended to support future mapping to FedRAMP
Moderate-relevant control families for AI agent deployments. A formal
alignment mapping is planned as a Phase 3 deliverable, in coordination
with GSA and relevant Agency AOs. Standards track: Engage IEEE, OASIS,
and where appropriate IETF-adjacent communities.

**Phase 4 \-- Ecosystem and Certification.** Independent quality review
services. Pre-built domain-specific behavioral memory sets. A
certification program modeled on FedRAMP's 3PAO structure. Standards
lifecycle: v1.0 (draft specification) → v1.1 (community comment
incorporation) → v2.0 (multi-agent coordination formalized, NIST AI
600-1 full coverage, FedRAMP alignment published).

12\. Limitations and Open Problems

**Context window cost.** The behavioral envelope consumes model context
capacity. Risk-proportional context loading is the recommended
mitigation. Optimal context budget management strategies are an open
research question.

**Bootstrap period.** A new OAgent deployment starts with an empty
behavioral envelope. Pre-built behavioral templates by domain can reduce
bootstrap time; developing such templates is identified as community
work.

**Verification latency.** Independent quality review and state
verification add latency to every operation. Risk-proportional
verification is the recommended mitigation, but requires accurate impact
classification.

**Empirical validation.** Systematic empirical measurement of the
profile's effectiveness remains to be conducted across diverse
deployment contexts by the community. Appendix C defines what that
measurement should look like.

**Multi-agent coordination.** The current specification is fully defined
for single-agent deployments. Coordination principles for multi-agent
environments are described in Section 12.1; full formal specification is
future work.

**Formal verification.** Mathematical proof that enforcement gates
cannot be bypassed, that memory staleness detection is complete, that
the lesson-to-enforcement pipeline terminates, is identified as future
work.

**NIST AI 600-1 full coverage.** The current profile explicitly
addresses the confabulation risk category. Full mapping to all 12 GAI
risk categories is planned for a subsequent revision.

12.1 OAgents in Multi-Agent Environments

Many high-value operational deployments involve multiple AI agents
coordinating on shared tasks. This specification addresses the
behavioral envelope of each individual agent. The following principles
govern OAgents coordination in multi-agent environments, pending full
formalization in a subsequent revision.

**Each OAgent maintains its own envelope.** A compliant OAgent does not
inherit behavioral guarantees from the orchestrating agent. An
orchestrated OAgent MUST apply its own pre-execution gates to
instructions received from another agent.

**Incident ownership follows action authority.** The agent that takes a
consequential action is the incident owner for that action. The
orchestrator SHOULD maintain a cross-agent incident summary for
pipeline-level observability.

**Independent quality review applies at output boundaries.** A compliant
implementation SHOULD include at least one independent review gate at
each significant inter-agent handoff, not only at the final pipeline
output.

**Shared memory requires versioned access.** Memory entries MUST include
an authoring agent identifier and a timestamp. Agents MUST NOT overwrite
memory entries authored by other agents without explicit conflict
resolution.

**Enforcement gates are non-negotiable across agents.** An orchestrating
agent cannot instruct a subordinate OAgent to bypass its enforcement
gates. An OAgent that receives an instruction to skip a MUST-level
component MUST treat this as a violation of its behavioral contract and
either refuse the instruction or escalate to human oversight.

13\. Conclusion

Enterprise AI agents operating in high-autonomy roles such as code
deployment, infrastructure management, and incident response face a
trust gap that model capability alone cannot close. The standards
infrastructure to address this gap is nascent: identity delegation has
OAuth, network trust has SP 800-207, but a control and conformance
profile for operational AI agent behavioral trust has no widely adopted
equivalent. OAgents contributes to that developing landscape through a
behavioral-envelope profile that makes AI agent operations reliable,
auditable, and self-improving for enterprise operational contexts,
regardless of which model powers the agent.

This draft is structured as an AI RMF Implementation Profile, grounding
its 26 components in the NIST AI RMF 1.0 functions, categories, and
subcategories, and offered as pre-standardization input for community
evaluation and future consensus development. The taxonomy is open. No
organization needs permission to implement the profile. Any organization
that implements the required controls at the stated conformance level
may claim conformance on the terms defined here.

We invite NIST, NCCoE, IEEE, OASIS, and the broader standards community
to evaluate this taxonomy, contribute replication evidence, propose
revisions, and engage in public comment and consensus processes as the
profile matures. We specifically invite federal agencies, regulated
enterprises, and enterprise platform teams to evaluate OAgents as an
implementation framework for AI agent trustworthiness, auditability, and
operational discipline.

OAgents offers a reviewable, implementable profile for behavioral trust
in operational AI agents. Its control taxonomy is explicit, its evidence
criteria are observable, and its reference implementation is available
for scrutiny and replication.

13A. Suggested Submission Cover Memo

The following text may be used as a concise submission note when sharing
this document with NIST, NCCoE, or other standards-facing reviewers.

> *Subject: Pre-standardization draft profile for trustworthy
> operational AI agents*
>
> *Dear Reviewer,*
>
> *Attached is OAgents: A Pre-Standardization Draft Profile for
> Operational AI Agent Trustworthiness. The document is a
> community-authored pre-standardization draft aligned with the NIST AI
> Risk Management Framework and with current NIST and NCCoE work on AI
> agent security, identity, authorization, interoperability, and
> evaluation.*
>
> *OAgents proposes a behavioral control and evidence profile for
> operational AI agents that take consequential actions in enterprise
> environments. The draft defines 26 controls across 7 categories, three
> conformance levels, and observable evidence criteria intended to
> support implementation, comparison, and future consensus development.*
>
> *This submission is not offered as a claim of NIST endorsement or as a
> request for immediate federal adoption. It is a pre-standardization
> contribution. The request is narrower: consideration as input to AI
> agent standards development, feedback on technical fit, and routing
> guidance regarding the most appropriate pathway or collaborative
> venue.*
>
> *Respectfully,*
>
> *JD Longmire*

References

\[1\] National Institute of Standards and Technology. (2023). Artificial
Intelligence Risk Management Framework (AI RMF 1.0) (NIST AI 100-1).
https://doi.org/10.6028/NIST.AI.100-1

\[2\] National Institute of Standards and Technology. (2024). AI Risk
Management Framework: Generative Artificial Intelligence Profile (NIST
AI 600-1). https://doi.org/10.6028/NIST.AI.600-1

\[3\] Hardt, D. (Ed.). (2012). The OAuth 2.0 Authorization Framework
(RFC 6749). IETF. https://doi.org/10.17487/RFC6749

\[4\] Brown, T. B., Mann, B., Ryder, N., et al. (2020). Language models
are few-shot learners. Advances in Neural Information Processing
Systems, 33, 1877-1901. arXiv:2005.14165.

\[5\] Schick, T., Dwivedi-Yu, J., Dessi, R., et al. (2023). Toolformer:
Language models can teach themselves to use tools. Advances in Neural
Information Processing Systems, 36. arXiv:2302.04761.

\[6\] Hong, S., Zhuge, M., Chen, J., et al. (2024). MetaGPT: Meta
programming for a multi-agent collaborative framework. ICLR.
arXiv:2308.00352.

\[7\] Shinn, N., Cassano, F., Berman, E., et al. (2023). Reflexion:
Language agents with verbal reinforcement learning. Advances in Neural
Information Processing Systems, 36. arXiv:2303.11366.

\[8\] Yao, S., Zhao, J., Yu, D., et al. (2023). ReAct: Synergizing
reasoning and acting in language models. ICLR. arXiv:2210.03629.

\[9\] Bhardwaj, V. P. (2026). Agent behavioral contracts: Formal
specification and runtime enforcement for reliable autonomous AI agents.
arXiv:2602.22302.

\[10\] National Institute of Standards and Technology. (2026). AI Agent
Standards Initiative. Center for AI Standards and Innovation.
https://www.nist.gov/caisi/ai-agent-standards-initiative

\[10a\] National Institute of Standards and Technology. (2026).
Accelerating the Adoption of Software and AI Agent Identity and
Authorization (Initial Public Draft Concept Paper). National
Cybersecurity Center of Excellence.
https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf

\[11\] Casper, S., Grossman, E., Bailey, L., et al. (2026). The 2025 AI
Agent Index: Documenting technical and safety features of deployed
agentic AI systems. arXiv:2602.17753.

\[12\] National Institute of Standards and Technology. (2020). NIST
Privacy Framework: A Tool for Improving Privacy through Enterprise Risk
Management, Version 1.0. https://doi.org/10.6028/NIST.CSWP.01162020

\[13\] National Institute of Standards and Technology. (2022). Towards a
Standard for Identifying and Managing Bias in Artificial Intelligence
(NIST Special Publication 1270). https://doi.org/10.6028/NIST.SP.1270

\[14\] ISO/IEC 23894:2023. Artificial intelligence, Guidance on risk
management. International Organization for Standardization.

\[14a\] ISO/IEC 42001:2023. Information technology, Artificial
intelligence, Management system. International Organization for
Standardization.

\[15\] National Institute of Standards and Technology. (2026). Standards
Information Center.
https://www.nist.gov/standardsgov/standards-information-center

\[16\] National Institute of Standards and Technology. (2020). Zero
Trust Architecture (NIST Special Publication 800-207).
https://doi.org/10.6028/NIST.SP.800-207

Appendix A: AI RMF Subcategory Mapping

This appendix provides the complete mapping between OAgents components
and AI RMF 1.0 subcategories. Mappings are drawn from the primary
source: NIST AI 100-1 (January 2023), Tables 1-4. The AI RMF subcategory
labels are verified primary-source anchors; the component-to-subcategory
assignments are authorial interpretive mappings proposed for community
scrutiny.

A.1 GOVERN Function Mappings

  -----------------------------------------------------------------------
  **AI RMF              **OAgents Component(s)**
  Subcategory**         
  --------------------- -------------------------------------------------
  GOVERN 1.1: Legal and Platform sovereignty; Vendor independence; Asset
  regulatory            registry
  requirements are      
  understood, managed,  
  and documented.       

  GOVERN 1.2:           Persistent feedback memory; Persistent memory
  Trustworthy AI        system; Domain skill loading
  characteristics are   
  integrated into       
  organizational        
  policies and          
  practices.            

  GOVERN 1.3: Risk      Impact level classification
  management activities 
  are determined based  
  on risk tolerance.    

  GOVERN 1.4: Risk      Process enforcement gate; Executable action
  management processes  gates; Structured operational logging
  are established       
  through transparent   
  policies and          
  controls.             

  GOVERN 1.5: Ongoing   Session lifecycle protocol; Protocol compliance
  monitoring and        verification
  periodic review are   
  planned with defined  
  roles.                

  GOVERN 1.6:           Asset registry; Centralized work tracking
  Mechanisms are in     
  place to inventory AI 
  systems.              

  GOVERN 2.1: Roles and Session lifecycle protocol; Centralized work
  responsibilities for  tracking; Protocol compliance verification
  AI risk management    
  are documented and    
  clear.                

  GOVERN 2.2: Personnel Domain skill loading; Named failure mode catalog
  receive AI risk       
  management training.  

  GOVERN 3.2: Policies  Impact level classification; Session lifecycle
  define roles for      protocol
  human-AI              
  configurations and    
  oversight.            

  GOVERN 4.1:           Persistent feedback memory; Reasoning anchors;
  Organizational        Named failure mode catalog
  practices foster a    
  critical thinking and 
  safety-first mindset. 

  GOVERN 4.2: Teams     Structured operational logging; Hallucination
  document risks and    tracking; State verification protocol
  communicate about     
  impacts.              

  GOVERN 4.3: Practices Independent output review; Incident lifecycle
  enable AI testing,    tracking; Security audit
  incident              
  identification, and   
  information sharing.  

  GOVERN 5.2:           Lessons-learned pipeline; Persistent feedback
  Mechanisms enable     memory
  regular incorporation 
  of adjudicated        
  feedback into design. 

  GOVERN 6.1: Policies  Vendor independence; Security audit; Asset
  address AI risks      registry
  associated with       
  third-party entities. 

  GOVERN 6.2:           Platform sovereignty; Incident lifecycle
  Contingency processes tracking; Severity escalation rules
  handle failures in    
  third-party systems.  
  -----------------------------------------------------------------------

A.2 MAP Function Mappings

  -----------------------------------------------------------------------
  **AI RMF              **OAgents Component(s)**
  Subcategory**         
  --------------------- -------------------------------------------------
  MAP 1.1: Intended     Persistent memory system; Domain skill loading;
  purposes, context,    Knowledge injection
  and prospective       
  settings are          
  understood and        
  documented.           

  MAP 2.2: AI system    Named failure mode catalog; Context degradation
  knowledge limits and  detection; State verification protocol
  human oversight of    
  outputs are           
  documented.           

  MAP 2.3: Scientific   Reasoning anchors; Schema validation; Independent
  integrity and TEVV    output review
  considerations are    
  identified and        
  documented.           

  MAP 3.4: Processes    Domain skill loading; Named failure mode catalog;
  for operator          Session lifecycle protocol
  proficiency with AI   
  system performance    
  are defined and       
  documented.           

  MAP 3.5: Processes    Impact level classification; Session lifecycle
  for human oversight   protocol
  are defined and       
  documented.           

  MAP 4.1: Approaches   Vendor independence; Asset registry; Security
  for mapping AI        audit
  technology and legal  
  risks of components   
  are in place.         

  MAP 4.2: Internal     Platform sovereignty; Asset registry; Process
  risk controls for AI  enforcement gate
  system components are 
  identified and        
  documented.           
  -----------------------------------------------------------------------

A.3 MEASURE Function Mappings

  -----------------------------------------------------------------------
  **AI RMF              **OAgents Component(s)**
  Subcategory**         
  --------------------- -------------------------------------------------
  MEASURE 1.1:          Independent output review; Schema validation;
  Approaches and        Hallucination tracking
  metrics for           
  measurement of AI     
  risks are selected    
  and implemented.      

  MEASURE 2.5: AI       Independent output review; State verification
  system effectiveness  protocol; Schema validation
  is evaluated through  
  TEVV processes.       

  MEASURE 2.6: AI       Context degradation detection; Memory staleness
  system performance is detection; Incident lifecycle tracking
  monitored for change. 

  MEASURE 2.7: AI       Security audit; Executable action gates; Process
  system security and   enforcement gate
  resilience are        
  evaluated.            

  MEASURE 2.8: Risks    Independent output review; Impact level
  from AI system use    classification; Named failure mode catalog
  and deployment are    
  evaluated.            

  MEASURE 3.1:          Structured operational logging; Incident
  Mechanisms for        lifecycle tracking; Hallucination tracking
  tracking identified   
  AI risks over time    
  are in place.         

  MEASURE 3.2: Risk     Severity escalation rules; Lessons-learned
  tracking approaches   pipeline
  are evaluated for     
  effectiveness.        

  MEASURE 4.1:          Lessons-learned pipeline; Hallucination tracking;
  Measurement           Independent output review
  approaches are        
  identified and        
  evaluated for         
  improvement.          
  -----------------------------------------------------------------------

A.4 MANAGE Function Mappings

  -----------------------------------------------------------------------
  **AI RMF              **OAgents Component(s)**
  Subcategory**         
  --------------------- -------------------------------------------------
  MANAGE 1.1: Risks are Impact level classification; Context degradation
  prioritized based on  detection
  assessment.           

  MANAGE 1.2: Responses Process enforcement gate; Executable action
  to risks are          gates; Session lifecycle protocol
  developed and         
  planned.              

  MANAGE 1.3: Risk      Named failure mode catalog; Severity escalation
  response plans are    rules; Memory staleness detection
  implemented and       
  documented.           

  MANAGE 1.4: Responses Platform sovereignty; Vendor independence; Asset
  to third-party risks  registry
  are planned.          

  MANAGE 2.2:           Executable action gates; Process enforcement
  Mechanisms are in     gate; Severity escalation rules
  place to respond to   
  emergent risks.       

  MANAGE 2.4:           Incident lifecycle tracking; Centralized work
  Identified risks are  tracking; Structured operational logging
  monitored and         
  resources allocated.  

  MANAGE 3.2: Incidents Incident lifecycle tracking; Structured
  are monitored,        operational logging; Severity escalation rules
  documented, and       
  reported.             

  MANAGE 4.1: Residual  Persistent feedback memory; Persistent memory
  risks are documented  system; Session lifecycle protocol
  and managed.          

  MANAGE 4.2: Processes Lessons-learned pipeline; Structured operational
  are in place for      logging; Hallucination tracking
  continual             
  improvement.          
  -----------------------------------------------------------------------

Appendix B: Trustworthiness Characteristic Coverage

This appendix maps OAgents compliance levels to the AI RMF 1.0
trustworthiness characteristics (NIST AI 100-1, Section 3).

  ---------------------------------------------------------------------------------
  **Trustworthiness        **Level 1**      **Level 2**      **Level 3**
  Characteristic**                                           
  ------------------------ ---------------- ---------------- ----------------------
  Valid and Reliable       Partial: state   Full: adds       Full
                           verification,    schema           
                           output review    validation,      
                                            degradation      
                                            detection        

  Safe                     Partial:         Full: adds       Full
                           enforcement      security audit,  
                           gates, impact    incident         
                           classification   tracking         

  Secure and Resilient     Partial:         Substantial:     Full: adds
                           executable gates adds security    sovereignty, vendor
                                            audit, logging   independence

  Accountable and          Partial: session Full: adds       Full
  Transparent              protocols,       structured       
                           output review    logging,         
                           logging          compliance       
                                            verification     

  Explainable and          Partial: named   Substantial:     Full
  Interpretable            failure modes,   adds             
                           reasoning        hallucination    
                           anchors          tracking         

  Privacy-Enhanced         Not directly     Not directly     Not directly addressed
                           addressed \--    addressed \--    
                           implementer      implementer      
                           responsibility   responsibility   

  Fair with Harmful Bias   Not directly     Not directly     Not directly addressed
  Managed                  addressed \--    addressed \--    
                           implementer      implementer      
                           responsibility   responsibility   
  ---------------------------------------------------------------------------------

Privacy-Enhanced and Fair with Harmful Bias Managed are not addressed by
the OAgents behavioral envelope, which is scoped to operational
reliability for enterprise AI agents managing software and
infrastructure. This is a deliberate scope decision, not an oversight.
Organizations deploying OAgents in contexts where these characteristics
are material should pair this profile with: NIST Privacy Framework 1.0;
NIST SP 1270 for bias identification and mitigation; NIST AI 600-1
(GenAI Profile) Sections on Harmful Bias and Homogenization; and ISO/IEC
23894:2023 for integrated AI risk management.

Appendix C: Conformance Evidence

This appendix defines observable criteria for each MUST-level component.
Conformance is demonstrated by producing the specified evidence
artifacts, which may be reviewed by an internal audit function or
external assessor. Evidence requirements are proportionate to the
component's risk significance. Evidence completeness (the ability to
produce all specified artifacts on demand) is the conformance
requirement; it is not expected that all artifacts will exist from day
one of a deployment. Implementations build toward complete evidence as
the system matures.

C.1 Behavioral Shaping

**Persistent feedback memory (MUST)**

-   Evidence 1: A structured memory store containing at minimum: rule
    text, rationale, date captured, and source session identifier for
    each entry.

-   Evidence 2: Session startup logs showing memory entries were loaded
    at the beginning of each session, with entry count and load
    timestamp.

-   Evidence 3: Demonstration that at least one behavioral correction
    entry exists and was applied in a subsequent session.

**Named failure mode catalog (MUST)**

-   Evidence 1: A documented catalog of named failure modes applicable
    to the agent's operational context, with description and detection
    indicators for each.

-   Evidence 2: Session logs or review verdicts referencing at least one
    failure mode by name during the evaluation period.

C.2 Quality Gates

**Independent output review (MUST)**

-   Evidence 1: Review logs showing for each reviewed output: timestamp,
    producing model identifier, reviewing model identifier (must
    differ), verdict, and specific findings where verdict is not clean
    pass.

-   Evidence 2: Confirmation that reviewing model is from a different
    provider, or documented rationale where provider diversity is not
    feasible.

-   Evidence 3: Aggregate pass/fail statistics covering the evaluation
    period, with total review count as denominator.

**Process enforcement gate (MUST)**

-   Evidence 1: At least one executable gate implemented at the tooling
    level that blocks a defined class of non-compliant action.

-   Evidence 2: Logs or test results demonstrating the gate fires on a
    known-non-compliant input and blocks the action.

-   Evidence 3: Documentation of which process invariants the gate
    enforces.

C.3 Operational Discipline

**Session lifecycle protocol (MUST)**

-   Evidence 1: Session startup logs showing system health check,
    pending incident review, and context loading were performed, with
    timestamps.

-   Evidence 2: Session wrap logs showing state verification was
    performed, with pass/fail status for each check.

-   Evidence 3: Protocol compliance rate over the evaluation period
    (target: 100%).

**Impact level classification (MUST)**

-   Evidence 1: A defined impact level scale (minimum: 3 levels
    distinguishing read-only, reversible write, and
    irreversible/external-facing actions).

-   Evidence 2: Action logs showing impact level was assessed and
    recorded for consequential actions during the evaluation period.

-   Evidence 3: At least one instance demonstrating elevated
    verification or human approval was triggered by a high-impact
    classification.

C.4 Knowledge Injection

**Persistent memory system (MUST)**

-   Evidence 1: Memory store structure showing typed entries with
    staleness metadata (last-verified timestamp or equivalent).

-   Evidence 2: Session logs showing at least one instance of staleness
    detection: a memory entry verified against current system state
    before being acted upon.

-   Evidence 3: Conflict resolution log or policy showing how memory
    entries that conflict with observed reality are handled.

**Domain skill loading (MUST)**

-   Evidence 1: At least one domain skill file loaded into agent context
    at session start, with load confirmed in session startup log.

-   Evidence 2: Demonstration that skill content was applied during a
    session: an action traceable to a loaded skill's guidance.

C.5 Enforcement Mechanisms

**Executable action gates (MUST)**

-   Evidence 1: At least one action gate implemented at the tooling
    level, distinct from prompt-level instructions.

-   Evidence 2: Gate source code or configuration demonstrating it is
    version-controlled and not modifiable by the agent at runtime.

-   Evidence 3: Test or log showing gate activation on a non-compliant
    action.

C.6 Anti-Hallucination

**State verification protocol (MUST)**

-   Evidence 1: Session logs showing verification commands were executed
    before system state claims were made to the user.

-   Evidence 2: At least one log entry showing a state claim that was
    corrected or withheld because verification failed.

**Memory staleness detection (MUST)**

-   Evidence 1: Memory system records showing last-verified timestamps
    on entries.

-   Evidence 2: At least one instance where a memory entry was verified
    and either confirmed or updated based on current system state, with
    the verification action logged.

C.7 Conformance Summary Checklist

The following checklist may be used by an internal audit function or
external assessor to verify Level 1 (OAgent-Basic) conformance.

  ---------------------------------------------------------------------------
  **Component**         **Evidence         **Evidence   **Notes**
                        Required**         Present**    
  --------------------- ------------------ ------------ ---------------------
  Persistent feedback   Memory store +                  
  memory                load logs +                     
                        applied entry                   

  Named failure mode    Catalog document +              
  catalog               session references              

  Independent output    Review logs with                
  review                model IDs +                     
                        aggregate stats                 

  Process enforcement   Gate                            
  gate                  implementation +                
                        block                           
                        demonstration                   

  Session lifecycle     Startup logs +                  
  protocol              wrap logs +                     
                        compliance rate                 

  Impact level          Scale definition +              
  classification        action logs +                   
                        escalation                      
                        instance                        

  Persistent memory     Typed entries +                 
  system                staleness                       
                        metadata +                      
                        conflict policy                 

  Domain skill loading  Skill files + load              
                        logs + applied                  
                        instance                        

  Executable action     Gate source +                   
  gates                 version control +               
                        activation log                  

  State verification    Verification                    
  protocol              commands in logs +              
                        corrected claim                 

  Memory staleness      Timestamps +                    
  detection             verified/updated                
                        entry log                       
  ---------------------------------------------------------------------------

Level 2 (OAgent-Standard) conformance requires the above plus evidence
for all SHOULD components. Detailed evidence criteria for SHOULD
components will be specified in a subsequent revision of this profile.

*Corresponding author: JD Longmire, Northrop Grumman Fellow
(unaffiliated research). jdlongmire@outlook.com. ORCID:
0009-0009-1383-7698*

*Published: https://doi.org/10.5281/zenodo.19425020*

*This document is offered as a community implementation profile aligned
with the NIST AI RMF. Comments and replication results may be directed
to the author.*
