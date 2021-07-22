from api import pipe, range_, filter_, is_mult, either

is_mult3and5 = either(is_mult(3), is_mult(5))


multiples_of_3_and_5 = pipe([
    range_(0),
    filter_(is_mult3and5),
    sum
])
