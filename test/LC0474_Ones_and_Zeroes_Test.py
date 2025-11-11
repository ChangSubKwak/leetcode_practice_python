import unittest

from main.LC0474_Ones_and_Zeroes import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(test.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3), 4)
        self.assertEqual(test.findMaxForm(["10", "0", "1"], 1, 1), 2)
