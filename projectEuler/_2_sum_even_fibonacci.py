
from api import append, com, is_even, filter_, sum_, then, until, len_, takeLast, eq, enhance


@enhance
def fibonacci(n):
    return until(
        com(len_, eq(n)),
        then(
            com(takeLast(2), sum_),
            append
        ),
        [0, 1]
    )


sum_even_fibonacci = fibonacci | filter_(is_even) | sum_
