"""
Sample Tests
"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""
    
    def test_add_numbers(self):
        res = calc.add(5,6)
        self.assertEqual(res, 11)
    
    def test_subtract_numbers(self):
        self.assertEqual(calc.subtract(10,5), 5)