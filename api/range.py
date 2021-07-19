from typing import List

from utils.checkers import check_is_int
from utils.decorators import curry


@curry
def range_(x: int, y: int) -> List[int]:
    check_is_int(x)
    check_is_int(y)

    # extend range to count downwards also
    xs = range(x, y) if x < y else reversed(range(y, x))
    return list(xs)
