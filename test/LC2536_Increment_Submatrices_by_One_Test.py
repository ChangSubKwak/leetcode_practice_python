import unittest
from main.LC2536_Increment_Submatrices_by_One import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.rangeAddQueries(3, [[1, 1, 2, 2], [0, 0, 1, 1]]), [[1, 1, 0], [1, 2, 1], [0, 1, 1]])
        self.assertEqual(test.rangeAddQueries(2, [[0, 0, 1, 1]]), [[1, 1], [1, 1]])
