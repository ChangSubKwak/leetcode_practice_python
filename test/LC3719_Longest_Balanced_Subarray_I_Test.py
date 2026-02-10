import unittest
from main.LC3719_Longest_Balanced_Subarray_I import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.longestBalanced([2, 5, 4, 3]), 4)
        self.assertEqual(test.longestBalanced([3, 2, 2, 5, 4]), 5)
        self.assertEqual(test.longestBalanced([1, 2, 3, 2]), 3)
