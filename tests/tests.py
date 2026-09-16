"""
Unit tests for all 6 sorting algorithms.
"""
import random
import unittest
from typing import Any

from src.bubble.bubble_sort import BubbleSort, bubble_sort
from src.heap.heap_sort import HeapSort, heap_sort
from src.insertion.insertion_sort import InsertionSort, insertion_sort
from src.merge.merge_sort import MergeSort, merge_sort
from src.quick.quick_sort import QuickSort, quick_sort
from src.selection.selection_sort import SelectionSort, selection_sort


class CustomItem:
    """Class to test object sorting and stability."""
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Item(key={self.key}, value='{self.value}')"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, CustomItem):
            return self.key == other.key and self.value == other.value
        return False


class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.sorters = [
            ("Bubble Sort", bubble_sort),
            ("Selection Sort", selection_sort),
            ("Insertion Sort", insertion_sort),
            ("Merge Sort", merge_sort),
            ("Quick Sort", quick_sort),
            ("Heap Sort", heap_sort),
        ]

    def test_empty_array(self):
        for name, sort_fn in self.sorters:
            with self.subTest(algorithm=name):
                res, metrics = sort_fn([])
                self.assertEqual(res, [])
                self.assertEqual(metrics["size"], 0)

    def test_single_element(self):
        for name, sort_fn in self.sorters:
            with self.subTest(algorithm=name):
                res, metrics = sort_fn([42])
                self.assertEqual(res, [42])
                self.assertEqual(metrics["size"], 1)

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for name, sort_fn in self.sorters:
            with self.subTest(algorithm=name):
                res, _ = sort_fn(list(arr))
                self.assertEqual(res, arr)

    def test_reverse_sorted(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = sorted(arr)
        for name, sort_fn in self.sorters:
            with self.subTest(algorithm=name):
                res, _ = sort_fn(list(arr))
                self.assertEqual(res, expected)

    def test_duplicate_elements(self):
        arr = [5, 1, 5, 3, 2, 5, 1, 4, 3, 2]
        expected = sorted(arr)
        for name, sort_fn in self.sorters:
            with self.subTest(algorithm=name):
                res, _ = sort_fn(list(arr))
                self.assertEqual(res, expected)

    def test_all_identical_elements(self):
        arr = [7, 7, 7, 7, 7, 7]
        expected = [7, 7, 7, 7, 7, 7]
        for name, sort_fn in self.sorters:
            with self.subTest(algorithm=name):
                res, _ = sort_fn(list(arr))
                self.assertEqual(res, expected)

    def test_negative_and_floats(self):
        arr = [-3.5, 10.2, 0.0, -100.0, 50.1, -3.5, 8.0]
        expected = sorted(arr)
        for name, sort_fn in self.sorters:
            with self.subTest(algorithm=name):
                res, _ = sort_fn(list(arr))
                self.assertEqual(res, expected)

    def test_random_large_arrays(self):
        random.seed(42)
        arr = [random.randint(-1000, 1000) for _ in range(200)]
        expected = sorted(arr)
        for name, sort_fn in self.sorters:
            with self.subTest(algorithm=name):
                res, _ = sort_fn(list(arr))
                self.assertEqual(res, expected)

    def test_custom_objects_with_key(self):
        items = [
            CustomItem(5, "E"),
            CustomItem(2, "B"),
            CustomItem(8, "H"),
            CustomItem(1, "A"),
            CustomItem(4, "D"),
        ]
        for name, sort_fn in self.sorters:
            with self.subTest(algorithm=name):
                res, _ = sort_fn(list(items), key=lambda item: item.key)
                keys_sorted = [item.key for item in res]
                self.assertEqual(keys_sorted, [1, 2, 4, 5, 8])

    def test_stability_stable_algorithms(self):
        # Bubble, Insertion, and Merge are stable
        stable_sorters = [
            ("Bubble Sort", bubble_sort),
            ("Insertion Sort", insertion_sort),
            ("Merge Sort", merge_sort),
        ]
        items = [
            CustomItem(1, "A1"),
            CustomItem(2, "B1"),
            CustomItem(1, "A2"),
            CustomItem(2, "B2"),
            CustomItem(1, "A3"),
        ]
        expected_values = ["A1", "A2", "A3", "B1", "B2"]

        for name, sort_fn in stable_sorters:
            with self.subTest(algorithm=name):
                res, _ = sort_fn(list(items), key=lambda x: x.key)
                actual_values = [x.value for x in res]
                self.assertEqual(actual_values, expected_values)


if __name__ == "__main__":
    unittest.main()
