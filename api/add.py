from utils.checkers import check_is_number
from utils.decorators import enhance


@enhance
def add(x: int, y: int) -> int:
    check_is_number(x)
    check_is_number(y)

    return x + y
