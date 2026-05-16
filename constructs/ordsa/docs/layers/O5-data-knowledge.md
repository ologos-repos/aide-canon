# O5 — Data and Knowledge Substrate

> Documents, logs, CMDB, code, policies, telemetry, vector stores.

## Definition

The layer of enterprise data and knowledge that AI systems read, retrieve, and reason against: documents, tickets, logs, CMDB, architecture repositories, codebases, policy libraries, threat intelligence, design repositories, and operational telemetry.

In AI systems, this layer is **not passive**. Data shapes output behavior. The same agent operating against different substrates produces different decisions. That makes O5 an **architectural concern**, not a data-quality concern.

## Authority boundary

- **Provides:** read access (and, where authorized, write access) to upstream layers through controlled retrieval interfaces.
- **Sets:** retrieval scope, freshness contract, provenance attribution, and per-source confidence weighting.
- **Cannot:** be queried without going through a governed retrieval interface — direct, ungoverned scrapes of stores bypass O1's identity and audit chain.

Every read from O5 by an AI system is a **context insertion**. That insertion must be attributable.

## Risks unique to this layer

Because data drives behavior, O5 introduces failure modes that have no counterpart in traditional architectures:

- **Context poisoning.** Maliciously or accidentally introduced content steers downstream outputs.
- **Stale documentation.** Confidently-wrong context drives confidently-wrong decisions.
- **Ambiguous policy.** Conflicting source documents produce nondeterministic behavior — different runs, different answers, all sourced.
- **Ungoverned retrieval pipelines.** Embedding stores or RAG indexes built from inputs nobody owns.
- **Provenance loss.** Retrieved snippets without source attribution become indistinguishable from model output, breaking the audit chain.

Each of these is **architectural**, not a content problem. The fix lives in how O5 is structured, not in editing individual documents.

## What lives here

- Source-of-truth stores per domain (CMDB, code repos, policy library, ticket system, telemetry)
- Retrieval interfaces (RAG endpoints, search APIs, structured query gateways)
- Provenance metadata for retrieved content
- Freshness contracts (how old can a document be before it must be re-verified)
- Per-source confidence weighting (a vendor-published spec versus an internal wiki page do not carry the same weight)

## What does not live here

- The reasoning that consumes the data (O3 agents, O2 workflows)
- The tools that mutate data (O4 — the *write* mechanism is at O4 even if the *substrate* is at O5)
- Outcome records (O6 — these are produced **about** O5 actions but stored as evidence, not substrate)

## The substrate-is-architecture rule

Treat every retrieval pipeline as part of the architecture diagram. If a RAG index exists but does not appear in the architecture, it is **shadow architecture** — outside governance and outside review.

This applies to:

- Vector stores fed by file-watchers nobody currently owns
- Per-team knowledge bases that the corporate retrieval interface secretly federates against
- Internal "context packs" assembled ad-hoc and pasted into agent prompts
- Cached snapshots that outlive the source document's revision

Each one is an O5 component. Each one needs an owner, a freshness contract, and a path into the architecture diagram.

## Anti-patterns

- **The "single source of truth" that nobody updates.** Worse than no canonical store — it confers false confidence on stale content.
- **Retrieval without provenance.** Snippets returned to agents without source attribution. Audits cannot reconstruct which document drove which decision.
- **Embedding stores as side-channels.** An index built once, queried forever, never re-derived from source. The store and its source drift; behavior follows the store, not the source.
- **Domain mingling at retrieval time.** A retrieval interface that returns context from outside the agent's domain envelope. Inserts unauthorized context into the reasoning.

## Evidence flowing up

To O6 (and through it, to O0): retrieval volume per source, provenance-completeness rate, freshness-contract violations, cross-domain leakage attempts, content-quality complaints traced to specific sources.

## See also

- [O3 — Agents and Workflows](O3-agents-workflows.md) — the consumers of O5
- [O4 — Tools and Execution Channels](O4-tools-execution.md) — the writers into O5
- [O6 — Outcome, Audit, Feedback](O6-outcome-audit.md) — where O5-driven outcome problems are surfaced
