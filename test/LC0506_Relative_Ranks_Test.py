import unittest
from main.LC0514_Relative_Ranks import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findRelativeRanks(self):
        self.assertEqual(
            test.findRelativeRanks([5, 4, 3, 2, 1]),
            [
                "Gold Medal",
                "Silver Medal",
                "Bronze Medal",
                "4",
                "5"
            ]
        )

        self.assertEqual(
            test.findRelativeRanks([10, 3, 8, 9, 4]),
            [
                "Gold Medal",
                "5",
                "Bronze Medal",
                "Silver Medal",
                "4"
            ]
        )