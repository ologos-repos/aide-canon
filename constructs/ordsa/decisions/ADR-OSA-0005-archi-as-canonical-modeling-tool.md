# ADR-OSA-0005 — ArchiMate as canonical visual notation; pyArchimate as reference renderer

- **Status:** Accepted
- **Date:** 2026-05-16
- **Author:** JD Longmire
- **Bundle:** Founding ADR (0005 of 0005)

## Context

OSA needs a canonical visual notation for layer diagrams, layer-coverage matrices, conformance examples, and adoption-story figures. Per [ADR-OSA-0001](ADR-OSA-0001-schema-first-canonical-form.md), the schema is the source of truth and visual renderings are derived from it. Per [ADR-OSA-0004](ADR-OSA-0004-reference-tooling-python-pydantic.md), reference tooling is Python.

The choice of visual notation locks two things: (a) which enterprise-architecture audiences see OSA in "their" language, and (b) what tooling sits in the rendering pipeline. Naively, the answer would be "use Archi-the-desktop-tool with ArchiMate-the-language." Research surfaced two facts that change that picture:

1. **Archi's CLI does not export views to SVG/PNG.** A long-standing open feature request ([archimatetool/archi#398](https://github.com/archimatetool/archi/issues/398), #756, #769). The desktop tool exports images via UI; headless CI cannot. This breaks any pipeline that wants to generate diagrams from the schema as part of a build.

2. **pyArchimate v1.9.1** (released 2026-05-14) implements both the full ArchiMate Open Exchange XML object model AND native SVG export via `View.to_svg()` with auto-layout — pure Python, no Java runtime required. License: **GPL-3.0-only**, which matters for how we use it.

Combined: the schema-first principle (ADR-OSA-0001) is best served by *generating diagrams from the schema at build time*, not by hand-editing them in a GUI. pyArchimate enables that. Archi-the-desktop-tool becomes an optional consumer of our artifacts, not a producer in the pipeline.

## Decision

**ArchiMate 3.2 is the canonical visual notation for OSA renderings.** Diagrams in the repo are produced by build-time tooling from the canonical YAML schema, not authored by hand in a GUI.

**The reference rendering pipeline:**

1. **YAML construct/deployment schema** (per ADR-OSA-0001/0002/0003) is the source.
2. Reference Python tooling (per ADR-OSA-0004) loads the schema and constructs a **pyArchimate** object model.
3. pyArchimate emits two artifacts:
   - **ArchiMate Open Exchange XML** — the cross-tool portability artifact. Consumable by Archi, Sparx EA, Cameo, Visual Paradigm, etc. UAF adopters import via Cameo's UAF 1.2 Plugin (lossy but standard).
   - **SVG** — via `View.to_svg()` with auto-layout. PNG and PDF are post-processed from the SVG via `cairosvg` (Apache-2.0-equivalent license).
4. Generated artifacts land under `docs/diagrams/` (or similar — finalized in the v0.2 schema PR) and are regenerated as part of the build, not hand-edited.

**License posture.** pyArchimate is GPL-3.0-only. The reference tooling invokes pyArchimate **as a build-time CLI subprocess**, not as an imported library — the standard "GCC posture": using a GPL tool to produce artifacts does not impose GPL on the artifacts or on the calling code. OSA's distributed Python code remains Apache-2.0 (per [ADR-OSA-0004](ADR-OSA-0004-reference-tooling-python-pydantic.md)). This boundary must be respected: importing pyArchimate as a library would create a license conflict.

**Documented fallback.** If the GPL-via-subprocess posture becomes untenable (legal pushback, pyArchimate stewardship change, or a need to import-link), the swap-in is **Archimate-PlantUML via Kroki HTTP**: MIT-licensed PlantUML macros covering Business/Application/Technology/Motivation/Strategy/Implementation layers, rendered via a Kroki server (no Java in the repo, no JAR dependency). Rendering fidelity is lower than pyArchimate's native output but preserves ArchiMate notation. This fallback is documented but not implemented in v0.2.

**Archi-the-desktop-tool is OPTIONAL** for OSA contributors and consumers. Users who prefer GUI editing/exploration of an ArchiMate model can open the Open Exchange XML we emit. They are not in the build pipeline.

## Consequences

