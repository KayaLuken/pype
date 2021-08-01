from utils.decorators import enhance


@enhance
def index(i, xs):
    return xs[i]
