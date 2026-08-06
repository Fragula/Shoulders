import shoulders.symbol as sb
from shoulders.fundamental import (
    AMOUNT_OF_SUBSTANCE,
    ELECTRIC_CURRENT,
    LENGTH,
    LUMINOUS_INTENSITY,
    MASS,
    THERMODYNAMIC_TEMPERATURE,
    TIME,
)


def test_t():
    assert sb.T == TIME


def test_l():
    assert sb.L == LENGTH


def test_m():
    assert sb.MASS == MASS


def test_i():
    assert sb.I == ELECTRIC_CURRENT


def test_theta():
    assert sb.THETA == THERMODYNAMIC_TEMPERATURE


def test_n():
    assert sb.N == AMOUNT_OF_SUBSTANCE
    

def test_j():
    assert sb.J == LUMINOUS_INTENSITY 