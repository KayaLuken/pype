from functools import wraps

from api import _


def curried_function(arg_count, original_name):
    def arity_1(x):pass
    def arity_2(x, y):pass
    def arity_3(x, y, z):pass
    def arity_4(x, y, z, v):pass
    def arity_5(x, y, z, v, w):pass

    m = {1: arity_1, 2: arity_2, 3: arity_3, 4: arity_4, 5: arity_5}
    cf = m[arg_count]
    cf.__name__ = original_name
    return cf



def curry_(f, total_args=None, name=''):
    if total_args is None:
        argc = f.__code__.co_argcount
        total_args = [_ for i in range(argc)]

    available_indices = [i for (i, arg) in enumerate(total_args) if arg is _]

    name = name or f.__name__
    w = curried_function(len(available_indices), name)

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
        return curry(q, new_total_args, name)

    return p



def curry(f):
    def inner(*args):
        return Curry.make(f, *args)
    return inner



class Curry:

    def __init__(self, f, *args):
        self.f = f
        argc = f.__code__.co_argcount
        self.total_args = [_ for i in range(argc)]

        self.fill_total_args(*args)

    @classmethod
    def make(cls, f, *args):
        instance = cls(f, *args)
        return instance.fire() if instance.ready else instance

    def __str__(self):
       return f"{self.f.__name__} "

    def fire(self):
        return self.f(*self.total_args)

    def fill_total_args(self, *args):
        available_indices = self.available_indices
        for (i, arg) in enumerate(args):
            next_index = available_indices[i]
            self.total_args[next_index] = arg

    @property
    def ready(self):
        return all(map(lambda x: x is not _, self.total_args))

    @property
    def available_indices(self):
        return [i for (i, arg) in enumerate(self.total_args) if arg is _]

    def __call__(self, *args):
        previous_total_args = self.total_args.copy()
        self.fill_total_args(*args)
        if self.ready:
            res = self.fire()
            self.total_args = previous_total_args
            return res
        else:
            return self
