
import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_string():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_rotate_zero_positions():
    assert module.rotate_string("hello", 0) == "hello"


def test_rotate_full_length():
    assert module.rotate_string("hello", 5) == "hello"


def test_rotate_more_than_length():
    assert module.rotate_string("hello", 7) == "lohel"


def test_empty_string():
    assert module.rotate_string("", 3) == ""
