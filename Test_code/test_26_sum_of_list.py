import os
import importlib.util

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "code",
    "26_sum_of_list.py"
)

spec = importlib.util.spec_from_file_location("sum_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

sum_of_list = module.sum_of_list


def test_positive_numbers():
    assert sum_of_list([1, 2, 3, 4]) == 10


def test_empty_list():
    assert sum_of_list([]) == 0


def test_negative_numbers():
    assert sum_of_list([-1, -2, -3]) == -6


def test_mixed_numbers():
    assert sum_of_list([-1, 5, 2]) == 6


def test_single_element():
    assert sum_of_list([7]) == 7