# Structural Evaluation Specification
## Purpose
Structural evaluation defines the deterministic rules used to verify whether a generated docstring satisfies the required documentation schema and conventions for a given Python code entity.

This evaluation stage is independent of semantic similarity and focuses strictly on:
- Presence of required sections.
- Alignment with the code signature.
- Absence of hallucinated structural elements.

Structural evaluation is model-agnostic and applies equally to baselines and learned models.

## Inputs
For each evaluation instance, the following inputs are required:
- Code entity type (function or class)
- Function or class signature
- List of parameter names extracted from the signature
- Return presence (if inferable from the code)
- Generated docstring text

The reference human-written docstring is not used during structural evaluation.

## Structural Rule Groups
### Rule A - Summary Section
Each generated docstring must begin with a short summary describing the purpose of the code entity.

**Requirements**
- Summary must be present.
- Summary must be non-empty
- Summary must consist of a single sentence.
- Summary must have how the entity works not only how it is implemented.

**Invalid cases include:**
- Missing summary
- Placeholder text
- Multi-sentence summaries

### Rule B - Parameters Section
If the code entity has one or more parameters, a parameters section is mandatory.

**Requirements:**
- A parameters section must exist if parameters are present
- Every parameter in the function signature must be documented
- Parameter names in documentation must exactly match the signature
- No additional (hallucinated) parameters may appear

**Invalid cases include:**
- Missing parameter descriptions
- Parameter name mismatches
- Undocumented parameters
- Extra parameters not present in the signature

### Rule C - Return Section
If the code entity returns a value, a returns section is required.

**Requirements:**
- Returns section must exist if a return value is present
- Return description must be non-empty and meaningful

For code entities that do not return a value:
- The returns section may be omitted
- If included, it must explicitly state that the return value is `None`

The chosen policy must be applied consistently across evaluations.

### Rule D - Section Ordering
Sections must appear in the following order:
1. Summary
2. Parameters (if applicable)
3. Returns (if applicable)
4. Optional sections (Notes, Raises, Examples)

Any deviation from this ordering is considered a structural violation.

## Error Taxonomy
Structural evaluation produces explicit error labels to support error analysis and debugging.

### Defined Error Types

- `MISSING_SUMMARY`
- `INVALID_SUMMARY_FORMAT`
- `MISSING_PARAMETERS_SECTION`
- `MISSING_PARAMETER_DOC`
- `HALLUCINATED_PARAMETER`
- `PARAMETER_NAME_MISMATCH`
- `MISSING_RETURNS_SECTION`
- `EMPTY_RETURNS_DESCRIPTION`
- `INVALID_SECTION_ORDER`

Multiple error types may be reported for a single docstring.

## Evaluation Output
The output of structural evaluation consist of:
- 'is_structurally_valid': Boolean indicating overall structural correctness.
- 'error_types': List of detected structural error labels.

A docstring is considered structurally valid only if no structural errors are detected.

## Design Rationale
Structural evaluation is intentionally strict to:
- Prevent hallucinated or incomplete documentation
- Ensure compatibility with downstream similarity evaluation
- Provide deterministic guarantees independent of language variability

This stage establishes a minimum quality bar that all generated documentation must satisfy.
