import unittest
from main.LC0664_Strange_Printer import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_replaceWords(self):
        self.assertEqual(test.strangePrinter("aaabbb"), 2)
        self.assertEqual(test.strangePrinter("aba"), 2)
