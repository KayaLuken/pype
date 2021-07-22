from utils.checkers import check_is_list, check_is_function
from utils.decorators import curry


@curry
def apply(f, xs):
    check_is_function(f)
    check_is_list(xs)

    return f(*xs)
