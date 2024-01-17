import unittest

from main.LC1207_Unique_Number_of_Occurrences import Solution

test = Solution()


class SolutionTest(unittest.TestCase):

  def test_uniqueOccurrences(self):
    self.assertEqual(test.uniqueOccurrences([1, 2, 2, 1, 1, 3]), True)
    self.assertEqual(test.uniqueOccurrences([1, 2]), False)
    self.assertEqual(test.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]), True)
