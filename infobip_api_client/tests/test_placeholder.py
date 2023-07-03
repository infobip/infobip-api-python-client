import pytest

def func(x):
    return x + 2

def test_simple():
    assert func(3) == 5