- **Contributors do not need any GUI tool installed.** Schema edits, ADR drafts, rendering changes — all happen in a text editor. CI regenerates diagrams.
- **Diagrams are reproducible.** The same schema produces the same SVG (modulo auto-layout determinism, which pyArchimate is generally good at). Diff-friendly in PRs because the source is the schema, not the SVG.
- **No GUI tool is load-bearing.** If Archi's stewardship lapses, OSA's pipeline keeps working; if pyArchimate's GPL posture changes, the Archimate-PlantUML+Kroki fallback exists.
- **The schema becomes the only thing PRs touch for visual changes.** "Edit the diagram" is "edit the schema, then re-render." No hand-tweaking SVG coordinates in commits.
- **Cross-tool portability is preserved** via the Open Exchange XML output. UAF, Sparx, Cameo, Visual Paradigm users all consume the same artifact.
- **pyArchimate auto-layout quality on dense OSA graphs is unverified.** Pilot during the v0.2 schema PR — if layout degrades badly for the seven-layer stack, the fallback may need to come forward.
- **License documentation is mandatory.** The first PR that introduces pyArchimate as a dependency must include a clear `tools/README.md` note explaining the subprocess-only usage and the Apache-2.0 boundary. Future contributors must not casually `import pyarchimate` from distributed code.
- **ArchiMate 3.2, not 4.** pyArchimate currently targets 3.2; ArchiMate 4 (released April 2026) is not yet covered by the broader Open Source ArchiMate ecosystem (Archi itself doesn't support 4 either). Migration is a 2026-Q4 or 2027 watch item, not an immediate concern.

## Alternatives considered

1. **Archi-the-desktop-tool as the canonical rendering tool.** What "Archi as tool of choice" originally meant. Rejected after research surfaced that Archi's CLI can't export SVG/PNG — this would force hand-rendering and break the schema-first principle. Archi remains useful as a *consumer* of our XML artifacts.

2. **Archi headless image export.** Would solve the rendering pipeline if it existed. It doesn't — the feature has been open since 2018. Rejected as not real.

3. **pyArchimate imported as a library (not subprocess).** Cleanest from a code-architecture perspective. Rejected — GPL-3.0 would impose GPL on the importing code, conflicting with [ADR-OSA-0004](ADR-OSA-0004-reference-tooling-python-pydantic.md)'s Apache-2.0 choice. The subprocess boundary preserves both.

4. **Archimate-PlantUML via Kroki as primary.** Apache-friendly license, no GPL concerns. Rejected as primary because rendering fidelity is lower than pyArchimate's native output, and Kroki adds an HTTP dependency that complicates offline build environments. Retained as documented fallback.

5. **Graphviz / Mermaid / D2 as primary visual.** All produce SVG/PNG/PDF natively from pure Python with permissive licenses. Rejected — none of them produce ArchiMate-shaped notation, which means adopters in EA tooling can't recognize the construct in "their" language. Loses the cross-audience portability that motivated picking ArchiMate at all.

6. **Sparx EA, Cameo, IBM Rhapsody as canonical tool.** Strong triad coverage (UAF + SysML v2 + ArchiMate). Rejected for v0.2 — commercial licenses incompatible with unaffiliated-research budget posture. Revisit if/when commercial sponsorship enters the picture.

7. **No designated rendering pipeline.** Adopters render diagrams themselves in whatever tool they prefer. Rejected — without canonical diagrams in the repo, the prose is the only OSA artifact most readers will see. Visualizable OSA matters for adoption.

## References

- [ADR-OSA-0001](ADR-OSA-0001-schema-first-canonical-form.md) — schema-first canonical form (the principle this ADR operationalizes for visuals)
- [ADR-OSA-0002](ADR-OSA-0002-schema-language-yaml-json-schema.md) — YAML + JSON Schema (the input to the rendering pipeline)
- [ADR-OSA-0004](ADR-OSA-0004-reference-tooling-python-pydantic.md) — Python + pydantic reference tooling (the host of the subprocess invocation)
- [pyArchimate on PyPI](https://pypi.org/project/pyArchimate/) — the reference renderer
- [pyArchimate on GitHub](https://github.com/pyArchimate/pyArchimate)
- [Archi CLI wiki (no SVG export)](https://github.com/archimatetool/archi/wiki/Archi-Command-Line-Interface)
- [Archi issue #398 — long-standing SVG export request](https://github.com/archimatetool/archi/issues/398)
- [Archimate-PlantUML — documented fallback](https://github.com/plantuml-stdlib/Archimate-PlantUML)
- [Kroki — fallback renderer host](https://kroki.io/)
- [ArchiMate 3.2 specification](https://pubs.opengroup.org/architecture/archimate3-doc/)
- [`../docs/relationship-to-frameworks.md`](../docs/relationship-to-frameworks.md) — ArchiMate's role relative to TOGAF/UAF/NIST AI RMF
