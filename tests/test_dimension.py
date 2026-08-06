import pytest

from shoulders.dimension import Dimension
from shoulders.fundamental import LENGTH, TIME

# Dimension order:
# (T, L, M, I, Θ, N, J)

def test_multiplication():
    assert LENGTH * TIME == Dimension((1, 1, 0, 0, 0, 0, 0))


def test_division():
    assert LENGTH / TIME == Dimension((-1, 1, 0, 0, 0, 0, 0))


def test_power():
    assert TIME ** -2 == Dimension((-2, 0, 0, 0, 0, 0, 0))


def test_dimensionless():
    assert LENGTH / LENGTH == Dimension((0, 0, 0, 0, 0, 0, 0))


def test_invalid_dimension_length():
    with pytest.raises(ValueError):
        Dimension((1, 0, 0))


def test_invalid_multiplication_type():
    with pytest.raises(TypeError):
        LENGTH * 5


def test_invalid_division_type():
    with pytest.raises(TypeError):
        LENGTH / 5


def test_invalid_equality():
    assert (LENGTH == 5) is False