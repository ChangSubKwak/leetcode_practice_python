import unittest
from main.LC0974_Subarray_Sums_Divisible_by_K import Solution

test = Solution()


class TestClass(unittest.TestCase):
    def test_minFallingPathSum(self):
        self.assertEqual(test.subarraysDivByK([4, 5, 0, -2, -3, 1], 5), 7)
        self.assertEqual(test.subarraysDivByK([5], 9), 0)
