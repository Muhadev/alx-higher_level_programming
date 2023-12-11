#!/usr/bin/python3
"""
classes and methods must be unit tested
and be PEP 8 validated.
"""
import unittest
from models.base import Base


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


if __name__ == '__main__':
    unittest.main()
