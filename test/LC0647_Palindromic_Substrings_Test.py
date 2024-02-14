import unittest

from main.LC0647_Palindromic_Substrings import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findErrorNums(self):
        self.assertEqual(test.countSubstrings("abc"), 3)
        self.assertEqual(test.countSubstrings("aaa"), 6)
