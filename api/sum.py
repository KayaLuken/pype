from typing import List

from utils.checkers import check_is_list_of_numbers
from utils.decorators import curry
from utils.types import Number


@curry
def sum_(xs: List[Number]) -> Number:
    check_is_list_of_numbers(xs)
    return sum(xs)
