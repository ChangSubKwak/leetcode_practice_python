import unittest

from main.LC1437_Check_If_All_1s_Are_at_Least_Length_K_Places_Away import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_maxScore(self):
        self.assertEqual(test.kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2), True)
        self.assertEqual(test.kLengthApart([1, 0, 0, 1, 0, 1], 2), False)

