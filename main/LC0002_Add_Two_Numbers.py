from typing import Optional

from main.ListNode import ListNode


class LC0002_Add_Two_Numbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length1 = 0
        t1 = l1
        while t1 is not None:
            t1 = t1.next
            length1 += 1

        length2 = 0
        t2 = l2
        while t2 is not None:
            t2 = t2.next
            length2 += 1

        longgerLength = max(length1, length2)

        t1 = l1
        t2 = l2
        t3 = None

        carry = 0
        for i in range(longgerLength):
            if t1 is not None:
                num1 = t1.val
                t1 = t1.next
            else:
                num1 = 0

            if t2 is not None:
                num2 = t2.val
                t2 = t2.next
            else:
                num2 = 0

            total = num1 + num2 + carry

            if total >= 10:
                carry = 1
            else:
                carry = 0

            if t3 is None:
                t3 = ListNode(total % 10)
                answer = t3
            else:
                t3.next = ListNode(total % 10)
                t3 = t3.next

        if carry > 0:
            t3.next = ListNode(1)

        return answer
