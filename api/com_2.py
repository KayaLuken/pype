from utils.checkers import check_is_function
from utils.decorators import curry
from utils.inspectors import arity


@curry
def com2(f, g, h):
    check_is_function(f)
    check_is_function(g)
    check_is_function(h)

    def _h(x):
        return h(g(f(x)))

    @curry
    def _k(x, y):
        return h(g(f(x, y)))

    @curry
    def _l(x, y, z):
        return h(g(f(x, y, z)))

    m = {1: _h, 2: _k, 3: _l}

    return m[arity(f)]
