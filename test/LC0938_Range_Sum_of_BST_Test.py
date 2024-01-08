import unittest

from main.LC0938_Range_Sum_of_BST import Solution
from main.TreeNode import TreeNode

test = Solution()


class TestClass(unittest.TestCase):
    def test_rangeSumBST(self):
        root = TreeNode(10)

        root.left = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)

        root.right = TreeNode(15)
        root.right.right = TreeNode(18)

        self.assertEqual(test.rangeSumBST(root, 7, 15), 32)

        root = TreeNode(10)

        root.left = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(1)

        root.left.right = TreeNode(7)
        root.left.right.left = TreeNode(6)

        root.right = TreeNode(15)
        root.right.right = TreeNode(18)

        self.assertEqual(test.rangeSumBST(root, 6, 10), 23)
