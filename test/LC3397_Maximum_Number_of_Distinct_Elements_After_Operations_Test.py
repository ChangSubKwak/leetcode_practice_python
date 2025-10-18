import unittest
from main.LC3397_Maximum_Number_of_Distinct_Elements_After_Operations import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.maxDistinctElements([1, 2, 2, 3, 3, 4], 2), 6)
        self.assertEqual(test.maxDistinctElements([4, 4, 4, 4], 1), 3)
