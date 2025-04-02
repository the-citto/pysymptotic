"""Fit."""

# import abc
# import timeit
# import typing as t
# from collections.abc import Callable
#
# import numpy as np
# import scipy
# from matplotlib import pyplot as plt
#
#
# class Complexities:
#     """Functions forms."""
#
#     @property
#     def types(self) -> list[Callable]:
#         return [
#             self._constant,
#             self._logarithmic,
#             self._linear,
#             self._linearithmic,
#             self._quadratic,
#             self._cubic,
#             # self._polinomial,
#             # self._exponential,
#             # self._factorial,
#         ]
#
#     def _constant(self, n: float, a: float) -> float:
#         return n**0 + a
#
#     def _logarithmic(self, n: float, a: float, b: float) -> float:
#         return a * np.log(n) + b
#
#     def _linear(self, n: float, a: float, b: float) -> float:
#         return a * n + b
#
#     def _linearithmic(self, n: float, a: float, b: float) -> float:
#         return a * n * np.log(n) + b
#
#     def _quadratic(self, n: float, a: float, b: float, c: float) -> float:
#         return a * n**2 + b * n + c
#
#     def  _cubic(self, n: float, a: float, b: float, c: float, d: float) -> float:
#         return a * n**3 + b * n**2 + c * n + d
#
#     def _polinomial(self, n: float, c: float, d: float) -> float:
#         return n**c + d
#
#     def _exponential(self, n: float, a: float, b: float) -> float:
#         return a * np.exp(n) + b
#
#     def _factorial(self, n: float, a: float, b: float) -> float:
#         ...
#
#
# # #
# # # P = t.ParamSpec("P")
# # # T = t.TypeVar("T")
# # #
# # #
# # # class ForTimer(t.Generic[P, T]):
# # #     """For timer."""
# # #
# # #     def __init__(self, func: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> None:
# # #         self.func = func
# # #         self.args = args
# # #         self.kwargs = kwargs
# # #
# # #     def __call__(self) -> T:
# # #         return self.func(*self.args, **self.kwargs)
# # #
# #
# #
# #
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
#
#
#
#
#
# def _try_constant(data: list[int]) -> int:
#     return data[-1]
#
# try_data = [list(range(n)) for n in range(10, 10_000, 10)]
# _plott(func=_try_constant, try_data=try_data)
#
#
#
# try_data = [{n: n for n in range(n)} for n in range(0, 1_000, 10)]
#
# def _o_linear(data: dict[int, int]) -> dict[int, int]:
#     return {k: v for k,v in data.items()}
#
# # # def _try_linear(data: dict[int, int]) -> dict[int, int]:
# # #     return {k: v for k,v in data.items()}
# #     # last = data[-1]
# #     # for d in data:
# #     #     if d == last:
# #     #         return d
# #     # raise RuntimeError
# #
# # try_data = [list(range(n)) for n in range(10, 1_000, 10)]
# def _try_linear(data: list[int]) -> list[int]:
#     return [d for d in data]
#
# _plott(_try_linear, try_data)
#
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
#
#
# try_data = [list(range(n)) for n in range(10, 250, 20)]
# def _try_cubic(data: list[int]) -> list[int]:
#     out = []
#     for _ in data:
#         for _ in data:
#             for d in data:
#                 out.append(d)
#     return out
#
# _plott(_try_cubic, try_data)
#
#
# #
# #
# #
# # # class Wrapper(ABC):
# # #     """Abstract time generator."""
# # #
# # #     def __init__(
# # #         self,
# # #         # n: int,
# # #         # /,
# # #         *args: ...,
# # #         **kwargs: ...,
# # #     ) -> None:
# # #         # self.n = n
# # #         self.args = args
# # #         self.kwargs = kwargs
# # #
# # #     @abstractmethod
# # #     def __call__(self) -> ...: ...
# #
# #
# #
# # # class _OConstant(TimesGenerator):
# # #
# # #     def __call__(self) -> int:
# # #         return 1
# #
# #
# # # def _o_constant(data: dict[int, int], key_: int) -> int:
# # #     return data[key_]
# # #
# # # data_test = [{n: n for n in range(2, n)} | {1: 1} for n in range(0, 1_000, 10)]
# # #
# # # class _OConstant(Wrapper):
# # #
# # #     def __call__(self) -> int:
# # #         return _o_constant(*self.args, **self.kwargs)
# # #
# # # times_test = []
# # # for r, data in enumerate(data_test):
# # #     times_test.append((r, timeit.Timer(_OConstant(data, 1)).timeit(100)))
# # #
# # # times_r = np.array(times_test)
# #
# # # func = _constant
# # # func = _linear
# # # func = _logarithmic
# #
# # popt, pcov = scipy.optimize.curve_fit(func, times_r[:, 0], times_r[:, 1], nan_policy="omit")
# #
# # perr = np.sqrt(np.diag(pcov))
# # print(perr)
# # for e in perr:
# #     print(f"{e:.2G}")
# #
# # print(sum(perr))
# #
# #
# # plt.plot(times_r[:, 0], times_r[:, 1], color="red")
# # plt.plot(times_r[:, 0], func(times_r[:, 0], *popt), color="blue")
# #
# # plt.show()
# #
# #
# #
# #
# #
# #
# # def _o_linear(data: dict[int, int]) -> dict[int, int]:
# #     return {k: v for k,v in data.items()}
# #
# # data_test = [{n: n for n in range(n)} for n in range(0, 1_000, 10)]
# #
# # class _OLinear(Wrapper):
# #
# #     def __call__(self) -> dict[int, int]:
# #         return _o_linear(*self.args, **self.kwargs)
# #
# # times_test = []
# # for r, data in enumerate(data_test, start=1):
# #     times_test.append((r, timeit.Timer(_OLinear(data)).timeit(100)))
# #
# # times_r = np.array(times_test)
# #
# #
# #
# # func = _constant
# # popt, pcov = scipy.optimize.curve_fit(func, times_r[:, 0], times_r[:, 1], nan_policy="omit")
# # perr = np.sqrt(np.diag(pcov))
# # print(perr)
# # for e in perr:
# #     print(f"{e:.2G}")
# #
# # _constant_err = sum(perr)
# #
# # func = _logarithmic
# # popt, pcov = scipy.optimize.curve_fit(func, times_r[:, 0], times_r[:, 1], nan_policy="omit")
# # perr = np.sqrt(np.diag(pcov))
# # print(perr)
# # for e in perr:
# #     print(f"{e:.2G}")
# #
# # _logarithmic_err = sum(perr)
# #
# # func = _linear
# # popt, pcov = scipy.optimize.curve_fit(func, times_r[:, 0], times_r[:, 1], nan_policy="omit")
# # perr = np.sqrt(np.diag(pcov))
# # print(perr)
# # for e in perr:
# #     print(f"{e:.2G}")
# #
# # _linear_err = sum(perr)
# #
# # func = _linearithmic
# # popt, pcov = scipy.optimize.curve_fit(func, times_r[:, 0], times_r[:, 1], nan_policy="omit")
# # perr = np.sqrt(np.diag(pcov))
# # print(perr)
# # for e in perr:
# #     print(f"{e:.2G}")
# #
# # _linearithmic_err = sum(perr)
# #
# #
# #
# #
# # print(_constant_err)
# # print(_logarithmic_err)
# # print(_linear_err)
# # print(_linearithmic_err)
# #
# # min(_constant_err, _logarithmic_err, _linear_err, _linearithmic_err)
# #
# # plt.plot(times_r[:, 0], times_r[:, 1], color="red")
# # plt.plot(times_r[:, 0], func(times_r[:, 0], *popt), color="blue")
# #
# # plt.show()
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # times_test = [
# # #     (r, timeit.Timer(lambda: _o_constant(data, 1)).timeit(10))
# # #     for r, data in enumerate(data_test)
# # # ]
# #
# # # timeit.Timer(lambda: _o_constant(data_test[-1], 1)).timeit(10)
# # #
# # #
# # # timeit.Timer(lambda: {n: n for n in range(100)}).timeit(1_000)
# # # timeit.Timer(lambda: {n: n for n in range(1_000)}).timeit(1_000)
# # # timeit.Timer(lambda: {n: n for n in range(10_000)}).timeit(1_000)
# # # timeit.Timer(lambda: {n: n for n in range(100_000)}).timeit(1_000)
# #
# #
# #
# #
# #
# #
# # # class func_wrapper(object):
# # #
# # #     def __init__(self, n):
# # #         self.data = data_generator(n)
# # #
# # #     def __call__(self):
# # #         return func(self.data)
# #
# #
# #
# # # def gen_two_sum_eafp(nums: list[int], target: int) -> c.Callable:
# # #     """Generate gen_two_sum_eafp."""
# # #     def _gen_two_sum_eafp() -> list[int]:
# # #         return two_sum_eafp(nums, target)
# # #     return _gen_two_sum_eafp
# # #
# # # # two_sum_eafp([2, 7, 11, 15], 9)
# # #
# # # class GenTwoSumEAFP:
# # #     """Generate gen_two_sum_eafp."""
# # #
# # #     def __init__(self, nums: list[int], target: int) -> None:
# # #         self.nums = nums
# # #         self.target = target
# # #
# # #     def __call__(self) -> list[int]:
# # #         return two_sum_eafp(self.nums, self.target)
# # #
# # #
# # # # class GenTwoSum2:
# # # #     """Generate gen_two_sum_eafp."""
# # # #
# # # #     def __init__(
# # # #         self,
# # # #         # n: int,
# # # #         func: t.Callable[P, T],
# # # #         # *args: P.args,
# # # #         # **kwargs: P.kwargs,
# # # #     ) -> None:
# # # #         self.func = func
# # # #         #self.args = args
# # # #         # self.kwargs = kwargs
# # # #
# # # #     def __call__(
# # # #         self,
# # # #         *args: P.args,
# # # #         **kwargs: P.kwargs,
# # # #     ) -> T:
# # # #         return self.func(*args, **kwargs)
# # #
# # #
# # # # P = t.ParamSpec("P")
# # # # T = t.TypeVar("T")
# # #
# # #
# # # class TimesGenerator(ABC):
# # #     """Abstract time generator."""
# # #
# # #     def __init__(self, n: int, /, *args: ..., step: int = 10, **kwargs: ...) -> None:
# # #         self.n = n
# # #         self.args = args
# # #         self.kwargs = kwargs
# # #
# # #     @abstractmethod
# # #     def __call__(self) -> ...: ...
# # #
# # #
# # # # class GenTwoSum3(TimesGenerator):
# # # #     """Foo."""
# # # #
# # # #     def __call__(self) -> ...:
# # # #         return super().__call__()
# # #
# # # class GenTwoSum2:
# # #     """Generate gen_two_sum_eafp."""
# # #
# # #     def __init__(
# # #         self,
# # #         n: int,
# # #         /,
# # #         # func: t.Callable[P, T],
# # #         # *args: P.args,
# # #         # **kwargs: P.kwargs,
# # #         # *args: t.Any,
# # #         *args: ...,
# # #         **kwargs: ...,
# # #     ) -> None:
# # #         # self.func = func
# # #         # print(func)
# # #         # print(args)
# # #         self.args = args
# # #         self.kwargs = kwargs
# # #
# # #     def __call__(
# # #         self,
# # #         # *args: P.args,
# # #         # **kwargs: P.kwargs,
# # #     ) -> list[int]:
# # #         # print(self.args)
# # #         # print(self.kwargs)
# # #         return two_sum_eafp(*self.args, **self.kwargs)
# # #         # return two_sum_eafp(*self.args, **self.kwargs)
# # #
# # #
# # #
# # # def dataset_generator(n: int, /, *args: ..., **kwargs: ...) -> ...:
# # #     """Dataset generator decorator."""
# # #
# # #     # def wrapper(func: c.Callable)
# # #
# # #
# # #
# # #
# # # # timed = timeit.Timer(GenTwoSum2(1, two_sum_eafp, [2, 7, 11, 15], 9))
# # # timed = timeit.Timer(GenTwoSum2(1, [2, 7, 11, 15], 9))
# # # timed.timeit(1_000)
# # #
# # # foo = tuple(range(10_000))
# # # timeit.Timer(lambda: foo.index(9_000)).timeit(10_000)
# # # foo = list(foo)
# # # timeit.Timer(lambda: foo.index(9_000)).timeit(10_000)
# #
# #
# #
# #
# # # class DataGenerator(ABC):
# # #     """Data generator."""
# # #
# # #     def __init__(
# # #         self,
# # #         n: int,
# # #         func: t.Callable[P, T],
# # #         *args: P.args,
# # #         **kwargs: P.kwargs,
# # #     ) -> None:
# # #         super().__init__()
# # #
# # #     @abstractmethod
# # #     def __call__(self, *args: Any, **kwds: Any) -> T:
# # #         return super().__call__(*args, **kwds)
# #
# #
# #
# # # timed = timeit.Timer(lambda: two_sum_eafp([2, 7, 11, 15], 9))
# # # timed.timeit(1_000)
# # # timed = timeit.Timer(gen_two_sum_eafp([2, 7, 11, 15], 9))
# # # timed.timeit(1_000)
# # # timed = timeit.Timer(GenTwoSumEAFP([2, 7, 11, 15], 9))
# # # timed.timeit(1_000)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # x = np.array([1, 7, 20, 50, 79])
# # # y = np.array([10, 19, 30, 35, 51])
# # #
# # # # param, param_cov = scipy.optimize.curve_fit(_logarithmic, x, y, full_output=True)
# # #
# # #
# # # x = np.array([1, 2, 3, 4, 5])
# # # y = np.array([2, 4, 6, 8, 10])
# # #
# # # func = _constant
# # # func = _linear
# # # func = _logarithmic
# # #
# # # popt, pcov = scipy.optimize.curve_fit(func, x, y, nan_policy="omit")
# # #
# # # perr = np.sqrt(np.diag(pcov))
# # # print(perr)
# # # for e in perr:
# # #     print(f"{e:.2G}")
# # #
# # # print(sum(perr))
# # #
# # #
# # # plt.plot(x, y, color="red")
# # # plt.plot(x, func(x, *popt), color="blue")
# # #
# # # plt.show()
# # #
# # #
