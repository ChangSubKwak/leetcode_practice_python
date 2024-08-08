import unittest

from main.LC0885_Spiral_Matrix_III import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_spiralMatrixIII(self):
        self.assertEqual(test.spiralMatrixIII(1, 4, 0, 0), [[0, 0], [0, 1], [0, 2], [0, 3]])
