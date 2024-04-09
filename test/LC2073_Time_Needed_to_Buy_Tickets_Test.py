import unittest

from main.LC2073_Time_Needed_to_Buy_Tickets import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_timeRequiredToBuy(self):
        self.assertEqual(test.timeRequiredToBuy([2, 3, 2], 2), 6)
        self.assertEqual(test.timeRequiredToBuy([5, 1, 1, 1], 0), 8)

