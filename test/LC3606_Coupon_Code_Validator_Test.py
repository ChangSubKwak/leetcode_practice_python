import unittest
from main.LC3606_Coupon_Code_Validator import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.validateCoupons(
            ["SAVE20","","PHARMA5","SAVE@20"],
            ["restaurant","grocery","pharmacy","restaurant"],
            [True, True, True, True]
        ), ["PHARMA5","SAVE20"])

        self.assertEqual(test.validateCoupons(
            ["GROCERY15","ELECTRONICS_50","DISCOUNT10"],
            ["grocery","electronics","invalid"],
            [False, True, True]
        ), ["ELECTRONICS_50"])
