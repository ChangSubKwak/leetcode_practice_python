import unittest
from main.LC3741_Minimum_Distance_Between_Three_Equal_Elements_II import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minimumDistance([1, 2, 1, 1, 3]), 6)
        self.assertEqual(test.minimumDistance([1, 1, 2, 3, 2, 1, 2]), 8)
        self.assertEqual(test.minimumDistance([1]), -1)
