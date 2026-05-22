# sota-survey/

State-of-the-art survey program — the evidence base from which VSOK [Objectives](../../vsok/objectives/) and [Key Results](../../vsok/key-results/) are derived per [ADR-EA-0010](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md).

## Purpose

Identify what the broader enterprise-AI / agentic-systems ecosystem is shipping, where it is heading, and how each piece relates to the current AIDE architecture. The survey produces three classifications per finding:

| Classification | Meaning | Objective shape it informs |
|---|---|---|
| **AIDE ahead** | AIDE has a coherent position, vocabulary, or architecture the surveyed work lacks or addresses less completely | *Defend-and-extend* — propagate the lead before SOTA catches up |
| **AIDE behind** | The surveyed work has a coherent position, vocabulary, or architecture AIDE lacks or addresses less completely | *Catch-up* — close the gap to the named SOTA target |
| **In flight elsewhere** | The surveyed work occupies similar ground to AIDE and is actively evolving in a direction AIDE may align with or differentiate from | *Converge-or-differentiate* — align with the convergent direction or articulate differentiation explicitly |

This three-way classification is the operational link between the survey and Doerr-style Objective writing.

## Scope — five slices

| Slice | Target population | Cadence sensitivity |
|---|---|---|
| [`vendor-stacks/`](vendor-stacks/) | Major enterprise AI vendor offerings | Fast (monthly product announcements) |
| [`oss-frameworks/`](oss-frameworks/) | Open-source agentic / LLM frameworks | Fast (weekly releases common) |
| [`standards-bodies/`](standards-bodies/) | Formal standards efforts (NIST, OASIS, IETF, IEEE) + de-facto protocols (MCP, A2A, ANP) | Slow (quarterly / annual deliverables) |
| [`analyst-frames/`](analyst-frames/) | Tier-1 analyst categorizations and assessments | Medium (annual Hype Cycles + Waves; quarterly notes) |
| [`academic/`](academic/) | Recent papers on agentic systems, enterprise-AI architecture, conformance | Medium (conference cycles; major venues quarterly) |

Each slice has its own README declaring exact scope, sources, and per-finding shape conventions.

## Output shape (per finding)

Each survey entry is a discrete artifact (one `.md` file under the appropriate slice). The recommended shape:

```
1. What it is — the surveyed work, in one paragraph
2. Source links — vendor docs, paper, standard, analyst note
3. Map against AIDE — which AIDE architectural element(s) it touches
4. Classification — ahead / behind / in-flight-elsewhere (with one-line justification)
5. Objective implication — the Doerr-style Objective shape this finding informs
6. Date + reviewer — when surveyed, by whom
```

Findings are versionable — when a vendor announces a major shift or a paper supersedes a prior one, the entry updates with a dated revision note rather than being deleted. Stale findings are valuable historical signal.

## Cadence

Per [ADR-EA-0010 §3](../../../decisions/ADR-EA-0010-adopt-doerr-okr-methodology.md), the canon's OKR cadence is annual full refresh + quarterly check-ins + ad-hoc revision on major shifts. The survey cadence aligns:

- **Continuous incremental** — new findings land as they're surfaced (no batch-and-wait)
- **Annual aggregate read** — full re-read at OKR refresh time to recompute classifications
- **Ad-hoc on shift** — major SOTA events (paradigm announcement, vendor pivot, standard ratification) trigger immediate slice revisits

## Relation to exemplar tracking

The survey identifies what *others* are doing; [`../exemplar-tracking/`](../exemplar-tracking/) tracks what *AIDE itself* demonstrates operationally via Hermetic and AEON-deployed. The two are complementary: survey findings classify AIDE relative to SOTA; exemplar tracking is the working evidence that AIDE's claims are operationally realized.

When a survey finding classifies AIDE as *ahead*, the exemplar should be cite-able as the proof. When *behind*, the gap analysis informs what the exemplars need to extend to.

## Status

Scaffolding established 2026-05-22. First slice content lands in subsequent PRs.
