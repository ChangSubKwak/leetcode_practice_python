import unittest
from main.LC1568_Minimum_Number_of_Days_to_Disconnect_Island import Solution

test = Solution()


class SolutionTest:
    def test_minDays(self):
        self.assertEqual(test.minDays([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]), 2)
        self.assertEqual(test.minDays([[1, 1], [0, 0]]), 2)
