from typing import Callable

from utils.checkers import check_is_function
from utils.decorators import enhance
from utils.inspectors import arity


@enhance
def com(f: Callable, g: Callable) -> Callable:
    check_is_function(f)
    check_is_function(g)

    def h(x):
        return g(f(x))

    @enhance
    def k(x, y):
        return g(f(x, y))

    @enhance
    def l(x, y, z):
        return g(f(x, y, z))

    m = {1: h, 2: k, 3: l}

    return m[arity(f)]
