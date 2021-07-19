from api import pipe, sub, rang, filt, is_mult, either

is_mult3and5 = either(is_mult(3), is_mult(5))

multiples_of_3_and_5 = pipe([
    rang(0),
    filt(is_mult3and5),
    sum
])
