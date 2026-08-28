# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations

from shoulders.types import Number
from shoulders.unit.unit import Unit


class Quantity:
    def __init__(self, magnitude: Number, unit: Unit) -> None:
        self.magnitude = magnitude
        self.unit = unit

    def __hash__(self) -> int:
        quantity_hash = self.magnitude, self.unit
        return hash(quantity_hash)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Quantity):
            return NotImplemented
        return (
            self.magnitude == other.magnitude
            and self.unit == other.unit
        )

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Quantity):
            return NotImplemented

        return not (self == other)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Quantity):
            return NotImplemented

        if self.unit != other.unit:
            raise TypeError('You cannot compare two different quantities')

        return self.magnitude < other.magnitude

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Quantity):
            return NotImplemented

        if self.unit != other.unit:
            raise TypeError('You cannot compare two different quantities')

        return self.magnitude <= other.magnitude

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Quantity):
            return NotImplemented

        if self.unit != other.unit:
            raise TypeError('You cannot compare two different quantities')

        return self.magnitude > other.magnitude

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Quantity):
            return NotImplemented

        if self.unit != other.unit:
            raise TypeError('You cannot compare two different quantities')

        return self.magnitude >= other.magnitude

    def __add__(self, other: object) -> Quantity:
        if not isinstance(other, Quantity):
            return NotImplemented
        
        if self.unit != other.unit:
            error_msg = (
                f"You cannot add different units | '{self.unit}' & '{other.unit}'"
            )
            raise TypeError(error_msg)
        
        return Quantity(
            self.magnitude + other.magnitude, 
            self.unit, 
        )

    def __radd__(self, other: object) -> Quantity:
        return self.__add__(other)

    def __sub__(self, other: object) -> Quantity:
        if not isinstance(other, Quantity):
            return NotImplemented
        
        if self.unit != other.unit:
            error_msg = (
                f"You cannot subtract different units | '{self.unit}' & '{other.unit}'"
            )
            raise TypeError(error_msg)
        
        return Quantity(
            self.magnitude - other.magnitude, 
            self.unit,
        )

    def __mul__(self, other: Quantity | Number) -> Quantity:
        if isinstance(other, Quantity):
            return Quantity(
                self.magnitude * other.magnitude, 
                self.unit * other.unit,
            )

        if not isinstance(other, Quantity):
            return NotImplemented

        return Quantity(
            self.magnitude * other,
            self.unit,
        )

    def __rmul__(self, other: Quantity | Number) -> Quantity:
        return self.__mul__(other)

    def __truediv__(self, other: Quantity | Number) -> Quantity:

        if isinstance(other, Quantity):
            if other.magnitude == 0: 
                raise ZeroDivisionError('You cannot divide by zero')

            return Quantity(
                self.magnitude / other.magnitude, 
                self.unit / other.unit,
            )

        if not isinstance(other, Quantity):
            return NotImplemented

        if other == 0: 
            raise ZeroDivisionError('You cannot divide by zero')

        return Quantity(
            self.magnitude / other, 
            self.unit,
        )

    def __pow__(self, exponent: float) -> Quantity:
        if self.magnitude == 0 and exponent < 0: raise ZeroDivisionError('Cannot power 0 by a negative exponent')

        return Quantity(
            self.magnitude**exponent, 
            self.unit**exponent,
        )
    
    def __abs__(self) -> Quantity:
        return Quantity(abs(self.magnitude), self.unit)

    def __neg__(self) -> Quantity:
        return Quantity(-self.magnitude, self.unit)

    def __pos__(self) -> Quantity:
        return Quantity(self.magnitude, self.unit,)

    def __str__(self) -> str:
        return f'{self.magnitude} {self.unit}'

    def __repr__(self) -> str:
        return f'Quantity({self.magnitude!r}, {self.unit!r})'