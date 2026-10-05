import importlib.util

spec = importlib.util.spec_from_file_location(
    "program", "Code/01_even_odd.py"
)

program = importlib.util.module_from_spec(spec)
spec.loader.exec_module(program)


def test_even():
    assert program.even_odd(10) == "Even"


def test_odd():
    assert program.even_odd(7) == "Odd"


def test_zero():
    assert program.even_odd(0) == "Even"