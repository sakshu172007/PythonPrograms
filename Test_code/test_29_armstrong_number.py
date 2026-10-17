import os
import importlib.util

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "code",
    "29_armstrong_number.py"
)

spec = importlib.util.spec_from_file_location("armstrong_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_armstrong = module.is_armstrong


def test_armstrong_number():
    assert is_armstrong(153) is True


def test_another_armstrong_number():
    assert is_armstrong(370) is True


def test_not_armstrong_number():
    assert is_armstrong(123) is False


def test_negative_number():
    assert is_armstrong(-153) is False


def test_zero():
    assert is_armstrong(0) is True