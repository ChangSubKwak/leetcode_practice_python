import unittest
from main.LC1482_Minimum_Number_of_Days_to_Make_m_Bouquets_Test import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minDays(self):
        self.assertEqual(test.minDays([1, 10, 3, 10, 2], 3, 1), 3)
        self.assertEqual(test.minDays([1, 10, 3, 10, 2], 3, 2), -1)
        self.assertEqual(test.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3), 12)
