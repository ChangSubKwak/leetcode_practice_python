import unittest

from main.LC1508_Range_Sum_of_Sorted_Subarray_Sums import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_rangeSum(self):
        self.assertEqual(test.rangeSum([1, 2, 3, 4], 4, 1, 5), 13)
        self.assertEqual(test.rangeSum([1, 2, 3, 4], 4, 3, 4), 6)
        self.assertEqual(test.rangeSum([1, 2, 3, 4], 4, 1, 10), 50)
