import unittest
from main.LC1975_Maximum_Matrix_Sum import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maxMatrixSum([[1, -1], [-1, 1]]), 4)
        self.assertEqual(test.maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]), 16)
