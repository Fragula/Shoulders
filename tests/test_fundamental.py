from shoulders.dimension.base import (
    AMOUNT_OF_SUBSTANCE,
    DIMENSIONLESS,
    ELECTRIC_CURRENT,
    LENGTH,
    LUMINOUS_INTENSITY,
    MASS,
    THERMODYNAMIC_TEMPERATURE,
    TIME,
)
from shoulders.dimension.dimension import Dimension

# Dimension order:
# (T, L, M, I, Θ, N, J)

def test_time():
    assert TIME == Dimension((1, 0, 0, 0, 0, 0, 0))


def test_length():    
    assert LENGTH == Dimension((0, 1, 0, 0, 0, 0, 0))


def test_mass():
    assert MASS == Dimension((0, 0, 1, 0, 0, 0, 0))


def test_electric_current():
    assert ELECTRIC_CURRENT == Dimension((0, 0, 0, 1, 0, 0, 0))


def test_thermodynamic_temperature():
    assert THERMODYNAMIC_TEMPERATURE == Dimension((0, 0, 0, 0, 1, 0, 0))


def test_amount_of_substance():
    assert AMOUNT_OF_SUBSTANCE == Dimension((0, 0, 0, 0, 0, 1, 0))


def test_luminous_intensity():
    assert LUMINOUS_INTENSITY == Dimension((0, 0, 0, 0, 0, 0, 1))


def test_dimensionless():
    assert DIMENSIONLESS == Dimension((0, 0, 0, 0, 0, 0, 0))