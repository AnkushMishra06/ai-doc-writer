import json
import os
from typing import Dict, List

from src.baseline.baseline_generator import baseline_generate_docstring
from src.evaluation.structural_evaluator import evaluate_structure


def load_json(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: str, data: Dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def run_baseline_evaluation(samples: List[Dict]) -> Dict:
    total = len(samples)
    structurally_valid = 0
    hallucination_errors = 0

    error_breakdown = {}

    for sample in samples:
        docstring = baseline_generate_docstring(sample)
        is_valid, errors = evaluate_structure(docstring, sample)

        if is_valid:
            structurally_valid += 1
        else:
            for e in errors:
                error_breakdown[e] = error_breakdown.get(e, 0) + 1

        # Hallucination = hallucinated parameter error
        if "HALLUCINATED_PARAMETER" in errors:
            hallucination_errors += 1

    return {
        "total_samples": total,
        "structural_validity_rate": structurally_valid / total if total else 0.0,
        "hallucination_error_rate": hallucination_errors / total if total else 0.0,
        "error_breakdown": error_breakdown
    }


def main():
    val_path = os.path.join("data", "splits", "val.json")
    report_path = os.path.join("reports", "baseline_eval_day2.json")

    samples = load_json(val_path)
    results = run_baseline_evaluation(samples)

    save_json(report_path, results)

    print("Baseline evaluation complete.")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
