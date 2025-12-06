import unittest
from main.LC3578_Count_Partitions_With_Max_Min_Difference_at_Most_K import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.countPartitions([9, 4, 1, 3, 7], 4), 6)
        self.assertEqual(test.countPartitions([3, 3, 4], 0), 2)
