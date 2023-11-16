"""
Comprehensive unit tests for the `Rectangle` class 
in the `rectangle.py` module.
"""

import unittest
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def setUp(self):
        """Reset the class attribute `_nb_objects` before each test"""
        Base._Base__nb_objects = 0

    def test_attributes(self):
        """Test the assignment and retrieval of attributes"""
        rectangle = Rectangle(12, 3, 4, 5)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 12)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

    def test_update(self):
        """Test the update method"""
        rectangle = Rectangle(1, 1, 1, 1)

        rectangle.update(2)
        self.assertEqual(rectangle.id, 2)

        rectangle.update(id=3, width=2, height=2, x=2, y=2)
        self.assertEqual(rectangle.id, 3)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 2)

        rectangle.update(width=100)
        self.assertEqual(rectangle.width, 100)

    def test_validation(self):
        """Test the validation of attribute values"""
        rectangle = Rectangle(5, 5)

        self.assertEqual(str(rectangle), '[Rectangle] (1) 0/0 - 5/5')

        rectangle.width = 6
        self.assertEqual(str(rectangle), '[Rectangle] (1) 0/0 - 6/5')


        with self.assertRaises(ValueError):
            rectangle.width = -1

    def test_area(self):
        """Test the area method"""
        rectangle = Rectangle(5, 5)
        self.assertEqual(rectangle.area(), 25)


if __name__ == '__main__':
    unittest.main()
