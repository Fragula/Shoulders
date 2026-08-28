import pytest

from shoulders.dimension.base import DIMENSION_ONE, LENGTH, TIME
from shoulders.dimension.dimension import Dimension

# Dimension order:
# (T, L, M, I, Θ, N, J)


def test_multiplication():
    assert LENGTH * TIME == Dimension((1, 1, 0, 0, 0, 0, 0))


def test_DIMENSION_ONE_multiplication():
    assert DIMENSION_ONE * LENGTH == LENGTH


def test_DIMENSION_ONE_muliplication_identity():
    assert DIMENSION_ONE * DIMENSION_ONE == DIMENSION_ONE


def test_division():
    assert LENGTH / TIME == Dimension((-1, 1, 0, 0, 0, 0, 0))


def test_DIMENSION_ONE_division():
    assert LENGTH / DIMENSION_ONE == LENGTH


def test_DIMENSION_ONE_div_identity():
    assert DIMENSION_ONE / DIMENSION_ONE == DIMENSION_ONE


def test_power():
    assert TIME**-2 == Dimension((-2, 0, 0, 0, 0, 0, 0))


def test_power_zero():
    assert TIME**0 == Dimension((0, 0, 0, 0, 0, 0, 0))


def test_power_float():
    assert TIME**0.5 == Dimension((0.5, 0, 0, 0, 0, 0, 0))


def test_DIMENSION_ONE_power():
    assert DIMENSION_ONE**2 == DIMENSION_ONE


def test_DIMENSION_ONE():
    assert LENGTH / LENGTH == Dimension((0, 0, 0, 0, 0, 0, 0))


def test_DIMENSION_ONE_everything():
    assert ((DIMENSION_ONE * LENGTH) / TIME) ** 2 == Dimension((-2, 2, 0, 0, 0, 0, 0))


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
