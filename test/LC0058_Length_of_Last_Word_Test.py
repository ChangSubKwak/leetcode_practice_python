import unittest
from main.LC0058_Length_of_Last_Word import Solution

test = Solution()

class SolutionTest(unittest.TestCase):
    def test_insert(self):
        self.assertEqual(test.lengthOfLastWord("Hello World"), 5)
        self.assertEqual(test.lengthOfLastWord("   fly me   to   the moon  "), 4)
        self.assertEqual(test.lengthOfLastWord("luffy is still joyboy"), 6)
