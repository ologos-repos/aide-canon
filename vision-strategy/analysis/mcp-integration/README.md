# mcp-integration — analysis

Slot for canon-side analysis of how MCP (Model Context Protocol, Anthropic) integrates with AEON. Mirrors the engagement-style pattern from [`hermetic-engagement/`](../hermetic-engagement/).

## Status

| Artifact | State |
|---|---|
| [`synthesis-paper-v0.1.md`](synthesis-paper-v0.1.md) | Draft for Micah's authorial alignment. Not yet a ratified canon position. |
| [`synthesis-paper-v0.1.docx`](synthesis-paper-v0.1.docx) | Same paper, .docx for review-tool friendliness; markdown is canonical |
| [`diagrams/`](diagrams/) | 4 architecture viewpoints embedded in the paper |

## Why

NG-AIDE-01's first agentic-orchestration loop (2026-05-23) shipped bespoke HTTP-JSON capability dispatch. A survey of Micah Longmire's published MCP work — ten repositories spanning specification, commercial product, reference architecture, and OrdSA-aligned protocol design — surfaced that AEON's Integration plane should be MCP-native, not bespoke. This directory holds the survey + draft recommendation; final integration direction is Micah's to author.

## Trigger

JD's question during the NG-AIDE-01 build session (*"have we taken into account MCP gateways?"*) — paired with Micah's existing 10-repo MCP corpus that this work had not accounted for.

## Cross-links

- [Discussion thread](https://github.com/ologos-repos/aide-canon/discussions) — conversational alignment surface (link added once thread opens)
- Open PR — paper landing in canon (link added once PR opens)
- [`standards-bodies/README.md`](../sota-survey/standards-bodies/README.md) — canon's pre-existing acknowledgement that *"AIDE behind on first-party MCP support"*
- [`hermetic-engagement/39-means-inventory/discussion-source.md`](../hermetic-engagement/39-means-inventory/discussion-source.md) — Galley as recommended-impl reference

## Authorship

Per Micah's *"let me read it before my name goes on it"* directive (2026-05-22 17:44), this artifact carries OlogosAI as draft author and lists Micah as co-author *pending review*. Authorship is settled by §9 Q9 of the synthesis paper.
