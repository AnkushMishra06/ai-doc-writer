import os
from typing import List

def list_python_files(root_dir: str) -> List[str]:
    """
    Recursively scans the directory and collect paths to all .py extension files
    """
    python_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for f in filenames:
            if f.endswith(".py"):
                python_files.append(os.path.join(dirpath,f))
    
    return python_files