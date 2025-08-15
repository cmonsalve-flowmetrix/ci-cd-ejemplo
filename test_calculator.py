# test_calculator.py
import unittest
from lambda_function import add, lambda_handler

class TestAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 2), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(1, 3), 15)


    def test_lambda_handler_add(self):
        event = {"operation": "add", "a": 10, "b": 15}
        response = lambda_handler(event, None)
        self.assertEqual(response["statusCode"], 200)
        self.assertIn("25", response["body"])

if __name__ == '__main__':
    unittest.main()
