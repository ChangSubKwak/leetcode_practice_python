import unittest
from main.LC1395_Count_Number_of_Teams import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_numTeams(self):
        self.assertEqual(test.numTeams([2, 5, 3, 4, 1]), 3)
        self.assertEqual(test.numTeams([2, 1, 3]), 0)
        self.assertEqual(test.numTeams([1, 2, 3, 4]), 4)