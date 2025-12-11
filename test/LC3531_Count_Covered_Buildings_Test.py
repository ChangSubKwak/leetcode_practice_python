import unittest
from main.LC3531_Count_Covered_Buildings import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.countCoveredBuildings(3, [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]), 1)
        self.assertEqual(test.countCoveredBuildings(3, [[1, 1], [1, 2], [2, 1], [2, 2]]), 0)
        self.assertEqual(test.countCoveredBuildings(3, [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]), 5)
