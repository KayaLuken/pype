from utils.decorators import enhance


@enhance
def compress(xs):
    return [x for x in xs if xs != False]
