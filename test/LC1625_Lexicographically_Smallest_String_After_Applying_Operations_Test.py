import unittest

from main.LC1625_Lexicographically_Smallest_String_After_Applying_Operations import Solution

test = Solution()


class LC1625_Lexicographically_Smallest_String_After_Applying_Operations_Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test.findLexSmallestString("5525", 9, 2), "2050")
        self.assertEqual(test.findLexSmallestString("74", 5, 1), "24")
        self.assertEqual(test.findLexSmallestString("0011", 4, 2), "0011")
