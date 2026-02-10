import unittest
from main.LC1382_Balance_a_Binary_Search_Tree import Solution
from main.TreeNode import TreeNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_balanceBST1(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)

        expected = TreeNode(2)
        expected.left = TreeNode(1)
        expected.right = TreeNode(3)
        expected.right.right = TreeNode(4)

        result = test.balanceBST(root)

        self.assertEqual(result.val, expected.val)
        self.assertEqual(result.left.val, expected.left.val)
        self.assertEqual(result.right.val, expected.right.val)
        self.assertEqual(result.right.right.val, expected.right.right.val)

    def test_balanceBST2(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)

        expected = TreeNode(2)
        expected.left = TreeNode(1)
        expected.right = TreeNode(3)

        result = test.balanceBST(root)

        self.assertEqual(result.val, expected.val)
        self.assertEqual(result.left.val, expected.left.val)
        self.assertEqual(result.right.val, expected.right.val)
