from inspect import signature


def arity(f):
    return len(signature(f).parameters)
