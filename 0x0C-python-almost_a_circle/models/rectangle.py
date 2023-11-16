#!/usr/bin/python3
"""Rectangle module with getters, setters, and methods"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class for representing rectangles"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        self.validate_positive_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        self.validate_positive_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle"""
        self.validate_non_negative_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle"""
        self.validate_non_negative_integer("y", value)
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Display the rectangle using '#' characters"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle"""
        if args:
            self.update_with_args(args)
        elif kwargs:
            self.update_with_kwargs(kwargs)

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def validate_positive_integer(self, name, value):
        """Validate that the value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be a positive integer")

    def validate_non_negative_integer(self, name, value):
        """Validate that the value is a non-negative integer"""
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} must be a non-negative integer")

    def update_with_args(self, args):
        """Update attributes using positional arguments"""
        attr_names = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            setattr(self, attr_names[i], arg)

    def update_with_kwargs(self, kwargs):
        """Update attributes using keyword arguments"""
        for key, value in kwargs.items():
            setattr(self, key, value)
