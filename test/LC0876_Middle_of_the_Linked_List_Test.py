import unittest

from main.LC0876_Middle_of_the_Linked_List import Solution
from main.ListNode import ListNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_middleNode(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        expected = ListNode(3)
        expected.next = ListNode(4)
        expected.next.next = ListNode(5)

        self.assertEqual(test.middleNode(head), expected)

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(6)

        expected = ListNode(4)
        expected.next = ListNode(5)
        expected.next.next = ListNode(6)

        self.assertEqual(test.middleNode(head), expected)



