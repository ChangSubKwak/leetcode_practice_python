import unittest

from main.LC0402_Remove_K_Digits import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findDuplicates(self):
        self.assertEqual(test.removeKdigits("1432219", 3), "1219")
        self.assertEqual(test.removeKdigits("10200", 1), "200")
        self.assertEqual(test.removeKdigits("10", 2), "0")

