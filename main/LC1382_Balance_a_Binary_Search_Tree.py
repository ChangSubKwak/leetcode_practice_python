from typing import List

from main.TreeNode import TreeNode


class Solution:
    def inorder(self, node, vals) -> List[TreeNode]:
        if not node:
            return

        self.inorder(node.left, vals)
        vals.append(node.val)
        self.inorder(node.right, vals)

    def build(self, vals, left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        node = TreeNode(vals[mid])
        node.left = self.build(vals, left, mid - 1)
        node.right = self.build(vals, mid + 1, right)
        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []
        self.inorder(root, vals)
        return self.build(vals, 0, len(vals) - 1)