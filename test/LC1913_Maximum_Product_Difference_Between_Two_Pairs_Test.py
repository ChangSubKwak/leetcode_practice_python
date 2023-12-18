import unittest

from main.LC1913_Maximum_Product_Difference_Between_Two_Pairs import LC1913_Maximum_Product_Difference_Between_Two_Pairs

test = LC1913_Maximum_Product_Difference_Between_Two_Pairs()


class LC1913_Maximum_Product_Difference_Between_Two_Pairs_Test(unittest.TestCase):
    def test_numberOfMatches(self):
        self.assertEqual(test.maxProductDifference([5, 6, 2, 7, 4]), 34)
        self.assertEqual(test.maxProductDifference([4, 2, 5, 9, 7, 4, 8]), 64)