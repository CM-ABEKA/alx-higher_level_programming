#!/usr/bin/python3


"""
Comprehensive unit tests for the `Base` class 
in the `base.py` module.

Unittest Classes:
    TestBaseInstantiation
    TestBaseToJsonString
    TestBaseSaveToFile
    TestBaseFromJsonString
    TestBaseCreate
    TestBaseLoadFromFile
"""
import os
import unittest
import json
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """Test cases for the Base class"""

    def setUp(self):
        """Reset the class attribute `_nb_objects` before each test"""
        Base._Base__nb_objects = 0

    def test_init(self):
        """Test the initialization of a Base instance"""
        new_base = Base()
        self.assertEqual(type(new_base), Base)

    def test_id(self):
        """Test the assignment and retrieval of object ids"""
        new_base1 = Base()
        self.assertEqual(new_base1.id, 1)

        new_base2 = Base(42)
        self.assertEqual(new_base2.id, 42)

    def test_to_json_string(self):
        """Test the conversion of a dictionary to a JSON string"""
        rectangle = Rectangle(9, 8, 3, 5)
        rectangle_dict = rectangle.to_dictionary()

        json_string = Base.to_json_string([rectangle_dict])
        self.assertEqual(type(rectangle_dict), dict)
        self.assertEqual(type(json_string), str)

        empty_json_string = Base.to_json_string([])
        self.assertEqual(empty_json_string, "[]")

    def test_save_to_file(self):
        """Test the saving of objects to a JSON file"""
        rectangle1 = Rectangle(9, 8, 3, 5)
        rectangle2 = Rectangle(7, 3)

        Rectangle.save_to_file([rectangle1, rectangle2])

        with open("Rectangle.json", "r") as file:
            saved_data = json.loads(file.read())

        expected_data = [rectangle1.to_dictionary(), rectangle2.to_dictionary()]
        self.assertEqual(expected_data, saved_data)

    def test_from_json_string(self):
        """Test the conversion of a JSON string to a list of dictionaries"""
        data = [
            {'id': 21, 'width': 12, 'height': 6},
            {'id': 12, 'width': 21, 'height': 11}
        ]

        json_string = Rectangle.to_json_string(data)
        parsed_data = Rectangle.from_json_string(json_string)

        self.assertEqual(type(data), list)
        self.assertEqual(type(json_string), str)
        self.assertEqual(type(parsed_data), list)
        self.assertEqual(data, parsed_data)

    def test_create(self):
        """Test the creation of a new object from a dictionary"""
        rectangle = Rectangle(9, 8, 3, 5)
        rectangle_dict = rectangle.to_dictionary()

        new_rectangle = Rectangle.create(**rectangle_dict)
        self.assertEqual(str(rectangle), str(new_rectangle))
        self.assertNotEqual(rectangle, new_rectangle)

    def test_load_from_file(self):
        """Test the loading of objects from a JSON file"""
        try:
            os.remove('Rectangle.json')
        except OSError:
            pass

        rectangle1 = Rectangle(9, 8, 3, 5)
        rectangle2 = Rectangle(10, 5)
        objects = [rectangle1, rectangle2]

        Rectangle.save_to_file(objects)

        loaded_objects = Rectangle.load_from_file()

        self.assertEqual(str(objects[0]), str(loaded_objects[0]))
        self.assertEqual(str(objects[1]), str(loaded_objects[1]))

if __name__ == '__main__':
    unittest.main()