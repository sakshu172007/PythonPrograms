import os
import importlib.util

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "code",
    "23_sort_without_sort.py"
)

spec = importlib.util.spec_from_file_location("sort_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

bubble_sort = module.bubble_sort


def test_sort_unsorted_list():
    assert bubble_sort([5, 2, 8, 1]) == [1, 2, 5, 8]


def test_sort_already_sorted_list():
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_sort_empty_list():
    assert bubble_sort([]) == []


def test_sort_single_element():
    assert bubble_sort([7]) == [7]


def test_original_list_unchanged():
    numbers = [5, 2, 8, 1]
    bubble_sort(numbers)
    assert numbers == [5, 2, 8, 1]