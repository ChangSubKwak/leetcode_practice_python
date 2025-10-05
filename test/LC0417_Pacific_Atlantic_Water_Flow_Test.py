import unittest

from main.LC0417_Pacific_Atlantic_Water_Flow import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_sumOfLeftLeaves(self):
        self.assertEqual(test.pacificAtlantic(
            [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]),
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        )

        self.assertEqual(test.pacificAtlantic([[1]]), [[0, 0]])
