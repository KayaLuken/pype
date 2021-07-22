from utils.checkers import check_is_function
from utils.decorators import curry


@curry
def also(f, x):
    check_is_function(f)
    return [x, f(x)]
