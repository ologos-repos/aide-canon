# ADR-EA-0013 — Define the MxM root file (the "mode" element) as the harness-attach + operating-mode activator, not a governing surface

- **Status:** Proposed
- **Date:** 2026-05-23
- **Author:** JD Longmire (drafted by OlogosAI)
- **Reviewers:** @ologos001 (canon prime), Micah Longmire (MxM co-author), thinx-Claude
- **Refines:** [ADR-EA-0005](ADR-EA-0005-clarify-mxm-archetype.md) (definition detail only; the five-surface archetype and bundling decisions stand unchanged)
- **Surfaced by:** [thinx-Claude review, ng-aide-01 discussion #3](https://github.com/ologos-repos/ng-aide-01/discussions/3), finding #1 ("what does 'mode' actually do as a layer?")

## Context

The MxM construct ([`constructs/mxm/README.md`](../README.md)) defines five governing surfaces — **Mind · Morals · Mission · Memory · Means** (the "4M+1") — and, in one sentence, an activator: *"A root file activates the operating posture; the model executes within the envelope the four discipline-bearing surfaces establish."*

That sentence is correct but under-specified, and it has caused a divergence at instantiation. NG-AIDE-01 instantiated the construct as **`mode → meta-harness (Mind·Morals·Mission·Memory) → means`** — pulling the root file out as a top layer named "mode," grouping the four disciplines as "meta-harness," and presenting Means as a third tier. thinx-Claude's review (discussion #3, finding #1) correctly observed that *as presented*, "mode" looks like a third **governance layer** with no governing content of its own — a 36-line doorway inflating the construct's name.

The resolution is not to promote the root file to a governance layer, nor to drop it — it is to **define what the root file is**, so instantiations present it correctly. JD's framing settles it: the root file is the **CLAUDE.md-equivalent** — the harness's entry/attach point. Claude Code reads `CLAUDE.md`; another harness reads its own bootstrap; the OlogosAI operator itself uses `CLAUDE.md` to route into its 4M modules + a Means adapter. The root file is the *harness-specific seam*, not a governing surface.

## Decision

**The MxM root file (the element NG-AIDE-01 names `mode.md`; Claude Code's `CLAUDE.md` is the canonical example) is the harness-attach point and operating-mode activator. It is not a sixth surface and not a governing altitude above the meta-harness.**

Its role has three parts, none of them governance:

1. **Harness-attach / entry (the CLAUDE.md role).** The root file is *harness-specific and swappable* — `CLAUDE.md` under Claude Code, a different bootstrap under another harness. It is the seam by which a given harness attaches to the five harness-agnostic surfaces. (Harness-agnosticism is the MxM archetype's core claim per ADR-EA-0005; the root file is where the harness-specificity is isolated, keeping the five surfaces clean.)

2. **Operating-mode / posture activation (the "Mx-Modes" name, earned).** The root file activates the operating *mode* under which the surfaces apply — **advisory / read-only / operational / degraded** — and the **autonomy posture** (how much an agent may self-direct before surfacing a decision to a human). This is the operating-mode the construct's name ("Mx-Modes — Multi-mode Meta-harness") refers to. The autonomy posture set here is where the [prep-pursue-pivot pattern](../../../patterns/prep-pursue-pivot.md)'s **pivot autonomy dial** (ADR-EA-0012) is configured.

3. **Routing.** It points the agent into the five surfaces (and, in instantiation, the architecture). This is the "doorway" role thinx observed — correct, but it is *one of three* roles, and it is not governance.

### The bracket framing (canonical)

The root file and **Means** *bracket* the four discipline-bearing surfaces:

```
   root file (mode)  ── harness-specific ENTRY + operating-mode activation   ── swappable
   ──────────────────────────────────────────────────────────────────────────────────
   Mind · Morals · Mission · Memory  ── harness-AGNOSTIC governance           ── durable
   ──────────────────────────────────────────────────────────────────────────────────
   Means             ── substrate-specific EXECUTION                          ── swappable
```

The root file (at the attach end) and Means (at the execution end) are the two *swappable seams*; the four discipline surfaces are the durable, harness-agnostic, substrate-agnostic core. Swap the root file to move harnesses; swap Means to move substrates; keep the governance. This is the portability claim of the MxM archetype made structural.

### Instantiation guidance

Instantiations **may** route through a root file named per harness convention (`CLAUDE.md`, `mode.md`, etc.) and **may** present the construct as `root-file → 4M → Means`, **provided** the root file is presented as the **activator/entry**, not as a governing altitude. The root file's content is legitimately: harness-operating notes, the operating-mode/autonomy-posture declaration, and routing — never governance rules (those live in the four discipline surfaces).

## Consequences

- **MxM README updated** to expand the one-sentence root-file mention into a defined element (the three roles + the bracket framing). The five-surface model is unchanged; the activator is now defined rather than implied.
- **NG-AIDE-01 instantiation reframes** (follow-on, separate PR): `mode.md` is presented as the harness entry + operating-mode/autonomy-posture setter (not a governance layer), and the NG-AEON-01/NG-AIDE-01 scope label is resolved (thinx finding #2). That work is gated on this definition being settled.
- **Connects three threads:** the root file's operating-mode is where prep-pursue-pivot's pivot autonomy dial (ADR-EA-0012) lives; the harness-attach role is the concrete form of the harness-agnosticism claim (ADR-EA-0005); and the root file is the "+activation" element relative to the 4M+1 paper-in-drafting (`harness-engineering`).
- **No change to the five surfaces, the bundling decision (ADR-EA-0004), or the archetype framing (ADR-EA-0005).** Definition detail only.
- **Out of scope (separate):** thinx finding #3 (whether Morals should *cite* OrdSA rather than re-author its authority model) is a distinct MxM↔OrdSA boundary question; it warrants its own treatment and is not decided here.

## Alternatives considered

1. **Promote the root file to a sixth governing surface.** Rejected: it *activates* the surfaces and isolates harness-specificity; it does not govern. A sixth surface would dilute the clean 4M+1 model and mis-locate harness-specific concerns inside the harness-agnostic core.
2. **Drop the root file from instantiation framing entirely** (call MxM just "the meta-harness," make the entry a contentless README). Rejected: the root file is a real, necessary element — the harness seam and the operating-mode activator. The fix is to define it correctly, not erase it. Erasing it would also strand the operating-mode/autonomy-posture concern with no home.
3. **Leave the one-sentence mention as-is.** Rejected: it under-specifies the element and already produced a divergent instantiation (the precipitating cause). Defining it is the point of this ADR.
4. **Decide the MxM↔OrdSA boundary (finding #3) here too.** Rejected as scope-creep: #1 (this ADR) is about what the root file *is*; #3 is about whether a discipline surface may absorb a peer construct. Different question, separate decision.

## References

- [`constructs/mxm/README.md`](../README.md) — the construct definition this ADR detail-clarifies
- [ADR-EA-0004](ADR-EA-0004-add-mx-modes-as-spine-construct.md) · [ADR-EA-0005](ADR-EA-0005-clarify-mxm-archetype.md) — the bundling + archetype decisions (unchanged)
- [ADR-EA-0012](../../../decisions/ADR-EA-0012-introduce-prep-pursue-pivot-pattern.md) — the pivot autonomy dial, set via the root file's operating-mode posture
- [thinx-Claude review, ng-aide-01#3](https://github.com/ologos-repos/ng-aide-01/discussions/3) — finding #1, which surfaced this
- Claude Code `CLAUDE.md` — the canonical root-file exemplar; the OlogosAI operator's own `CLAUDE.md` → 4M + adapter is a working reference
