import unittest
from main.LC3130_Find_All_Possible_Stable_Binary_Arrays_II import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minOperations(self):
        self.assertEqual(test.numberOfStableArrays(1, 1, 2), 2)
        self.assertEqual(test.numberOfStableArrays(1, 2, 1), 1)
        self.assertEqual(test.numberOfStableArrays(3, 3, 2), 14)
