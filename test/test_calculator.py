import pytest
from calculator import Calculator


def test_sum():
    assert Calculator.sum(-3.5, 2.1) == -1.4

def test_minus():
    assert Calculator.minus(-3.5, 2.1) == -5.6

def test_divide():
    assert Calculator.divide(12, 3) == 4
    assert Calculator.divide(-12, 3) == -4
    assert Calculator.divide(12, -3) == -4
    assert Calculator.divide(-12, -3) == 4

def test_divideByZero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(-3.5, 0) == -2.4

def test_divideByOne():
    assert Calculator.divide(-3.5, 1) == -3.5

def test_multiply():
    assert Calculator.multiply(-3.5, 2) == -7
    assert Calculator.multiply(12, 1.5) == 18

def test_multiplyByZero():
    assert Calculator.multiply(-3.5, 0) == 0

def test_multiplyByOne():
    assert Calculator.multiply(-3.5, 1) == -3.5
