from typing import Optional

from main.TreeNode import TreeNode


class Solution:
    def inorder(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        sum = 0
        sum += self.inorder(root.left, low, high)
        if low <= root.val <= high:
            sum += root.val
        sum += self.inorder(root.right, low, high)

        return sum

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.inorder(root, low, high)
