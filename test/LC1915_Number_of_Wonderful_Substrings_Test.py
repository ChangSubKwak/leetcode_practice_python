import unittest

from main.LC1915_Number_of_Wonderful_Substrings import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_numberOfMatches(self):
        self.assertEqual(test.wonderfulSubstrings("abc"), 4)
        self.assertEqual(test.wonderfulSubstrings("aabb"), 9)