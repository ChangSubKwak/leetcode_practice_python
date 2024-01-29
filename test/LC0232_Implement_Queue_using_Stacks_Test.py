import unittest

from main.LC0232_Implement_Queue_using_Stacks import MyQueue

test = MyQueue()


class Solution(unittest.TestCase):
    def test_MyQueue(self):
        test.push(1)
        test.push(2)

        self.assertEqual(test.peek(), 1)
        self.assertEqual(test.pop(), 1)
        self.assertEqual(test.empty(), False)
