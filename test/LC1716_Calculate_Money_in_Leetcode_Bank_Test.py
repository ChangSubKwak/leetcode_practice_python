import unittest
from main.LC1716_Calculate_Money_in_Leetcode_Bank import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_averageWaitingTime(self):
        self.assertEqual(test.totalMoney(4), 10)
        self.assertEqual(test.totalMoney(10), 37)
        self.assertEqual(test.totalMoney(20), 96)
