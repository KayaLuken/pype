from utils.decorators import curry


@curry
def last(xs):
    return xs[-1]
