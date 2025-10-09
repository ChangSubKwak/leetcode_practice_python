import unittest
from main.LC3494_Find_the_Minimum_Amount_of_Time_to_Brew_Potions import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minTime([1, 5, 2, 4], [5, 1, 4, 2]), 110)
        self.assertEqual(test.minTime([1, 1, 1], [1, 1, 1]), 5)
        self.assertEqual(test.minTime([1, 2, 3, 4], [1, 2]), 21)
