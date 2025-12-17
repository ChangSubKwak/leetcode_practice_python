import unittest
from main.LC3573_Best_Time_to_Buy_and_Sell_Stock_V import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maximumProfit([1, 7, 9, 8, 2], 2), 14)
        self.assertEqual(test.maximumProfit([12, 16, 19, 19, 8, 1, 19, 13, 9], 3), 36)
