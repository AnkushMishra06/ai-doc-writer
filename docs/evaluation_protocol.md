# Evaluation Protocol

## Purpose

This document defines the dataset splitting strategy and the evaluation protocol used to assess the performance of the AI-powered documentation generation system.

Its purpose is to ensure:
- Reproducible and trustworthy evaluation
- Strict separation between training and evaluation data
- Prevention of data leakage
- Fair comparison between baselines and learned models

Once defined, this protocol must remain fixed for all experiments and reported results.

---

## Dataset Splitting Strategy

### Split Granularity

The dataset is split at the **repository or module level**, not at the individual function or class level.

All code entities originating from the same repository or module must belong to the same dataset split.

**Rationale:**
- Code within a repository shares documentation style, naming conventions, and implicit assumptions
- Function-level or file-level splitting risks style and content leakage
- Leakage inflates similarity metrics and produces misleading evaluation results

---

### Split Ratios

The dataset is divided into the following splits:

- **Training set:** 70%
- **Validation set:** 15%
- **Test set:** 15%

Split ratios are applied at the repository or module level, not per individual code entity.

---

## Role of Each Dataset Split

### Training Set

The training set is used exclusively for:
- Training documentation generation models
- Learning generation patterns from data

The training set must not be used for:
- Reporting evaluation metrics
- Model comparison
- Hyperparameter selection

---

### Validation Set

The validation set is used for:
- Comparing model variants
- Selecting prompts or hyperparameters
- Early-stage evaluation and debugging

Metrics computed on the validation set are considered **informational** and must not be reported as final results.

---

### Test Set

The test set is reserved for:
- Final evaluation of a frozen model
- Reporting metrics in summaries, reports, and conclusions

Rules for test set usage:
- The test set must be evaluated only once per model version
- No tuning or modification is allowed after observing test results
- Test metrics represent the final reported performance

---

## Evaluation Workflow

For each evaluation run on the validation or test set, the following steps must be executed in order:

1. Generate docstrings using the selected model or baseline
2. Apply structural evaluation rules to all generated docstrings
3. Record the structural validity rate
4. Filter out structurally invalid docstrings
5. Compute semantic similarity metrics on structurally valid samples
6. Compute hallucination error rates
7. Aggregate metrics across all evaluated samples
8. Store results along with:
   - Model or baseline identifier
   - Dataset split (validation or test)
   - Timestamp of evaluation

No steps may be skipped or reordered.

---

## Leakage Prevention Rules

The following practices are strictly prohibited:

- Using reference docstrings during docstring generation
- Using test set metrics to guide model tuning or design decisions
- Mixing repositories or modules across dataset splits
- Re-running test evaluation after modifying the model
- Selecting metrics or thresholds based on test set performance

Any violation of these rules invalidates the affected evaluation results.

---

## Baseline and Model Comparisons

All learned models must be evaluated using the same protocol as the baseline generator.

Comparisons are valid only if:
- The same dataset splits are used
- The same evaluation metrics are applied
- The same evaluation workflow is followed

This ensures fair and interpretable comparisons between systems.

---

## Reproducibility and Reporting

For reproducibility:
- Dataset split mappings must be logged and preserved
- Evaluation outputs must be saved with metadata
- Reported results must reference the exact protocol version used

All reported metrics are assumed to follow this protocol unless explicitly stated otherwise.
