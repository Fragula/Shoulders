# SPDX-License-Identifier: LGPL-3.0-or-later

from shoulders.dimension.base import (
    AMOUNT_OF_SUBSTANCE,
    ELECTRIC_CURRENT,
    LENGTH,
    LUMINOUS_INTENSITY,
    MASS,
    THERMODYNAMIC_TEMPERATURE,
    TIME,
)

from .unit import Unit

SECOND = Unit('second', 's', TIME)
METRE = Unit('metre', 'm', LENGTH)
KILOGRAM = Unit('kilogram', 'kg', MASS)
AMPERE = Unit('ampere', 'A', ELECTRIC_CURRENT)
KELVIN = Unit('kelvin', 'K', THERMODYNAMIC_TEMPERATURE)
MOLE = Unit('mole', 'mol', AMOUNT_OF_SUBSTANCE)
CANDELA = Unit('candela', 'cd', LUMINOUS_INTENSITY)