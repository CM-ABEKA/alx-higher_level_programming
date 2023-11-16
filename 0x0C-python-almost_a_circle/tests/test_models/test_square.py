"""
Comprehensive unit tests for the `Square` class 
in the `square.py` module.
"""

import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):

    def setUp(self):
        """Reset the class attribute `_nb_objects` before each test"""
        Base._Base__nb_objects = 0

    def test_str_representation(self):
        """Test the string representation of a Square object"""
        square = Square(12, 3, 4, 5)
        expected_str = '[Square] (5) 3/4 - 12'
        self.assertEqual(str(square), expected_str)

    def test_validation_positive_size(self):
        """Test that the size attribute must be a positive integer"""
        square = Square(5)
        self.assertEqual(square.size, 5)

        square.size = 6
        self.assertEqual(square.size, 6)

        with self.assertRaises(ValueError):
            square.size = -1

    def test_validation_invalid_size_type(self):
        """Test that the size attribute must be an integer"""
        square = Square(5)
        self.assertEqual(square.size, 5)

        with self.assertRaises(TypeError):
            square.size = "6"

    def test_to_dictionary(self):
        """Test the conversion of a Square object to a dictionary"""
        square = Square(12, 3, 4)
        square_dict = square.to_dictionary()

        expected_dict = {'id': 1, 'size': 12, 'x': 3, 'y': 4}
        self.assertEqual(square_dict, expected_dict)
        self.assertEqual(type(square_dict), dict)

    def test_update_with_id(self):
        """Test the update method with an ID argument"""
        square = Square(1, 1, 1)
        square.update(id=2)
        self.assertEqual(square.id, 2)

    def test_update_with_all_attributes(self):
        """Test the update method with all attributes"""
        square = Square(1, 1, 1)
        square.update(id=3, size=2, x=2, y=2)
        self.assertEqual(square.id, 3)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 2)

    def test_update_with_size_only(self):
        """Test the update method with just the size attribute"""
        square = Square(1, 1, 1)
        square.update(size=100)
        self.assertEqual(square.size, 100)

if __name__ == '__main__':
    unittest.main()
