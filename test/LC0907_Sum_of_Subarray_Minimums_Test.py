import unittest

from main.LC0907_Sum_of_Subarray_Minimums import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_sumSubarrayMins(self):
        self.assertEqual(test.sumSubarrayMins([3, 1, 2, 4]), 17)
        self.assertEqual(test.sumSubarrayMins([11, 81, 94, 43, 3]), 444)
