import os
import json
import logging
from typing import List

from src.ingestion.file_loader import list_python_files
from src.ingestion.parser import parse_code_entities
from src.ingestion.extractor import extract_entity_metadata
from src.ingestion.validation import is_valid_docstring

def setup_logger(log_path:str) -> None:
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    logging.basicConfig(
        filename=log_path,
        filemode='w',
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(message)s'
    )

def run_ingestion(source_dir:str, output_path:str, log_path:str) -> None:
    setup_logger(log_path=log_path)
    logging.info("starting ingestion run")
    logging.info("source directory : %s", source_dir)

    py_files:List[str] = list_python_files(source_dir)
    logging.info("Python files discovered : %d", len(py_files))

    all_valid_samples = []
    error_files = 0

    for idx, file_path in enumerate(py_files, start=1):
        logging.info(f"[{idx}/{len(py_files)}] Processing file: {file_path}")

        try:
            entities = parse_code_entities(file_path)
            for e in entities:
                meta = extract_entity_metadata(e, file_path)
                if is_valid_docstring(meta.get("docstring_reference")):
                    all_valid_samples.append(meta)

        except Exception:
            error_files = error_files+1
            logging.error(f"failed processing {file_path}: {Exception}")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path,'w',encoding='utf-8') as f:
        json.dump(all_valid_samples, f, indent=2)
    
    logging.info("Ingestion run complete")
    logging.info(f"valid samples saved : {len(all_valid_samples)}")
    logging.info("files with errors : %d", error_files)
    logging.info(f"output path : {output_path}")

if __name__ == "__main__":
    SOURCE_DIRECTORY = r"C:\Users\ankus\ai-doc-writer\data\raw\requests\src\requests"
    OUTPUT_PATH = os.path.join('data','processed','requests_batch_samples.json')
    LOG_PATH = os.path.join('reports','ingestion_run_1.log')

    run_ingestion(SOURCE_DIRECTORY, OUTPUT_PATH, LOG_PATH)