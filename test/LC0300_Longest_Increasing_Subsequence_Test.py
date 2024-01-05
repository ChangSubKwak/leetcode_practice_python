import unittest

from main.LC0300_Longest_Increasing_Subsequence import LC0300_Longest_Increasing_Subsequence

test = LC0300_Longest_Increasing_Subsequence()


class LC0300_Longest_Increasing_Subsequence_Test(unittest.TestCase):
    def test_lengthOfLIS(self):
        self.assertEqual(test.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(test.lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)
        self.assertEqual(test.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1)


