import unittest
from main.LC0330_Patching_Array import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minPatches(self):
        self.assertEqual(test.minPatches([1, 3], 6), 1)
        self.assertEqual(test.minPatches([1, 5, 10], 20), 2)
        self.assertEqual(test.minPatches([1, 2, 2], 5), 0)
