import unittest

from main.LC0100_Same_Tree import Solution
from main.TreeNode import TreeNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_isSameTree(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        self.assertEqual(test.isSameTree(p, q), True)

        p = TreeNode(1)
        p.left = TreeNode(2)
        q = TreeNode(1)
        q.right = TreeNode(2)
        self.assertEqual(test.isSameTree(p, q), False)

        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(1)
        q = TreeNode(1)
        q.left = TreeNode(1)
        q.right = TreeNode(2)
        self.assertEqual(test.isSameTree(p, q), False)