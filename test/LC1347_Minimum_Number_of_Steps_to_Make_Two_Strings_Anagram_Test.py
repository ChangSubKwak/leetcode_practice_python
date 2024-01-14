import unittest
from main.LC1347_Minimum_Number_of_Steps_to_Make_Two_Strings_Anagram import Solution

test = Solution()


class Test_LC1347_Minimum_Number_of_Steps_to_Make_Two_Strings_Anagram(unittest.TestCase):
    def test_minSteps(self):
        self.assertEqual(test.minSteps("bab", "aba"), 1)
        self.assertEqual(test.minSteps("leetcode", "practice"), 5)
        self.assertEqual(test.minSteps("anagram", "mangaar"), 0)
