import ast
from typing import List, Dict

def parse_code_entities(file_path:str) -> List[Dict]:
    """
    Parse a Python source file using AST and extract function/class definitions.
    Returns a list of entity dictionaries with metadata placeholders.
    """
    with open(file_path,'r',encoding='utf-8') as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []                                 # for skipping malformed files
    
    entities = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
            entities.append({
                "code_entity_type" : type(node).__name__ ,
                "entity_name" : node.name,
                "node" : node
            })
    
    return entities