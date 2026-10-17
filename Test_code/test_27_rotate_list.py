import os
import importlib.util

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "code",
    "27_rotate_list.py"
)

spec = importlib.util.spec_from_file_location("rotate_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

rotate_list = module.rotate_list


def test_rotate_right():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotate_left():
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]


def test_rotate_empty_list():
    assert rotate_list([], 3) == []


def test_rotate_more_than_length():
    assert rotate_list([1, 2, 3], 5) == [2, 3, 1]


def test_rotate_zero():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]