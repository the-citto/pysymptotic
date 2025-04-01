"""Complexities.

Ref:
    https://en.wikipedia.org/wiki/Big_O_notation

Common notations:
    O(1)        constant
    O(log n)    logarithmic
    O(n)	    linear
    O(n log n)  linearithmic
    O(n^2)      quadratic
    O(n^c)      polinomial
    O(c^x)      exponential
    O(n!)	    factorial
"""

# type ignore[misc] -> https://github.com/python/mypy/issues/15182
# ruff: noqa: D400 D415

import abc
import math
import typing

import numpy as np


__all__ = [
    "Constant",
    "Cubic",
    "Exponential",
    "Linear",
    "Linearithmic",
    "Logarithmic",
    "Quadratic",
]

def constant(n: int, a: float) -> float:
    """O(1)"""
    return n * 0 + a


def logarithmic(n: int, a: float, b: float) -> float:
    """O(log n)"""
    return a * math.log2(n) + b



constant.__name__
constant.__doc__



class ComplexityType(abc.ABC):
    """Complexity type."""

    notation: str

    @abc.abstractmethod
    def __new__(cls, n: int) -> float: # type: ignore[misc]
        """Set new."""
        raise NotImplementedError


class Constant(ComplexityType):
    """Constant."""

    notation: str = "O(1)"

    def __new__(cls, n: int, a: float) -> float: # type: ignore[misc]
        """Set new."""
        return n * 0 + a


class Logarithmic(ComplexityType):
    """Logarithmyc."""

    notation: str = "O(log n)"

    def __new__(cls, n: int, a: float, b: float) -> float: # type: ignore[misc]
        """Set new."""
        return typing.cast("float", a * np.log(n) + b)


class Linear(ComplexityType):
    """Linear."""

    notation: str = "O(n)"

    def __new__(cls, n: int, a: float, b: float) -> float: # type: ignore[misc]
        """Set new."""
        return a * n + b


class Linearithmic(ComplexityType):
    """Linearithmyc."""

    notation: str = "O(n log n)"

    def __new__(cls, n: int, a: float, b: float) -> float: # type: ignore[misc]
        """Set new."""
        return typing.cast("float", a * n * np.log(n) + b)


class Quadratic(ComplexityType):
    """Quadratic."""

    notation: str = "O(n^2)"

    def __new__(cls, n: int, a: float, b: float, c: float) -> float: # type: ignore[misc]
        """Set new."""
        return a * n**2 + b * n + c


class Cubic(ComplexityType):
    """Cubic."""

    notation: str = "O(n^3)"

    def __new__(cls, n: int, a: float, b: float, c: float, d: float) -> float: # type: ignore[misc]
        """Set new."""
        return a * n**3 + b * n**2 + c * n + d


class Exponential(ComplexityType):
    """Exponential."""

    notation: str = "O(2^n)"

    def __new__(cls, n: int, a: float, b: float) -> float: # type: ignore[misc]
        """Set new."""
        return typing.cast("float", a * 2**n + b)


class Factorial(ComplexityType):
    """Factorial."""

    notation: str = "O(n!)"

    def __new__(cls, n: int, a: float) -> float: # type: ignore[misc]
        """Set new."""
        return math.factorial(n) + a













