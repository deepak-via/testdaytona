#!/usr/bin/env python3
"""
Unit tests for the Calculator class.
"""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(10, 20), 30)

    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)

    def test_add_floats(self):
        """Test addition of floating point numbers."""
        self.assertAlmostEqual(self.calc.add(1.5, 2.3), 3.8)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)

    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 15), 5)

    def test_subtract_negative_numbers(self):
        """Test subtraction of negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_subtract_floats(self):
        """Test subtraction of floating point numbers."""
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.3), 3.2)

    def test_subtract_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(10, 4), 40)

    def test_multiply_negative_numbers(self):
        """Test multiplication of negative numbers."""
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        self.assertEqual(self.calc.multiply(-5, 3), -15)

    def test_multiply_floats(self):
        """Test multiplication of floating point numbers."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_multiply_by_one(self):
        """Test multiplication by one."""
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(1, 5), 5)

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(20, 4), 5)

    def test_divide_negative_numbers(self):
        """Test division of negative numbers."""
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_divide_floats(self):
        """Test division of floating point numbers."""
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_divide_zero_by_number(self):
        """Test zero divided by a number."""
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_divide_by_one(self):
        """Test division by one."""
        self.assertEqual(self.calc.divide(5, 1), 5)


class TestCalculatorEdgeCases(unittest.TestCase):
    """Test edge cases for the Calculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_large_numbers(self):
        """Test operations with large numbers."""
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)

    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        self.assertAlmostEqual(self.calc.add(0.0001, 0.0002), 0.0003)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.1), 0.01)

    def test_mixed_types(self):
        """Test operations with mixed int and float types."""
        self.assertEqual(self.calc.add(5, 2.5), 7.5)
        self.assertEqual(self.calc.multiply(3, 2.5), 7.5)


if __name__ == "__main__":
    unittest.main()
