import unittest
from main.LC0040_Combination_Sum_II import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_combinationSum2(self):
        self.assertEqual(test.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8).sort(), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]].sort())
        self.assertEqual(test.combinationSum2([2, 5, 2, 1, 2], 5), [[1, 2, 2].sort(), [5]].sort())
