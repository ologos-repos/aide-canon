# AIDEX — AI Digital Experience

The worker-facing subdomain under AEON. The architecture that **expresses HCAE operationally** at the digital experience layer. One of nine peer subdomains.

## Authors

Co-authored by **JD Longmire** (ORCID [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)) and **Micah Longmire** (ORCID [0009-0006-7608-9322](https://orcid.org/0009-0006-7608-9322)) per [ADR-EA-0008](../../decisions/ADR-EA-0008-reframe-corpus-authorship.md). The published white paper + decks record the pre-reframe sole authorship.

## Canonical artifact

[`docs/AIDEX-White-Paper.pdf`](docs/AIDEX-White-Paper.pdf) — eight-axis modularity (presentation, persona, role, authority, context, memory, modality, lineage); HCAE framework; multi-backend topology; Claude Cowork as deployed reference.

## Layout

```
enterprise-platforms/aidex/
├── README.md (this file)
├── docs/
│   └── AIDEX-White-Paper.{docx,pdf}
├── decks/
│   ├── AIDEX-Deck.{pptx,pdf}                  # AIDEX standalone
│   └── AIDEX-AEON-Deck.{pptx,pdf}             # AIDEX positioned within AEON
└── spec/                           # reserved (buildable spec)
```

## Relation to HCAE

AIDEX is the **architectural expression at the experience layer**; HCAE (at [`../../foundation/hcae/`](../../foundation/hcae/)) is the **practice discipline** AIDEX expresses. AIDEX is downstream in the argument lineage:

> AIDK → HCAE → **AIDEX** → AEON

HCAE pre-exists AIDEX (its own published Zenodo DOI), and AIDEX explicitly cites HCAE as its operational source. Subordinating HCAE under AIDEX would invert the dependency.

## Provenance

Sourced from `osa-ai-org/enterprise-ai/docs/` (snapshot copy).
