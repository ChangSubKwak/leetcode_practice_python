import unittest
from main.LC1701_Average_Waiting_Time import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_averageWaitingTime(self):
        self.assertEqual(test.averageWaitingTime([[1, 2], [2, 5], [4, 3]]), 5.00000)
        self.assertEqual(test.averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]), 3.25000)
