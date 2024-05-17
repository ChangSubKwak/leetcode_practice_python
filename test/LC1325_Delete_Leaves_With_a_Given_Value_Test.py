import unittest
from main.LC1325_Delete_Leaves_With_a_Given_Value import Solution

from main.TreeNode import TreeNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_removeLeafNodes1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(2)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(4)

        expected = TreeNode(1)
        expected.right = TreeNode(3)
        expected.right.right = TreeNode(4)

        self.assertEqual(test.removeLeafNodes(root, 2), expected)

    def test_removeLeafNodes2(self):
        root = TreeNode(1)
        root.left = TreeNode(3)
        root.right = TreeNode(3)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(2)

        expected = TreeNode(1)
        expected.left = TreeNode(3)
        expected.left.right = TreeNode(2)

        self.assertEqual(test.removeLeafNodes(root, 3), expected)

    def test_removeLeafNodes3(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(2)

        expected = TreeNode(1)

        self.assertEqual(test.removeLeafNodes(root, 2), expected)
