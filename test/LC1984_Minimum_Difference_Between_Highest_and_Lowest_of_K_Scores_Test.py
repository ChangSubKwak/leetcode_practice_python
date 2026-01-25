import unittest
from main.LC1984_Minimum_Difference_Between_Highest_and_Lowest_of_K_Scores import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minimumDifference([90], 1), 0)
        self.assertEqual(test.minimumDifference([9, 4, 1, 7], 2), 2)
