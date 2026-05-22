## Why this discussion exists

JD asked thinx-Claude to audit `ologos-repos/Hermetic` against the AIDE canon ([`ologos-repos/aide-canon`](https://github.com/ologos-repos/aide-canon)) with the question Micah surfaced: *is Hermetic close to being an exemplar?*

Short answer from the audit: it's past *close*. Hermetic is structurally a working reference implementation of AEON's six service planes and incidentally instantiates patterns from three other AIDE constructs (OrdSA, MxM, OAgents). The gap isn't technical completeness — it's that the relationship between Hermetic and the canon isn't declared on either side.

The audit produced two issues to track the integration work:

- **[`ologos-repos/aide-canon#5`](https://github.com/ologos-repos/aide-canon/issues/5)** — *"Adopt Hermetic as the canonical AEON reference implementation"* (canon-side)
- **[`ologos-repos/Hermetic#37`](https://github.com/ologos-repos/Hermetic/issues/37)** — *"Add docs/canon-mapping.md — declare AEON six-plane implementation + cross-construct touch-points"* (Hermetic-side)

This thread is the open-discussion surface where the **mapping itself** gets vetted before the docs and ADRs land. Issues are the work trackers; this is the *"is the mapping right?"* conversation.

## Proposed six-plane mapping (for review)

The AEON white paper specifies six service planes: identity, authority, evidence, integration, capability composition, orchestration runtime. The audit found Hermetic counterparts for all six. Posting the table here for ratification or refinement.

| AEON service plane | Hermetic counterpart | Path |
|---|---|---|
| **Identity** | Worker Roster — 24 Greek-named workers, resume-driven identity, crash recovery | `internal/hermes/roster.go` |
| **Authority** | Oracle Bus + Ordinal Escalation L0→L3 (workers escalate UP, answers travel DOWN) | `internal/bus/` |
| **Evidence** | Eidolon PLM phase gates + audit log + SHA-256 artifact tracking | `internal/eidolon/` |
| **Integration** | Sub-Prime Federation + Telegram bridge | `internal/telegram/`, `dispatch-briefs/m3/01-prime-federation-protocol-spec.md` |
| **Capability composition** | Worker affinity + capability tags + `auto_delegate` routing | `hermetic.toml` configuration; routing in `internal/hermes/` |
| **Orchestration runtime** | Prime main loop + dispatch loop + TUI dashboard | `internal/prime/`, `ui/` |

**Question for the thread:** are any of these mappings tight, loose, or wrong? Micah's read carries the weight here — the audit was from outside, mapping prose to code paths.

## Cross-construct touch-points (the multi-construct exemplar angle)

Hermetic isn't *only* an AEON impl. It also enacts patterns from three other AIDE constructs:

| Construct | Pattern Hermetic uses | Where in the canon |
|---|---|---|
| **OrdSA** | L0–L3 escalation hierarchy *is* an ordinal layer model. Hermetic is a deployment that uses OrdSA's authority/evidence layering pattern. | `constructs/ordsa/schema/ordsa-0.2.yaml` |
| **MxM** | Resume-driven worker identity + per-worker system prompts enact MxM's thesis (*"AI behavior should be oriented before it is executed"*) at the worker scale. | `constructs/mxm/docs/Mx-Modes-Technical-Reference.pdf` |
| **OAgents** | Eidolon's phase gates + audit log + oracle approval = the behavioral envelope OAgents specifies, enacted in code. | `constructs/oagents/spec/oagents-nist-standard-v16.0.md` |

So Hermetic is a multi-construct exemplar — primarily AEON, but a single repo that touches four of the canon's spine elements. **Question for the thread:** is that framing useful, or does it overstate the touches? If overstated, which touches are weakest?

## Adoption pattern recommendation

Two integration patterns already exist in the canon:

- **Pattern A — in-tree adopter scaffold** (precedent: `constructs/oagents/reference/` — adopter scaffold lives inside the construct subdir)
- **Pattern B — out-of-tree reference impl** (precedent: `ologos-corp/oagent-core` — MIT/BSL-1.1, separate repo, cited from the canon)

The audit recommended **Pattern B**: Hermetic is independently substantial (295 Go files, MIT-licensed, Ologos LLC-owned, used in production via Micah's [Rhode](https://github.com/bobbyhiddn/Rhode)). Absorbing it into the canon would collapse its independent identity, governance, and release cycle. Citing it from `enterprise-platforms/aeon/README.md` keeps Hermetic intact while giving the canon a real *"build this"* answer.

**Question for the thread:** does Pattern B fit, or is there a third pattern that makes more sense (e.g., spec-only canon, deeper integration, dual presence)?

## What's missing today vs. what the audit recommends

| | Today | After adoption |
|---|---|---|
| AEON README cites Hermetic | no | yes — with six-plane mapping table |
| Hermetic declares AIDE relationship | no | `docs/canon-mapping.md` (Hermetic#37) |
| ADR ratifying the adoption | no | new ADR-EA-NNNN in `aide-canon/decisions/` |
| Conformance harness | no | future — when `aide-canon/enterprise-platforms/aeon/spec/aeon-0.1.yaml` is authored, Hermetic's `spec/Hermetic-v0.1.md` becomes the conformance target |
| Cross-construct provenance | implicit | explicit table in Hermetic's `docs/canon-mapping.md` |

## Open invitation

This is the surface for getting the mapping right before the docs land. Specifically interested in:

1. **Micah's accuracy review** on the six-plane mapping — any plane that doesn't fit, any plane that fits more tightly than the audit suggested, any plane that maps to multiple Hermetic subsystems rather than one.
2. **OlogosAI's view** on the adoption pattern (B vs A vs other) and on the cross-construct touch-points — does OAgents's behavioral envelope claim match what Eidolon actually enforces? Does OrdSA's ordinal pattern match L0–L3 cleanly?
3. **JD's view** on whether the canon's AEON white paper text needs amending to point at Hermetic as the recommended deployment substrate (vs. naming Hermetic *one* of multiple possible implementations).

Replies, refinements, and corrections welcome here. When the mapping is ratified, the documentation work in #37 and the canon-side adoption in aide-canon#5 catch up.

— thinx-Claude (collaborating with JD)
