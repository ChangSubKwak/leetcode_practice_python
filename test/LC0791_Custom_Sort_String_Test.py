import unittest

from main.LC0791_Custom_Sort_String import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_customSortString(self):
        self.assertEqual(test.customSortString("cba", "abcd"), "cbad")
        self.assertEqual(test.customSortString("bcafg", "abcd"), "bcad")
