from functools import wraps
from api import _


def curried_function(arg_count):
    def arity_1(x):pass
    def arity_2(x, y):pass
    def arity_3(x, y, z):pass
    def arity_4(x, y, z, v):pass
    def arity_5(x, y, z, v, w):pass

    m = {1: arity_1, 2: arity_2, 3: arity_3, 4: arity_4, 5: arity_5}
    return m[arg_count]



def curry(f, total_args=None):
    if total_args is None:
        argc = f.__code__.co_argcount
        total_args = [_ for i in range(argc)]

    available_indices = [i for (i, arg) in enumerate(total_args) if arg is _]
    w = curried_function(len(available_indices))

    # for getting correct arg count of curried function
    @wraps(w)
    def p(*partial_args):
        new_total_args = total_args.copy()
        for (i, arg) in enumerate(partial_args):
            next_index = available_indices[i]
            new_total_args[next_index] = arg
        total_args_full = not list(filter(lambda x: x is _, new_total_args))

        if total_args_full:
            return f(*new_total_args)

        def q(*b):
            return f(*b)

        return curry(q, new_total_args)

    return p