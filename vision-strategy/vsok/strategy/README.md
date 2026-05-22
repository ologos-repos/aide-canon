# Strategy — Enterprise Agentic AI Platform Strategy

The corpus's enterprise-strategic positioning argument: pain-first framing, four-plane architecture, staged maturity. Argues for an enterprise-owned, four-plane platform architecture with a staged maturity model. Addressed to CIO / CTO.

This artifact occupies the **Strategy** slot of [VSOK](..) within [Vision-Strategy](../..) (Tier 0). It is the *positioning argument that bridges Vision to action* — the corpus's umbrella case for the enterprise-platforms it advocates.

## Canonical artifacts

| File | Description |
|---|---|
| [`docs/Enterprise-Agentic-AI-Platform-Strategy.pdf`](docs/Enterprise-Agentic-AI-Platform-Strategy.pdf) | The strategic brief — read first for the umbrella argument |
| [`decks/Enterprise-Agentic-Platform-Architecture-Deck.pdf`](decks/Enterprise-Agentic-Platform-Architecture-Deck.pdf) | Companion architecture deck |

## Layout

```
vision-strategy/vsok/strategy/
├── README.md (this file)
├── docs/                           # strategic brief
├── decks/                          # architecture deck
└── spec/                           # reserved (buildable spec — not applicable; positioning prose)
```

## Provenance

Sourced from `osa-ai-org/enterprise-ai/docs/` via snapshot copy in [ADR-EA-0006](../../../decisions/ADR-EA-0006-migrate-corpus-to-aide-canon.md) (umbrella migration). Relocated from `enterprise-platforms/strategy/` to `vision-strategy/vsok/strategy/` per [ADR-EA-0007](../../../decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) (Tier 0 structural amendment).

## Non-buildability

Strategy is positioning prose, not a software target. Non-buildability is now **structurally evident** from the Tier 0 placement — no `MANIFEST.yaml: buildable: false` flag is needed (per ADR-EA-0007 §Decision item 4 / Refinement B retirement).
