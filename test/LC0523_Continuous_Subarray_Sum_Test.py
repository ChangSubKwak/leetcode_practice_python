import unittest
from main.LC0523_Continuous_Subarray_Sum import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_checkSubarraySum(self):
        self.assertEqual(test.checkSubarraySum([23, 2, 4, 6, 7], 6), True)
        self.assertEqual(test.checkSubarraySum([23, 2, 6, 4, 7], 6), True)
        self.assertEqual(test.checkSubarraySum([23, 2, 6, 4, 7], 13), False)
