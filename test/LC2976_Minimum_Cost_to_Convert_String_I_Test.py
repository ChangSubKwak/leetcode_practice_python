import unittest

from main.LC2976_Minimum_Cost_to_Convert_String_I import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_minimumCost(self):
        self.assertEqual(test.minimumCost("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"], [2, 5, 5, 1, 2, 20]), 28)
        self.assertEqual(test.minimumCost("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]), 12)
        self.assertEqual(test.minimumCost("abcd", "abce", ["a"], ["e"], [10000]), -1)
