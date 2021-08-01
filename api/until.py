from utils.checkers import check_is_function
from utils.decorators import enhance


@enhance
def until(p, f, x):
    check_is_function(p)
    check_is_function(f)

    acc = x
    while not p(acc):
        acc = f(acc)

    return acc

