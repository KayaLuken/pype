from utils.checkers import check_is_list
from utils.decorators import enhance


@enhance
def len_(xs) -> int:
    check_is_list(xs)

    return len(xs)
