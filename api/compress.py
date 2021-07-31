from utils.decorators import curry


@curry
def compress(xs):
    return [x for x in xs if xs != False]
