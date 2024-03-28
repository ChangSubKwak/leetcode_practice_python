import unittest

from main.LC0442_Find_All_Duplicates_in_an_Array import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findDuplicates(self):
        self.assertTrue(set(test.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])).issubset([2, 3]))
        self.assertTrue(set(test.findDuplicates([1, 1, 2])).issubset([1]))
        self.assertTrue(set(test.findDuplicates([1])).issubset([]))

