import unittest

from main.LC2141_Maximum_Running_Time_of_N_Computers import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maxRunTime(2, [3, 3, 3]), 4)
        self.assertEqual(test.maxRunTime(2, [1, 1, 1, 1]), 2)
