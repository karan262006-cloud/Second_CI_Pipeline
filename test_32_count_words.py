
import importlib

module = importlib.import_module("32_count_words")


def test_count_words():
    assert module.count_words("Hello world") == 2


def test_empty_string():
    assert module.count_words("") == 0


def test_multiple_spaces():
    assert module.count_words("Python   is great") == 3


def test_whitespace_only():
    assert module.count_words("   \n  ") == 0
