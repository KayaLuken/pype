from utils.checkers import check_is_list
from utils.decorators import enhance



@enhance
def append(x, xs):
    check_is_list(xs)

    ys = xs.copy()
    ys.append(x)
    return ys
