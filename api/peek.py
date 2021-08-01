from utils.decorators import enhance


@enhance
def peek(x):
    print(f"PEEKED: ===> {x} <===")
    return x
