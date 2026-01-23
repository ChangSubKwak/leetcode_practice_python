import unittest
from main.LC3510_Minimum_Pair_Removal_to_Sort_Array_II import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minimumPairRemoval([5, 2, 3, 1]), 2)
        self.assertEqual(test.minimumPairRemoval([1, 2, 2]), 0)
