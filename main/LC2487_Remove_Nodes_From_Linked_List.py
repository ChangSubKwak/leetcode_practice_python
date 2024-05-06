from typing import Optional

from main.ListNode import ListNode


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        current = head

        while current != None:
            nodes.append(current)
            current = current.next

        i = 0
        while i + 1 < len(nodes):
            if nodes[i].val < nodes[i + 1].val:
                del nodes[i]
                i = max(0, i - 1)
                continue
            i += 1

        result = nodes[0]
        for i, node in enumerate(nodes):
            if i == 0:
                continue
            nodes[i - 1].next = nodes[i]

        return result