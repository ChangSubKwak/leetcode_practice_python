import unittest

from main.LC0513_Find_Bottom_Left_Tree_Value import Solution
from main.TreeNode import TreeNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findBottomLeftValue(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(test.findBottomLeftValue(root), 1)

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)
        root.right.left.left = TreeNode(7)


        self.assertEqual(test.findBottomLeftValue(root), 1)