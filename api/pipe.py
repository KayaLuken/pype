from typing import List, Callable

from utils.checkers import check_is_list_of_functions
from utils.decorators import enhance
from utils.inspectors import arity


@enhance
def pipe(fs: List[Callable]):
    check_is_list_of_functions(fs)

    def _f(*x):
        x0 = fs[0](*x)
        acc = x0
        for f in fs[1:]:
            acc = f(acc)
        return acc

    def f1(x): return _f(x)

    def f2(x, y): return _f(x, y)

    def f3(x, y, z): return _f(x, y, z)

    def f4(x, y, z, v): return _f(x, y, z, v)

    def f5(x, y, z, v, w): return _f(x, y, z, v, w)

    m = {1: f1, 2: f2, 3: f3, 4: f4, 5: f5}
    a = arity(fs[0])

    return m[a]
