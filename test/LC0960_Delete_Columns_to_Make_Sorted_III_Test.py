import unittest

from main.LC0955_Delete_Columns_to_Make_Sorted_II import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minDeletionSize(["babca", "bbazb"]),3)
        self.assertEqual(test.minDeletionSize(["edcba"]),4)
        self.assertEqual(test.minDeletionSize(["ghi", "def", "abc"]),0)
