import unittest

from main.LC2812_Find_the_Safest_Path_in_a_Grid import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_doubleIt1(self):
        self.assertEqual(test.maximumSafenessFactor([
            [0, 0, 1],
            [0, 0, 0],
            [0, 0, 0]
        ]), 0)

        self.assertEqual(test.maximumSafenessFactor([
            [0, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 0]
        ]), 2)
