from typing import Callable

from utils.checkers import check_is_function, check_is_1_arity_function
from utils.decorators import curry
from utils.inspectors import arity


@curry
def com(f: Callable, g: Callable) -> Callable:
    check_is_function(f)
    check_is_1_arity_function(g)

    def h(x):
        return g(f(x))

    @curry
    def k(x, y):
        return g(f(x, y))

    @curry
    def l(x, y, z):
        return g(f(x, y, z))

    m = {1: h, 2: k, 3: l}

    return m[arity(f)]
