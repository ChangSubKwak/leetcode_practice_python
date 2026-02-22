import unittest

from main.LC0868_Binary_Gap import Solution
test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.binaryGap(22), 2)
        self.assertEqual(test.binaryGap(8), 0)
        self.assertEqual(test.binaryGap(5), 2)
