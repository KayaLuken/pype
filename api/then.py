from utils.checkers import check_is_function
from utils.decorators import enhance



@enhance
def then(f, g, x):
    check_is_function(f)
    check_is_function(g)

    y = f(x)
    return g(y, x)
