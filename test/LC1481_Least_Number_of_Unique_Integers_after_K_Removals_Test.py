import unittest

from main.LC1481_Least_Number_of_Unique_Integers_after_K_Removals import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findLeastNumOfUniqueInts(self):
        self.assertEqual(test.findLeastNumOfUniqueInts([5, 5, 4]), 1)
        self.assertEqual(test.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2]), 3)
