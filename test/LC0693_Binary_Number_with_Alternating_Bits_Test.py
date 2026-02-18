import unittest
from main.LC0693_Binary_Number_with_Alternating_Bits import Solution

test = Solution()


class SolutionTest(unittest.TestCase):
    def test_replaceWords(self):
        self.assertEqual(test.hasAlternatingBits(5), True)
        self.assertEqual(test.hasAlternatingBits(7), False)
        self.assertEqual(test.hasAlternatingBits(11), False)
        self.assertEqual(test.hasAlternatingBits(3), False)
        self.assertEqual(test.hasAlternatingBits(6), False)
