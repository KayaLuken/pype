from utils.checkers import check_is_int
from utils.decorators import enhance



@enhance
def lt(x, y) -> bool:
    check_is_int(x)
    check_is_int(y)

    return x > y
