# enterprise-platforms/ — Tier 4

Enterprise-altitude instantiations of the methodological constructs. Each platform is what you get when the constructs compose at enterprise scale around a specific concern.

## Members

| Subdir | Stands for | What it is |
|---|---|---|
| [`aeon/`](aeon/) | AI Enterprise Orchestration Nexus | The enterprise control plane for the agentic era — six service planes (identity, authority, evidence, integration, capability composition, orchestration runtime) |
| [`aidex/`](aidex/) | AI Digital Experience | The worker-facing subdomain under AEON; architectural expression of HCAE operationally at the digital experience layer |
| [`oaad/`](oaad/) | Open Source Software Agentic AI DevSecOps | OSS + agentic AI + DevSecOps governance replacing the COTS business capability stack |

All three are buildable software targets.

## Pattern α (simplified)

Per-platform: `README.md`, `docs/` (papers), `decks/` (presentation collateral, if any), `infographics/` (platform-specific visuals, if any), `spec/` (reserved for buildable spec). Platform-level ADRs hoist to canon-level [`../decisions/`](../decisions/) — they're corpus-wide architectural decisions, not platform-internal.

## Strategy is NOT here

The *Enterprise Agentic AI Platform Strategy* — the positioning argument that bridges Vision to these platforms — lives at [`../vision-strategy/vsok/strategy/`](../vision-strategy/vsok/strategy/) (Tier 0), not at this tier. It is umbrella prose, not a buildable platform peer.

See [ADR-EA-0007](../decisions/ADR-EA-0007-introduce-vsok-tier-0-and-mode-alpha.md) for the structural reasoning — Strategy's non-buildability is now structurally evident from its Tier 0 placement, so no `MANIFEST.yaml: buildable: false` flag is needed.

## HCAE placement

**HCAE is at [`../foundation/hcae/`](../foundation/hcae/), not here.** AIDEX is the architectural expression at the experience layer; HCAE is the practice discipline AIDEX expresses. The argument lineage is `AIDK → HCAE → AIDEX → AEON` — splitting HCAE off as an enterprise-platform peer would invert the upstream-of-AIDE story.

## `BUILD.md` and `MANIFEST.yaml`

A follow-on PR adds canon-root `BUILD.md` and `MANIFEST.yaml` for autonomous-build-agent navigation (per cross-ai #40 Refinement A). All three platforms at this tier declare `buildable: true` in the MANIFEST (Strategy's `buildable: false` flag is no longer needed since Strategy moved to Tier 0).
