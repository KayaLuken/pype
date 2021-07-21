from utils.checkers import check_is_int


def inc(x):
    check_is_int(x)
    return x + 1