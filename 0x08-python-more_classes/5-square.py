#!/usr/bin/python3
''' OOP Classes'''


class Square:
    '''This is a Square object'''
    def __init__(self, size=0):
        '''
        __init__
        instantiates size in the square

        Fields:
        size (int): integer of the square size

        Raises:
        ValueError: size less than 0
        TypeError: size not integer

        '''
        self.size = size

    def area(self):
        '''
        area(): returns the area of the square

        '''

        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print('#' * self.__size)
