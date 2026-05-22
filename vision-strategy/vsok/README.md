# vsok/ — V/S/O/K methodology product

The structured artifact that operationalizes [Vision-Strategy](..) into four named slots. VSOK decomposes the corpus's umbrella strategic frame into discrete, navigable components — each slot reserved for its own artifact.

## The four slots

| Slot | What it carries |
|---|---|
| [`vision/`](vision/) | The long-horizon outcome the corpus advances toward |
| [`strategy/`](strategy/) | The positioning argument that bridges Vision to action — carries *Enterprise Agentic AI Platform Strategy* |
| [`objectives/`](objectives/) | Strategic goals deriving from Vision |
| [`key-results/`](key-results/) | Measurable outcomes anchoring Objectives |

## Status

At stand-up time, only **Strategy** is populated (relocated from `enterprise-platforms/strategy/` per [ADR-EA-0007](../../decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md)). Vision, Objectives, and Key Results are reserved placeholders the canon commits to populating over time.

## Why VSOK is *inside* Vision-Strategy, not its own tier

Vision-Strategy is the *umbrella concept*; VSOK is the methodology product that operationalizes the umbrella. Conflating them would (a) lock Tier 0's artifact surface to exactly four slots with no room for additional umbrella-altitude artifacts (investment thesis, market positioning brief), and (b) cause naming redundancy in hierarchy listings ("Tier 0 — VSOK / VSOK paper").

Separating the tier from the artifact preserves a clean *tier ↔ artifact* relationship throughout the canon and keeps Tier 0's artifact surface open. See [ADR-EA-0007 §Alternatives considered (option 6)](../../decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) for the full reasoning.
