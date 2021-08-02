from projectEuler._1_multiplesOf3and5 import multiples_of_3_and_5
from projectEuler._2_sum_even_fibonacci import sum_even_fibonacci
from projectEuler._3_prime_factors import factors, is_prime, primes_naive, next_prime, primes_sieve_of_erosthenes, \
    primes_imperative


def test_1():
    assert multiples_of_3_and_5(10) == 23

def test_2():
    assert sum_even_fibonacci(10) == 44

def test_3():
    assert factors(9) == [1, 3, 9]
    assert is_prime(7) == True
    assert is_prime(6) == False
    assert primes_naive(15) == [2, 3, 5, 7, 11, 13]
    assert next_prime([[2, 3, 4, 5], []]) == [[3, 5], [2]]
    assert primes_sieve_of_erosthenes(15) == [2, 3, 5, 7, 11, 13]
    assert primes_imperative(15) == [2, 3, 5, 7, 11, 13]
