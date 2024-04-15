import unittest

from main.LC0129_Sum_Root_to_Leaf_Numbers import Solution
from main.TreeNode import TreeNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_sumNumbers(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(test.sumNumbers(root), 25)

        root = TreeNode(4)
        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)
        self.assertEqual(test.sumNumbers(root), 1026)