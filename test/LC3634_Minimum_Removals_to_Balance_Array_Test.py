import unittest
from main.LC3634_Minimum_Removals_to_Balance_Array import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minRemoval([2, 1, 5], 2), 1)
        self.assertEqual(test.minRemoval([1, 6, 2, 9], 3), 2)
        self.assertEqual(test.minRemoval([4, 6], 2), 0)
