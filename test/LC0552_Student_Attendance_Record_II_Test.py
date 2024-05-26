import unittest

from main.LC0543_Diameter_of_Binary_Tree import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_checkRecord(self):
        self.assertEqual(test.checkRecord(2), 8)
        self.assertEqual(test.checkRecord(1), 3)
        self.assertEqual(test.checkRecord(10101), 183236316)
