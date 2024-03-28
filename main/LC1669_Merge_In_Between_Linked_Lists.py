from main.ListNode import ListNode


class Solution:
    @staticmethod
    def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head1 = ListNode()
        head1.next = list1
        head2 = ListNode()
        head2.next = list1

        while b >= -1:
            if a > 0:
                head1 = head1.next
                a -= 1

            head2 = head2.next
            b -= 1

        tail_list2 = list2
        while tail_list2.next != None:
            tail_list2 = tail_list2.next

        head1.next = list2
        tail_list2.next = head2

        return list1