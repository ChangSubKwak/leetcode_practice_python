from typing import Optional

from main.TreeNode import TreeNode


def left_pad(string, width, pad_char=' '):
    return string.rjust(width, pad_char)


class Solution:
    def recur(self, root, string):
        if not root:
            return

        if not root.left and not root.right:
            if string < self.result or self.result == "":
                self.result = string
            return

        if root.left:
            self.recur(root.left, left_pad(str(root.left.val), 2, "0") + "," + string)

        if root.right:
            self.recur(root.right, left_pad(str(root.right.val), 2, "0") + "," + string)

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.result = ""
        self.recur(root, left_pad(str(root.val), 2, "0"))
        self.result = self.result.strip()

        lexicographically_smallest = ""
        for num in self.result.split(","):
            lexicographically_smallest += chr(97 + int(num.strip()))

        return lexicographically_smallest
