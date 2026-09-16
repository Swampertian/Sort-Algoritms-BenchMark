import time
from typing import Any, Callable, Dict, List, Optional, Tuple

class InsertionSort:


    def __init__(self, key: Optional[Callable[[Any], Any]] = None):
        self.key = key if key is not None else (lambda x: x)
        self.comparisons = 0
        self.swaps = 0
        self.time_taken = 0.0

    def sort(self, arr: List[Any], in_place: bool = True) -> Tuple[List[Any], Dict[str, Any]]:
        """
        Sorts the given list using the Insertion Sort algorithm.

        :param arr: The list of elements to be sorted.
        :param in_place: If True, mutates the input array; otherwise works on a copy.
        :return: (sorted_list, metrics_dict)
        """
        target = arr if in_place else list(arr)
        n = len(target)
        key = self.key
        comparisons = 0
        swaps = 0  # In insertion sort, counts shifts/assignments

        start_time = time.perf_counter()

        for i in range(1, n):
            current_item = target[i]
            current_key = key(current_item)
            j = i - 1

            while j >= 0:
                comparisons += 1
                if key(target[j]) > current_key:
                    target[j + 1] = target[j]
                    swaps += 1
                    j -= 1
                else:
                    break

            target[j + 1] = current_item

        self.time_taken = time.perf_counter() - start_time
        self.comparisons = comparisons
        self.swaps = swaps

        metrics = {
            "algorithm": "Insertion Sort",
            "size": n,
            "comparisons": self.comparisons,
            "swaps": self.swaps,
            "time_taken": self.time_taken,
        }
        return target, metrics


def insertion_sort(arr: List[Any], key: Optional[Callable[[Any], Any]] = None, in_place: bool = True) -> Tuple[List[Any], Dict[str, Any]]:
    """Helper function to execute Insertion Sort."""
    sorter = InsertionSort(key=key)
    return sorter.sort(arr, in_place=in_place)
