import unittest

from main.LC1544_Make_The_String_Great import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_makeGood(self):
        self.assertEqual(test.makeGood("leEeetcode"), "leetcode")
        self.assertEqual(test.makeGood("abBAcC"), "")
        self.assertEqual(test.makeGood("s"), "s")
