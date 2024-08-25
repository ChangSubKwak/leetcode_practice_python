import unittest

from main.LC0145_Binary_Tree_Postorder_Traversal import Solution
from main.TreeNode import TreeNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_postorderTraversal(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(test.postorderTraversal(root), [3, 2, 1])

        root = None
        self.assertEqual(test.postorderTraversal(root), [])

        root = TreeNode(1)
        self.assertEqual(test.postorderTraversal(root), [1])
