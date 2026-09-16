"""
Merge Sort Algorithm Implementation
Independent module with self-contained logic and metric collection.
"""
import time
from typing import Any, Callable, Dict, List, Optional, Tuple


class MergeSort:
    """
    Merge Sort implementation (divide-and-conquer) with metric tracking.
    """

    def __init__(self, key: Optional[Callable[[Any], Any]] = None):
        self.key = key if key is not None else (lambda x: x)
        self.comparisons = 0
        self.swaps = 0  # Counts element copy/merge assignments
        self.time_taken = 0.0

    def sort(self, arr: List[Any], in_place: bool = True) -> Tuple[List[Any], Dict[str, Any]]:
        """
        Sorts the given list using the Merge Sort algorithm.

        :param arr: The list of elements to be sorted.
        :param in_place: If True, mutates the input array; otherwise returns a new sorted list.
        :return: (sorted_list, metrics_dict)
        """
        target = arr if in_place else list(arr)
        n = len(target)
        self.comparisons = 0
        self.swaps = 0

        start_time = time.perf_counter()
        if n > 1:
            self._merge_sort_recursive(target, 0, n - 1)
        self.time_taken = time.perf_counter() - start_time

        metrics = {
            "algorithm": "Merge Sort",
            "size": n,
            "comparisons": self.comparisons,
            "swaps": self.swaps,
            "time_taken": self.time_taken,
        }
        return target, metrics

    def _merge_sort_recursive(self, arr: List[Any], left: int, right: int) -> None:
        if left < right:
            mid = (left + right) // 2
            self._merge_sort_recursive(arr, left, mid)
            self._merge_sort_recursive(arr, mid + 1, right)
            self._merge(arr, left, mid, right)

    def _merge(self, arr: List[Any], left: int, mid: int, right: int) -> None:
        left_part = arr[left : mid + 1]
        right_part = arr[mid + 1 : right + 1]

        i = 0
        j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            self.comparisons += 1
            if self.key(left_part[i]) <= self.key(right_part[j]):  # <= maintains stability
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            self.swaps += 1
            k += 1

        while i < len(left_part):
            arr[k] = left_part[i]
            self.swaps += 1
            i += 1
            k += 1

        while j < len(right_part):
            arr[k] = right_part[j]
            self.swaps += 1
            j += 1
            k += 1


def merge_sort(arr: List[Any], key: Optional[Callable[[Any], Any]] = None, in_place: bool = True) -> Tuple[List[Any], Dict[str, Any]]:
    """Helper function to execute Merge Sort."""
    sorter = MergeSort(key=key)
    return sorter.sort(arr, in_place=in_place)
