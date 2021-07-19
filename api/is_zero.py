from utils.checkers import check_is_int
from utils.decorators import curry



@curry
def is_zero(x: int) -> bool:
    check_is_int(x)
    return x == 0