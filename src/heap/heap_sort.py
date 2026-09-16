import time
from typing import Any, Callable, Dict, List, Optional, Tuple


class HeapSort:

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

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(target, n, i)

        # Extract elements one by one from the heap
        for i in range(n - 1, 0, -1):
            target[0], target[i] = target[i], target[0]
            self.swaps += 1
            self._heapify(target, i, 0)

        self.time_taken = time.perf_counter() - start_time

        metrics = {
            "algorithm": "Heap Sort",
            "size": n,
            "comparisons": self.comparisons,
            "swaps": self.swaps,
            "time_taken": self.time_taken,
        }
        return target, metrics

    def _heapify(self, arr: List[Any], n: int, i: int) -> None:
        key = self.key
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            self.comparisons += 1
            if key(arr[left]) > key(arr[largest]):
                largest = left

        if right < n:
            self.comparisons += 1
            if key(arr[right]) > key(arr[largest]):
                largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.swaps += 1
            self._heapify(arr, n, largest)


def heap_sort(arr: List[Any], key: Optional[Callable[[Any], Any]] = None, in_place: bool = True) -> Tuple[List[Any], Dict[str, Any]]:
    """Helper function to execute Heap Sort."""
    sorter = HeapSort(key=key)
    return sorter.sort(arr, in_place=in_place)
