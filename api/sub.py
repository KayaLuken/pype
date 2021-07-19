from utils.checkers import check_is_number


def sub(x: int) -> int:
    check_is_number(x)
    return x - 1
