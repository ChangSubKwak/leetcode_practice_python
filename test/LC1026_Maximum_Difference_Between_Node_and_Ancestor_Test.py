import unittest

from main.LC1026_Maximum_Difference_Between_Node_and_Ancestor import Solution
from main.TreeNode import TreeNode

test = Solution()


class TestClass(unittest.TestCase):
    def test_maxAncestorDiff(self):
        root = TreeNode(8)
        root.left = TreeNode(3)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)
        root.left.right.left = TreeNode(4)
        root.left.right.right = TreeNode(7)

        root.right = TreeNode(10)
        root.right.right = TreeNode(14)
        root.right.left = TreeNode(14)

        self.assertEqual(test.rangeSumBST(root), 7)

        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(0)
        root.right.right.left = TreeNode(3)

        self.assertEqual(test.rangeSumBST(root), 3)
