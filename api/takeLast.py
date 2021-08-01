from utils.checkers import check_is_list
from utils.decorators import enhance


@enhance
def takeLast(x, xs):
    check_is_list(xs)
    if x > len(xs):
        raise ValueError(f"{x} greater than length of list {len(xs)}")

    ys = xs[-x:]
    return ys
