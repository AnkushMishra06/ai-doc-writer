# Evaluation Problem

## Task Definition
The task of this project is to generate high quality python docstrings according to source code given to it.
Formally the task is defined as a Conditional text generation problem.

P(D|C) :
- C represents the input condition, consisting of Python source code, including function or class definitions, signatures, parameters, and available metadata.
- D represents the generated documentation text in the form of structured natural-language docstrings.

---

## Limitations of Accuracy
Evaluation metrics like accuracy, precision, or recall cannot be used here as for a given input there exists multiple correct responses.
For example, these sentences are semantically same but lexically different:
- "Compute the cosine similarity between two vectors."
- "Compute cosine similarity for a pair of vectors."

Both sentences show same functionality but are different, but an exact-match type metric will say one as wrong.
As a result:
- Exact match evaluation is overly strict and penalizes valid paraphrasing.
- Accuracy-based metrics are not meaningful for this task.
- Deterministic correctness cannot be defined purely at the string level.

Therefore, Document Generation cannot be evaluated using a classification style metrics.

---

## Evaluation Axes
Given the probabilistic and generative nature of the task, evaluation must be decomposed into multiple independent axes:
### Structural Correctness
Evaluates whether the generated documentation follows the required structure and schema, such as presence of summaries, parameter sections, return descriptions, and alignment with the function signature.
### Semantic Similarity
Measures how closely the meaning of the generated documentation aligns with the reference human-written docstring, allowing for paraphrasing and stylistic variation.
### Hallucination Detection
Identifies critical errors where the generated documentation introduces information not supported by the source code, such as undocumented parameters, incorrect return values, or invented side effects.

These axes are evaluated independently to provide a comprehensive assessment of documentation quality

---

## Evaluation Philosophy
The evaluation framework prioritizes:
- Structural and factual correctness over surface-level similarity
- Robustness to paraphrasing
- Explicit detection of hallucinations and factual errors

This multi-axis approach ensures that evaluation reflects real-world documentation quality rather than superficial textual overlap.