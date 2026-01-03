from typing import Dict, List, Tuple
import re

SUMMARY_ERROR = "MISSING_OR_INVALID_SUMMARY"
MISSING_PARAMS_SECTION = "MISSING_PARAMETER_SECTION"
MISSING_PARAM_DOC = "MISSING_PARAMETER_DOC"
HALLUCINATED_PARAM = "HALLUCINATED_PARAMETER"
MISSING_RETURNS_SECTION = "MISSING_RETURN_SECTION"
INVALID_SECTION_ORDER = "INVALID_SECTION_ORDER"

def validate_summary(sections, errors):
    if not sections or not isinstance(sections, dict):
        errors.append(SUMMARY_ERROR)
        return
    summary = sections.get("summary", "").strip()
    if not summary:
        errors.append(SUMMARY_ERROR)
        return
    # must not start with section header
    if summary.lower().startswith(("parameters", "returns")):
        errors.append(SUMMARY_ERROR)

def extract_documented_parameters(parameters_block: str) -> List[str]:
    """
    Extract parameters name from parameters section
    """
    params = []
    for line in parameters_block.splitlines():
        match = re.match(r"^(\w+)\s*:\s*", line)
        if match:
            params.append(match.group(1))
    return params

def extract_sections(docstring: str) -> Dict[str, str]:
    sections = {"summary": ""}
    lines = docstring.strip().splitlines()

    current = "summary"
    buffer = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line in ("Parameters", "Returns"):
            sections[current] = "\n".join(buffer).strip()
            current = line.lower()
            buffer = []
            i += 2  # skip dashed line
            continue

        buffer.append(lines[i])
        i += 1

    sections[current] = "\n".join(buffer).strip()
    return sections

def validate_parameters(
    sections: Dict[str, str],
    expected_params: List[str],
    errors: List[str]
) -> None:
    if not expected_params:
        return

    params_block = sections.get("parameters")
    if not params_block:
        errors.append(MISSING_PARAMS_SECTION)
        return

    documented = extract_documented_parameters(params_block)

    for p in expected_params:
        if p not in documented:
            errors.append(MISSING_PARAM_DOC)

    for p in documented:
        if p not in expected_params:
            errors.append(HALLUCINATED_PARAM)


def validate_returns(
    sections: Dict[str, str],
    return_type: str,
    errors: List[str]
) -> None:
    if return_type and return_type != "None":
        if "returns" not in sections:
            errors.append(MISSING_RETURNS_SECTION)


def validate_section_order(docstring: str, errors: List[str]) -> None:
    order = []
    for line in docstring.splitlines():
        if line.strip() in ("Parameters", "Returns"):
            order.append(line.strip())

    if order != sorted(order, key=lambda x: ["Parameters", "Returns"].index(x)):
        errors.append(INVALID_SECTION_ORDER)


def evaluate_structure(
    docstring: str,
    sample: Dict
) -> Tuple[bool, List[str]]:
    """
    Perform structural evaluation on a generated docstring.
    """
    errors: List[str] = []
    sections = extract_sections(docstring)

    validate_summary(sections, errors)
    validate_parameters(
        sections,
        sample.get("parameters", []),
        errors
    )
    validate_returns(
        sections,
        sample.get("return_type"),
        errors
    )
    validate_section_order(docstring, errors)

    return len(errors) == 0, errors
