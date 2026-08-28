from shoulders.conversion.registry import compass
from shoulders.quantity.quantity import Quantity
from shoulders.unit.unit import Unit


def _affine_conversion(quantity: Quantity, target_unit: Unit) -> Quantity:
    dimension = quantity.unit.dimension
    factor = compass[dimension][0]

    # y = ax + b

    a1, b1 = factor[quantity.unit] # type: ignore
    x = quantity.magnitude
    y = a1 * x + b1  # type: ignore

    # x = (y-b/a)  

    a2, b2 = factor[target_unit]  # type: ignore
    result = (1 / a2) * y - (b2 / a2)  # type: ignore

    return Quantity(
        result, # type: ignore
        target_unit
    )

# TODO: remove 'type: ignore'