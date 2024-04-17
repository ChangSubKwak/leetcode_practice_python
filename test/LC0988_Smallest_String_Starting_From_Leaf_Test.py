import unittest

from main.LC0988_Smallest_String_Starting_From_Leaf import Solution

from main.TreeNode import TreeNode

test = Solution()


class TestClass(unittest.TestCase):
    def test_smallestFromLeaf1(self):
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)
        self.assertEqual(test.smallestFromLeaf(root), "dba")

    def test_smallestFromLeaf2(self):
        root = TreeNode(25)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(2)
        self.assertEqual(test.smallestFromLeaf(root), "adz")

    def test_smallestFromLeaf3(self):
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(1)
        root.left.right = TreeNode(1)
        root.right.left = TreeNode(0)
        root.left.right.left = TreeNode(0)
        self.assertEqual(test.smallestFromLeaf(root), "abc")