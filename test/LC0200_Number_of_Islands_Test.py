import unittest

from main.LC0200_Number_of_Islands import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_isPowerOfTwo(self):
        self.assertEqual(test.numIslands([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]), 1)

        self.assertEqual(test.numIslands([
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]), 3)