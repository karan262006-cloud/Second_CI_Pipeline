
import importlib

module = importlib.import_module("33_first_non_repeating")


def test_first_character_non_repeating():
    assert module.first_non_repeating("abcdef") == "a"


def test_character_after_repeats():
    assert module.first_non_repeating("aabbcdd") == "c"


def test_all_characters_repeat():
    assert module.first_non_repeating("aabbcc") is None


def test_empty_string():
    assert module.first_non_repeating("") is None
