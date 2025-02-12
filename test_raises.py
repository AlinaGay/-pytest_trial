import pytest


def division(x, y):
    return x/y


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)