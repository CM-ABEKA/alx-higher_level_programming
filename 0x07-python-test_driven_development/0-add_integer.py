''' Addition Function '''


def add_integer(a, b=98):
    '''
        adds two integers
        Arguments:
        @a: integer or float
        @b: integer or float
        both arguments are to be casted into integers
    '''

    if type(a) not in [float, int]:
        raise TypeError('a must be an integer')
    if type(b) not in [float, int]:
        raise TypeError('b must be an integer')
    if (a + 1) == a or (b + 1) == b:
        raise OverflowError('cannot convert float infinity to integer')
    return int(a) + int(b)
