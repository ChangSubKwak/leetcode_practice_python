import unittest
from main.LC2943_Maximize_Area_of_Square_Hole_in_Grid import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maximizeSquareHoleArea(2, 1, [2, 3], [2]), 4)
        self.assertEqual(test.maximizeSquareHoleArea(1, 1, [2], [2]), 4)
        self.assertEqual(test.maximizeSquareHoleArea(2, 3, [2, 3], [2, 4]), 4)
