
from utils.decorators import enhance


@enhance
def map_(f, xs):
    return [f(x) for x in xs]
