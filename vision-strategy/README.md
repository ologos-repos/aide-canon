# vision-strategy/ — Tier 0

The corpus's **enterprise-strategic frame at the umbrella altitude**. Vision-Strategy carries the strategic direction (the *what* and *why* at corpus level) and points downward into [Mode Alpha](../mode-alpha/) (which carries the synthesizing argument).

## Tier vs. artifact

> **Vision-Strategy is the *tier*; [VSOK](vsok/) is one *artifact* within it.**

The distinction matters. Vision-Strategy is the *umbrella concept* — the corpus's strategic frame as a layer. VSOK is the *methodology product* that operationalizes the umbrella into four named slots (Vision · Strategy · Objectives · Key Results). Other Tier 0 artifacts may sit alongside VSOK over time (e.g., investment thesis, market positioning brief) without expanding or fragmenting VSOK's four-slot decomposition.

VSOK's slots remain stable as a single methodology output; the tier's artifact surface can grow if the corpus's strategic frame requires additional umbrella-altitude work.

## Members

| Artifact | What it is |
|---|---|
| [`vsok/`](vsok/) | The V/S/O/K methodology product — the structured artifact within Vision-Strategy |

Future artifacts may be added as their authoring lands.

## Position in the canon

Vision-Strategy sits **above** the synthesizing tier (Mode Alpha) and the methodological / instantiation tiers below:

```
Tier 0 — Vision-Strategy        ← this tier (umbrella)
Tier 1 — Mode Alpha             ← synthesizing argument (AI-centric Digital Ecosystem)
Tier 2 — Foundation             ← cognitive-theory + training-methodology basis
Tier 3 — Constructs             ← peer methodological patterns
Tier 4 — Enterprise Platforms   ← enterprise-altitude instantiations
```

Vision-Strategy answers *why does this corpus exist and what is it advancing*; everything below answers *how it composes and what it produces*.

## Governance

Vision-Strategy was introduced post-stand-up via [ADR-EA-0007](../decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md), refining the cross-ai #40 / [ADR-EA-0006](../decisions/ADR-EA-0006-migrate-corpus-to-aide-canon.md) shape. The amendment surfaced because *Enterprise Agentic AI Platform Strategy* — originally placed at `enterprise-platforms/strategy/` with a `MANIFEST.yaml: buildable: false` flag — sits at the wrong altitude for a buildable-platform tier. Lifting it to Vision-Strategy / VSOK / Strategy makes the altitude structurally honest.
