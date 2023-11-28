import unittest
from main import calculator

c = calculator.Calculator()


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(c.add(1, 2), 3)

    def test_substract(self):
        self.assertEqual(c.substract(1, 2), -1)

    def test_multiply(self):
        self.assertEqual(c.multiply(1, 2), 2)

    def test_divide(self):
        self.assertEqual(c.divide(4, 2), 2)
