import os
import importlib.util

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "code",
    "28_set_intersection.py"
)

spec = importlib.util.spec_from_file_location("intersection_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

set_intersection = module.set_intersection


def test_common_elements():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_no_common_elements():
    assert set_intersection({1, 2}, {3, 4}) == set()


def test_both_empty_sets():
    assert set_intersection(set(), set()) == set()


def test_one_empty_set():
    assert set_intersection({1, 2, 3}, set()) == set()


def test_duplicate_values_in_lists():
    assert set_intersection([1, 2, 2, 3], [2, 2, 4]) == {2}