import unittest

from main.LC1018_Binary_Prefix_Divisible_By_5 import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.prefixesDivBy5([0, 1, 1]), [True, False, False])
        self.assertEqual(test.prefixesDivBy5([1, 1, 1]), [False, False, False])
