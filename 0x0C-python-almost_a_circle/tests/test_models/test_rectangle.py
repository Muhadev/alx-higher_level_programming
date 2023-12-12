#!/usr/bin/python3
"""
classes and methods must be unit tested
and be PEP 8 validated.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test object creation and attribute assignment"""
    def test_initialization(self):
        """Test if the ID is assigned when an ID is provided"""
        rect = Rectangle(10, 20, 3, 5, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 5)
        self.assertEqual(rect.id, 1)

    def test_attribute_setters(self):
        """Test if the ID increments when no ID is provided"""
        rect = Rectangle(10, 20)
        rect.width = 15
        rect.height = 25
        rect.x = 5
        rect.y = 10
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 10)


if __name__ == '__main__':
    unittest.main()
