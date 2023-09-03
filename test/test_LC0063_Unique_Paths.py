import unittest

from main.LC0063_Unique_Paths import LC0063_Unique_Paths

test = LC0063_Unique_Paths()


class test_LC0063_Unique_Paths(unittest.TestCase):
  def test_uniquePaths(self):
    self.assertEqual(test.uniquePaths(3, 7), 28)
    self.assertEqual(test.uniquePaths(3, 2), 3)
