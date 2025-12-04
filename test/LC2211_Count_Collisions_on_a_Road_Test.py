import unittest

from main.LC2211_Count_Collisions_on_a_Road import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_triangularSum(self):
        self.assertEqual(test.countCollisions("RLRSLL"), 5)
        self.assertEqual(test.countCollisions("LLRR"), 0)
