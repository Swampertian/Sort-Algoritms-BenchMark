"""
Selection Sort Algorithm Implementation
Independent module with self-contained logic and metric collection.
"""
import time
from typing import Any, Callable, Dict, List, Optional, Tuple


class SelectionSort:
    """
    Selection Sort implementation with metric tracking.
    """

    def __init__(self, key: Optional[Callable[[Any], Any]] = None):
        self.key = key if key is not None else (lambda x: x)
        self.comparisons = 0
        self.swaps = 0
        self.time_taken = 0.0

    def sort(self, arr: List[Any], in_place: bool = True) -> Tuple[List[Any], Dict[str, Any]]:
        """
        Sorts the given list using the Selection Sort algorithm.

        :param arr: The list of elements to be sorted.
        :param in_place: If True, mutates the input array; otherwise works on a copy.
        :return: (sorted_list, metrics_dict)
        """
        target = arr if in_place else list(arr)
        n = len(target)
        self.comparisons = 0
        self.swaps = 0

        start_time = time.perf_counter()

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.comparisons += 1
                if self.key(target[j]) < self.key(target[min_idx]):
                    min_idx = j

            if min_idx != i:
                target[i], target[min_idx] = target[min_idx], target[i]
                self.swaps += 1

        self.time_taken = time.perf_counter() - start_time

        metrics = {
            "algorithm": "Selection Sort",
            "size": n,
            "comparisons": self.comparisons,
            "swaps": self.swaps,
            "time_taken": self.time_taken,
        }
        return target, metrics


def selection_sort(arr: List[Any], key: Optional[Callable[[Any], Any]] = None, in_place: bool = True) -> Tuple[List[Any], Dict[str, Any]]:
    """Helper function to execute Selection Sort."""
    sorter = SelectionSort(key=key)
    return sorter.sort(arr, in_place=in_place)
