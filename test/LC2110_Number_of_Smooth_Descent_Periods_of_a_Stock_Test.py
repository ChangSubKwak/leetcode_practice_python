import unittest

from main.LC2110_Number_of_Smooth_Descent_Periods_of_a_Stock import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.getDescentPeriods([3, 2, 1, 4]), 7)
        self.assertEqual(test.getDescentPeriods([8, 6, 7, 7]), 4)
        self.assertEqual(test.getDescentPeriods([1]), 1)
