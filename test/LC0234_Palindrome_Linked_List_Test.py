import unittest

from main.LC0234_Panlindrome_Linked_List import Solution
from main.ListNode import ListNode


class SolutionTest(unittest.TestCase):
    def test_isPalindrome(self):
        head = ListNode.from_list([1, 2, 2, 1])
        self.assertEqual(Solution.isPalindrome(head), True)

        head = ListNode.from_list([1, 2])
        self.assertEqual(Solution.isPalindrome(head), False)
