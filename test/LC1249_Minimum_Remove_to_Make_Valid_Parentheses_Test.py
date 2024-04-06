import unittest

from main.LC1249_Minimum_Remove_to_Make_Valid_Parentheses import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
  def test_maxLength(self):
    self.assertIn(test.minRemoveToMakeValid("lee(t(c)o)de)"), ["lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"])
    self.assertIn(test.minRemoveToMakeValid("a)b(c)d"), ["ab(c)d"])
    self.assertIn(test.minRemoveToMakeValid("))(("), [""])



