from typing import Union

from utils.checkers import check_is_number
from utils.decorators import enhance

Number = Union[int, float, complex]

@enhance
def mod(x: Number, y: Number) -> Number:
    check_is_number(x)
    check_is_number(y)

    return x % y
