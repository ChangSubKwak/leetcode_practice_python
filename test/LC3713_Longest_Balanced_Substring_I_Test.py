import unittest
from main.LC3719_Longest_Balanced_Substring_I import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.longestBalanced("abbac"), 4)
        self.assertEqual(test.longestBalanced("zzabccy"), 4)
        self.assertEqual(test.longestBalanced("aba"), 2)
