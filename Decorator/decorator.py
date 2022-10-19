from typing import Callable, Any, Optional


class FunctionCounterDecorator():
    """Class decorator to count the num of function calls"""
    def __init__(self, func: Callable[..., Optional[Any]]):
        self._func = func
        self._counter = 0

    @property
    def counter(self):
        return self._counter

    def __call__(self, *args, **kwargs):
        self._counter += 1
        return self._func(*args, **kwargs)