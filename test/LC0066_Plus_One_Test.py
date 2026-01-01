import unittest

from main.LC0066_Plus_One import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
  def test(self):
    self.assertEqual(test.plusOne([1, 2, 3]), [1, 2, 4])
    self.assertEqual(test.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
    self.assertEqual(test.plusOne([9]), [1, 0])
