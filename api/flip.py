from utils.decorators import curry


@curry
def flip(f):
    def _f(x, y):
        return f(y, x)
    return _f
