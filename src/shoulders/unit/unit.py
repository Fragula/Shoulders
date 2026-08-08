# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations

from shoulders.dimension.dimension import Dimension


class Unit:
    def __init__(
        self,
        # TODO: input name as a parameter
        symbol:str,
        dimension: Dimension,
    ) -> None:
        self.symbol = symbol
        self.dimension = dimension

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Unit):
            return NotImplemented
        return self.symbol == other.symbol

    def __mul__(self, other: object) -> Unit:
        ...
