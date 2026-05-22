# RLEG — Reinforcement Learning from Expert Guidance

A draft proposal replacing RLHF (Reinforcement Learning from Human Feedback) with RLEG (Reinforcement Learning from Expert Guidance) — expert grounding as a solution to the fluency-calibration tradeoff in current alignment training.

## Status

| Field | Value |
|---|---|
| **Status** | **In draft** — no Zenodo deposit yet |
| **DOI** | (pending — deposits on author ratification) |
| **Author** | JD Longmire (ORCID [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)) |

## Artifacts

| File | Description |
|---|---|
| [`RLHF-to-RLEG-outline.md`](RLHF-to-RLEG-outline.md) | Paper outline — *From RLHF to RLEG: Expert Grounding as a Solution to the Fluency-Calibration Tradeoff* |
| [`RLHF-to-RLEG-draft.md`](RLHF-to-RLEG-draft.md) | Full draft (in progress) |

## Position in the canon

RLEG sits **adjacent to HCAE** at the foundation tier:

- **HCAE** prescribes human curation at the **practice level** — the practitioner curates AI output and remains the locus of judgment after the model produces
- **RLEG** addresses the **training-methodology level** — replace RLHF preference signal (lay-rater approval) with RLEG (expert grounding) so that the trained model is calibrated to expert judgment *before* deployment

Different layers of the same broader concern: expert grounding of AI behavior.

## Provenance

Sourced from `jdlongmire/AI-Research/1.0-Foundation/RLEG/`. Migrated in current draft state per the canon's "published *and* in-progress work coexist" pattern. Deposit on author ratification.
