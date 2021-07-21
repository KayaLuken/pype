from utils.checkers import check_is_int

def is_even(x: int) -> bool:
    check_is_int(x)
    return x % 2 == 0
