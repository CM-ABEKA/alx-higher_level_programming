"""Module square for the module that holds the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square object.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The id of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self) -> int:
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value: int):
        """Sets the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square's attributes."""
        if args:
            for arg in args:
                if arg is None:
                    self.__init__(self.size, self.x, self.y)
                elif isinstance(arg, int):
                    if arg == self.id:
                        self.id = arg
                    elif arg == self.size:
                        self.size = arg
                    elif arg == self.x:
                        self.x = arg
                    elif arg == self.y:
                        self.y = arg
                    else:
                        raise ValueError(f"Invalid argument: {arg}")

        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key in {"size", "width", "height"}:
                    self.size = value
                elif key in {"x", "y"}:
                    setattr(self, key, value)
                else:
                    raise ValueError(f"Invalid keyword argument: {key}")

    def to_dictionary(self) -> dict:
        """Returns a dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self) -> str:
        """Returns the string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
