import os, json, random
from typing import List, Dict
from collections import defaultdict

SEED = 42
TRAIN_RATIO = 0.70
TEST_RATIO = 0.15
VAL_RATIO = 0.15

def load_dataset(path:str) -> List[Dict]:
    with open(path, mode='r', encoding='utf-8') as f:
        return json.load(f)


def extract_module_key(file_path:str) -> str:
    """
    extract module key from file path
    example:
    C:\\...\\requests\\src\\requests\\api.py -> requests/api.py
    """
    parts = file_path.replace('\\','/').split('/')
    return "/".join(parts[-2:]) # two path components

def group_by_module(samples: List[Dict]) -> Dict[str, List[Dict]]:
    grouped = defaultdict(list)
    for sample in samples:
        module_key = extract_module_key(sample["file_path"])
        grouped[module_key].append(sample)
    return grouped

def split_modules(module_keys: List[str]) -> Dict[str, List[str]]:
    random.seed(SEED)
    random.shuffle(module_keys)

    total = len(module_keys)
    train_end = int(total*TRAIN_RATIO)
    val_end = train_end + int(total*VAL_RATIO)

    return {
        'train': module_keys[:train_end],
        'val': module_keys[train_end:val_end],
        'test': module_keys[val_end:]
    }

def assign_samples(grouped: Dict[str, List[Dict]], split_map:Dict[str, List[str]]) -> Dict[str ,List[Dict]]:
    splits = {'train': [], 'val': [], 'test': []}
    for split_name, modules in split_map.items():
        for module in modules:
            splits[split_name].extend(grouped[module])
    return splits

def save_split(path: str, data: List[Dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def save_metadata(path: str, split_map: Dict[str, List[str]]) -> None:
    metadata = {
        "seed": SEED,
        "ratios": {
            "train": TRAIN_RATIO,
            "val": VAL_RATIO,
            "test": TEST_RATIO
        },
        "modules_per_split": {
            k: len(v) for k, v in split_map.items()
        },
        "module_assignment": split_map
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

def main():
    input_path = os.path.join("data", "processed", "requests_batch_samples.json")
    output_dir = os.path.join("data", "splits")

    samples = load_dataset(input_path)
    grouped = group_by_module(samples)

    module_key = list(grouped.keys())
    split_map = split_modules(module_key)
    splits = assign_samples(grouped, split_map)

    save_split(os.path.join(output_dir, "train.json"), splits['train'])
    save_split(os.path.join(output_dir, "val.json"), splits['val'])
    save_split(os.path.join(output_dir, "test.json"), splits['test'])
    save_metadata(os.path.join(output_dir, "split_metadata.json"), split_map)

    print("Dataset Split Complete")
    print(f"Train samples: {len(splits['train'])}")
    print(f"Val samples: {len(splits['val'])}")
    print(f"Test samples: {len(splits['test'])}")

if __name__ == "__main__":
    main()