import importlib

module = importlib.import_module("40_gcd")


def test_gcd_positive_numbers():
    assert module.find_gcd(12, 18) == 6


def test_coprime_numbers():
    assert module.find_gcd(7, 9) == 1


def test_same_numbers():
    assert module.find_gcd(5, 5) == 5


def test_zero_and_number():
    assert module.find_gcd(0, 10) == 10


def test_negative_numbers():
    assert module.find_gcd(-12, 18) == 6