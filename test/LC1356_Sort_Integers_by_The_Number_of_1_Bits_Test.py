import unittest
from main.LC1356_Sort_Integers_by_The_Number_of_1_Bits import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]), [0, 1, 2, 4, 8, 3, 5, 6, 7])
        self.assertEqual(test.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]), [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
