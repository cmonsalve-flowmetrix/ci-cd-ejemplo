# test_calculator.py
import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 2), 5)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)

if __name__ == '__main__':
    unittest.main()
