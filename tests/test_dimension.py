import pytest

from shoulders.dimension.base import DIMENSIONLESS, LENGTH, TIME
from shoulders.dimension.dimension import Dimension

# Dimension order:
# (T, L, M, I, Θ, N, J)

def test_multiplication():
    assert LENGTH * TIME == Dimension((1, 1, 0, 0, 0, 0, 0))

def test_dimensionless_multiplication():
    assert DIMENSIONLESS * LENGTH == LENGTH


def test_dimensionless_muliplication_identity():
    assert DIMENSIONLESS * DIMENSIONLESS == DIMENSIONLESS


def test_division():
    assert LENGTH / TIME == Dimension((-1, 1, 0, 0, 0, 0, 0))


def test_dimensionless_division():
    assert LENGTH / DIMENSIONLESS == LENGTH


def test_dimensionless_div_identity():
    assert DIMENSIONLESS / DIMENSIONLESS == DIMENSIONLESS


def test_power():
    assert TIME**-2 == Dimension((-2, 0, 0, 0, 0, 0, 0))


def test_power_zero():
    assert TIME**0 == Dimension((0, 0, 0, 0, 0, 0, 0))


def test_power_float():
    assert TIME**0.5 == Dimension((0.5, 0, 0, 0, 0, 0, 0))


def test_dimensionless_power():
    assert DIMENSIONLESS**2 == DIMENSIONLESS


def test_dimensionless():
    assert LENGTH / LENGTH == Dimension((0, 0, 0, 0, 0, 0, 0))


def test_dimensionless_everything():
    assert ((DIMENSIONLESS * LENGTH) / TIME)**2 == Dimension((-2, 2, 0, 0, 0, 0, 0))


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