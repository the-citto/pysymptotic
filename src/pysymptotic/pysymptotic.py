"""Fitter."""

import typing

from . import complexity


# complexity.Constant,
# complexity.Cubic,
# complexity.Exponential,
# complexity.Factorial,
# complexity.Linear,
# complexity.Linearithmic,
# complexity.Logarithmic,
# complexity.Quadratic,

class TimeitData:
    """Tiemit data."""

    def __new__(cls) -> typing.Self:
        """Set new."""
        return cls

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



