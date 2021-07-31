from utils.decorators import curry


@curry
def fst(xs):
    return xs[0]
