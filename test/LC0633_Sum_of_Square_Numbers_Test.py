import unittest
from main.LC0633_Sum_of_Square_Numbers import Solution


test = Solution()

class SolutionTest(unittest.TestCase):
    def test_judgeSquareSum(self):
        self.assertEqual(test.judgeSquareSum(5), True)
        self.assertEqual(test.judgeSquareSum(3), False)
