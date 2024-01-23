import unittest

from main.LC1239_Maximum_Length_of_a_Concatenated_String_with_Unique_Characters import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
  def test_maxLength(self):
    self.assertEqual(test.maxLength(["un", "iq", "ue"]), 4)
    self.assertEqual(test.maxLength(["cha", "r", "act", "ers"]), 6)
    self.assertEqual(test.maxLength(["abcdefghijklmnopqrstuvwxyz"]), 26)



