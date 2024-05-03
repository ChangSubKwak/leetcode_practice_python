import unittest

from main.LC0165_Compare_Version_Numbers import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_evalRPN(self):
        self.assertEqual(test.compareVersion(["1.01", "1.001"]), 0)
        self.assertEqual(test.compareVersion(["1.0", "1.0.0"]), 0)
        self.assertEqual(test.compareVersion(["0.1", "1.1"]), -1)
        self.assertEqual(test.compareVersion(["1.2", "1.10"]), -1)
        self.assertEqual(test.compareVersion(["3.0.4.10", "3.0.4.2"]), 1)


