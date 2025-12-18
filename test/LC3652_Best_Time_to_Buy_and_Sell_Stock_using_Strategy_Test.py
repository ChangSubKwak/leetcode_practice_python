import unittest
from main.LC3652_Best_Time_to_Buy_and_Sell_Stock_using_Strategy import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maxProfit([4, 2, 8], [-1, 0, 1], 2), 10)
        self.assertEqual(test.maxProfit([5, 4, 3], [1, 1, 0], 2), 9)
