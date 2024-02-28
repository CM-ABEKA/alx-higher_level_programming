#!/usr/bin/python3


"""
Defines an integer addition function.
Prototype: def add_integer(a, b=98)
Returns the sum of the integers a + b
"""


def add_integer(a, b=98):
    ''' Raises type error if a or b is not int or float
        Floats are casted into integers
    '''

    if type(a) not in [float, int]:
        raise TypeError('a must be an integer')
    if type(b) not in [float, int]:
        raise TypeError('b must be an integer')

    return (int(a) + int(b))
