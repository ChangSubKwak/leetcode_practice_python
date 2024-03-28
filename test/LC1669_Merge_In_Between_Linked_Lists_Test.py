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

        expected = ListNode(10)
        expected.next = ListNode(1)
        expected.next.next = ListNode(13)
        expected.next.next.next = ListNode(1000000)
        expected.next.next.next.next = ListNode(1000001)
        expected.next.next.next.next.next = ListNode(1000002)
        expected.next.next.next.next.next.next = ListNode(5)

        result = Solution.mergeInBetween(list1, 3, 4, list2)

        while result:
            self.assertEqual(result.val, expected.val)
            result = result.next
            expected = expected.next

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

        expected = ListNode(0)
        expected.next = ListNode(1)
        expected.next.next = ListNode(1000000)
        expected.next.next.next = ListNode(1000001)
        expected.next.next.next.next = ListNode(1000002)
        expected.next.next.next.next.next = ListNode(1000003)
        expected.next.next.next.next.next.next = ListNode(1000004)
        expected.next.next.next.next.next.next.next = ListNode(6)

        # self.assertEqual(Solution.mergeInBetween(list1, 2, 5, list2), result)

        result = Solution.mergeInBetween(list1, 2, 5, list2)

        while result:
            self.assertEqual(result.val, expected.val)
            result = result.next
            expected = expected.next
