import unittest
from main.LC1550_Three_Consecutive_Odds import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_makeGood(self):
        self.assertEqual(test.threeConsecutiveOdds([2, 6, 4, 1]), False)
        self.assertEqual(test.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]), True)
