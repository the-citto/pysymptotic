"""Fitter."""

import collections.abc
import functools
import timeit
import typing

import numpy as np
import scipy

from pysymptotic import complexity


class AsymptoticFitter:
    """Asymptotic fitter."""

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
    def _complexity_types(self) -> list[type[complexity.ComplexityType]]:
        return [
            complexity.Constant,
            complexity.Logarithmic,
            complexity.Linear,
            complexity.Linearithmic,
            complexity.Quadratic,
            complexity.Cubic,
            complexity.Exponential,
            # complexity.Factorial,
        ]

    @property
    def _timeit(self) -> tuple[tuple[float, ...], tuple[float, ...]]:
        _ids_times = [
            (float(id_), timeit.Timer(functools.partial(self.func, d)).timeit(self.timeit_number))
            for id_, d in enumerate(self.data, start=1)
        ]
        n, times = zip(*_ids_times, strict=True)
        return n, times

    def _fit(self) -> str:
        n, times = self._timeit
        fits = []
        for complexity_type in self._complexity_types:
            popt, pcov = scipy.optimize.curve_fit(
                complexity_type,
                n,
                times,
                nan_policy="omit",
            )
            perr = np.sqrt(np.diag(pcov))
            fit_err: float = sum(perr)
            fits.append((fit_err, complexity_type, popt))
        best_fit = min(fits)
        _, best_func, _ = best_fit
        return f"{best_func.notation}"



# def _try_constant(data: list[int]) -> int:
#     return data[-1]
#
# try_data = [list(range(n)) for n in range(10, 10_000, 10)]
# foo = AsymptoticFitter(func=_try_constant, data=try_data)
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
#
# Constant.func(1,2)
#
# popt: numpy.typing.NDArray[np.float64]
# pcov: numpy.typing.NDArray[np.float64]
# popt, pcov = scipy.optimize.curve_fit(
#     Constant.func,
#     n,
#     times,
#     nan_policy="omit",
# )
#
# list(popt)
# def _constant(n: float, a: float) -> float:
#     return n**0 + a
#
# popt, pcov = scipy.optimize.curve_fit(
#     _constant,
#     n,
#     times,
#     nan_policy="omit",
# )




#
# try_data = [{n: n for n in range(n)} for n in range(0, 1_000, 10)]
#
# def _o_linear(data: dict[int, int]) -> dict[int, int]:
#     return {k: v for k,v in data.items()}
#
#
# try_data = [list(range(n)) for n in range(10, 500, 10)]
# def _try_quardatic(data: list[int]) -> list[int]:
#     out = []
#     for _ in data:
#         for d in data:
#             out.append(d)
#     return out
#
# _plott(_try_quardatic, try_data)








# def _plott(func: Callable, try_data: t.Any) -> None:
#     print(func.__name__)
#     try_times = [
#         # (id_, timeit.Timer(lambda: func(data)).timeit(100))
#         (id_, timeit.Timer(lambda data=data: func(data)).timeit(100))
#         # (id_, timeit.Timer(lambda: _Wrapper(data)).timeit(100))
#         # (id_, timeit.Timer(lambda: _try_constant(data)).timeit(100))
#         for id_, data in enumerate(try_data, start=1)
#     ]
#     try_times_r = np.array(try_times)
#     fit_ = []
#     for comp_func in Complexities().types:
#         # print(func.__name__)
#         popt, pcov = scipy.optimize.curve_fit(comp_func, try_times_r[:, 0], try_times_r[:, 1], nan_policy="omit")
#         perr = np.sqrt(np.diag(pcov))
#         fit_err = sum(perr)
#         fit_.append((fit_err, comp_func, popt))
#     best_ = min(fit_)
#     _, best_func, popt_ = best_
#     print(best_func.__name__)
#     plt.plot(try_times_r[:, 0], try_times_r[:, 1], color="red")
#     plt.plot(try_times_r[:, 0], best_func(try_times_r[:, 0], *popt_), color="blue")
#     plt.show()



# def _try_constant(data: list[int]) -> int:
#     return data[-1]
#
# try_data = [list(range(n)) for n in range(10, 10_000, 10)]
# _plott(_try_constant, try_data)
















# class func_wrapper(object):
#
#     def __init__(self, n):
#         self.data = data_generator(n)
#
#     def __call__(self):
#         return func(self.data)

# class TimeComplexity:
#     """Time complexity."""
#
#     def __new__(
#         cls,
#         complexity_type: complexity.ComplexityType,
#         data: collections.abc.Iterable[typing.Any],
#         timeit_number: int = 10,
#     ) -> list[tuple[int, float]]:
#     # ) -> typing.Self:
#         """Set new."""
#         # return cls(func=func, data=data, timeit_number=timeit_number)
#
#     def _out(cls) -> list



# class TimeComplexity:
#     """Time complexity."""
#
#     def __new__[T, **P](
#         cls,
#         func: collections.abc.Callable[P, T],
#         data: collections.abc.Iterable[typing.Any],
#         timeit_number: int = 10,
#     ) -> list[tuple[int, float]]:
#     # ) -> typing.Self:
#         """Set new."""
#         return cls(func=func, data=data, timeit_number=timeit_number)


# timeit.Timer().timeit()


# complexity.Constant,
# complexity.Cubic,
# complexity.Exponential,
# complexity.Factorial,
# complexity.Linear,
# complexity.Linearithmic,
# complexity.Logarithmic,
# complexity.Quadratic,

# def _plott(func: Callable, try_data: t.Any) -> None:
#     print(func.__name__)
#     try_times = [
#         # (id_, timeit.Timer(lambda: func(data)).timeit(100))
#         (id_, timeit.Timer(lambda data=data: func(data)).timeit(100))
#         # (id_, timeit.Timer(lambda: _Wrapper(data)).timeit(100))
#         # (id_, timeit.Timer(lambda: _try_constant(data)).timeit(100))
#         for id_, data in enumerate(try_data, start=1)
#     ]
#     try_times_r = np.array(try_times)
#     fit_ = []
#     for comp_func in Complexities().types:
#         # print(func.__name__)
#         popt, pcov = scipy.optimize.curve_fit(comp_func, try_times_r[:, 0], try_times_r[:, 1], nan_policy="omit")
#         perr = np.sqrt(np.diag(pcov))
#         fit_err = sum(perr)
#         fit_.append((fit_err, comp_func, popt))
#     best_ = min(fit_)
#     _, best_func, popt_ = best_
#     print(best_func.__name__)
#     plt.plot(try_times_r[:, 0], try_times_r[:, 1], color="red")
#     plt.plot(try_times_r[:, 0], best_func(try_times_r[:, 0], *popt_), color="blue")
#     plt.show()


# def _try_constant(data: list[int]) -> int:
#     return data[-1]
#
# try_data = [list(range(n)) for n in range(10, 10_000, 10)]
# _plott(_try_constant, try_data)



