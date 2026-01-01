# Baseline Docstring Generator Specification

## Purpose

The baseline docstring generator defines a deterministic, non-learning reference system for documentation generation. Its purpose is to establish a lower bound on documentation quality against which all learned models can be compared.

This baseline does not attempt to infer semantic meaning from the code body. Instead, it relies exclusively on explicit metadata extracted from the code signature. As a result, it produces structurally valid but semantically shallow documentation.

---

## Design Philosophy

The baseline generator is designed to be:
- Deterministic and reproducible
- Free from learned linguistic knowledge
- Resistant to hallucination by construction
- Structurally compliant with documentation standards

The baseline answers the question:
“What documentation quality can be achieved without learning from data?”

---

## Allowed Inputs

The baseline generator may use only the following inputs:
- Code entity type (function or class)
- Entity name
- Ordered list of parameter names
- Presence or absence of a return value

The baseline must not:
- Inspect the function or class body
- Use reference docstrings
- Use pretrained models or external language resources
- Infer functionality beyond explicit metadata

---

## Generation Rules

### Summary Generation

For functions, the summary is generated using the following template:

`Perform the <entity_name> operation.`

For classes, the summary is generated using:

`Represent a <entity_name> object.`

No attempt is made to infer actual behavior.

---

### Parameters Section

If the code entity has parameters, a parameters section is generated.

For each parameter `p` in the function signature, the following template is used:

```
p: Any
Input parameter
```
Rules:
- All parameters are included
- Parameter order matches the function signature
- No additional parameters are introduced

---

### Returns Section
If the code entity returns a value, a returns section is generated using the following template:
```
Returns
Any
Result of the operation.
```
if the code entity does not return any value then its return section is empty and omitted

---

### Formatting and Structure
The baseline generator enforces the following section order:
1. Summary
2. Parameters (if applicable)
3. Returns (if applicable)

The output must always satisfy the structural evaluation rules defined in the structural evaluation specification.

---

## Expected Behavior and Limitations
### Expected Strengths
- Always structurally valid
- No hallucinated parameters or behaviors
- Fully deterministic output

### Expected Weaknesses
- Low semantic similarity to human-written documentation
- Generic and uninformative descriptions
- Limited usefulness for real developers

The baseline is not intended to be useful documentation but serves as a reference point for evaluating learned models.

---

## 6. Role in Evaluation Pipeline

The baseline generator establishes the minimum acceptable performance level. All trained or fine-tuned models must demonstrate measurable improvements over this baseline in terms of semantic similarity while maintaining structural correctness and avoiding hallucinations.