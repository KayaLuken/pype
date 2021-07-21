from utils.checkers import check_is_list


def len_(xs) -> int:
    check_is_list(xs)

    return len(xs)
