import unittest

from main.LC0085_Maximal_Rectangle import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_climbStairs(self):
        self.assertEqual(test.maximalRectangle(
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"]
            ]
        ), 6)
        self.assertEqual(test.maximalRectangle([["0"]]), 0)
        self.assertEqual(test.maximalRectangle([["1"]]), 1)