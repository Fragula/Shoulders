# SPDX-License-Identifier: LGPL-3.0-or-later

from .dimension import Dimension

TIME = Dimension((1, 0, 0, 0, 0, 0, 0))
LENGTH = Dimension((0, 1, 0, 0, 0, 0, 0))
MASS = Dimension((0, 0, 1, 0, 0, 0, 0))
ELECTRIC_CURRENT = Dimension((0, 0, 0, 1, 0, 0, 0))
THERMODYNAMIC_TEMPERATURE = Dimension((0, 0, 0, 0, 1, 0, 0))
AMOUNT_OF_SUBSTANCE = Dimension((0, 0, 0, 0, 0, 1, 0))
LUMINOUS_INTENSITY = Dimension((0, 0, 0, 0, 0, 0, 1))
DIMENSION_ONE = Dimension((0, 0, 0, 0, 0, 0, 0))