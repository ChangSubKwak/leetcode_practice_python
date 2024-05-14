import unittest

from main.LC0861_Score_After_Flipping_Matrix import Solution
test = Solution()


class SolutionTest(unittest.TestCase):
    def test_sumOfDistancesInTree(self):
        self.assertEqual(test.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]), 39)
        self.assertEqual(test.matrixScore([[0]]), 1)
