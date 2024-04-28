import unittest

from main.LC0834_Sum_of_Distances_in_Tree import Solution
from main.TreeNode import TreeNode

test = Solution()


class Test(unittest.TestCase):
    def test_sumOfDistancesInTree(self):
        self.assertEqual(test.sumOfDistancesInTree(6, [
            [0, 1], [0, 2], [2, 3], [2, 4], [2, 5]
        ]),
            [8, 12, 6, 10, 10, 10]
        )

        self.assertEqual(test.sumOfDistancesInTree(1, [
            [0]
        ]),
            [0]
        )

        self.assertEqual(test.sumOfDistancesInTree(2, [
            [1, 0]
        ]),
            [1, 1]
        )
