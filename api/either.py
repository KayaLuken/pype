from typing import Callable

from utils.checkers import check_is_function, check_is_bool
from utils.decorators import curry


@curry
def either(f: Callable, g: Callable, x) -> bool:
    check_is_function(f)
    check_is_function(g)

    y, z = f(x), g(x)
    check_is_bool(y)
    check_is_bool(z)

    return y or z
