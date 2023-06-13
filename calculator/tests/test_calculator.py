import unittest
from dovydas_calculator import add, subtract, multiply, divide, nth_root


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 0), "Error: Division by zero")

    def test_nth_root(self):
        self.assertEqual(nth_root(8, 3), 2)
        self.assertEqual(nth_root(16, 4), 2)
        self.assertEqual(nth_root(27, 3), 3)


if __name__ == "__main__":
    unittest.main()
