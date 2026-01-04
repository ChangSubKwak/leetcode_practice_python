import unittest
from main.LC1390_Four_Divisors import Solution
from main.TreeNode import TreeNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.sumFourDivisors([21, 4, 7]), 32)
        self.assertEqual(test.sumFourDivisors([21, 21]), 64)
        self.assertEqual(test.sumFourDivisors([1, 2, 3, 4, 5]), 0)
