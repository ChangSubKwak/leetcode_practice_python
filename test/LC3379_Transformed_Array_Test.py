import unittest
from main.LC3379_Transformed_Array import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maxSubarraySum([3, -2, 1, 1]), [1, 1, 1, 1])
        self.assertEqual(test.maxSubarraySum([-1, 4, -1]), [-1, -1, 4])
