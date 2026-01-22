import unittest
from main.LC3507_Minimum_Pair_Removal_to_Sort_Array_I import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minOperations([5, 2, 3, 1]), 2)
        self.assertEqual(test.minOperations([1, 2, 2]), 0)
