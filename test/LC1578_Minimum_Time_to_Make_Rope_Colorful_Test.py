import unittest
from main.LC1578_Minimum_Time_to_Make_Rope_Colorful import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_makeGood(self):
        self.assertEqual(test.minCost("abaac", [1, 2, 3, 4, 5]), 2)
        self.assertEqual(test.minCost("abc", [1, 2, 3]), 0)
        self.assertEqual(test.minCost("aabaa", [1, 2, 3, 4, 1]), 2)
