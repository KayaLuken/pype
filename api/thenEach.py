from utils.decorators import enhance


@enhance
def thenEach(g, fs, xs):
    t = g(xs)
    return [f(t, xs[i]) for (i, f) in enumerate(fs)]
