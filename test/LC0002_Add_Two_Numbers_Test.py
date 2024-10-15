import unittest 
from main.LC0002_Add_Two_Numbers import LC0002_Add_Two_Numbers
from main.ListNode import ListNode

test = LC0002_Add_Two_Numbers()


class Test_LC0002_Add_Two_Numbers(unittest.TestCase):
    def test_addTwoNumbers1(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        result = ListNode(7)
        result.next = ListNode(0)
        result.next.next = ListNode(8)

        self.assertEqual(test.addTwoNumbers(l1, l2), result)
