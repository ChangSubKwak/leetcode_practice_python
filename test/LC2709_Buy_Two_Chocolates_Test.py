import unittest

from main.LC2706_Buy_Two_Chocolates import LC2706_Buy_Two_Chocolates

test = LC2706_Buy_Two_Chocolates()


class LC2709_Buy_Two_Chocolates_Test(unittest.TestCase):
    def test_onesMinusZeros(self):
        self.assertEqual(test.buyChoco([1, 2, 2], 3), 0)
        self.assertEqual(test.buyChoco([3, 2, 3], 3), 3)
        self.assertEqual(test.buyChoco([74, 31, 38, 24, 25, 24, 5], 79), 50)
