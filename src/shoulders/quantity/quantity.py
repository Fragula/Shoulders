# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations

from numbers import Number

from shoulders.dimension.dimension import Dimension


class Quantity:
    def __init__(self, magnitude: Number, dimension: Dimension) -> None:
        self.magnitude = magnitude
        self.dimension = dimension

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Quantity):
            return NotImplemented
        return (
            self.dimension == other.dimension
            and self.magnitude == other.magnitude
        )
    
    def __add__(self, other: object) -> Quantity:
        if not isinstance(other, Quantity):
            return NotImplemented
        
        if self.dimension != other.dimension:
            error_msg = (
                f"You cannot add different dimensions | '{self.dimension}' & '{other.dimension}'"
            )
            raise TypeError(error_msg)
        
        return Quantity(
            self.magnitude + other.magnitude, 
            self.dimension, 
        )

    def __sub__(self, other: object) -> Quantity:
        if not isinstance(other, Quantity):
            return NotImplemented
        
        if self.dimension != other.dimension:
            error_msg = (
                f"You cannot subtract different dimensions | '{self.dimension}' & '{other.dimension}'"
            )
            raise TypeError(error_msg)
        
        return Quantity(
            self.magnitude - other.magnitude, 
            self.dimension,
        )

    def __mul__(self, other: Quantity | Number) -> Quantity:
        if isinstance(other, Quantity):
            return Quantity(
                self.magnitude * other.magnitude, 
                self.dimension * other.dimension,
            )

        if isinstance(other, Number):
            return Quantity(
                self.magnitude * other,
                self.dimension,
            )

        return NotImplemented

    def __truediv__(self, other: Quantity | Number) -> Quantity:

        if isinstance(other, Quantity):
            if other.magnitude == 0: 
                raise ZeroDivisionError('You cannot divide by zero')

            return Quantity(
                self.magnitude / other.magnitude, 
                self.dimension / other.dimension,
            )

        if isinstance(other, Number):
            if other == 0: 
                raise ZeroDivisionError('You cannot divide by zero')

            return Quantity(
                self.magnitude / other, 
                self.dimension,
            )

        return NotImplemented

    def __pow__(self, exponent: float) -> Quantity:
    # TODO: support complex exponents
        if self.magnitude == 0 and exponent < 0: raise ZeroDivisionError('Cannot power 0 by a negative exponent')

        return Quantity(
            self.magnitude**exponent, 
            self.dimension**exponent,
        )
    
    def __abs__(self) -> Quantity:
        return Quantity(abs(self.magnitude), self.dimension)

    def __neg__(self) -> Quantity:
        return Quantity(-self.magnitude, self.dimension)

    def __pos__(self) -> Quantity:
        return Quantity(self.magnitude, self.dimension,)

    def __str__(self) -> str:
        return f'{self.magnitude} {self.dimension}'

    def __repr__(self) -> str:
        return f'Quantity({self.dimension!r}, {self.magnitude!r})'