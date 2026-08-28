from shoulders.conversion.conversion.affine import _affine_conversion
from shoulders.conversion.conversion.multiplicative import _multiplicative_conversion
from shoulders.conversion.registry import compass
from shoulders.quantity.quantity import Quantity
from shoulders.unit.unit import Unit


def conversion(quantity: Quantity, target_unit: Unit) -> Quantity | None:
    dimension = quantity.unit.dimension
    conversion_type = compass[dimension][1]

    if dimension != target_unit.dimension:
        error_msg = f"You cannot convert '{quantity.unit}' to '{target_unit}'"
        raise ValueError(error_msg)

    if conversion_type == 'multiplicative':
        return _multiplicative_conversion(quantity, target_unit)

    if conversion_type == 'affine':
        return _affine_conversion(quantity, target_unit)
        
# TODO: remove 'type: ignore'