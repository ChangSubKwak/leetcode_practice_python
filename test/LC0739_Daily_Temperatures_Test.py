import unittest

from main.LC0739_Daily_Temperatures import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findErrorNums(self):
        self.assertEqual(test.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
        self.assertEqual(test.dailyTemperatures([30, 40, 50, 60]), [1, 1, 1, 0])
        self.assertEqual(test.dailyTemperatures([30, 60, 90]), [1, 1, 0])
