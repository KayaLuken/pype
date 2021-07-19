from functools import wraps

def curry(f, argc=None):
    if argc is None:
        argc = f.__code__.co_argcount

    def g(x):pass
    def h(x, y):pass
    def i(x, y, z):pass
    def j(x, y, z, v):pass
    def k(x, y, z, v, w):pass

    m = {1: g, 2: h, 3: i, 4: j, 5: k}
    w = m[argc]

    # for getting correct arg count of curried function
    @wraps(w)
    def p(*a):
        if len(a) == argc:
            return f(*a)

        def q(*b):
            return f(*(a + b))

        return curry(q, argc - len(a))

    return p