from utils.decorators import enhance


@enhance
def path(xs, yss):
    y = yss
    for i in xs:
        y = y[i]
    return y
