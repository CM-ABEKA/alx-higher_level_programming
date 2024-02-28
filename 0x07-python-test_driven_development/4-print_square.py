#!/usr/bin/python3
'''
    module prints square with character #
'''


def print_square(size):
    '''
        prints square of dimension equal to size
        using character #
        Args:
        @size: size of the square side

        Raises:
        ===> size not int
        TypeError: size must be an integer
        ===> size less than 0
        ValueError: size must be >= 0
        ===> size is float and less than 0
        TypeError: size must be an integer

    '''
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    [print('#' * size) for l in range(size)]
