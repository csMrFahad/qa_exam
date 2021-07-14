import pytest
from calculator import Calculator


def test_addition():
    calculator = Calculator()
    result = calculator.addition(2, 3)
    assert result == 5


def test_addition_string():
    calculator = Calculator()
    with pytest.raises(Exception):
        result = calculator.addition("2", 3)
        assert result == 5


def test_division():
    calculator = Calculator()
    result = calculator.division(3, 2)
    assert result == 1.5


def test_division_zero():
    calculator = Calculator()
    with pytest.raises(Exception):

        result = calculator.division(5, 1)
