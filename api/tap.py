from utils.decorators import enhance


@enhance
def tap(f, x):
    f()
    return x
