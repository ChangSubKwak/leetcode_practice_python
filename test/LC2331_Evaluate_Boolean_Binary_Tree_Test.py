import unittest

from main.LC2331_Evaluate_Boolean_Binary_Tree import Solution
from main.TreeNode import TreeNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_evaluateTree(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(1)

        self.assertEqual(test.evaluateTree(root), True)

        root = TreeNode(0)
        self.assertEqual(test.evaluateTree(root), False)
