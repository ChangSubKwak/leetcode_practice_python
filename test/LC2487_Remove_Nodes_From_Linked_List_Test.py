import unittest

from main.LC2487_Remove_Nodes_From_Linked_List import Solution
from main.ListNode import ListNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_removeNodes1(self):
        head = ListNode.from_list(5, 2, 13, 3, 8)
        expected = ListNode.from_list(13, 8)
        self.assertEqual(test.removeNodes(head), expected)

    def test_removeNodes2(self):
        head = ListNode.from_list(1, 1, 1, 1)
        expected = ListNode.from_list(1, 1, 1, 1)
        self.assertEqual(test.removeNodes(head), expected)
