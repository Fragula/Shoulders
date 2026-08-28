from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction

from shoulders.dimension.dimension import Dimension
from shoulders.types import Number
from shoulders.unit.unit import Unit


class UnitRegistry:
    def __init__(self) -> None:
        _units: dict[Unit, UnitDefinition] = {}
        self._units = _units

    def get_factor(self, symbol: Unit) -> Number:
        if symbol not in self._units:
            error_msg = f"The symbol '{symbol} is not in the registry'"
            raise ValueError(error_msg)
        
        return self._units[symbol].factor

    def get_offset(self, symbol: Unit) -> Number:
        if symbol not in self._units:
            error_msg = f"The symbol '{symbol} is not in the registry'"
            raise ValueError(error_msg)
        
        return self._units[symbol].offset

    def get_dimension(self, symbol: Unit) -> Dimension:
        if symbol not in self._units:
            error_msg = f"The symbol '{symbol} is not in the registry'"
            raise ValueError(error_msg)
        
        return symbol.dimension

    def get_kind(self, symbol: Unit) -> str:
        if symbol not in self._units:
            error_msg = f"The symbol '{symbol} is not in the registry'"
            raise ValueError(error_msg)
        
        return self._units[symbol].kind

    def register_unit(self, symbol: Unit, factor: Number = 1, offset: Number = 0, kind: str = 'multiplicative') -> None:
        if not isinstance(factor, (int, float, Decimal, Fraction)):  # type: ignore
            error_msg = (
                "Factor must be a number (int | float | Decimal | Fraction)"
                f"| factor = {factor} & type = {type(factor)}"
                         )
            raise NotImplementedError(error_msg)

        if not isinstance(offset, (int, float, Decimal, Fraction)):  # type: ignore
            error_msg = (
                "Offset must be a number (int | float | Decimal | Fraction)"
                f"| offset = {offset} & type = {type(offset)}"
                         )
            raise NotImplementedError

        if factor < 0:
            error_msg = f"Factor must be positive | factor = '{factor}'"
            raise ValueError(error_msg)

        if symbol in self._units:
            error_msg = f"The symbol '{symbol}' is already used by another unit"
            raise ValueError(error_msg)

        valid_kinds = {'multiplicative', 'affine', 'logarithmic'}
        if kind not in valid_kinds:
            error_msg = f"Kind can only be: 'multiplicative', 'affine', 'logarithmic' | kind = {kind}" 
            raise TypeError(error_msg)

        unit = UnitDefinition(symbol, factor, offset, kind)
        self._units[symbol] = unit

    def remove_unit(self, symbol: Unit):
        if symbol not in self._units:
            error_msg = f"The unit '{symbol}' isn't used by any unit"
            raise ValueError(error_msg)  

        del self._units[symbol]

    def clear_dict(self):
        self._units.clear()

@dataclass
class UnitDefinition:
    symbol: Unit
    factor: Number = 1
    offset: Number = 0
    kind: str = 'multiplicative'

# TODO: Use YAML to make this better