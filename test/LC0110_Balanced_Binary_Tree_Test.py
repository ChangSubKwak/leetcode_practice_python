import unittest

from main.LC0110_Balanced_Binary_Tree import Solution
from main.TreeNode import TreeNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(test.isBalanced(root), True)

    def test2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        self.assertEqual(test.isBalanced(root), False)

    def test3(self):
        root = TreeNode()
        self.assertEqual(test.isBalanced(root), True)