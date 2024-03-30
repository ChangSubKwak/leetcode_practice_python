import unittest

from main.LC2952_Count_Subarrays_Where_Max_Element_Appears_at_Least_K_Times import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_countSubarrays(self):
        self.assertEqual(test.countSubarrays([1, 3, 2, 3, 3]), 2)
        self.assertEqual(test.countSubarrays([1, 4, 2, 1]), 3)
