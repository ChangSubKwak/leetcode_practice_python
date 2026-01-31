import unittest

from main.LC0744_Find_Smallest_Letter_Greater_Than_Target import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findErrorNums(self):
        self.assertEqual(test.nextGreatestLetter(["c", "f", "j"], "a"), "c")
        self.assertEqual(test.nextGreatestLetter(["c", "f", "j"], "c"), "f")
        self.assertEqual(test.nextGreatestLetter(["x", "x", "y", "y"], "z"), "x")
