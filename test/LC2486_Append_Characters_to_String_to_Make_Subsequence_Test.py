import unittest
from main.LC2486_Append_Characters_to_String_to_Make_Subsequence import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_pivotInteger(self):
        self.assertEqual(test.appendCharacters("coaching", "coding"), 4)
        self.assertEqual(test.appendCharacters("abcde", "a"), 0)
        self.assertEqual(test.appendCharacters("z", "abcde"), 5)
