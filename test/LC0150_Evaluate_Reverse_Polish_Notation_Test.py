import unittest

from main.LC0150_Evaluate_Reverse_Polish_Notation import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_evalRPN(self):
        self.assertEqual(test.evalRPN(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(test.evalRPN(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(test.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)


