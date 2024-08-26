from typing import List


class Solution:
    def recur(self, root, result):
        if not root or root is None:
            return

        if root.children:
            for node in root.children:
                self.recur(node, result)
        result.append(root.val)

    def postorder(self, root) -> List[int]:
        result = []
        self.recur(root, result)

        # print(f"root.children : {root.children}")

        return result
