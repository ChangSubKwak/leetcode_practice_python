import unittest

from main.LC0404_Sum_of_Left_Leaves import Solution
from main.TreeNode import TreeNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_sumOfLeftLeaves(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertEqual(test.sumOfLeftLeaves(root), 24)

        root = TreeNode(1)
        self.assertEqual(test.sumOfLeftLeaves(root), 0)
