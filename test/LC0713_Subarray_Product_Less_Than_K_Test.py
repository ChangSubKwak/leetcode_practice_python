import unittest

from main.LC0713_Subarray_Product_Less_Than_K import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findErrorNums(self):
        self.assertEqual(test.numSubarrayProductLessThanK([10, 5, 2, 6], 100), 8)
        self.assertEqual(test.numSubarrayProductLessThanK([1, 2, 3], 0), 0)
