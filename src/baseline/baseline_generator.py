from typing import Dict, List


def generate_summary(entity_type: str, entity_name: str) -> str:
    if entity_type == "FunctionDef":
        return f"Perform the {entity_name} operation."
    elif entity_type == "ClassDef":
        return f"Represent a {entity_name} object."
    else:
        return f"Perform the {entity_name} operation."


def generate_parameters_section(parameters: List[str]) -> str:
    if not parameters:
        return ""

    lines = ["Parameters", "----------"]
    for p in parameters:
        lines.append(f"{p} : Any")
        lines.append("    Input parameter.")
    return "\n".join(lines)


def generate_returns_section(return_type: str) -> str:
    """
    Generate returns section only if return_type is explicitly present.
    """
    if not return_type or return_type == "None":
        return ""

    return "\n".join([
        "Returns",
        "-------",
        "Any",
        "    Result of the operation."
    ])


def baseline_generate_docstring(sample: Dict) -> str:
    """
    Generate a deterministic baseline docstring using schema-aligned metadata only.
    """
    entity_type = sample.get("code_entity_type")
    entity_name = sample.get("entity_name")
    parameters = sample.get("parameters", [])
    return_type = sample.get("return_type")

    summary = generate_summary(entity_type, entity_name)
    params_section = generate_parameters_section(parameters)
    returns_section = generate_returns_section(return_type)

    sections = [summary]

    if params_section:
        sections.append("")
        sections.append(params_section)

    if returns_section:
        sections.append("")
        sections.append(returns_section)

    return "\n".join(sections)
