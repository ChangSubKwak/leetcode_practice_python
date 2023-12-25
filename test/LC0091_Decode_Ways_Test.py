import unittest

from main.LC0091_Decode_Ways import LC0091_Decode_Ways

test = LC0091_Decode_Ways()


class LC0091_Decode_Ways_Test(unittest.TestCase):
  def test_numDecodings(self):
    self.assertEqual(test.numDecodings("12"), 2)
    self.assertEqual(test.numDecodings("226"), 3)
    self.assertEqual(test.numDecodings("06"), 0)
