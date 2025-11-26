import unittest

from main.LC2435_Paths_in_Matrix_Whose_Sum_Is_Divisible_by_K import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_evaluateTree(self):
        self.assertEqual(test.numberOfPaths([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3), 2)
        self.assertEqual(test.numberOfPaths([[0, 0]], 5), 1)
        self.assertEqual(test.numberOfPaths([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1), 10)
