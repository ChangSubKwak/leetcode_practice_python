import unittest
from main.LC2597_The_Number_of_Beautiful_Subsets import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_beautifulSubsets(self):
        self.assertEqual(test.beautifulSubsets([2, 4, 6], 2), 4)
        self.assertEqual(test.beautifulSubsets([1], 1), 1)
