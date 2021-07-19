from typing import Union


from utils.checkers import check_is_number
from utils.decorators import curry

Number = Union[int, float, complex]

@curry
def mod(x: Number, y: Number) -> Number:
    check_is_number(x)
    check_is_number(y)

    return x % y
