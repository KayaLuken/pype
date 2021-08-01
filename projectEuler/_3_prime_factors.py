from api import is_factor, range_, apply, filter_, com2, also, inc, bi, len_, lt, compress

factors = com2(

    also(inc),
    bi(
        [is_factor, range_(1)])
    ,
    apply(filter_)

)

is_prime = com2(

    factors,
    len_,
    lt(3)

)

primes_naive = com2(
    range_(1),
    filter_(is_prime),
    compress
)

# next_prime = com2(also(fst),also(apply(flip(filter_))),append, last)
# get 1st in left list and append to right list
# filter from left list


# primes_sieve_of_erosthenes = lambda n: until(
#     com(fst, ne([])),
#     next_prime,
#     [[range(2, n)], []]
# )(n)
