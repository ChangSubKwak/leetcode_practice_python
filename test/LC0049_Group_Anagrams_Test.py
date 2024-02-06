import unittest
from main.LC0049_Group_Anagrams import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_groupAnagrams(self):
        self.assertIn(["bat"], test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        self.assertIn(["nat", "tan"], sorted(test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])))
        self.assertIn(["ate", "eat", "tea"], sorted(test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])))
        self.assertEqual(test.groupAnagrams([""]), [[""]])
        self.assertEqual(test.groupAnagrams(["a"]), [["a"]])
