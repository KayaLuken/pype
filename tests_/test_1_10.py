from projectEuler._1_multiplesOf3and5 import multiples_of_3_and_5
from projectEuler._2_sum_even_fibonacci import sum_even_fibonacci
from projectEuler._3_prime_factors import factors
from utils.decorators import curry

@curry
def add(x,y):
    return x + y

def test_1():
    assert multiples_of_3_and_5(10) == 23

def test_2():
    assert sum_even_fibonacci(10) == 44

def test_3():
    assert factors(9) == [1, 3, 9]
