"""
Utilities for benchmark data generation, measurement, and export.
"""
import copy
import csv
import json
import os
import random
import time
from dataclasses import asdict, dataclass
from typing import Any, Callable, Dict, List, Optional, Tuple


@dataclass
class BenchmarkItem:
    """Class representing an object data structure for sorting."""
    id: int
    val: int
    name: str

    def __repr__(self) -> str:
        return f"Item(id={self.id}, val={self.val})"


def generate_random_integers(n: int, min_val: int = -1000000, max_val: int = 1000000, seed: Optional[int] = 42) -> List[int]:
    """Generates a list of n random integers."""
    rng = random.Random(seed)
    return [rng.randint(min_val, max_val) for _ in range(n)]


def generate_sorted_integers(n: int) -> List[int]:
    """Generates an already sorted list of n integers."""
    return list(range(n))


def generate_reverse_sorted_integers(n: int) -> List[int]:
    """Generates a reverse-sorted list of n integers."""
    return list(range(n, 0, -1))


def generate_nearly_sorted_integers(n: int, swap_ratio: float = 0.05, seed: Optional[int] = 42) -> List[int]:
    """Generates a nearly sorted list of n integers with a small percentage of randomized swaps."""
    arr = list(range(n))
    rng = random.Random(seed)
    num_swaps = max(1, int(n * swap_ratio))
    for _ in range(num_swaps):
        i = rng.randint(0, n - 1)
        j = rng.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def generate_duplicate_integers(n: int, unique_count: int = 5, seed: Optional[int] = 42) -> List[int]:
    """Generates a list of n integers with many duplicate values."""
    rng = random.Random(seed)
    return [rng.randint(1, unique_count) for _ in range(n)]


def generate_custom_objects(n: int, seed: Optional[int] = 42) -> List[BenchmarkItem]:
    """Generates a list of n custom objects with key and payload."""
    rng = random.Random(seed)
    return [
        BenchmarkItem(id=i, val=rng.randint(-100000, 100000), name=f"Obj_{i}")
        for i in range(n)
    ]


def verify_sorted(arr: List[Any], key: Optional[Callable[[Any], Any]] = None) -> bool:
    """Verifies whether an array is correctly sorted."""
    extractor = key if key is not None else (lambda x: x)
    for i in range(len(arr) - 1):
        if extractor(arr[i]) > extractor(arr[i + 1]):
            return False
    return True


def save_results_to_json(results: List[Dict[str, Any]], filepath: str) -> None:
    """Saves benchmark results to a JSON file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)


def save_results_to_csv(results: List[Dict[str, Any]], filepath: str) -> None:
    """Saves benchmark results to a CSV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    if not results:
        return
    fieldnames = list(results[0].keys())
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
