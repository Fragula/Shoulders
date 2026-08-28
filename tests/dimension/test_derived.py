import shoulders.dimension.derived as dv
from shoulders.dimension.base import (
    AMOUNT_OF_SUBSTANCE,
    DIMENSION_ONE,
    ELECTRIC_CURRENT,
    LENGTH,
    LUMINOUS_INTENSITY,
    MASS,
    TIME,
)

# Dimension order:
# (T, L, M, I, Θ, N, J)


def test_plane_angle():
    assert dv.PLANE_ANGLE == DIMENSION_ONE


def test_solid_angle():
    assert dv.SOLID_ANGLE == DIMENSION_ONE


def test_plane_angle_to_solid_angle():
    assert dv.SOLID_ANGLE == dv.PLANE_ANGLE**2


def test_frequency():
    assert dv.FREQUENCY == TIME**-1


def test_force():
    assert dv.FORCE == MASS * LENGTH / TIME**2


def test_pressure():
    assert dv.PRESSURE == dv.FORCE / dv.LENGTH**2


def test_stress():
    assert dv.PRESSURE == dv.STRESS


def test_energy():
    assert dv.ENERGY == dv.FORCE * LENGTH


def test_work():
    assert dv.WORK == dv.ENERGY


def test_amount_of_heat():
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
    assert (
        dv.ELECTRICAL_RESISTANCE == dv.ELECTRIC_POTENTIAL_DIFFERENCE / ELECTRIC_CURRENT
    )


def test_conductance():
    assert (
        dv.ELECTRICAL_CONDUCTANCE == ELECTRIC_CURRENT / dv.ELECTRIC_POTENTIAL_DIFFERENCE
    )


def test_capacitance():
    assert dv.CAPACITANCE == dv.ELECTRIC_CHARGE / dv.ELECTRIC_POTENTIAL_DIFFERENCE


def test_magnetic_flux():
    assert dv.MAGNETIC_FLUX == dv.ELECTRIC_POTENTIAL_DIFFERENCE * TIME


def test_inductance():
    assert dv.INDUCTANCE == dv.MAGNETIC_FLUX / ELECTRIC_CURRENT


def test_magnetic_flux_density():
    assert dv.MAGNETIC_FLUX_DENSITY == dv.MAGNETIC_FLUX / LENGTH**2


def test_luminous_flux():
    assert dv.LUMINOUS_FLUX == LUMINOUS_INTENSITY * dv.SOLID_ANGLE


def test_illuminance():
    assert dv.ILLUMINANCE == dv.LUMINOUS_FLUX / LENGTH**2


def test_radionuclide_activity():
    assert dv.RADIONUCLIDE_ACTIVITY == dv.FREQUENCY


def test_aborbed_dose():
    assert dv.ABSORBED_DOSE == dv.ENERGY / MASS


def test_kerma():
    assert dv.KERMA == dv.ENERGY / MASS


def test_dose_equivalent():
    assert dv.DOSE_EQUIVALENT == dv.ENERGY / MASS


def test_catalytic_activity():
    assert dv.CATALYTIC_ACTIVITY == AMOUNT_OF_SUBSTANCE / TIME
