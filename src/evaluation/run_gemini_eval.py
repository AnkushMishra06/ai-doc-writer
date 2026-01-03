import json, os
from typing import List, Dict
from src.evaluation.structural_evaluator import evaluate_structure
from src.evaluation.rouge_l import rouge_l_score
from src.generation.prompt_generator import generate_docstring_with_prompt

MAX_SAMPLES = 5

def load_json(path: str) -> List[Dict]:
    with open(path, "r") as f:
        return json.load(f)

def save_json(path: str, data: Dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def run_gemini_evaluation(samples: List[Dict]) -> Dict:
    total = len(samples)
    structurally_valid = 0
    hallucinations = 0
    rouge_scores = []
    error_breakdown = {}

    for sample in samples[:MAX_SAMPLES]:
        generated = generate_docstring_with_prompt(sample)
        is_valid, errors = evaluate_structure(generated, sample)
        if is_valid:
            structurally_valid += 1
            score = rouge_l_score(generated, sample.get("docstring_reference", ""))
            rouge_scores.append(score)
        else:
            for e in errors:
                error_breakdown[e] = error_breakdown.get(e, 0) + 1

        if "HALLUCINATED_PARAMETERS" in errors:
            hallucinations += 1

    return {
        "total_samples": total,
        "structural_validity_rate": structurally_valid / total if total else 0.0,
        "hallucination_error_rate": hallucinations / total if total else 0.0,
        "mean_rouge_l_f1": (sum(rouge_scores)/len(rouge_scores) if rouge_scores else 0.0),
        "evaluated_samples": len(rouge_scores),
        "error_breakdown": error_breakdown
    }

def main():
    val_path = os.path.join("data", "splits", "val.json")
    report_path = os.path.join("reports", "gemini_eval_day4.json")

    samples = load_json(val_path)
    results = run_gemini_evaluation(samples)

    save_json(report_path, results)

    print("Gemini Evaluation complete")
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()