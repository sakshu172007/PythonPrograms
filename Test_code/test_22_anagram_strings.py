import importlib.util
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "code",
    "22_anagram_strings.py"
)

spec = importlib.util.spec_from_file_location("anagram_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_anagram = module.is_anagram


def test_anagram():
    assert is_anagram("listen", "silent") is True


def test_not_anagram():
    assert is_anagram("hello", "world") is False


def test_ignore_case():
    assert is_anagram("Listen", "Silent") is True


def test_ignore_spaces():
    assert is_anagram("Dormitory", "Dirty room") is True