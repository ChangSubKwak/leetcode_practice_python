import unittest

from main.LC2441_Largest_Positive_Integer_That_Exists_With_Its_Negative import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_onesMinusZeros(self):
        self.assertEqual(test.findMaxK([-1, 2, -3, 3]), 3)
        self.assertEqual(test.findMaxK([-1, 10, 6, 7, -7, 1]), 7)
        self.assertEqual(test.findMaxK([-10, 8, 6, 7, -2, -3]), -1)
