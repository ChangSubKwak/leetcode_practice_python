import unittest
from main.LC3761_Minimum_Absolute_Distance_Between_Mirror_Pairs import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.minMirrorPairDistance([12, 21, 45, 33, 54]), 1)
        self.assertEqual(test.minMirrorPairDistance([120, 21]), 1)
        self.assertEqual(test.minMirrorPairDistance([21, 120]), -1)
