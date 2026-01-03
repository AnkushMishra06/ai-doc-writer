# Semantic Evaluation Specification

## Purpose

Semantic evaluation means how closely a generated docstring aligns in meaning with a human-written reference docstring.

This evaluation focuses exclusively on linguistic and semantic similarity and does not assess structural correctness or factual validity.

---

## Evaluation Scope

Semantic similarity is evaluated by comparing:
- The generated docstring produced by a baseline or model
- The reference docstring extracted from the source code

Semantic evaluation is performed only on samples that pass structural validation.

---

## Metric Selection

The semantic similarity metric used is:

- ROUGE-L (F1 score)

ROUGE-L measures the longest common subsequence between the generated and reference docstrings, capturing sentence-level overlap while allowing for limited paraphrasing.

---

## Exclusions

Semantic evaluation explicitly excludes:
- Structurally invalid docstrings
- Hallucination detection
- Factual correctness checks
- Human evaluation

These aspects are handled by separate evaluation stages.

---

## Baseline Expectations

For the rule-based baseline generator:
- ROUGE-L scores are expected to be low
- High variance across samples is expected
- Scores serve as a lower bound for learned models

Low semantic scores are not considered failures but serve as a reference point for improvement.
