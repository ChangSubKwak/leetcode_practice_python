import unittest

from main.LC2225_Find_Players_With_Zero_or_One_Losses import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findWinners(self):
        self.assertEqual(test.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]), [[1, 2, 10], [4, 5, 7, 8]])
        self.assertEqual(test.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]), [[1, 2, 5, 6], []])
