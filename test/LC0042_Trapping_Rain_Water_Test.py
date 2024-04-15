import unittest
from main.LC0042_Trapping_Rain_Water import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_firstMissingPositive(self):
        self.assertEqual(test.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(test.trap([4, 2, 0, 3, 2, 5]), 9)
