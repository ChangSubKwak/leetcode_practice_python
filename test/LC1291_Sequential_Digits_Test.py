import unittest

from main.LC1291_Sequential_Digits import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.sequentialDigits(100, 300), [123, 234])
        self.assertEqual(test.sequentialDigits(100, 300), [123, 234])



