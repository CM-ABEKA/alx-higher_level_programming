#!/usr/bin/python3
"""
    Creates a Rectangle Class
"""


class Rectangle:
    """ Heading: Rectangle
        Body: 
            Properties: 
            _width: private property: integer > 0
            _height: pribate property: integer > 0

    """
    

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle"""
        self.width = width
        self.height = height

        @property
        def width(self):
            """Getter for rectangle width"""
            return self.__width

        @width.setter
        def width(self, value):
            """Setter for width"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Getter for rectangle height"""
            return self.__height

        @height.setter
        def height(self, value):
            """Setter for height"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
