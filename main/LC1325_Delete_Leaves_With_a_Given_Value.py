from typing import Optional
from main.TreeNode import TreeNode


class Solution:
    def recur(self, root, target, parent, is_left):
        if not root:
            return

        self.recur(root.left, target, root, True)
        self.recur(root.right, target, root, False)

        if not root.left and not root.right and root.val == target:
            if is_left:
                parent.left = None
            else:
                parent.right = None

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self.recur(root.left, target, root, True)
        self.recur(root.right, target, root, False)

        if not root.left and not root.right and root.val == target:
            root = None

        return root