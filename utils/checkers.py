from numbers import Number



def check_is_function(x):
    if not callable(x):
        raise TypeError(f"Expected function but got {x}")


def check_is_list(x):
    if not isinstance(x, list):
        raise TypeError(f"Expected list but got {x}")


def check_is_list_of_functions(xs):
    check_is_list(xs)
    for x in xs:
        if not callable(x):
            raise TypeError(f"Expected list of functions but got {x} in list")


def check_is_number(x):
    if not isinstance(x, Number):
        raise TypeError(f"Expected number but got {x}")


def check_is_int(x):
    if not isinstance(x, int):
        raise TypeError(f"Expected integer but got {x}")


def check_is_bool(x):
    if not isinstance(x, bool):
        raise TypeError(f"Expected bool but got {x}")


def check_is_list_of_numbers(xs):
    check_is_list(xs)
    for x in xs:
        if not isinstance(x, Number):
            raise TypeError(f"Expected list of numbers but got {x} in list")
