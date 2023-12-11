"""
classes and methods must be unit tested
and be PEP 8 validated.
"""
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Create an instance of Calculator for each test"""
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(3, 5), 8)
        self.assertEqual(self.calculator.add(-2, 2), 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)
        self.assertEqual(self.calculator.subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 4), 12)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(8, 4), 2)

        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)


if __name__ == '__main__':
    unittest.main()
