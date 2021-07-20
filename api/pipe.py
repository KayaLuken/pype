from typing import List, Callable

from utils.checkers import check_is_list_of_functions
from utils.decorators import curry

@curry
def pipe(fs: List[Callable], x):
    check_is_list_of_functions(fs)
    acc = x
    for f in fs:
        acc = f(acc)
    return acc
