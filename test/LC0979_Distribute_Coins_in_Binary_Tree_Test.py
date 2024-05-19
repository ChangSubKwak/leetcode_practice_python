import unittest

from main.LC0979_Distribute_Coins_in_Binary_Tree import Solution

from main.TreeNode import TreeNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_distributeCoins1(self):
        root = TreeNode(3)
        root.left = TreeNode(0)
        root.right = TreeNode(0)
        self.assertEqual(test.distributeCoins(root), 2)

    def test_distributeCoins1(self):
        root = TreeNode(0)
        root.left = TreeNode(3)
        root.right = TreeNode(0)
        self.assertEqual(test.distributeCoins(root), 3)
