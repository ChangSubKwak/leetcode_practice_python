import unittest
from main.LC3381_Maximum_Subarray_Sum_With_Length_Divisible_by_K import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maxSubarraySum([1, 2], 1), 3)
        self.assertEqual(test.maxSubarraySum([-1, -2, -3, -4, -5], 4), -10)
        self.assertEqual(test.maxSubarraySum([-5, 1, 2, -3, 4], 2), 4)
