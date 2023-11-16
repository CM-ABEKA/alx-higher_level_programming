#!/usr/bin/python3
"""Module square for the module that holds the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class sqr, for the class of square, has getters setters, 
    inherits from base>>rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """Update"""
        if args is not None and len(args) != 0:
            self._update_with_args(args)
        elif kwargs is not None and len(kwargs) != 0:
            self._update_with_kwargs(kwargs)

    def _update_with_args(self, args):
        """Update with positional arguments"""
        n_arg = len(args)
        if n_arg >= 1:
            self.id = args[0]
        if n_arg >= 2:
            self.size = args[1]
        if n_arg >= 3:
            self.x = args[2]
        if n_arg >= 4:
            self.y = args[3]

    def _update_with_kwargs(self, kwargs):
        """Update with keyword arguments"""
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]
        if "id" in kwargs:
            self.id = kwargs["id"]

    @property
    def size(self):
        """Size"""
        return self.width

    @size.setter
    def size(self, val):
        """Size"""
        self._validate_size(val)
        self.width = val
        self.height = val

    def _validate_size(self, val):
        """Validate size"""
        if type(val) is not int:
            raise TypeError('Width must be an integer')
        elif val <= 0:
            raise ValueError('Width must be > 0')

    def __str__(self):
        """String representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """To dictionary"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
