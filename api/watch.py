from utils.checkers import check_is_function
from utils.decorators import enhance


@enhance
def watch(f):
    check_is_function(f)

    def g(*x):
        y = f(*x)
        print(f"WATCHED: {f.__name__}  {x} ===> {y}")
        return f(*x)

    return g
