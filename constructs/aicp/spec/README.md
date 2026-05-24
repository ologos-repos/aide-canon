# AICP spec — vendored snapshot

This directory is a **pinned, verbatim snapshot** of the AICP specification and JSON schemas, vendored into the canon for archival convenience and offline/air-gapped reading.

| | |
|---|---|
| **Snapshot version** | AICP v0.1.0 (Draft) |
| **Pinned at** | `ologos-repos/AICP@f85a76c` (2026-05-24) |
| **Canonical / living source** | [`ologos-repos/AICP`](https://github.com/ologos-repos/AICP) — refer here for the current version |
| **Author / rights** | Micah Longmire / Ologos LLC. **MIT License** — see [`../LICENSE`](../LICENSE) |

The MIT license carried in [`../LICENSE`](../LICENSE) governs this subdirectory; it overrides the canon's top-level CC BY 4.0 for these files (per the canon's embedded-license convention — see the top-level README License section). For citation, the latest spec, or contributions, use the canonical source above; this snapshot may lag the upstream repo.

## Contents

| File | What it is |
|---|---|
| [`AICP-v0.1.md`](AICP-v0.1.md) | The full protocol specification (L1–L6, conformance levels, federation) |
| [`schemas/card.schema.json`](schemas/card.schema.json) | AICP Card document |
| [`schemas/attestation.schema.json`](schemas/attestation.schema.json) | Federation attestation claim (JWT payload) |
| [`schemas/agreement.schema.json`](schemas/agreement.schema.json) | Work agreement |
| [`schemas/audit-event.schema.json`](schemas/audit-event.schema.json) | Authorization / lifecycle / governance audit record |
| [`schemas/platform-capability.schema.json`](schemas/platform-capability.schema.json) | `/.well-known/aicp.json` capability document |
