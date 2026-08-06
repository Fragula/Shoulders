from __future__ import annotations


class Dimension:
    def __init__(self, dimension) -> None:
        if len(dimension) != 7:
            error_msg = f"Length of {dimension} must equal to seven | len = {len(dimension)}"
            raise ValueError(error_msg)
        self.dimension = dimension

    def __eq__(self, other) -> bool:
        if not isinstance(other, Dimension):
            return NotImplemented
        return self.dimension == other.dimension

    def __mul__(self, other) -> Dimension:
        if not isinstance(other, Dimension):
            return NotImplemented
        new_dimension = tuple(a + b for a, b in zip(self.dimension, other.dimension))
        return Dimension(new_dimension)
    
    def __truediv__(self, other) -> Dimension:
        if not isinstance(other, Dimension):
            return NotImplemented
        new_dimension = tuple(a - b for a, b in zip(self.dimension, other.dimension))
        return Dimension(new_dimension)

    def __pow__(self, exponent: float) -> Dimension:
        new_dimension = tuple(a * exponent for a in (self.dimension))
        return Dimension(new_dimension)

    def __str__(self) -> str:
        return f'{self.dimension}'

    def __repr__(self) -> str:
        return f'Dimension({self.dimension!r})'