from utils.decorators import curry



@curry
def eq(x, y):
    return x == y
