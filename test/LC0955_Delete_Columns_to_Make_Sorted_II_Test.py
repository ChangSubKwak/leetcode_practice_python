import unittest

from main.LC0955_Delete_Columns_to_Make_Sorted_II import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minDeletionSize(["ca", "bb", "ac"]), 1)
        self.assertEqual(test.minDeletionSize(["xc", "yb", "za"]), 0)
        self.assertEqual(test.minDeletionSize(["zyx", "wvu", "tsr"]), 3)
