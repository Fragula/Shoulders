import shoulders.derived as dv
from shoulders.fundamental import (
    AMOUNT_OF_SUBSTANCE,
    DIMENSIONLESS,
    ELECTRIC_CURRENT,
    LENGTH,
    LUMINOUS_INTENSITY,
    MASS,
    TIME,
)

# Dimension order:
# (T, L, M, I, Θ, N, J)

def test_radian():
    assert dv.RADIAN == DIMENSIONLESS


def test_steradian():
    assert dv.STERADIAN == DIMENSIONLESS


def test_frequency():
    assert dv.FREQUENCY == TIME ** -1


def test_accelaration():
    assert dv.ACCELERATION == LENGTH / TIME ** 2


def test_force():
    assert dv.FORCE == MASS * dv.ACCELERATION


def test_pressure():
    assert dv.PRESSURE == dv.FORCE / dv.LENGTH ** 2


def test_stress():
    assert dv.PRESSURE == dv.STRESS


def test_energy():
    assert dv.FORCE * LENGTH


def test_work():
    assert dv.WORK == dv.ENERGY


def test_amout_of_heat():
    assert dv.AMOUNT_OF_HEAT == dv.ENERGY


def test_power():
    assert dv.POWER == dv.ENERGY / TIME


def test_radiant_flux():
    assert dv.RADIANT_FLUX == dv.POWER


def test_eletric_charge():
    assert dv.ELECTRIC_CHARGE == TIME * ELECTRIC_CURRENT


def test_electric_potential_difference():
    assert dv.ELECTRIC_POTENTIAL_DIFFERENCE == dv.POWER / ELECTRIC_CURRENT


def test_electrical_resistance():
    assert dv.ELECTRICAL_RESISTANCE == dv.ELECTRIC_POTENTIAL_DIFFERENCE / ELECTRIC_CURRENT


def test_conductance():
    assert dv.ELECTRICAL_CONDUCTANCE == ELECTRIC_CURRENT / dv.ELECTRIC_POTENTIAL_DIFFERENCE


def test_capacitance():
    assert dv.CAPACITANCE == dv.ELECTRIC_CHARGE / dv.ELECTRIC_POTENTIAL_DIFFERENCE


def test_magnetic_flux():
    assert dv.MAGNETIC_FLUX == dv.ELECTRIC_POTENTIAL_DIFFERENCE * TIME


def test_inductance():
    assert dv.INDUCTANCE == dv.MAGNETIC_FLUX / ELECTRIC_CURRENT


def test_magnetic_flux_density():
    assert dv.MAGNETIC_FLUX_DENSITY == dv.MAGNETIC_FLUX / LENGTH ** 2


def test_lumen():
    assert dv.LUMEN == LUMINOUS_INTENSITY * dv.STERADIAN


def test_lux():
    assert dv.LUX == dv.LUMEN / LENGTH ** 2


def test_becquerel():
    assert dv.BECQUEREL == dv.FREQUENCY


def test_gray():
    assert dv.GRAY == dv.ENERGY / MASS


def test_sievert():
    assert dv.SIEVERT == dv.GRAY


def test_katal():
    assert dv.KATAL == AMOUNT_OF_SUBSTANCE / TIME