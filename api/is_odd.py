from utils.checkers import check_is_int


def is_odd(x: int) -> bool:
    check_is_int(x)
    return x % 1 == 0
