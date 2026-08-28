# SPDX-License-Identifier: LGPL-3.0-or-later

from decimal import Decimal
from fractions import Fraction

Number = int | float | Fraction

SUBSCRIPT = {
    "0": "₀",
    "1": "₁",
    "2": "₂",
    "3": "₃",
    "4": "₄",
    "5": "₅",
    "6": "₆",
    "7": "₇",
    "8": "₈",
    "9": "₉",
    "-": "₋",
    "/": "⁄",
}

SUPERSCRIPT = {
    "0": "⁰",
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹",
    "-": "⁻",
    "/": "⁄",
}

FRACTION = {
    "1/2": "½",
    "1/3": "⅓",
    "2/3": "⅔",
    "1/4": "¼",
    "3/4": "¾",
    "1/5": "⅕",
    "2/5": "⅖",
    "3/5": "⅗",
    "4/5": "⅘",
    "1/6": "⅙",
    "5/6": "⅚",
    "1/7": "⅐",
    "1/8": "⅛",
    "3/8": "⅜",
    "5/8": "⅝",
    "7/8": "⅞",
    "1/9": "⅑",
    "1/10": "⅒",
}


def to_subscript(exponent: Number) -> str:
    result: list[str] = []

    if exponent.is_integer() is False:
        float_exponent = Fraction(Decimal(f"{exponent}")).limit_denominator()
        for k, v in FRACTION.items():
            if str(float_exponent) == k and float_exponent > 0:
                return v

            elif str(float_exponent * -1) == k:
                return f"⁻{v}"

        numerator = to_superscript(float_exponent.numerator)
        denominator = to_subscript(float_exponent.denominator)

        return f"{numerator}⁄{denominator}"

    for char in str(int(exponent)):
        result.append(SUBSCRIPT[char])
    return "".join(result)


def to_superscript(exponent: Number) -> str:
    result: list[str] = []

    if exponent.is_integer() is False:
        float_exponent = Fraction(Decimal(f"{exponent}")).limit_denominator()

        for k, v in FRACTION.items():
            if str(float_exponent) == k and float_exponent > 0:
                return v

            elif str(float_exponent * -1) == k:
                return f"⁻{v}"

        numerator = to_superscript(float_exponent.numerator)
        denominator = to_subscript(float_exponent.denominator)

        return f"{numerator}⁄{denominator}"

    for char in str(int(exponent)):
        result.append(SUPERSCRIPT[char])
    return "".join(result)