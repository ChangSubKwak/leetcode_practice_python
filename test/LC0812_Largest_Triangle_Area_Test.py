import unittest

from main.LC0812_Largest_Triangle_Area import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_customSortString(self):
        self.assertEqual(test.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]), 2.00000)
        self.assertEqual(test.largestTriangleArea([[1, 0], [0, 0], [0, 1]]), 0.50000)
