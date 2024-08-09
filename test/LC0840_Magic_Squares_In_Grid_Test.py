import unittest
from main.LC0840_Magic_Squares_In_Grid import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_numMagicSquaresInside(self):
        self.assertEqual(test.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]), 1)
        self.assertEqual(test.numMagicSquaresInside([[8]]), 0)
        self.assertEqual(test.numMagicSquaresInside([[5, 5, 5], [5, 5, 5], [5, 5, 5]]), 0)
        self.assertEqual(test.numMagicSquaresInside([[10, 3, 5], [1, 6, 11], [7, 9, 2]]), 0)
        self.assertEqual(test.numMagicSquaresInside([[7, 0, 5], [2, 4, 6], [3, 8, 1]]), 0)
