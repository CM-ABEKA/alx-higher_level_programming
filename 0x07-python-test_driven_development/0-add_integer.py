#!/usr/bin/python3
"""Defines an integer addition function.
    >>> print(add_integer(100.3, -2))
    98
    >>> print(add_integer(4, "School"))
    b must be an integer """

def add_integer(a, b=98):
    ''' Returns integer addition a + b
        Raises type error if a or b is not int or float
        Floats are casted into integers '''

    if type(a) not in [float, int]:
        raise TypeError('a must be an integer')
    if type(b) not in [float, int]:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
