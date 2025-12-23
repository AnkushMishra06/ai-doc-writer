# Batch Ingestion Summary — Week 1

## Source
- Repository: requests
- Source path: data/raw/requests/src/requests

## Run Statistics
- Python files scanned: 18
- Code entities parsed: <188>
- Valid documentation samples: <188>
- Invalid samples filtered: <0>
- Files with errors: 0

## Output Artifact
- Path: data/processed/requests_batch_samples.json
- Format: JSON
- Schema: configs/dataset_schema.json

## Observations
- Batch ingestion executed successfully across multiple files
- Logging captured per-file progress and summary statistics
- Validation rules are permissive and will be tightened later
- Pipeline is ready to scale to additional repositories
