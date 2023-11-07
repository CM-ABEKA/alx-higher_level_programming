#!/usr/bin/python3
""" OOP classes """


class Square:
    """The Square object """

    def __init__(self, size=0):
        """
        __init__
        instantiates the size attribute

        Fields:
        size (int): size of square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
