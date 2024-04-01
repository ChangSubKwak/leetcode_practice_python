import unittest

from main.LC2444_Count_Subarrays_With_Fixed_Bounds import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_onesMinusZeros(self):
        self.assertEqual(test.countSubarrays([1, 3, 5, 2, 7, 5], 1, 5), 2)
        self.assertEqual(test.countSubarrays([1, 1, 1, 1], 1, 1), 10)
