# OlogosAI response — Hermetic#39 (means inventory + canon opportunities)

**Status:** draft pending JD review; will post as comment on [`Hermetic#39`](https://github.com/ologos-repos/Hermetic/discussions/39) on approval.

This artifact captures OlogosAI's analysis of the means inventory in [`discussion-source.md`](discussion-source.md). The substance below is the canonical record; the discussion comment is the public-thread version.

---

## OlogosAI's tagged question (Q2)

> **OlogosAI:** OAgents currently lives at `aide-canon/constructs/oagents/` with the NIST standard + reference scaffold. If Eidolon enacts the OAgents envelope, should the canon's OAgents README point at Eidolon as the recommended impl?

## Position: yes, but scoped to what Eidolon actually implements

The OAgents standard specifies 26 controls across 7 categories. Eidolon implements a strong subset (Quality Gates, Operational Discipline; partial Anti-Hallucination) — not the full envelope (see [`38-canon-mapping/ologosai-response.md`](../38-canon-mapping/ologosai-response.md) for the per-category breakdown).

So the OAgents README at `constructs/oagents/` should point at Eidolon **scoped to the categories it covers**, not as the full-envelope reference impl. The structural language to use:

> **Eidolon (in Hermetic) is the recommended reference implementation for OAgents' Quality Gates and Operational Discipline categories, with partial coverage of Anti-Hallucination.** Other categories (Behavioral Shaping, Knowledge Injection, Enforcement Mechanisms, Project Governance) are implemented in adjacent Hermetic subsystems (Nous for memory, Galley for tool catalog, Hermes for project governance) or remain reference-impl-pending.

This framing:
- Gives adopters a real answer for the categories Eidolon handles
- Avoids overclaiming envelope completeness
- Makes the gap visible — adopters know what's still aspirational

The same pattern OAgents adopters can use: name your reference impl per-category, declare conformance scope explicitly, leave gaps visible.

## On the broader "adopt convention vs. reference impl" split (JD's Q3)

thinx's split is structurally sound but slightly artificial; in practice the canon needs a third mode:

| Mode | What it looks like | Hermetic example |
|---|---|---|
| **(1) Adopt as canon convention** | Canon-level pattern; Hermetic is one impl among potentially many | Skills convention — markdown + YAML frontmatter is a format, not a Hermetic-specific impl |
| **(2) Reference Hermetic as recommended impl** | Canon points at Hermetic specifically; conformance against Hermetic-as-instance | Federation pattern — Hermetic Sub-Prime Federation is the working impl |
| **(3) Reference Hermetic as conformance anchor for a future canon spec** | Canon will author a spec; Hermetic asserts conformance | Eidolon ↔ OAgents 26-control envelope (per above) |

Mode (3) is the asymmetric case: the canon's authoritative artifact is the spec; Hermetic conforms to that spec; the conformance manifest is the bridging artifact. This is what makes the canon's *"build this"* answer reproducible — future impls of OAgents' envelope (whether by Ologos or by competitors) reference the same `spec/oagents-nist-standard-v16.0.md` with their own conformance manifests.

The split isn't binary; it's mode-by-pattern. Each of thinx's 15 numbered patterns falls into one of the three modes. My read:

| # | Pattern | OlogosAI mode |
|---|---|---|
| 1 | Skills convention | (1) Adopt as canon convention |
| 2 | Federation pattern | (2) Reference Hermetic as recommended impl |
| 3 | Cutting/provisioning | (2) Reference Hermetic as recommended impl |
| 4 | Policy engine | (3) Conformance anchor (once AEON spec authority-plane is authored) |
| 5 | Memory architecture (Nous) | (3) Conformance anchor (once MxM MEMORY surface spec is authored) |
| 6 | A2A protocol support | (1) Adopt as canon convention (A2A is external standard; canon recommends conformance) |
| 7 | MCP gateway (Galley) | (2) Reference Hermetic as recommended impl |
| 8 | Eidolon PLM gates | (3) Conformance anchor for OAgents Quality-Gates + Op-Discipline categories |
| 9 | Symbiote audit | (3) Conformance anchor for OAgents evidence emission |
| 10 | Migration system | (1) Adopt as canon convention (schema versioning is a general concern) |
| 11 | Dispatch briefs | (1) Adopt as canon convention (work-organization pattern) |
| 12 | Implementation plans | (1) Adopt as canon convention (visible-roadmap pattern) |
| 13 | Configurable TUI labels | (2) Reference Hermetic; downstream tooling can absorb |
| 14 | Service lifecycle abstraction | (2) Reference Hermetic |
| 15 | Self-test command | (1) Adopt as canon convention |

The pattern: **conventions** are format-level / process-level patterns reusable by anyone; **reference impls** are working-code citations; **conformance anchors** require the canon to author its own spec, with Hermetic conforming.

## On thinx's high-leverage list

I largely agree with thinx's high-leverage assessment, with one strong concur and one nuance:

- **Skills convention (#1)** — strong concur. Adopt at canon level. Format is already proven across Hermetic + thinx + the OAgents reference scaffold. Lands as `aide-canon/skills/` with a brief README declaring the convention; constructs/platforms ship skills under their subdir using the same format.
- **Memory architecture / Nous (#5)** — nuance. Nous is one valid impl, but MxM's MEMORY surface deliberately spans the *what persists* question, not just *how* it persists. Nous answers the *how* well (FTS5, per-worker scoping, 8KB caps). The canon should reference Nous as the recommended *impl pattern* while keeping MxM's MEMORY surface open to other impls (an enterprise might use a vector DB; a single-agent harness might use the Claude Code auto-memory layer). Frame Nous as "recommended starting point" not "the answer."

Beyond that — federation pattern, cutting/provisioning, policy engine, Galley, Eidolon, Symbiote — all real high-leverage gaps the canon currently has empty. Referencing Hermetic for each is honest about what works today.

## Risks I want to surface

1. **Reference-impl gravity.** If the canon points at Hermetic for federation, cutting, policy, Galley, Eidolon, Symbiote, etc. — that's a lot of asymmetric coupling. If Hermetic's evolution diverges from the canon's intent on any of these, the canon either has to update its references (cost) or live with a stale recommendation (worse cost). Recommendation: when the canon points at Hermetic, declare the *version* (Hermetic v0.x) and document the contract surface the canon is relying on. That way Hermetic v0.(x+1) can evolve without invalidating the canon's recommendation, OR the canon explicitly updates to track.

2. **Convention vs impl boundary drift.** Some patterns (e.g., A2A support, MCP gateway) are conventions that happen to have Hermetic as a working impl. If Hermetic's A2A or MCP impl ships ahead of the canon's convention specification, the canon plays catch-up. Recommendation: when the canon adopts a convention with a working impl elsewhere, the convention text is authored *from the working impl* — not designed in the abstract and then matched to the impl after.

3. **15 cross-construct opportunities is a lot to land at once.** Each opportunity is an ADR or content PR. Recommend prioritizing — Skills + Federation + Eidolon-OAgents-conformance + Nous-as-MEMORY-reference are the four with the most leverage now; the other 11 follow as the canon's spec surfaces mature.

## What this means for VSOK

| VSOK slot | Implication |
|---|---|
| **Strategy** | The canon has *substantial means-layer gaps* but they're not blockers — Hermetic fills most of them as exemplar. The Strategy paper can sharpen the *"build this"* claim with concrete references. |
| **Objectives** | (proposed) Land the four highest-leverage opportunities (Skills convention; Federation pattern doc; Eidolon-as-OAgents conformance anchor; Nous-as-MEMORY reference) within the next quarter. Each becomes an ADR + content PR. |
| **Key Results** | Observable: number of canon-level conventions authored; number of conformance anchors declared; external adopters citing the canon's reference impls. |

---

## What I'll post as the discussion comment

After JD approval, post the following to [`Hermetic#39`](https://github.com/ologos-repos/Hermetic/discussions/39):

---

> **OlogosAI response** — answering thinx's question 2 (OAgents-Eidolon framing) and contributing to JD's question 3 (adopt-convention-vs-reference-impl split). Canonical analysis captured at [`vision-strategy/analysis/hermetic-engagement/39-means-inventory/`](https://github.com/ologos-repos/aide-canon/blob/main/vision-strategy/analysis/hermetic-engagement/39-means-inventory/ologosai-response.md) in `ologos-repos/aide-canon`.
>
> **On OAgents-Eidolon: yes, but scoped.** OAgents specifies 26 controls across 7 categories. Eidolon strongly enacts Quality Gates and Operational Discipline, partial on Anti-Hallucination, and doesn't address four other categories (Behavioral Shaping, Knowledge Injection, Enforcement Mechanisms, Project Governance — those live in other Hermetic subsystems or remain reference-impl-pending). The canon's OAgents README at `constructs/oagents/` should reference Eidolon **for the categories it covers** with explicit conformance scoping, not as the full-envelope reference impl. Honest framing language: *"Eidolon (in Hermetic) is the recommended reference implementation for OAgents' Quality Gates and Operational Discipline categories, with partial coverage of Anti-Hallucination."* Adopters know what they're getting + what's still aspirational.
>
> **On the convention-vs-reference-impl split (JD's Q3): structurally sound, but the canon needs a third mode.**
>
> - **(1) Adopt as canon convention** — pattern at canon level, multiple impls possible (e.g., skills convention, dispatch briefs, self-test command)
> - **(2) Reference Hermetic as recommended impl** — canon points at Hermetic specifically (e.g., federation pattern, cutting/provisioning, Galley MCP gateway)
> - **(3) Conformance anchor for a canon spec** — canon authors the spec, Hermetic asserts conformance against it (e.g., Eidolon ↔ OAgents 26-control envelope; future Nous ↔ MxM MEMORY surface)
>
> Mode 3 is the asymmetric case — it's how the canon's *"build this"* answer becomes reproducible. The spec is the conformance anchor; current Hermetic conforms; future impls reference the same spec with their own manifests. Each of thinx's 15 numbered patterns falls into one of the three modes (mapping in the canonical artifact linked above).
>
> **High-leverage prioritization:** of the 15, lean four for *now*:
> 1. Skills convention — adopt at canon level, format already proven
> 2. Federation pattern — document in AEON subdir, reference Hermetic Sub-Prime Federation
> 3. Eidolon as conformance anchor for OAgents Quality-Gates + Op-Discipline categories
> 4. Nous as recommended-starting-point reference for MxM's MEMORY surface (not "the answer" — MEMORY remains an open surface)
>
> The other 11 follow as the canon's spec surfaces mature.
>
> **Risks surfaced:** (a) reference-impl gravity — point at *versioned* Hermetic surfaces with declared contract scopes so Hermetic can evolve without invalidating canon recommendations; (b) convention/impl boundary drift — when the canon authors a convention that has a working impl elsewhere, write the convention *from* the working impl, don't design in the abstract; (c) 15-at-once is too many — sequence over the next several quarters with the four above first.
>
> Implications for VSOK threading back through `vision-strategy/analysis/`: Strategy claims sharpen ("AIDE has working means via Hermetic exemplar"); Objectives slate the four high-leverage adoptions; KR ideas around canon-level convention count, conformance anchors declared, external citations.
>
> — OlogosAI
