"""Fitter."""

# ruff: noqa: D400 D415

import collections.abc
import functools
import timeit
import typing

import numpy as np
import scipy


_CurveFitFunc = collections.abc.Callable[[np.ndarray[tuple[int], np.dtype[np.float64]]], np.typing.NDArray[np.float64]]
_ComplexityFunc = collections.abc.Callable[..., np.float64]


def constant(n: int, a: float) -> np.float64:
    """O(1)"""
    return np.float64(n * 0 + a)


def logarithmic(n: int, a: float, b: float) -> np.float64:
    """O(log n)"""
    return np.float64(a * np.log2(n) + b)


def linear(n: int, a: float, b: float) -> np.float64:
    """O(n)"""
    return np.float64(a * n + b)


def linearithmic(n: int, a: float, b: float) -> np.float64:
    """O(n log n)"""
    return np.float64(a * n * np.log2(n) + b)


def quadratic(n: int, a: float, b: float, c: float) -> np.float64:
    """O(n^2)"""
    return np.float64(a * n**2 + b * n + c)


def cubic(n: int, a: float, b: float, c: float, d: float) -> np.float64:
    """O(n^3)"""
    return np.float64(a * n**3 + b * n**2 + c * n + d)


def exponential(n: int, a: float, b: float) -> np.float64:
    """O(2^n)"""
    return np.float64(a * 2**n + b)


class Asymptotic:
    """Asymptotic fit."""

    def __init__[T, **P](
        self,
        func: collections.abc.Callable[P, T],
        data: collections.abc.Iterable[typing.Any],
        timeit_number: int = 10,
    ) -> None:
        """Init."""
        self.func = func
        self.data = data
        self.timeit_number = timeit_number

    @property
    def _complexity_types(self) -> list[_ComplexityFunc]:
        return [
            constant,
            logarithmic,
            linear,
            linearithmic,
            quadratic,
            cubic,
            # exponential,
        ]

    @property
    def _timeit(self) -> np.ndarray[tuple[int, ...], np.dtype[np.float64]]:
        _ids_times = [
            (id_, timeit.Timer(functools.partial(self.func, d)).timeit(self.timeit_number))
            for id_, d in enumerate(self.data, start=1)
        ]
        return np.array(_ids_times).T

    @property
    def fit(self) -> str:
        """Fit."""
        times = self._timeit
        fits: list[tuple[float, _ComplexityFunc]] = []
        for complexity_type in self._complexity_types:
            _, pcov = scipy.optimize.curve_fit(
                # f=complexity_type,
                f=typing.cast("_CurveFitFunc", complexity_type),
                xdata=times[0],
                ydata=times[1],
                nan_policy="omit",
            )
            perr = np.sqrt(np.diag(pcov))
            fit_err: float = sum(perr)
            fits.append((fit_err, complexity_type))
        best_fit = min(fits)
        _, best_func = best_fit
        return f"{best_func.__doc__} - {best_func.__name__}"


def _try_constant(data: list[int]) -> int:
    return data[-1]

try_data = [list(range(n)) for n in range(10, 10_000, 10)]
# foo = Asymptotic(func=_try_constant, data=try_data)
# foo.fit
Asymptotic(func=_try_constant, data=try_data).fit

#
#
# foo._timeit
# n, times = foo._timeit
#
# # bar
# # baz
# # bar, baz =
# foo._fit()
# foo._fit()[0].details
# # bar
# # baz


