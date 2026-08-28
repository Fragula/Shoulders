# WARNING: this will be deleted soon

from decimal import Decimal
from fractions import Fraction
from typing import Literal

from shoulders.conversion.base.electric_current import ABAMPERE, STATAMPERE
from shoulders.conversion.base.length import FOOT, INCH, MILE, YARD
from shoulders.conversion.base.mass import POUND
from shoulders.conversion.base.themodynamic_temperature import (
    DEGREE_CELSIUS,
    DEGREE_FAHRENHEIT,
    DEGREE_RANKINE,
)
from shoulders.conversion.base.time import DAY, HOUR, MINUTE, WEEK
from shoulders.dimension.base import (
    ELECTRIC_CURRENT,
    LENGTH,
    MASS,
    THERMODYNAMIC_TEMPERATURE,
    TIME,
)
from shoulders.dimension.dimension import Dimension
from shoulders.types import Number
from shoulders.unit.base import AMPERE, KELVIN, KILOGRAM, METRE, SECOND
from shoulders.unit.unit import Unit

time_list: dict[Unit, Number] = {
    SECOND: 1,
    MINUTE: 60,
    HOUR: 3600,
    DAY: 86400,
    WEEK: 604800,
}

length_list: dict[Unit, Number] = {
    INCH: Decimal('0.0254'),
    FOOT: Decimal('0.3048'),
    YARD: Decimal('0.9144'),
    METRE: 1,
    MILE: Decimal('1609.344'),
}

mass_list: dict[Unit, Number] = {
    POUND: Decimal('0.45359237'),
    KILOGRAM: 1,
}

electric_current_list: dict[Unit, Number] = {
    STATAMPERE: Decimal('3.3356409519815206e-10'),
    AMPERE: 1,
    ABAMPERE: 10,
}

thermodynamic_temperature_list: dict[Unit, tuple[Number, Number]] = {
    KELVIN: (1, 0),  # 1, 0 stands for a, b in the y = ax + b formula
    DEGREE_CELSIUS: (1, Fraction(5463, 20)),  # 5463/20 = 273.15
    DEGREE_FAHRENHEIT: (Fraction(5, 9), Fraction(229835, 900)),  # 229835/900 = 255.372222222...
    DEGREE_RANKINE: (Fraction(5, 9), 0),
}

# Setting up a compass to the conversion function

MultiplicativeDefinition = dict[Unit, Number]
AffineDefinition = dict[Unit, tuple[Number, Number]]
ConversionKind = Literal[
    'multiplicative',
    'affine',
    'logarithmic',
]

compass_type = dict[
    Dimension,
    tuple[
        MultiplicativeDefinition | AffineDefinition,
        str
    ]
]

compass: compass_type = {
    TIME: (time_list, 'multiplicative'),
    LENGTH: (length_list, 'multiplicative'),
    MASS: (mass_list, 'multiplicative'),
    ELECTRIC_CURRENT: (electric_current_list, 'multiplicative'),
    THERMODYNAMIC_TEMPERATURE: (thermodynamic_temperature_list, 'affine'),
}