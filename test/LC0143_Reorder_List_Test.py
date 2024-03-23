import unittest

from main.LC0143_Reorder_List import Solution
from main.ListNode import ListNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_reorderList(self):
        head = ListNode.from_list([1, 2, 3, 4])
        expected = ListNode.from_list([1, 4, 2, 3])
        self.assertEqual(Solution.reorderList(head), expected)

        head = ListNode.from_list([1, 2, 3, 4, 5])
        expected = ListNode.from_list([1, 5, 2, 4, 3])
        self.assertEqual(Solution.reorderList(head), expected)
