# aide-canon

**AI-centric Digital Ecosystem (AIDE)** — the canonical home for the AIDE corpus. Independent research by **James D. Longmire** (Northrop Grumman Fellow, Chief Architect – Digital Ecosystems; ORCID [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)). One construct in the corpus, **Mx-Modes**, is co-authored with **Micah Longmire** ([ORCID 0009-0006-7608-9322](https://orcid.org/0009-0006-7608-9322)); attribution is recorded per-construct.

This canon consolidates the foundational, methodological, enterprise-altitude, and related work into a single navigable structure. The canon's identity is **AI-centric Digital Ecosystem (AIDE)** — the architectural surface a digitally-realized enterprise must compose to operate trustworthy AI at scale.

> *This canon presents independent research and reflects the views of the author(s). It does not represent the position of any employer or program.*

---

![AIDE Architecture Overview](infographics/AIDE-Architecture-Overview.png)

*High-level AIDE architecture overview — marketing/communication tier. Canonical architecture diagrams are rendered from construct and platform schemas via ArchiMate + pyArchimate at build time (per ADR-ORDSA-0005). The two tiers coexist with different purposes.*

---

## Canon structure

Four content tiers stratified by altitude and role:

| Tier | What it holds | Members |
|---|---|---|
| **[`foundation/`](foundation/)** | Upstream cognitive-theory + training-methodology grounding for the AIDE architecture | HCAE · AIDK · RLEG |
| **[`constructs/`](constructs/)** | Peer methodological patterns, transverse to altitude | DEA · OrdSA · MxM · OAgents |
| **[`enterprise-platforms/`](enterprise-platforms/)** | Enterprise-altitude instantiations of the constructs | Strategy · AEON · AIDEX · OAAD |
| **[`related-work/`](related-work/)** | Allied research that informs the canon without being part of its spine | Theseus |

Two cross-cutting directories:

- **[`decisions/`](decisions/)** — canon-level Architecture Decision Records (umbrella + structural)
- **[`infographics/`](infographics/)** — canon-level visuals (cross-construct, cross-platform)

A reserved **`thesis/`** directory will hold the master thesis once the constituent DOIs mint and synthesis lands.

---

## Foundation — the upstream basis

Three artifacts establish the canon's grounding in cognitive-theory and training-methodology. The argument lineage is explicit:

> **[AIDK](foundation/aidk/)** (AI has structural epistemic limits) → **[HCAE](foundation/hcae/)** (so AI work must be human-curated) → **[AIDEX](enterprise-platforms/aidex/)** (architectural expression of HCAE at the experience layer) → **[AEON](enterprise-platforms/aeon/)** (control plane the deployment lives in)

| Artifact | Status | DOI |
|---|---|---|
| **HCAE** — *Human-Curated, AI-Enabled: A Framework for Reliable AI Deployment* | Published | [`10.5281/zenodo.18368697`](https://doi.org/10.5281/zenodo.18368697) |
| **AIDK** — *AI Dunning-Kruger: A Framework for Understanding Structural Epistemic Limitations* | Published | [`10.5281/zenodo.18316059`](https://doi.org/10.5281/zenodo.18316059) |
| **RLEG** — *From RLHF to RLEG: Expert Grounding as a Solution to the Fluency-Calibration Tradeoff* | In draft | (deposit pending) |

RLEG sits adjacent to HCAE: HCAE prescribes human curation of AI output at the practice level; RLEG addresses the training-methodology level — replacing RLHF with Reinforcement Learning from Expert Guidance.

---

## Constructs — four peer methodological patterns

Four methodological constructs sit at the same tier, each patterning a different concern. None subsumes another; they compose:

| Construct | What it patterns | Canonical artifact |
|---|---|---|
| **[DEA](constructs/dea/)** | EA coherence — three-baseline architecture frame (Digital Capability / Digital Technical / Digital Operational baselines, owned by EA / Systems / Solutions architecture disciplines) | `Digital-Ecosystems-Architecture-Base.pdf` |
| **[OrdSA](constructs/ordsa/)** | Authority and evidence — seven-ordinal layering (O0 Enterprise Intent → O6 Outcome/Audit/Feedback). Schema-first canonical (`schema/ordsa-0.2.yaml`); prose is companion | `schema/ordsa-0.2.yaml` + concept paper |
| **[MxM](constructs/mxm/)** | Harness — five-surface composition archetype (Mind / Morals / Mission / Memory / Means); applies at any harness altitude, not just per-agent | `Mx-Modes-Technical-Reference.pdf` |
| **[OAgents](constructs/oagents/)** | Agent — behavioral envelope standard + reference implementation; specifies what an agent **is** as a typed object. Schema-first canonical (`spec/oagents-nist-standard-v16.0.md`); paper is companion | `spec/oagents-nist-standard-v16.0.md` |

The enterprise-platforms below become **enterprise-altitude instantiations** of these patterns — what you get when you compose MxM (harness) ordered by OrdSA (authority/evidence) within DEA (EA coherence) at enterprise scale, with OAgents as the domain object.

---

## Enterprise platforms — instantiations at the enterprise altitude

| Platform | Stands for | What it is |
|---|---|---|
| **[Strategy](enterprise-platforms/strategy/)** | (umbrella) | The enterprise-platform strategy — pain-first framing, four-plane architecture, staged maturity. Positioning prose, not a software target |
| **[AEON](enterprise-platforms/aeon/)** | AI Enterprise Orchestration Nexus | The enterprise control plane for the agentic era. Six service planes: identity, authority, evidence, integration, capability composition, orchestration runtime |
| **[AIDEX](enterprise-platforms/aidex/)** | AI Digital Experience | The worker-facing subdomain under AEON. Architectural expression of HCAE operationally at the digital experience layer |
| **[OAAD](enterprise-platforms/oaad/)** | Open Source Software Agentic AI DevSecOps | A platform thesis: OSS + agentic AI + DevSecOps governance replaces the COTS business capability stack |

HCAE is **not** an enterprise-platform peer — it sits at `foundation/hcae/` upstream of AIDEX in the argument lineage. AIDEX is the architectural expression at the experience layer; HCAE is the practice discipline AIDEX expresses.

---

## Related work

| Artifact | What it is |
|---|---|
| **[Theseus](related-work/theseus/)** | Micah Longmire's master's thesis on agentic cognitive architecture. Allied research; not part of the AIDE spine but informs the constructs |

---

## Governance

The canon adopts the **OrdSA development process** ratified for the corpus in [ADR-EA-0001](decisions/ADR-EA-0001-adopt-ordsa-development-process.md): `dev` branch + PR flow; append-only ADRs under `decisions/` for substantive decisions; ordinary content PRs for new papers, refinements, infographics. Direct commits to `main` are not permitted.

ADR-worthy triggers and the comment-out period are defined in [CONTRIBUTING.md](CONTRIBUTING.md) (to be added in a follow-on PR). Until then, the canon inherits the same triggers as the source corpus: new construct, construct redefinition, audience/positioning shift, framework alignment claim, license, governance change.

Per Pattern α, each construct and platform's `decisions/` directory holds artifact-internal ADRs; canon-level ADRs (umbrella, structural, governance) live at the root [`decisions/`](decisions/).

The migration from `osa-ai-org/enterprise-ai` to this canon is recorded in [ADR-EA-0006](decisions/ADR-EA-0006-migrate-corpus-to-aide-canon.md).

---

## Suggested reading order

For readers walking the canon top-down:

1. **Foundation** — read [HCAE](foundation/hcae/) and [AIDK](foundation/aidk/) first; they establish why human curation is structurally necessary
2. **Constructs (foundation methodology)** — [DEA](constructs/dea/) for general-EA coherence; [OrdSA](constructs/ordsa/) for authority/evidence layering
3. **Strategy** — [Enterprise Agentic AI Platform Strategy](enterprise-platforms/strategy/) for the platform thesis at altitude
4. **Enterprise platforms** — [AEON](enterprise-platforms/aeon/) (the control plane), [AIDEX](enterprise-platforms/aidex/) (the experience subdomain), [OAAD](enterprise-platforms/oaad/) (the capability platform)
5. **Constructs (harness + agent)** — [MxM](constructs/mxm/) for per-harness orientation; [OAgents](constructs/oagents/) for the agent domain model
6. **Related work** — [Theseus](related-work/theseus/) for the cognitive-architecture context

---

## License

The canon is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). Where embedded construct repositories carry their own licenses (e.g., OrdSA, OAgents-standard), those licenses apply to their respective subdirectories.

## Citation

Cite individual artifacts by their published DOI where available (foundation tier; per-platform/per-construct Zenodo records as they mint). For the canon as a whole, cite:

> Longmire, J. D. (2026). *AI-centric Digital Ecosystem (AIDE) canon* [Software/corpus]. https://github.com/ologos-repos/aide-canon
