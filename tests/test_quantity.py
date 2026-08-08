import pytest

from shoulders.dimension.base import (
    AMOUNT_OF_SUBSTANCE,
    DIMENSIONLESS,
    ELECTRIC_CURRENT,
    LENGTH,
    TIME,
)
from shoulders.dimension.derived import (
    CATALYTIC_ACTIVITY,
    ELECTRIC_CHARGE,
    FORCE,
    FREQUENCY,
    POWER,
    STRESS,
)
from shoulders.quantity.quantity import Quantity


def test_addition():
    assert Quantity(2, LENGTH) + Quantity(4, LENGTH) == Quantity(6, LENGTH)


def test_subtraction():
    assert Quantity(3, LENGTH) - Quantity(10, LENGTH) == Quantity(-7, LENGTH)


def test_multiplication_length_by_time():
    assert Quantity(5, LENGTH) * Quantity(2, TIME) == Quantity(10, TIME * LENGTH)


def test_multiplication_time_by_electric_current():
    assert Quantity(5, TIME) * Quantity(5, ELECTRIC_CURRENT) == Quantity(25, ELECTRIC_CHARGE)


def test_multiplication_number():
    assert Quantity(7, ELECTRIC_CURRENT) * 2 == Quantity(14, ELECTRIC_CURRENT)    


def test_multiplication_dimensionless():
    assert Quantity(5, TIME) * Quantity(7, DIMENSIONLESS) == Quantity(35, TIME)


def test_multiplication_dimensionless_number():
    assert Quantity(3, DIMENSIONLESS) * 4 == Quantity(12, DIMENSIONLESS)


def test_division_length_per_time():
    assert Quantity(6, LENGTH) / Quantity(12, TIME) == Quantity(0.5, LENGTH / TIME)


def test_division_number():
    assert Quantity(3, POWER) / 3 == Quantity(1, POWER)


def test_division_dimensionless():
    assert Quantity(5, TIME) / Quantity(7, TIME) == Quantity(5/7, DIMENSIONLESS)


def test_division_dimensionless_number():
    assert Quantity(18, DIMENSIONLESS) / 2 == Quantity(9, DIMENSIONLESS)


def test_division_amount_of_substance_per_time():
    assert Quantity(10, AMOUNT_OF_SUBSTANCE) / Quantity(2, TIME) == Quantity(5, CATALYTIC_ACTIVITY)


def test_power_time():
    assert Quantity(10, ELECTRIC_CHARGE)**-1 == Quantity(1/10, ELECTRIC_CHARGE ** -1)


def test_power_dimensionless():
    assert Quantity(2, DIMENSIONLESS)**3 == Quantity(8, DIMENSIONLESS)


def test_power_time_to_frequency():
    assert Quantity(30, TIME)**-1 == Quantity(1/30, FREQUENCY)


def test_power_POWER():
    assert Quantity(20, FORCE) / Quantity(2, LENGTH)**2 == Quantity(5, STRESS)


def test_absolute():
    assert abs(Quantity(-30, CATALYTIC_ACTIVITY)) == Quantity(30, CATALYTIC_ACTIVITY)


def test_negative():
    quantity = Quantity(30, ELECTRIC_CHARGE)

    assert -quantity == Quantity(-30, ELECTRIC_CHARGE)


def test_positive():
    quantity = Quantity(30, POWER)

    assert +quantity == Quantity(30, POWER)


def test_invalid_addition():
    with pytest.raises(TypeError):
        Quantity(10, LENGTH) + 8


def test_invalid_addition_different_dimensions():
    with pytest.raises(TypeError):
        Quantity(10, LENGTH) + Quantity(5, TIME)


def test_invalid_subtraction():
    with pytest.raises(TypeError):
        Quantity(20, CATALYTIC_ACTIVITY) - 10


def test_invalid_subtraction_different_dimensions():
    with pytest.raises(TypeError):
        Quantity(20, CATALYTIC_ACTIVITY) - Quantity(5, TIME)


def test_invalid_division():
    with pytest.raises(ZeroDivisionError):
        Quantity(4, ELECTRIC_CURRENT) / Quantity(0, TIME)


def test_inavalid_division_number():
    with pytest.raises(ZeroDivisionError):
        Quantity(6, AMOUNT_OF_SUBSTANCE) / 0