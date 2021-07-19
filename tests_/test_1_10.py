from projectEuler.multiplesOf3and5__1 import multiples_of_3_and_5
from utils.decorators import curry

@curry
def add(x,y):
    return x + y

def test_1():
    assert multiples_of_3_and_5(10) == 23
