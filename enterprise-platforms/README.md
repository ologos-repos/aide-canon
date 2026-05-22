# enterprise-platforms/

Enterprise-altitude instantiations of the methodological constructs. Each platform is what you get when the constructs compose at enterprise scale around a specific concern.

## Members

| Subdir | Stands for | What it is | Buildable |
|---|---|---|---|
| [`strategy/`](strategy/) | (umbrella) | Pain-first framing + four-plane architecture + staged maturity. Positioning prose, not a software target | `buildable: false` |
| [`aeon/`](aeon/) | AI Enterprise Orchestration Nexus | The enterprise control plane for the agentic era — six service planes (identity, authority, evidence, integration, capability composition, orchestration runtime) | yes |
| [`aidex/`](aidex/) | AI Digital Experience | The worker-facing subdomain under AEON; architectural expression of HCAE operationally at the digital experience layer | yes |
| [`oaad/`](oaad/) | Open Source Software Agentic AI DevSecOps | OSS + agentic AI + DevSecOps governance replacing the COTS business capability stack | yes |

## Pattern α (simplified)

Per-platform: `README.md`, `docs/` (papers), `decks/` (presentation collateral, if any), `infographics/` (platform-specific visuals, if any), `spec/` (reserved for buildable spec). Platform-level ADRs hoist to canon-level [`../decisions/`](../decisions/) — they're corpus-wide architectural decisions, not platform-internal.

## HCAE placement

**HCAE is at [`../foundation/hcae/`](../foundation/hcae/), not here.** AIDEX is the architectural expression at the experience layer; HCAE is the practice discipline AIDEX expresses. The argument lineage is `AIDK → HCAE → AIDEX → AEON` — splitting HCAE off as an enterprise-platform peer would invert the upstream-of-AIDE story.

## `BUILD.md` and `MANIFEST.yaml`

A follow-on PR adds canon-root `BUILD.md` and `MANIFEST.yaml` for autonomous-build-agent navigation (per cross-ai #40 Refinement A/B). `strategy/`'s `buildable: false` flag is the first MANIFEST entry that materially differs from the rest.
