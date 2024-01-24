import unittest

from main.LC1457_Pseudo_Palindromic_Paths_in_a_Binary_Tree import Solution
from main.TreeNode import TreeNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_pseudoPalindromicPaths(self):
        root = TreeNode(2)
        root.left = TreeNode(3)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(1)
        root.right = TreeNode(1)
        root.right.right = TreeNode(1)
        self.assertEqual(test.pseudoPalindromicPaths(root), 2)

        root = TreeNode(2)
        root.left = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.left.right.right = TreeNode(1)
        root.right = TreeNode(1)
        self.assertEqual(test.pseudoPalindromicPaths(root), 1)

        root = TreeNode(9)
        self.assertEqual(test.pseudoPalindromicPaths(root), 1)



