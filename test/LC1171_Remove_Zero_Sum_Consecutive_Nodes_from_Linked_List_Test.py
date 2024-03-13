import unittest

from main.LC1171_Remove_Zero_Sum_Consecutive_Nodes_from_Linked_List import Solution
from main.ListNode import ListNode

test = Solution()


class LC1160_Find_Words_That_Can_Be_Formed_by_Characters_Test(unittest.TestCase):

    def test_1(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(-3)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(1)

        result1 = ListNode(3)
        result1.next = ListNode(1)

        result2 = ListNode(1)
        result2.next = ListNode(2)
        result2.next.next = ListNode(1)

        self.assertIn(test.removeZeroSumSublists(head), [result1, result2])

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(-3)
        head.next.next.next.next = ListNode(4)

        result1 = ListNode(1)
        result1.next = ListNode(2)
        result1.next.next = ListNode(4)

        self.assertEqual(test.removeZeroSumSublists(head), result1)

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(-3)
        head.next.next.next.next = ListNode(2)

        result1 = ListNode(1)

        self.assertEqual(test.removeZeroSumSublists(head), result1)
