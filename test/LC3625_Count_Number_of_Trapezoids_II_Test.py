import unittest
from main.LC3625_Count_Number_of_Trapezoids_II import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.countTrapezoids([[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]), 2)
        self.assertEqual(test.countTrapezoids([[0, 0], [1, 0], [0, 1], [2, 1]]), 1)
