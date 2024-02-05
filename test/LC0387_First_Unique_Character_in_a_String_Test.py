import unittest

from main.LC0387_First_Unique_Character_in_a_String import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_firstUniqChar(self):
        self.assertEqual(test.firstUniqChar("leetcode"), 0)
        self.assertEqual(test.firstUniqChar("loveleetcode"), 2)
        self.assertEqual(test.firstUniqChar("aabb"), -1)


