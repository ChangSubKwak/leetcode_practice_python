import unittest

from main.LC0310_Minimum_Height_Trees import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_lengthOfLIS(self):
        self.assertEqual(test.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]), [1])
        self.assertEqual(test.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]), [3, 4])
