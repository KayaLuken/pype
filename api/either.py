from typing import Callable

from utils.checkers import check_is_bool, check_is_1_arity_function
from utils.decorators import enhance


@enhance
def either(f: Callable, g: Callable, x) -> bool:
    check_is_1_arity_function(f)
    check_is_1_arity_function(g)

    y, z = f(x), g(x)
    check_is_bool(y)
    check_is_bool(z)

    return y or z
