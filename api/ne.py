from utils.decorators import curry



@curry
def ne(x, y):
    return x != y
