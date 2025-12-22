import ast
from typing import Dict

def extract_entity_metadata(entity: Dict, file_path:str) -> Dict:
    """
    Extract metadata for a single code entity (function or class) including:-
    - file path
    - entity type
    - name
    - parameters
    - docstring
    - code block text
    """
    node = entity["node"]

    # extract function arguments if present
    parameters = []
    if hasattr(node,"args") and hasattr(node.args,"args"):
        parameters = [arg.arg for arg in node.args.args]

    return {
        "file_path":file_path,
        "code_entity_type":entity["code_entity_type"],
        "entity_name":entity["entity_name"],
        "parameters":parameters,
        "docstring_reference":ast.get_docstring(node),
        "code_block": ast.unparse(node) if hasattr(ast, "unparse") else None
    }