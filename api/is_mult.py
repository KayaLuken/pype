from utils.checkers import check_is_int
from utils.decorators import enhance



@enhance
def is_mult(x: int, y: int) -> bool:
    check_is_int(x)
    check_is_int(y)
    return y % x == 0
