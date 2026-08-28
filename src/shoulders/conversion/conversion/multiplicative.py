from shoulders.conversion.registry import compass
from shoulders.quantity.quantity import Quantity
from shoulders.unit.unit import Unit


def _multiplicative_conversion(quantity: Quantity, target_unit: Unit) -> Quantity:
    dimension = quantity.unit.dimension
    factor = compass[dimension][0]

    f_a = factor[quantity.unit]
    f_b = factor[target_unit]
    x_a = quantity.magnitude

    x_b = x_a * (f_a / f_b) # type: ignore

    return Quantity(
        x_b, # type: ignore
        target_unit
    )

# TODO: remove 'type: ignore'