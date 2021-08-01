from utils.decorators import enhance


@enhance
def last(xs):
    return xs[-1]
