from utils.checkers import check_is_number
from utils.decorators import curry


@curry
def sub(x: int, y: int) -> int:
    check_is_number(x)
    check_is_number(y)

    return x - y
