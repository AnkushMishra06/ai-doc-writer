import json, os
from typing import Dict, List

from src.baseline.baseline_generator import baseline_generate_docstring
from src.evaluation.rouge_l import rouge_l_score
from src.evaluation.structural_evaluator import evaluate_structure

def load_json(path: str) -> List[Dict]:
    with open(path, "r", encoding='utf-8') as f:
        return json.load(f)

def save_json(path: str, data: Dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def run_semantic_evaluation(samples: List[Dict]) -> Dict:
    scores = []
    skipped = 0

    for sample in samples:
        generated = baseline_generate_docstring(sample)
        is_valid, _ = evaluate_structure(generated, sample)
        if not is_valid:
            skipped += 1
            continue
        reference = sample.get("docstring_reference", "" )
        score = rouge_l_score(generated, reference)
        scores.append(score)

    mean_score = sum(scores)/len(scores) if scores else 0.0
    return {
        "total_samples": len(samples),
        "evaluated_samples": len(scores),
        "skipped_structural_invalid": skipped,
        "mean_rouge_l_score": mean_score,
        "sll_scores": scores
    }


def main():
    val_path = os.path.join("data", "splits", "val.json")
    report_path = os.path.join("reports","baseline_semantic_eval_day3.json")

    samples = load_json(val_path)
    results = run_semantic_evaluation(samples)

    save_json(report_path, results)
    print("Baseline semantic evaluation completed")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()