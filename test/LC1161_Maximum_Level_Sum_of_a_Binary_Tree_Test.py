import unittest
from main.LC1161_Maximum_Level_Sum_of_a_Binary_Tree import Solution

from main.TreeNode import TreeNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(0)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(-8)
        self.assertEqual(test.maxLevelSum(root), 2)

        root = TreeNode(989)
        root.right = TreeNode(10250)
        root.right.left = TreeNode(98693)
        root.right.right = TreeNode(-89388)
        root.right.right.right = TreeNode(-32127)
        self.assertEqual(test.maxLevelSum(root), 2)
