import os
import importlib.util

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "code",
    "24_merge_sorted_lists.py"
)

spec = importlib.util.spec_from_file_location("merge_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

merge_sorted_lists = module.merge_sorted_lists


def test_merge_two_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_merge_with_empty_list():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]


def test_merge_both_empty_lists():
    assert merge_sorted_lists([], []) == []


def test_merge_with_duplicates():
    assert merge_sorted_lists([1, 2, 2], [2, 3, 3]) == [1, 2, 2, 2, 3, 3]


def test_merge_does_not_change_original_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]

    merge_sorted_lists(list1, list2)

    assert list1 == [1, 3, 5]
    assert list2 == [2, 4, 6]