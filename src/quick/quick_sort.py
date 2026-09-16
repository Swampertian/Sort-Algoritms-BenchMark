import sys
import time
from typing import Any, Callable, Dict, List, Optional, Tuple


class QuickSort:

    def __init__(self, key: Optional[Callable[[Any], Any]] = None):
        self.key = key if key is not None else (lambda x: x)
        self.comparisons = 0
        self.swaps = 0
        self.time_taken = 0.0

    def sort(self, arr: List[Any], in_place: bool = True) -> Tuple[List[Any], Dict[str, Any]]:

        target = arr if in_place else list(arr)
        n = len(target)
        self.comparisons = 0
        self.swaps = 0

        start_time = time.perf_counter()
        if n > 1:
            self._quick_sort_iterative(target, 0, n - 1)
        self.time_taken = time.perf_counter() - start_time

        metrics = {
            "algorithm": "Quick Sort",
            "size": n,
            "comparisons": self.comparisons,
            "swaps": self.swaps,
            "time_taken": self.time_taken,
        }
        return target, metrics

    def _median_of_three(self, arr: List[Any], low: int, high: int) -> int:
        mid = (low + high) // 2
        a, b, c = arr[low], arr[mid], arr[high]
        ka, kb, kc = self.key(a), self.key(b), self.key(c)

        self.comparisons += 2
        if (ka <= kb <= kc) or (kc <= kb <= ka):
            return mid
        elif (kb <= ka <= kc) or (kc <= ka <= kb):
            return low
        else:
            return high

    def _partition(self, arr: List[Any], low: int, high: int) -> int:
        pivot_idx = self._median_of_three(arr, low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        self.swaps += 1

        key = self.key
        pivot_val = key(arr[high])
        i = low - 1
        comparisons = 0
        swaps = 0

        for j in range(low, high):
            comparisons += 1
            if key(arr[j]) <= pivot_val:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        self.comparisons += comparisons
        self.swaps += swaps
        return i + 1

    def _quick_sort_iterative(self, arr: List[Any], low: int, high: int) -> None:
        stack = [(low, high)]

        while stack:
            l, h = stack.pop()
            if l < h:
                p = self._partition(arr, l, h)
                # Push smaller partition first to minimize stack space
                if (p - 1 - l) > (h - (p + 1)):
                    stack.append((l, p - 1))
                    stack.append((p + 1, h))
                else:
                    stack.append((p + 1, h))
                    stack.append((l, p - 1))


def quick_sort(arr: List[Any], key: Optional[Callable[[Any], Any]] = None, in_place: bool = True) -> Tuple[List[Any], Dict[str, Any]]:
    """Helper function to execute Quick Sort."""
    sorter = QuickSort(key=key)
    return sorter.sort(arr, in_place=in_place)
