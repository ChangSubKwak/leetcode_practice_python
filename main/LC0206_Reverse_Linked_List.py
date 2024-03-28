from typing import Optional

from main.ListNode import ListNode


class Solution:
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        result_first = None
        is_first = True
        head_first = head

        def recur(head):
            nonlocal result, result_first, is_first, head_first
            if not head:
                return

            recur(head.next)
            # print("head.val", head.val)

            if is_first:
                result = ListNode(head.val)
                result_first = result
                is_first = False
            else:
                result.val = head.val

            # if head.val != head_first.val:
            if head != head_first:
                result.next = ListNode()
                result = result.next

        recur(head)

        return result_first
