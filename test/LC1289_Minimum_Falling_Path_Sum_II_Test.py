import unittest

from main.LC1289_Minimum_Falling_Path_Sum_II import Solution

test = Solution()


class LC1266_Minimum_Time_Visiting_All_Points_test(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minFallingPathSum([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]), 13)

        self.assertEqual(test.minFallingPathSum([
            [7]
        ]), 7)
