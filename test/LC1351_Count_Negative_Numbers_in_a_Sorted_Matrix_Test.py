import unittest
from main.LC1351_Count_Negative_Numbers_in_a_Sorted_Matrix import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.countNegatives([
            [4, 3, 2, -1],
            [3, 2, 1, -1],
            [1, 1, -1, -2],
            [-1, -1, -2, -3]
        ]), 8)

        self.assertEqual(test.countNegatives([
            [3, 2],
            [1, 0]
        ]), 8)
