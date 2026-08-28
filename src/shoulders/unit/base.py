# SPDX-License-Identifier: LGPL-3.0-or-later

from shoulders.dimension.base import (
    AMOUNT_OF_SUBSTANCE,
    DIMENSION_ONE,
    ELECTRIC_CURRENT,
    LENGTH,
    LUMINOUS_INTENSITY,
    MASS,
    THERMODYNAMIC_TEMPERATURE,
    TIME,
)

from .unit import Unit

SECOND = Unit('s', TIME, {'s': 1})
s = SECOND

METRE = Unit('m', LENGTH, {'m': 1})
m = METRE

KILOGRAM = Unit('kg', MASS, {'kg': 1})
kg = KILOGRAM

AMPERE = Unit('A', ELECTRIC_CURRENT, {'A': 1})
A = AMPERE

KELVIN = Unit('K', THERMODYNAMIC_TEMPERATURE, {'K': 1})
K = KELVIN

MOLE = Unit('mol', AMOUNT_OF_SUBSTANCE, {'mol': 1})
mol = MOLE

CANDELA = Unit('cd', LUMINOUS_INTENSITY, {'cd': 1})
cd = CANDELA

ONE = Unit("1", DIMENSION_ONE, {"1": 1})