from typing import Optional
from main.TreeNode import TreeNode


class Solution:
    def inorder(self, root: Optional[TreeNode], leaves):
        if not root:
            return

        self.inorder(root.left, leaves)
        if not root.left and not root.right:
            leaves.append(root.val)
        self.inorder(root.right, leaves)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return True