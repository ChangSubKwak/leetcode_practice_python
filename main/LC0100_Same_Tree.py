from typing import Optional

from main.TreeNode import TreeNode


class Solution:
    def recur(self, p, q):
        if (not p and q) or (p and not q):
            return False

        if not p and not q:
            return True

        comparison = p.val == q.val
        return comparison and self.recur(p.left, q.left) and self.recur(p.right, q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.recur(p, q)