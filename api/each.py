from utils.checkers import check_is_list_of_functions, check_equal_list_lengths
from utils.decorators import enhance


@enhance
def each(fs, xs):
    check_is_list_of_functions(fs)
    check_equal_list_lengths(fs, xs)

    ys = []
    for (i, x) in enumerate(xs):
        y = fs[i](x)
        ys.append(y)
    return ys
