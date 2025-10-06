import unittest

from main.LC0778_Swim_in_Rising_Water import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findErrorNums(self):
        self.assertEqual(test.swimInWater([[0, 2], [1, 3]]), 3)
        self.assertEqual(test.swimInWater([
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6]
        ]), 16)
