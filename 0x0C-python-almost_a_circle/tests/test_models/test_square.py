#!/usr/bin/python3
"""
classes and methods must be unit tested
and be PEP 8 validated.
"""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Square is a special Rectangle"""
    def test_square_creation(self):
        """Create a square with initial attributes"""
        square = Square(5, 2, 3, 10)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_str_representation(self):
        """Create a square"""
        square = Square(5, 2, 3, 10)
        string_repr = str(square)
        self.assertEqual(string_repr, "[Square] (10) 2/3 - 5")


if __name__ == '__main__':
    unittest.main()
