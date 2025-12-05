import unittest
from main.LC3432_Count_Partitions_with_Even_Sum_Difference import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.countPartitions([0, 10, 3, 7, 6]), 4)
        self.assertEqual(test.countPartitions([1, 2, 2]), 0)
        self.assertEqual(test.countPartitions([2, 4, 6, 8]), 3)
