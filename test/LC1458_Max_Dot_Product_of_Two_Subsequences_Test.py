import unittest

from main.LC1458_Max_Dot_Product_of_Two_Subsequences import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_pseudoPalindromicPaths(self):
        self.assertEqual(test.maxDotProduct([2, 1, -2, 5], [3, 0, -6]), 18)
        self.assertEqual(test.maxDotProduct([3, -2], [2, -6, 7]), 21)
        self.assertEqual(test.maxDotProduct([-1, -1], [1, 1]), -1)
