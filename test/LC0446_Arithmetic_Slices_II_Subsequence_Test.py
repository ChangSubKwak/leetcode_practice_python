import unittest

from main.LC0446_Arithmetic_Slices_II_Subsequence import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_numberOfArithmeticSlices(self):
        self.assertEqual(test.numberOfArithmeticSlices([2, 4, 6, 8, 10]), 7)
        self.assertEqual(test.numberOfArithmeticSlices([7, 7, 7, 7, 7]), 16)
