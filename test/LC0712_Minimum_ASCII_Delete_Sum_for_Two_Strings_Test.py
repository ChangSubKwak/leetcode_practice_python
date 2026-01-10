import unittest

from main.LC0712_Minimum_ASCII_Delete_Sum_for_Two_Strings import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findErrorNums(self):
        self.assertEqual(test.minimumDeleteSum("sea", "eat"), 231)
        self.assertEqual(test.minimumDeleteSum("delete", "leet"), 403)
