from typing import Optional

from main.ListNode import ListNode


class Solution:
    @staticmethod
    def isPalindrome(head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("slow", slow)
        print("fast", fast)

        reverse = []
        while slow:
            reverse.insert(0, slow.val)
            slow = slow.next

        slow = head
        for val in reverse:
            if slow.val != val:
                return False
            slow = slow.next

        return True
