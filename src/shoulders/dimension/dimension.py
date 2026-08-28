# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations

from shoulders.types import DimensionExponent

N_BASE = 7  # stands for number of base dimension

class Dimension:
    def __init__(self, exponents: tuple[DimensionExponent, ...]) -> None:
        if len(exponents) != N_BASE:
            error_msg = (
                f"Length of {exponents} must equal to seven | len = {len(exponents)}"
            )
            raise ValueError(error_msg)
        self.exponents = exponents

    def __hash__(self) -> int:
        return hash(self.exponents)

    def __len__(self) -> int:
        return len(self.exponents)

    def __getitem__(self, index: int) -> DimensionExponent:
        return self.exponents[index]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Dimension):
            return NotImplemented
        return self.exponents == other.exponents

    def __mul__(self, other: object) -> Dimension:
        if not isinstance(other, Dimension):
            return NotImplemented
        new_exponents = tuple(a + b for a, b in zip(self.exponents, other.exponents))
        return Dimension(new_exponents)

    def __truediv__(self, other: object) -> Dimension:
        if not isinstance(other, Dimension):
            return NotImplemented
        new_exponents = tuple(a - b for a, b in zip(self.exponents, other.exponents))
        return Dimension(new_exponents)

    def __pow__(self, exponent: DimensionExponent) -> Dimension:
        new_exponent = tuple(a * exponent for a in self.exponents)
        return Dimension(new_exponent)

    def __str__(self) -> str:
        return f"{self.exponents}"

    def __repr__(self) -> str:
        return f"Dimension({self.exponents!r})"