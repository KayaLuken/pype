from api import is_factor, range_, apply, filter_, com2, also, inc, bi

factors = com2(
    also(inc),
    bi(
        [is_factor, range_(1)])
    ,
    apply(filter_)
)
