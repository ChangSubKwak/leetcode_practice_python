import unittest
from main.LC2373_Largest_Local_Values_in_a_Matrix import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_largestLocal(self):
        self.assertEqual(test.largestLocal([
            [9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]
        ]), [[9, 9], [8, 6]])

        self.assertEqual(test.largestLocal([
            [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]
        ]), [[2, 2, 2], [2, 2, 2], [2, 2, 2]])
