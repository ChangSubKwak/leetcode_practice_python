import unittest

from main.LC0872_Leaf_Similar_Trees import Solution
from main.TreeNode import TreeNode

test = Solution()


class Test(unittest.TestCase):
    def test_imageSmoother(self):
        root1 = TreeNode(3)
        root1.left = TreeNode(5)
        root1.left.left = TreeNode(6)
        root1.left.right = TreeNode(2)
        root1.left.right.left = TreeNode(7)
        root1.left.right.right = TreeNode(4)

        root1.right = TreeNode(1)
        root1.right.left = TreeNode(9)
        root1.right.right = TreeNode(8)

        root2 = TreeNode(3)
        root2.left = TreeNode(5)
        root2.left.left = TreeNode(6)
        root2.left.right = TreeNode(7)

        root2.right = TreeNode(1)
        root2.right.left = TreeNode(4)
        root2.right.right = TreeNode(2)
        root2.right.right.left = TreeNode(9)
        root2.right.right.right = TreeNode(8)

        self.assertEqual(test.leafSimilar(root1, root2), True)

        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)

        root2 = TreeNode(1)
        root2.left = TreeNode(3)
        root2.right = TreeNode(2)

        self.assertEqual(test.leafSimilar(root1, root2), False)
