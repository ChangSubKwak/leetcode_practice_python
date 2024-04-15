from typing import Optional
from main.TreeNode import TreeNode


class Solution:
    def __init__(self):
        self.sum = None

    def recur(self, root, current_value):
        if not root.left and not root.right:
            self.sum += int(current_value)
            return

        if root.left:
            self.recur(root.left, current_value + str(root.left.val))

        if root.right:
            self.recur(root.right, current_value + str(root.right.val))

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.recur(root, str(root.val))
        return self.sum

