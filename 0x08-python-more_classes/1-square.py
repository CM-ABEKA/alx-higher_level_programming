#!/usr/bin/python3
"""A square object"""


class Square:
    """This is a square object. Initialised with size"""
    def __init__(self, size):
        """
        The __init Method initializes the class

        Fields:
        size (int): size of square
        """
        self.__size = size
