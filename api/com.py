from typing import Callable

from utils.checkers import check_is_function
from utils.decorators import curry


@curry
def com(f: Callable, g: Callable) -> Callable:
    check_is_function(f)
    check_is_function(g)

    @curry
    def h(f, g, x):
        return f(g(x))
    return h
