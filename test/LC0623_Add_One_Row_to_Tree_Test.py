import unittest

from main.LC0623_Add_One_Row_to_Tree import Solution

from main.TreeNode import TreeNode


class SolutionTest(unittest.TestCase):

    def test_addOneRow1(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(1)
        root.right.left = TreeNode(5)

        result = TreeNode(4)
        result.left = TreeNode(1)
        result.right = TreeNode(1)
        result.left.left = TreeNode(2)
        result.left.left.left = TreeNode(3)
        result.left.left.right = TreeNode(1)

        result.right.right = TreeNode(6)
        result.right.right.left = TreeNode(5)

        self.assertEqual(Solution.addOneRow(root, 1, 2), result)

    def test_addOneRow2(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(1)

        result = TreeNode(4)
        result.left = TreeNode(2)
        result.left.left = TreeNode(1)
        result.left.left.left = TreeNode(3)
        result.left.right.right = TreeNode(1)

        self.assertEqual(Solution.addOneRow(root, 1, 3), result)
