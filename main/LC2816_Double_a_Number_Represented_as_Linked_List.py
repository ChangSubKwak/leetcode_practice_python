from typing import Optional
from main.ListNode import ListNode


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        dummy = head

        while dummy:
            next_node = dummy.next
            dummy.next = rev
            rev = dummy
            dummy = next_node

        current = ListNode()
        result = current
        carry = 0

        while rev:
            double_value = rev.val * 2 + carry
            if double_value >= 10:
                carry = 1
            else:
                carry = 0

            current.next = ListNode(double_value % 10)
            current = current.next
            rev = rev.next

        if carry == 1:
            current.next = ListNode(1)

        result = result.next

        rev = None
        dummy = result

        while dummy:
            next_node = dummy.next
            dummy.next = rev
            rev = dummy
            dummy = next_node

        return rev