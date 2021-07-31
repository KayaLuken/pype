from utils.decorators import curry


@curry
def index(i, xs):
    return xs[i]
