import unittest

from main.LC0564_Find_the_Closest_Palindrome import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_checkRecord(self):
        self.assertEqual(test.nearestPalindromic("123"), "121")
        self.assertEqual(test.nearestPalindromic("1"), "0")
