
from utils.decorators import curry


@curry
def map_(f, xs):
    return [f(x) for x in xs]
