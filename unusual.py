# Partial function - allows one to derive a function with x parameters to a function with
# fewer parameters and fixed values set for the more limited function.

from functools import partial


def multiply(x, y):
    return x * y


# create a new function that multiplies by 2
dbl = partial(multiply, 5)
print(dbl(4))
