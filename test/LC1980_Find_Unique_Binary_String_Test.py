import unittest
from main.LC1980_Find_Unique_Binary_String import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.findDifferentBinaryString(["01", "10"]), "11")
        self.assertEqual(test.findDifferentBinaryString(["00", "01"]), "11")
        self.assertEqual(test.findDifferentBinaryString(["111", "011", "001"]), "101")
