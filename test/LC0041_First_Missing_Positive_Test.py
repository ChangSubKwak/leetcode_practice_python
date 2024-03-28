import unittest
from main.LC0041_First_Missing_Positive import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_firstMissingPositive(self):
        self.assertEqual(test.firstMissingPositive([1, 2, 0]), 3)
        self.assertEqual(test.firstMissingPositive([3, 4, -1, 1]), 2)
        self.assertEqual(test.firstMissingPositive([7, 8, 9, 11, 12]), 1)
