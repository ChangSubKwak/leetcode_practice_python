import unittest

from main.LC0141_Linked_List_Cycle import Solution
from main.ListNode import ListNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_has_cycle(self):
        listnode = ListNode(3)
        listnode.next = ListNode(2)
        listnode.next.next = ListNode(0)
        listnode.next.next.next = ListNode(-4)
        listnode.next.next.next.next = listnode.next

        self.assertEqual(test.hasCycle(listnode), True)

        listnode = ListNode(1)
        listnode.next = ListNode(2)
        listnode.next.next = listnode
        self.assertEqual(test.hasCycle(listnode), True)

        listnode = ListNode(1)
        self.assertEqual(test.hasCycle(listnode), False)


