# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations


class Dimension:
    def __init__(self, exponent: tuple[float, ...]) -> None:
        if len(exponent) != 7:
            error_msg = f"Length of {exponent} must equal to seven | len = {len(exponent)}"
            raise ValueError(error_msg)
        self.exponent = exponent

    def __len__(self) -> int:
        return len(self.exponent)

    def __getitem__(self, index: int) -> float:
        return self.exponent[index]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Dimension):
            return NotImplemented
        return self.exponent == other.exponent

    def __mul__(self, other: object) -> Dimension:
        if not isinstance(other, Dimension):
            return NotImplemented
        new_exponent = tuple(
            a + b for a, b in zip(self.exponent, other.exponent)
        )
        return Dimension(new_exponent)
    
    def __truediv__(self, other: object) -> Dimension:
        if not isinstance(other, Dimension):
            return NotImplemented
        new_exponent = tuple(
            a - b for a, b in zip(self.exponent, other.exponent)
        )
        return Dimension(new_exponent)

    def __pow__(self, exponent: float) -> Dimension:
        if exponent == 0: 
            return Dimension((0, 0, 0, 0, 0, 0, 0))

        new_exponent = tuple(
            a * exponent for a in self.exponent
        )
        return Dimension(new_exponent)

    def __str__(self) -> str:
        return f'{self.exponent}'

    def __repr__(self) -> str:
        return f'exponent({self.exponent!r})'