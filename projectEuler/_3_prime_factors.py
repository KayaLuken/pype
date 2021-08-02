from api import is_factor, reject, fst, range_, apply, filter_, also, inc, each, len_, lt, \
    compress, thenEach, append, is_mult, until, peek, eq, snd

factors = also(inc) | each( [is_factor, range_(1)]) | apply(filter_)

is_prime = factors | len_ | lt(3)

primes_naive = range_(2) | filter_(is_prime) | compress

next_prime = thenEach(peek | fst | peek | fst | peek, [lambda x, xs: reject(is_mult(x), xs), append] )

primes_sieve_of_erosthenes = lambda n: until(
    fst | eq([]),
    next_prime,
    [range_(2, n), []]
) | snd
