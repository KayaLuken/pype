from typing import List, Callable

from utils.checkers import check_is_list, check_is_bool, check_is_1_arity_function
from utils.decorators import enhance


@enhance
def filter_(p: Callable, xs: List) -> List:
    check_is_1_arity_function(p)
    check_is_list(xs)

    ys = []
    for x in xs:
        y = p(x)
        check_is_bool(y)
        if y:
            ys.append(x)
    return ys
