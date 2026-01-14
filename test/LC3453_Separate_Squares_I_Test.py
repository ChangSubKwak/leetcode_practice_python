import unittest
from main.LC3453_Separate_Squares_I import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.separateSquares([[0, 0, 1], [2, 2, 1]]), 1.00000)
        self.assertEqual(test.separateSquares([[0, 0, 1], [2, 2, 1]]), 1.16667)
