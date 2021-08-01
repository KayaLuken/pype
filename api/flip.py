from utils.decorators import enhance


@enhance
def flip(f):
    def _f(x, y):
        return f(y, x)
    return _f
