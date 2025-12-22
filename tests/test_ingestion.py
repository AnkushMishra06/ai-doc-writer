from src.ingestion.parser import parse_code_entities
import os

def test_parse_entities_basic():
    test_file = os.path.join("tests","samples","sample1.py")
    entities = parse_code_entities(test_file)
    assert len(entities) > 0