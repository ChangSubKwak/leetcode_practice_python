import unittest
from main.LC3318_Find_X_Sum_of_All_K_Long_Subarrays_I import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.findXSum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2),  [6, 10, 12])
        self.assertEqual(test.findXSum([3, 8, 7, 8, 7, 5], 2, 2),  [11, 15, 15, 15, 12])
