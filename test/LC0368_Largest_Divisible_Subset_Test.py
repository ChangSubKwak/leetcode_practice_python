import unittest

from main.LC0368_Largest_Divisible_Subset import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_largestDivisibleSubset(self):
        self.assertIn(test.largestDivisibleSubset([1, 2, 3]), [1, 2])
        self.assertIn(test.largestDivisibleSubset([1, 2, 3]), [1, 3])
        self.assertIn(test.largestDivisibleSubset([1, 2, 4, 8]), [1, 2, 4, 8])


