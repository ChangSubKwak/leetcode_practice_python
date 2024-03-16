import unittest

from main.LC0525_Contiguous_Array import Solution


class SolutionTest(unittest.TestCase):
    def test_findMaxLength(self):
        self.assertEqual(Solution.findMaxLength([0, 1]), 2)
        self.assertEqual(Solution.findMaxLength([0, 1, 0]), 2)
