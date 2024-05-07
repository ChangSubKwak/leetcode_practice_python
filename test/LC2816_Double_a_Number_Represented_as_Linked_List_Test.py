import unittest

from main.LC2816_Double_a_Number_Represented_as_Linked_List import Solution

from main.ListNode import ListNode

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_doubleIt1(self):
        head = ListNode.from_list([1, 8, 9])
        expected = ListNode.from_list([3, 7, 8])
        self.assertEqual(test.doubleIt(head), expected)

    def test_doubleIt2(self):
        head = ListNode.from_list([9, 9, 9])
        expected = ListNode.from_list([1, 9, 9, 8])
        self.assertEqual(test.doubleIt(head), expected)
