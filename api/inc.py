from utils.checkers import check_is_int
from utils.decorators import enhance


@enhance
def inc(x):
    check_is_int(x)
    return x + 1