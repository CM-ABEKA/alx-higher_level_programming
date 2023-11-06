#!/usr/bin/python3
import unittest
max_integer = __import__("6-max_integer").max_integer
'''
unit tests for function max_integer(list=[])
'''


class TestMaxInteger(unittest.TestCase):
    '''Define unittests for max_integer function'''

    def test_max_integer(self):
        '''Test Max Integer in a list'''
        self.assertEqual(max_integer([1, 2, 4, 5]), 5)
        self.assertIsNone(max_integer([]))
        self.assertAlmostEqual(max_integer([-4, -2, 0]), 0)
        self.assertAlmostEqual(max_integer([1.0, 1.6, 5.5, 3.4]), 5.5)
        self.assertAlmostEqual(max_integer([8.9]), 8.9)
        self.assertIsNone(max_integer(""))
        self.assertEqual(max_integer("james"), "s")
    
    def test_types(self):
        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(['M', 3, 4])

if __name__ == '__main__':
    unittest.main()
