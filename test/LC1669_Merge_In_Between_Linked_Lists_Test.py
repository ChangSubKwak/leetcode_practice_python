import unittest

from main.LC1669_Merge_In_Between_Linked_Lists import Solution

from main.ListNode import ListNode


class SolutionTest(unittest.TestCase):
    def test_mergeInBetween1(self):
        list1 = ListNode(10)
        list1.next = ListNode(1)
        list1.next.next = ListNode(13)
        list1.next.next.next = ListNode(6)
        list1.next.next.next.next = ListNode(9)
        list1.next.next.next.next.next = ListNode(5)

        list2 = ListNode(1000000)
        list2.next = ListNode(1000001)
        list2.next.next = ListNode(1000002)

        result = ListNode(10)
        result.next = ListNode(1)
        result.next.next = ListNode(13)
        result.next.next.next = ListNode(1000000)
        result.next.next.next.next = ListNode(1000001)
        result.next.next.next.next.next = ListNode(1000002)

        self.assertEqual(Solution.mergeInBetween(list1, 3, 4, list2), result)

    def test_mergeInBetween2(self):
        list1 = ListNode(0)
        list1.next = ListNode(1)
        list1.next.next = ListNode(2)
        list1.next.next.next = ListNode(3)
        list1.next.next.next.next = ListNode(4)
        list1.next.next.next.next.next = ListNode(5)
        list1.next.next.next.next.next.next = ListNode(6)

        list2 = ListNode(1000000)
        list2.next = ListNode(1000001)
        list2.next.next = ListNode(1000002)
        list2.next.next.next = ListNode(1000003)
        list2.next.next.next.next = ListNode(1000004)

        result = ListNode(0)
        result.next = ListNode(1)
        result.next.next = ListNode(1000000)
        result.next.next.next = ListNode(1000001)
        result.next.next.next.next = ListNode(1000002)
        result.next.next.next.next.next = ListNode(1000003)
        result.next.next.next.next.next.next = ListNode(1000004)
        result.next.next.next.next.next.next.next = ListNode(6)

        self.assertEqual(Solution.mergeInBetween(list1, 2, 5, list2), result)
