from utils.decorators import curry


@curry
def tap(f, x):
    f()
    return x
