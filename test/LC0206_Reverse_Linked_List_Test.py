import unittest

from main.LC0206_Reverse_Linked_List import Solution

from main.ListNode import ListNode


class SolutionTest(unittest.TestCase):
    def test_reverseList(self):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        expected = ListNode.from_list([5, 4, 3, 2, 1])
        self.assertEqual(Solution.reverseList(head), expected)

        head = ListNode.from_list([1, 2])
        expected = ListNode.from_list([2, 1])
        self.assertEqual(Solution.reverseList(head), expected)

        head = ListNode.from_list([])
        expected = ListNode.from_list([])
        self.assertEqual(Solution.reverseList(head), expected)