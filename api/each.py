from utils.checkers import check_is_list_of_functions
from utils.decorators import curry


@curry
def each(fs, x):
    check_is_list_of_functions(fs)
    return [f(x) for f in fs]
