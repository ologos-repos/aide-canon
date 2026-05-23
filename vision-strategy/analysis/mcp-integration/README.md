# mcp-integration — analysis

Slot for canon-side analysis of how MCP (Model Context Protocol, Anthropic) integrates with AEON. Mirrors the engagement-style pattern from [`hermetic-engagement/`](../hermetic-engagement/).

## Status

| Artifact | State |
|---|---|
| [`synthesis-paper-v0.2.md`](synthesis-paper-v0.2.md) | **Current.** Draft v0.2 for Micah's authorial alignment. Incorporates GPT external review + JD's sole-author authorship correction + four-way authority distinction + new Risks/Tradeoffs section. Not yet a ratified canon position; not an ADR. |
| [`synthesis-paper-v0.2.docx`](synthesis-paper-v0.2.docx) | Same paper, .docx for review-tool friendliness; markdown is canonical |
| [`mcp-synthesis-poster-v0.1.jpg`](mcp-synthesis-poster-v0.1.jpg) | Visual overview poster by JD — referenced as Appendix A in the paper |
| [`diagrams/`](diagrams/) | 4 architecture viewpoints + v0.2 architectural poster, all embedded in the paper |
| `synthesis-paper-v0.1.*` | Historical — lives in git history at commit `1919e5b` and earlier |

## Why

NG-AIDE-01's first agentic-orchestration loop (2026-05-23) shipped bespoke HTTP-JSON capability dispatch. A survey of Micah Longmire's published 10-repo MCP corpus surfaced that AEON's Integration plane should treat MCP as primary, not bespoke. This directory holds the survey + draft recommendation; final integration direction is Micah's to author.

## Trigger

JD's question during the NG-AIDE-01 build session (*"have we taken into account MCP gateways?"*) — paired with Micah's existing 10-repo MCP corpus that this work had not accounted for.

## v0.1 → v0.2 revision drivers

Three streams of feedback drove the v0.2 revision (landed 2026-05-23 within the same session as v0.1):

1. **JD's authorship correction** (Discussion #25, 11:39) — *"Micah is sole author - you are simply synthesizing his IP."* Paper metadata, Authorship section, and Q9 framing now reflect Micah as sole author; OlogosAI as scribe.
2. **JD's four-way authority distinction** (Telegram, Ologos thread, 06:48) — earlier draft's *"you can only invoke capabilities at-or-above your altitude"* conflated request authority with execution authority. v0.2 §7.1 distinguishes the four modes: request upward / execute lateral / receive downward / escalate to human oracle.
3. **GPT external review** (Telegram, Ologos thread, 06:48) — surfaced gaps: no claim-confidence layer, no risk/tradeoff analysis, wording softness ("thrown away" / "MCP-native, not bespoke" / "Canon's path is clear" / "no single Micah-canonical auth pattern"), references without commit hashes. v0.2 adds §1 Glossary, §9 Risks/Tradeoffs/Non-Goals, [observed]/[inferred]/[recommendation] tagging on key claims, and commit-pinned references.

## Cross-links

- [Discussion #25 — authorial alignment thread](https://github.com/ologos-repos/aide-canon/discussions/25) — conversational alignment surface where v0.1 feedback landed
- [PR #24 — paper landing in canon](https://github.com/ologos-repos/aide-canon/pull/24) — v0.2 push lands here
- [`standards-bodies/README.md`](../sota-survey/standards-bodies/README.md) — canon's pre-existing acknowledgement that *"AIDE behind on first-party MCP support"*
- [`hermetic-engagement/39-means-inventory/discussion-source.md`](../hermetic-engagement/39-means-inventory/discussion-source.md) — Galley as recommended-impl reference

## Authorship

**Per JD's 2026-05-23 11:39 correction on Discussion #25: Micah Longmire is sole author of the architectural IP this paper synthesizes.** OlogosAI's role is scribe/synthesizer — surveying Micah's published MCP corpus, mapping it onto AEON's planes, and drafting a substrate for Micah's revision. The paper carries Micah as Author; OlogosAI as Synthesizer (drafting role only). Final framing is settled by §11 Q9 of the v0.2 paper.
