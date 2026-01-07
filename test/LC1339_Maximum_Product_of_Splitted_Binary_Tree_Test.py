import unittest
from main.LC1339_Maximum_Product_of_Splitted_Binary_Tree import Solution
from main.TreeNode import TreeNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_findTheCity(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)

        self.assertEqual(test.maxProduct(root), 110)

        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(6)

        self.assertEqual(test.maxProduct(root), 90)