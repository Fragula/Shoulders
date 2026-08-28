import pytest

from shoulders.quantity.quantity import Quantity
from shoulders.unit.base import (
    ONE,
    A,
    m,
    mol,
    s,
)
from shoulders.unit.derived import C, Hz, N, Pa, W, kat


def test_addition():
    assert Quantity(2, m) + Quantity(4, m) == Quantity(6, m)


def test_subtraction():
    assert Quantity(3, m) - Quantity(10, m) == Quantity(-7, m)


def test_multiplication_length_by_time():
    assert Quantity(5, m) * Quantity(2, s) == Quantity(10, m*s)


def test_multiplication_time_by_electric_current():
    assert Quantity(5, s) * Quantity(5, A) == Quantity(25, C)


def test_multiplication_number():
    assert Quantity(7, A) * 2 == Quantity(14, A)


def test_multiplication_dimensionless():
    assert Quantity(5, s) * Quantity(7, ONE) == Quantity(35, s)


def test_multiplication_dimensionless_number():
    assert Quantity(3, ONE) * 4 == Quantity(12, ONE)


def test_division_length_per_time():
    assert Quantity(6, m) / Quantity(12, s) == Quantity(0.5, m/s)


def test_division_number():
    assert Quantity(3, W) / 3 == Quantity(1, W)


def test_division_dimensionless():
    assert Quantity(5, s) / Quantity(7, s) == Quantity(5 / 7, ONE)


def test_division_dimensionless_number():
    assert Quantity(18, ONE) / 2 == Quantity(9, ONE)


def test_division_amount_of_substance_per_time():
    assert Quantity(10, mol) / Quantity(2, s) == Quantity(5, kat)


def test_power_eletric_charge():
    assert Quantity(10, C) ** -1 == Quantity(1 / 10, C**-1)


def test_power_dimensionless():
    assert Quantity(2, ONE) ** 3 == Quantity(8, ONE)


def test_power_time_to_frequency():
    assert Quantity(30, s) ** -1 == Quantity(1 / 30, Hz)


def test_power_power():
    assert Quantity(20, N) / Quantity(2, m) ** 2 == Quantity(5, Pa)


def test_absolute():
    assert abs(Quantity(-30, kat)) == Quantity(30, kat)


def test_negative():
    quantity = Quantity(30, C)

    assert -quantity == Quantity(-30, C)


def test_positive():
    quantity = Quantity(30, W)

    assert +quantity == Quantity(30, W)


def test_invalid_addition():
    with pytest.raises(TypeError):
        Quantity(10, m) + 8


def test_invalid_addition_different_dimensions():
    with pytest.raises(TypeError):
        Quantity(10, m) + Quantity(5, s)


def test_invalid_subtraction():
    with pytest.raises(TypeError):
        Quantity(20, kat) - 10


def test_invalid_subtraction_different_dimensions():
    with pytest.raises(TypeError):
        Quantity(20, kat) - Quantity(5, s)


def test_invalid_division():
    with pytest.raises(ZeroDivisionError):
        Quantity(4, A) / Quantity(0, s)


def test_inavalid_division_number():
    with pytest.raises(ZeroDivisionError):
        Quantity(6, mol) / 0
