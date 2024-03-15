import unittest

from main.LC0238_Product_of_Array_Except_Self import Solution

test = Solution()


class Solution(unittest.TestCase):
    def test_productExceptSelf(self):
        self.assertEqual(test.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(test.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
