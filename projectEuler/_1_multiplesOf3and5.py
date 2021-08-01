from api import range_, filter_, is_mult, either, sum_

is_mult3and5 = either(is_mult(3), is_mult(5))


multiples_of_3_and_5 = range_(0) | filter_(is_mult3and5) | sum_
