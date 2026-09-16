from typing import Any, Callable, Dict, Optional

from src.bubble import BubbleSort
from src.heap import HeapSort
from src.insertion import InsertionSort
from src.merge import MergeSort
from src.quick import QuickSort
from src.selection import SelectionSort

ALGORITHMS = {
    "bubble": BubbleSort,
    "selection": SelectionSort,
    "insertion": InsertionSort,
    "merge": MergeSort,
    "quick": QuickSort,
    "heap": HeapSort,
}


def build_algorithms(key: Optional[Callable[[Any], Any]] = None) -> Dict[str, Any]:
    return {name: cls(key=key) for name, cls in ALGORITHMS.items()}

if __name__ == "__main__":
    algorithms = build_algorithms()
    for name, instance in algorithms.items():
        print(f"{name}: {instance.__class__.__name__}")
