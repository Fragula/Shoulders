# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType

from shoulders.dimension.base import *
from shoulders.dimension.dimension import Dimension
from shoulders.formatting.unicode import to_superscript
from shoulders.types import DimensionExponent

# TODO: fix the composition problem

@dataclass(eq=True, frozen=True)
class Unit:
    # TODO: input name as a parameter
    symbol: str
    dimension: Dimension
    composition: MappingProxyType[str, DimensionExponent]

    def __post_init__(self) -> None:
        composition_proxy = MappingProxyType(self.composition)
        object.__setattr__(self, 'composition', composition_proxy)

    @classmethod
    def self_referential(
        cls,
        symbol: str,
        dimension: Dimension,
        composition: MappingProxyType[Unit, DimensionExponent],
    ) -> Unit:
        instance = cls(symbol, dimension, composition={})
        instance.composition = {symbol: 1}
        return instance

    def __mul__(self, other: object) -> Unit:
        if not isinstance(other, Unit):
            return NotImplemented

        composition = dict(self.composition)

        for s, p in other.composition.items():
            if s in composition:
                new_p = p + composition[s]

                if new_p == 0:
                    del composition[s]

                else:
                    composition[s] = new_p

            else:
                composition[s] = p

        new_symbol = f"{self.symbol}*{other.symbol}"
        new_dimension = self.dimension * other.dimension

        return Unit(new_symbol, new_dimension, composition)

    def __truediv__(self, other: object) -> Unit:
        if not isinstance(other, Unit):
            return NotImplemented

        composition = dict(self.composition)

        for s, p in other.composition.items():
            if s in composition:
                new_p = p - composition[s]

                if new_p == 0:
                    del composition[s]

                else:
                    composition[s] = new_p

            else:
                composition[s] = p

        new_symbol = f"{self.symbol}/{other.symbol}"
        new_dimension = self.dimension / other.dimension

        return Unit(new_symbol, new_dimension, composition)

    def __pow__(self, exponent: DimensionExponent):
        composition = dict(self.composition)

        for s in self.composition:
            p = self.composition[s] * exponent

            if p == 0:
                del composition[s]

            else:
                composition[s] = p

        new_symbol = f"{self.symbol}^{exponent}"
        new_dimension = self.dimension**exponent

        return Unit(new_symbol, new_dimension, composition)

    def __str__(self) -> str:
        composition: list[str] = []

        for s, p in self.composition.items():
            superstring = f"{s}{to_superscript(p)}"
            if p == 1:
                superstring = s
            composition.append(superstring)

        symbol = "".join(composition)

        return symbol

    def __repr__(self) -> str:
        return f"Unit({self.symbol!r}, {self.dimension!r}, {self.composition!r})"