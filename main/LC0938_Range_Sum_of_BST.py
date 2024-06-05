from typing import Optional

from main.TreeNode import TreeNode


class Solution:
    def inorder(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        total = 0
        total += self.inorder(root.left, low, high)
        if low <= root.val <= high:
            total += root.val
        total += self.inorder(root.right, low, high)

        return total

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.inorder(root, low, high)
