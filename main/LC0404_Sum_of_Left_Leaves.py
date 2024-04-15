from typing import Optional

from main.TreeNode import TreeNode


class Solution:
    def recur(self, root, is_left_parent):
        if not root:
            return 0

        if not root.left and not root.right and is_left_parent:
            return root.val

        return self.recur(root.left, True) + self.recur(root.right, False)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.recur(root.left, True) + self.recur(root.right, False)