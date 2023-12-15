#!/usr/bin/python3
"""
classes and methods must be unit tested
and be PEP 8 validated.
"""
import unittest
from models.base import Base
import os
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def setUp(self):
        """Reset __nb_objects to 0 before each test"""
        Base._Base__nb_objects = 0

    def test_id_assignment_with_id_argument(self):
        """Test if the ID is assigned when an ID is provided"""
        base_instance = Base(100)
        self.assertEqual(base_instance.id, 100)

    def test_id_assignment_without_id_argument(self):
        """Test if the ID increments when no ID is provided"""
        base_instance1 = Base()
        base_instance2 = Base()
        self.assertEqual(base_instance1.id, 1)
        self.assertEqual(base_instance2.id, 2)

    def test_id_assignment_multiple_instances(self):
        """Test if IDs are unique for multiple instances"""
        base_instance1 = Base()
        base_instance2 = Base()
        base_instance3 = Base()
        self.assertNotEqual(base_instance1.id, base_instance2.id)
        self.assertNotEqual(base_instance2.id, base_instance3.id)
        self.assertNotEqual(base_instance1.id, base_instance3.id)

    def test_to_json_string_empty_list(self):
        """Test if IDs are unique for multiple instances"""
        empty_list = []
        result = Base.to_json_string(empty_list)
        self.assertEqual(result, [])

    def test_to_json_string_none(self):
        """Test if IDs are unique for multiple instances"""
        result = Base.to_json_string(None)
        self.assertEqual(result, [])

    def test_to_json_string_list_of_dicts(self):
        """Test if IDs are unique for multiple instances"""
        list_dicts = [
                {'id': 1, 'name': 'Alice'},
                {'id': 2, 'name': 'Bob'},
                ]
        expect_json = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        result = Base.to_json_string(list_dicts)
        self.assertEqual(result, expect_json)

    def test_save_to_file(self):
        """Test if IDs are unique for multiple instances"""
        rect1 = Rectangle(4, 5)
        rect2 = Rectangle(3, 7)
        Rectangle.save_to_file([rect1, rect2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        square = Square(6)
        Square.save_to_file([square])
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Rectangle.json")
        os.remove("Square.json")


if __name__ == '__main__':
    unittest.main()
