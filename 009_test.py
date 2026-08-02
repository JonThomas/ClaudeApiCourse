import unittest
import math
import importlib

_main = importlib.import_module("009_main")
calculate_pi_to_5th_digit = _main.calculate_pi_to_5th_digit


class TestPiCalculation(unittest.TestCase):
    """Test cases for the pi calculation function."""
    
    def test_pi_value(self):
        """Test that calculated pi matches expected value to 5 decimal places."""
        calculated_pi = calculate_pi_to_5th_digit()
        expected_pi = 3.14159
        self.assertEqual(calculated_pi, expected_pi)
    
    def test_pi_precision(self):
        """Test that calculated pi is close to math.pi within acceptable tolerance."""
        calculated_pi = calculate_pi_to_5th_digit()
        # Should be within 0.000005 (half of the 5th decimal place)
        self.assertAlmostEqual(calculated_pi, math.pi, places=5)
    
    def test_return_type(self):
        """Test that the function returns a float."""
        result = calculate_pi_to_5th_digit()
        self.assertIsInstance(result, float)
    
    def test_pi_range(self):
        """Test that pi is within the expected range."""
        calculated_pi = calculate_pi_to_5th_digit()
        self.assertGreater(calculated_pi, 3.14158)
        self.assertLess(calculated_pi, 3.14160)
    
    def test_pi_string_representation(self):
        """Test the string representation of pi to verify 5 digits."""
        calculated_pi = calculate_pi_to_5th_digit()
        pi_str = str(calculated_pi)
        # Should be "3.14159"
        self.assertEqual(pi_str, "3.14159")


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)
