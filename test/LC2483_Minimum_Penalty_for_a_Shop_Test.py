import unittest
from main.LC2483_Minimum_Penalty_for_a_Shop import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.bestClosingTime([[1, 3, 2], [4, 5, 2], [2, 4, 3]]), 4)