import unittest
from main.LC0826_Most_Profit_Assigning_Work import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_maxProfitAssignment(self):
        self.assertEqual(test.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]), 100)
        self.assertEqual(test.maxProfitAssignment([85, 47, 57], [24, 66, 99], [40, 25, 25]), 0)
