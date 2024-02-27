import unittest

from main.TreeNode import TreeNode
from main.LC0543_Diameter_of_Binary_Tree import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findContentChildren(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(test.diameterOfBinaryTree(root), 3)

        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(test.diameterOfBinaryTree(root), 1)


