import os
import importlib.util
import pytest

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "code",
    "25_max_min_list.py"
)

spec = importlib.util.spec_from_file_location("max_min_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

find_max_min = module.find_max_min


def test_positive_numbers():
    assert find_max_min([4, 2, 9, 1, 7]) == (9, 1)


def test_negative_numbers():
    assert find_max_min([-5, -2, -9, -1]) == (-1, -9)


def test_single_element():
    assert find_max_min([5]) == (5, 5)


def test_duplicate_numbers():
    assert find_max_min([3, 3, 3]) == (3, 3)


def test_empty_list():
    with pytest.raises(ValueError):
        find_max_min([])