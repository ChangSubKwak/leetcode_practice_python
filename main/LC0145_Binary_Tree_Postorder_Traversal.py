from typing import Optional, List

from main.TreeNode import TreeNode


class Solution:
    def recur(self, root, result):
        if not root:
            return

        self.recur(root.left, result)
        self.recur(root.right, result)
        result.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.recur(root, result)

        # print(f"result : {result}")

        return result

