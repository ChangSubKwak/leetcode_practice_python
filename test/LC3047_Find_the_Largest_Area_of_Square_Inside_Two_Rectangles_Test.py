import unittest

from main.LC3047_Find_the_Largest_Area_of_Square_Inside_Two_Rectangles import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minOperations(self):
        self.assertEqual(test.largestSquareArea([[1, 1], [2, 2], [3, 1]], [[3, 3], [4, 4], [6, 6]]), 1)
        self.assertEqual(test.largestSquareArea([[1, 1], [1, 3], [1, 5]], [[5, 5], [5, 7], [5, 9]]), 4)
        self.assertEqual(test.largestSquareArea([[1, 1], [2, 2], [1, 2]], [[3, 3], [4, 4], [3, 4]]), 1)
        self.assertEqual(test.largestSquareArea([[1, 1], [3, 3], [3, 1]], [[2, 2], [4, 4], [4, 2]]), 0)
