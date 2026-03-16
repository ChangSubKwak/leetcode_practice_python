import unittest
from main.LC1878_Get_Biggest_Three_Rhombus_Sums_in_a_Grid import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.getBiggestThree([
            [3, 4, 5, 1, 3],
            [3, 3, 4, 2, 3],
            [20, 30, 200, 40, 10],
            [1, 5, 5, 4, 1],
            [4, 3, 2, 2, 5]
        ]), [228, 216, 211])

        self.assertEqual(test.getBiggestThree([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]), [20, 9, 8])

        self.assertEqual(test.getBiggestThree([
            [7, 7, 7]
        ]), [7])
