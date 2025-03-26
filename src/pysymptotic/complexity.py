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

import abc
import dataclasses
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


@dataclasses.dataclass
class ComplexityDetails:
    """Complexity details."""

    notation: str
    name: str
    general_form: str


class ComplexityFunction(float, abc.ABC):
    """Complexity function ABC."""

    @abc.abstractmethod
    def __new__(cls, value: float) -> typing.Self:
        """Set new."""
        return super().__new__(cls, value)

    @property
    @abc.abstractmethod
    def description(self) -> ComplexityDetails:
        """Description."""


class Constant(ComplexityFunction):
    """Constant."""

    def __new__(cls, n: int, a: float) -> typing.Self:
        """Set new."""
        cls.general_form = "n * 0 + a"
        value = n * 0 + a
        return super().__new__(cls, value)

    @property
    def description(self) -> ComplexityDetails:
        """Description."""
        return ComplexityDetails(
            notation="O(1)",
            name=self.__class__.__name__,
            general_form=self.general_form,
        )


class Logarithmic(ComplexityFunction):
    """Logarithmyc."""

    def __new__(cls, n: int, a: float, b: float) -> typing.Self:
        """Set new."""
        cls.general_form = "a * log n + b"
        value = a * np.log(n) + b
        return super().__new__(cls, value)

    @property
    def description(self) -> ComplexityDetails:
        """Description."""
        return ComplexityDetails(
            notation="O(log n)",
            name=self.__class__.__name__,
            general_form=self.general_form,
        )


class Linear(ComplexityFunction):
    """Linear."""

    def __new__(cls, n: int, a: float, b: float) -> typing.Self:
        """Set new."""
        cls.general_form = "a * n + b"
        value = a * n + b
        return super().__new__(cls, value)

    @property
    def description(self) -> ComplexityDetails:
        """Description."""
        return ComplexityDetails(
            notation="O(n)",
            name=self.__class__.__name__,
            general_form=self.general_form,
        )


class Linearithmic(ComplexityFunction):
    """Linearithmyc."""

    def __new__(cls, n: int, a: float, b: float) -> typing.Self:
        """Set new."""
        cls.general_form = "a * n * log n  + b"
        value = a * n * np.log(n) + b
        return super().__new__(cls, value)

    @property
    def description(self) -> ComplexityDetails:
        """Description."""
        return ComplexityDetails(
            notation="O(n log n)",
            name=self.__class__.__name__,
            general_form=self.general_form,
        )


class Quadratic(ComplexityFunction):
    """Quadratic."""

    def __new__(cls, n: int, a: float, b: float, c: float) -> typing.Self:
        """Set new."""
        cls.general_form = "a * n^2 + b * n + c"
        value = a * n**2 + b * n + c
        return super().__new__(cls, value)

    @property
    def description(self) -> ComplexityDetails:
        """Description."""
        return ComplexityDetails(
            notation="O(n^2)",
            name=self.__class__.__name__,
            general_form=self.general_form,
        )


class Cubic(ComplexityFunction):
    """Quadratic."""

    def __new__(cls, n: int, a: float, b: float, c: float, d: float) -> typing.Self:
        """Set new."""
        cls.general_form = "a * n^3 + b * n^2 + c * n + d"
        value = a * n**3 + b * n**2 + c * n + d
        return super().__new__(cls, value)

    @property
    def description(self) -> ComplexityDetails:
        """Description."""
        return ComplexityDetails(
            notation="O(n^3)",
            name=self.__class__.__name__,
            general_form=self.general_form,
        )


class Exponential(ComplexityFunction):
    """Exponential."""

    def __new__(cls, n: int, a: float, b: float) -> typing.Self:
        """Set new."""
        cls.general_form = "a * e^x + b"
        value = a * np.exp(n) + b
        return super().__new__(cls, value)

    @property
    def description(self) -> ComplexityDetails:
        """Description."""
        return ComplexityDetails(
            notation="O(e^n)",
            name=self.__class__.__name__,
            general_form=self.general_form,
        )


class Factorial(ComplexityFunction):
    """Factorial."""

    def __new__(cls, n: int, a: float) -> typing.Self:
        """Set new."""
        cls.general_form = "a * e^x + b"
        value = math.factorial(n) + a
        return super().__new__(cls, value)

    @property
    def description(self) -> ComplexityDetails:
        """Description."""
        return ComplexityDetails(
            notation="O(e^n)",
            name=self.__class__.__name__,
            general_form=self.general_form,
        )














