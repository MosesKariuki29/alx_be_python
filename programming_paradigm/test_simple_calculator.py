# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Unit tests for the SimpleCalculator class.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each test method runs."""
        self.calc = SimpleCalculator()

    # --- Test Cases for Add Method ---
    # This method satisfies the specific naming requirement ("test_addition")
    def test_addition(self):
        """Test addition with various combinations (positive, negative, zero, float)."""
        self.assertEqual(self.calc.add(2, 3), 5)        # Positive integers
        self.assertEqual(self.calc.add(-1, 1), 0)       # Mixed integers resulting in zero
        self.assertEqual(self.calc.add(10, -5), 5)      # Mixed integers
        self.assertEqual(self.calc.add(0, 7), 7)        # Addition with zero
        self.assertEqual(self.calc.add(2.5, 1.5), 4.0)   # Floating-point numbers

    def test_add_negative_numbers(self):
        """Test addition with two negative integers."""
        self.assertEqual(self.calc.add(-10, -5), -15)

    # --- Test Cases for Subtract Method ---
    def test_subtract_positive_numbers(self):
        """Test subtraction with two positive integers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_subtract_negative_numbers(self):
        """Test subtraction with two negative integers."""
        self.assertEqual(self.calc.subtract(-10, -5), -5)
        
    def test_subtract_with_zero(self):
        """Test subtraction where one operand is zero."""
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        
    # --- Test Cases for Multiply Method ---
    def test_multiply_positive_numbers(self):
        """Test multiplication with two positive integers."""
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        """Test multiplication where one operand is zero (edge case)."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, -10), 0)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative integers."""
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    # --- Test Cases for Divide Method ---
    def test_divide_positive_numbers(self):
        """Test division with two positive integers for a clean result."""
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        
    def test_divide_floating_point_result(self):
        """Test division that results in a float."""
        self.assertEqual(self.calc.divide(10, 4), 2.5)

    def test_divide_by_zero_returns_none(self):
        """Test division by zero, which should return None as per the class specification (edge case)."""
        self.assertIsNone(self.calc.divide(10, 0))
        
    def test_divide_negative_numbers(self):
        """Test division involving negative numbers."""
        self.assertEqual(self.calc.divide(-10, 5), -2.0)
        self.assertEqual(self.calc.divide(-10, -5), 2.0)

    def test_divide_zero_by_number(self):
        """Test division of zero by a non-zero number."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)

if __name__ == '__main__':
    unittest.main()