from typing import Optional

from main.TreeNode import TreeNode


class Solution:
    def preorder(self, node, path):
        if node:
            path = path ^ (1 << node.val)
            if node.left is None and node.right is None:
                if path & (path - 1) == 0:
                    self.count += 1
            else:
                self.preorder(node.left, path)
                self.preorder(node.right, path)

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.preorder(root, 0)
        return self.count