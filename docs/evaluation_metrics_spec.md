# Evaluation Metrics Specification

## Purpose

This document defines the quantitative and rule-based metrics used to evaluate the quality of generated docstrings in the AI-powered documentation generation system.

Given the probabilistic nature of documentation generation and the existence of multiple valid outputs for a single input, evaluation is decomposed into multiple complementary metrics rather than a single score.

The selected metrics are designed to be:
- Aligned with the project idea
- Robust to paraphrasing
- Sensitive to hallucinations
- Interpretable and defensible

---

## Metric Categories

Evaluation metrics are grouped according to the evaluation axes defined in the evaluation problem definition.

| Evaluation Axis | Metric Category |
|-----------------|----------------|
| Structural correctness | Rule-based validation |
| Semantic similarity | Text similarity metrics |
| Hallucination detection | Error rate analysis |

Each metric category operates independently and captures a distinct aspect of documentation quality.

---

## Structural Evaluation Metric

### Structural Validity Rate

**Definition:**
The proportion of generated docstrings that pass all structural validation rules defined in the structural evaluation specification.

**Computation:**
Structural Validity Rate = (Number of structurally valid docstrings) / (Total generated docstrings)


**Rationale:**
- Structural correctness is deterministic and non-negotiable
- Missing or hallucinated parameters represent hard failures
- Structural validity acts as a quality gate rather than an optimization objective

**Limitations:**
- Does not measure semantic quality
- A structurally valid docstring may still be uninformative

---

## Semantic Similarity Metrics

Semantic similarity metrics are computed **only on structurally valid docstrings** to avoid rewarding structurally incorrect outputs.

### ROUGE-L (Primary Metric)

**Definition:**
ROUGE-L measures the longest common subsequence (LCS) between the generated docstring and the reference human-written docstring.

**What it measures:**
- Sentence-level and phrase-level overlap
- Partial tolerance to reordering and paraphrasing

**Rationale for inclusion:**
- Widely used in text generation and summarization tasks
- Interpretable and well-understood
- Suitable as a baseline semantic similarity metric

**Known limitations:**
- Relies on surface-level token overlap
- Penalizes valid paraphrases with different wording
- Does not capture factual correctness or hallucinations

ROUGE-L is therefore used in conjunction with structural and hallucination metrics.

---

### BLEU (Secondary / Reference Metric)

**Definition:**
BLEU measures n-gram overlap between the generated and reference docstrings.

**Purpose:**
- Serves as a historical and baseline comparison metric
- Demonstrates limitations of n-gram-based evaluation for this task

**Rationale for limited use:**
- Easy to compute
- Useful for illustrating why BLEU is insufficient for documentation generation

**Limitations:**
- Highly sensitive to wording
- Poor handling of paraphrasing
- Weak correlation with human judgment for this task

BLEU is not treated as a primary optimization metric.

---

## Hallucination Metrics

Hallucinations are treated as critical errors and are evaluated independently of similarity metrics.

### Hallucination Error Rate

**Definition:**
The proportion of generated docstrings that contain at least one hallucinated element not supported by the source code.

**Examples of hallucinations include:**
- Parameters not present in the function signature
- Incorrect or invented return values
- Claims about side effects not evident from the code
- Mention of exceptions not raised by the function

**Computation:**
Hallucination Error Rate = (Number of docstrings with ≥1 hallucination) / (Total generated docstrings)


**Rationale:**
- High semantic similarity does not guarantee factual correctness
- Hallucinated documentation is unacceptable in real-world usage
- Explicit tracking prevents fluent but incorrect outputs from being rewarded

---

## Metric Exclusions

The following metrics are explicitly excluded due to misalignment with the task formulation:

| Metric | Reason for Exclusion |
|------|---------------------|
| Accuracy | Multiple valid outputs exist |
| Exact string match | Penalizes valid paraphrasing |
| Precision / Recall | No discrete label space |
| Perplexity | Measures fluency, not correctness |
| Human evaluation | Not scalable at current project stage |

These exclusions ensure methodological consistency and prevent misleading conclusions.

---

## Evaluation Philosophy

No single metric adequately captures documentation quality. Instead, evaluation relies on a combination of:

- Hard structural validation
- Soft semantic similarity scoring
- Explicit hallucination detection

This multi-metric approach ensures that improvements reflect genuine documentation quality rather than superficial textual overlap.
