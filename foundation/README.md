# foundation/

The upstream cognitive-theory and training-methodology grounding for the AIDE architecture. Pre-AIDEX, pre-OrdSA: the arguments these artifacts develop are what the rest of the canon presumes.

## Artifacts

| Subdir | Title | Status | DOI |
|---|---|---|---|
| [`hcae/`](hcae/) | *Human-Curated, AI-Enabled: A Framework for Reliable AI Deployment* | Published | [`10.5281/zenodo.18368697`](https://doi.org/10.5281/zenodo.18368697) |
| [`aidk/`](aidk/) | *AI Dunning-Kruger: A Framework for Understanding Structural Epistemic Limitations* | Published | [`10.5281/zenodo.18316059`](https://doi.org/10.5281/zenodo.18316059) |
| [`rleg/`](rleg/) | *From RLHF to RLEG: Expert Grounding as a Solution to the Fluency-Calibration Tradeoff* | In draft | (deposit pending) |

## Argument lineage

> **AIDK** (AI has structural epistemic limits) → **HCAE** (so AI work must be human-curated) → **AIDEX** (architectural expression of HCAE at the experience layer) → **AEON** (control plane the deployment lives in)

HCAE prescribes human curation at the practice level. RLEG sits adjacent: it addresses the training-methodology level (replacing RLHF with expert-grounded RL). AIDK is the cognitive-theory basis HCAE rests on.

## Provenance

The published-tier artifacts (HCAE, AIDK) cite their existing Zenodo DOIs as the canonical citation target. Source artifacts live at `jdlongmire/AI-Research/1.0-Foundation/{HCAE,AIDK,RLEG}/`; the canon hosts derivative copies for reading-proximity. The source tree remains live; this is a Theseus-pattern relocation, not a move.

RLEG migrates in its current draft state; deposit occurs on author ratification.
