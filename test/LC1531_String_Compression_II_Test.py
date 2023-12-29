import unittest

from main.LC1531_String_Compression_II import LC1531_String_Compression_II

test = LC1531_String_Compression_II()


class LC1531_String_Compression_II_Test(unittest.TestCase):
    def test_getLengthOfOptimalCompression(self):
        self.assertEqual(test.getLengthOfOptimalCompression("aaabcccd", 2), 4)
        self.assertEqual(test.getLengthOfOptimalCompression("aabbaa", 2), 2)
        self.assertEqual(test.getLengthOfOptimalCompression("aaaaaaaaaa", 0), 3)
