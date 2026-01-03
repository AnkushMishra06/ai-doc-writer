# Prompt-Based Docstring Generation Specification

## Purpose

This component generates Python docstrings using a large language model through prompting only, without any fine-tuning or training.

It serves as a semantic baseline that improves upon the rule-based generator by leveraging pretrained language understanding.

---

## Input Scope

The prompt may include:
- Code entity type (function or class)
- Function or class signature
- Parameter names
- Return type
- Code body

The prompt must not include:
- Reference docstrings
- Evaluation metrics
- Examples from the dataset

---

## Output Requirements

The generated output must:
- Be a valid Python docstring
- Follow standard documentation conventions
- Document only parameters present in the signature
- Avoid hallucinated behavior or side effects

---

## Evaluation Discipline

All generated docstrings will be evaluated using:
- Structural validation
- Hallucination detection
- ROUGE-L semantic similarity

No special handling or exemptions are applied to prompt-based outputs.
