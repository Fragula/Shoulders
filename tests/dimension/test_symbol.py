import shoulders.dimension.symbol as sb
from shoulders.dimension.base import (
    AMOUNT_OF_SUBSTANCE,
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


def test_mul():
    assert sb.L * sb.T == sb.T * sb.L


def test_div():
    assert (sb.L * sb.T) / sb.T == sb.L


def test_pow():
    assert (sb.L / sb.T) ** 2 == Dimension((-2, 2, 0, 0, 0, 0, 0))


def test_equivalence():
    assert (sb.L / sb.T) == (sb.T**-1) * sb.L
