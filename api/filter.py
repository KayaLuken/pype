from typing import List, Callable

from utils.checkers import check_is_function, check_is_list, check_is_bool
from utils.decorators import curry


@curry
def filt(f: Callable, xs: List) -> List:
    check_is_function(f)
    check_is_list(xs)

    ys = []
    for x in xs:
        y = f(x)
        check_is_bool(y)
        if y:
            ys.append(x)
    return ys
